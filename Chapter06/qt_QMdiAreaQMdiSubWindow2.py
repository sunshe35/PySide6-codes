from argparse import ArgumentParser, RawTextHelpFormatter
from functools import partial
import sys

from PySide6.QtCore import (QByteArray, QFile, QFileInfo, QPoint, QSettings,
        QSaveFile, QSize, QTextStream, Qt)
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
        QMdiArea, QMessageBox, QTextEdit, QWidget)
import os
os.chdir(os.path.dirname(__file__))
# import mdi_rc


class MdiChild(QTextEdit):
    sequence_number = 1

    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_DeleteOnClose)
        self._is_untitled = True

    def new_file(self):
        self._is_untitled = True
        self._cur_file = f"document{MdiChild.sequence_number}.txt"
        MdiChild.sequence_number += 1
        self.setWindowTitle(f"{self._cur_file}[*]")

        self.document().contentsChanged.connect(self.document_was_modified)

    def load_file(self, fileName):
        file = QFile(fileName)
        if not file.open(QFile.ReadOnly | QFile.Text):
            reason = file.errorString()
            message = f"Cannot read file {fileName}:\n{reason}."
            QMessageBox.warning(self, "MDI", message)
            return False

        instr = QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.setPlainText(instr.readAll())
        QApplication.restoreOverrideCursor()

        self.set_current_file(fileName)

        self.document().contentsChanged.connect(self.document_was_modified)

        return True

    def save(self):
        if self._is_untitled:
            return self.save_as()
        else:
            return self.save_file(self._cur_file)

    def save_as(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save As", self._cur_file)
        if not fileName:
            return False

        return self.save_file(fileName)

    def save_file(self, fileName):
        error = None
        QApplication.setOverrideCursor(Qt.WaitCursor)
        file = QSaveFile(fileName)
        if file.open(QFile.WriteOnly | QFile.Text):
            outstr = QTextStream(file)
            outstr << self.toPlainText()
            if not file.commit():
                reason = file.errorString()
                error = f"Cannot write file {fileName}:\n{reason}."
        else:
            reason = file.errorString()
            error = f"Cannot open file {fileName}:\n{reason}."
        QApplication.restoreOverrideCursor()

        if error:
            QMessageBox.warning(self, "MDI", error)
            return False

        self.set_current_file(fileName)
        return True

    def user_friendly_current_file(self):
        return self.stripped_name(self._cur_file)

    def current_file(self):
        return self._cur_file

    def closeEvent(self, event):
        if self.maybe_save():
            event.accept()
        else:
            event.ignore()

    def document_was_modified(self):
        self.setWindowModified(self.document().isModified())

    def maybe_save(self):
        if self.document().isModified():
            f = self.user_friendly_current_file()
            message = f"'{f}' has been modified.\nDo you want to save your changes?"
            ret = QMessageBox.warning(self, "MDI", message,
                    QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

            if ret == QMessageBox.Save:
                return self.save()

            if ret == QMessageBox.Cancel:
                return False

        return True

    def set_current_file(self, fileName):
        self._cur_file = QFileInfo(fileName).canonicalFilePath()
        self._is_untitled = False
        self.document().setModified(False)
        self.setWindowModified(False)
        self.setWindowTitle(f"{self.user_friendly_current_file()}[*]")

    def stripped_name(self, fullFileName):
        return QFileInfo(fullFileName).fileName()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._mdi_area = QMdiArea()
        self._mdi_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self._mdi_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self._mdi_area)

        self._mdi_area.subWindowActivated.connect(self.update_menus)

        self.create_actions()
        self.create_menus()
        self.create_tool_bars()
        self.create_status_bar()
        self.update_menus()

        self.read_settings()

        self.setWindowTitle("MDI")

    def closeEvent(self, event):
        self._mdi_area.closeAllSubWindows()
        if self._mdi_area.currentSubWindow():
            event.ignore()
        else:
            self.write_settings()
            event.accept()

    def new_file(self):
        child = self.create_mdi_child()
        child.new_file()
        child.show()

    def open(self):
        file_name, _ = QFileDialog.getOpenFileName(self)
        if file_name:
            existing = self.find_mdi_child(file_name)
            if existing:
                self._mdi_area.setActiveSubWindow(existing)
            else:
                self.load(file_name)

    def load(self, file_name):
        child = self.create_mdi_child()
        if child.load_file(file_name):
            self.statusBar().showMessage("File loaded", 2000)
            child.show()
        else:
            child.close()

    def save(self):
        if self.active_mdi_child() and self.active_mdi_child().save():
            self.statusBar().showMessage("File saved", 2000)

    def save_as(self):
        if self.active_mdi_child() and self.active_mdi_child().save_as():
            self.statusBar().showMessage("File saved", 2000)

    def cut(self):
        if self.active_mdi_child():
            self.active_mdi_child().cut()

    def copy(self):
        if self.active_mdi_child():
            self.active_mdi_child().copy()

    def paste(self):
        if self.active_mdi_child():
            self.active_mdi_child().paste()

    def about(self):
        QMessageBox.about(self, "About MDI",
                "The <b>MDI</b> example demonstrates how to write multiple "
                "document interface applications using Qt.")

    def update_menus(self):
        has_mdi_child = (self.active_mdi_child() is not None)
        self._save_act.setEnabled(has_mdi_child)
        self._save_as_act.setEnabled(has_mdi_child)
        self._paste_act.setEnabled(has_mdi_child)
        self._close_act.setEnabled(has_mdi_child)
        self._close_all_act.setEnabled(has_mdi_child)
        self._tile_act.setEnabled(has_mdi_child)
        self._cascade_act.setEnabled(has_mdi_child)
        self._next_act.setEnabled(has_mdi_child)
        self._previous_act.setEnabled(has_mdi_child)
        self._separator_act.setVisible(has_mdi_child)

        has_selection = (self.active_mdi_child() is not None and
                        self.active_mdi_child().textCursor().hasSelection())
        self._cut_act.setEnabled(has_selection)
        self._copy_act.setEnabled(has_selection)

    def update_window_menu(self):
        self._window_menu.clear()
        self._window_menu.addAction(self._close_act)
        self._window_menu.addAction(self._close_all_act)
        self._window_menu.addSeparator()
        self._window_menu.addAction(self._tile_act)
        self._window_menu.addAction(self._cascade_act)
        self._window_menu.addSeparator()
        self._window_menu.addAction(self._next_act)
        self._window_menu.addAction(self._previous_act)
        self._window_menu.addAction(self._separator_act)

        windows = self._mdi_area.subWindowList()
        self._separator_act.setVisible(len(windows) != 0)

        for i, window in enumerate(windows):
            child = window.widget()

            f = child.user_friendly_current_file()
            text = f'{i + 1} {f}'
            if i < 9:
                text = '&' + text

            action = self._window_menu.addAction(text)
            action.setCheckable(True)
            action.setChecked(child is self.active_mdi_child())
            slot_func = partial(self.set_active_sub_window, window=window)
            action.triggered.connect(slot_func)

    def create_mdi_child(self):
        child = MdiChild()
        self._mdi_area.addSubWindow(child)

        child.copyAvailable.connect(self._cut_act.setEnabled)
        child.copyAvailable.connect(self._copy_act.setEnabled)

        return child

    def create_actions(self):

        icon = QIcon.fromTheme("document-new", QIcon('images/new.png'))
        self._new_act = QAction(icon, "&New", self,
                shortcut=QKeySequence.New, statusTip="Create a new file",
                triggered=self.new_file)

        icon = QIcon.fromTheme("document-open", QIcon('images/open.png'))
        self._open_act = QAction(icon, "&Open...", self,
                shortcut=QKeySequence.Open, statusTip="Open an existing file",
                triggered=self.open)

        icon = QIcon.fromTheme("document-save", QIcon('images/save.png'))
        self._save_act = QAction(icon, "&Save", self,
                shortcut=QKeySequence.Save,
                statusTip="Save the document to disk", triggered=self.save)

        self._save_as_act = QAction("Save &As...", self,
                shortcut=QKeySequence.SaveAs,
                statusTip="Save the document under a new name",
                triggered=self.save_as)

        self._exit_act = QAction("E&xit", self, shortcut=QKeySequence.Quit,
                statusTip="Exit the application",
                triggered=QApplication.instance().closeAllWindows)

        icon = QIcon.fromTheme("edit-cut", QIcon('images/cut.png'))
        self._cut_act = QAction(icon, "Cu&t", self,
                shortcut=QKeySequence.Cut,
                statusTip="Cut the current selection's contents to the clipboard",
                triggered=self.cut)

        icon = QIcon.fromTheme("edit-copy", QIcon('images/copy.png'))
        self._copy_act = QAction(icon, "&Copy", self,
                shortcut=QKeySequence.Copy,
                statusTip="Copy the current selection's contents to the clipboard",
                triggered=self.copy)

        icon = QIcon.fromTheme("edit-paste", QIcon('images/paste.png'))
        self._paste_act = QAction(icon, "&Paste", self,
                shortcut=QKeySequence.Paste,
                statusTip="Paste the clipboard's contents into the current selection",
                triggered=self.paste)

        self._close_act = QAction("Cl&ose", self,
                statusTip="Close the active window",
                triggered=self._mdi_area.closeActiveSubWindow)

        self._close_all_act = QAction("Close &All", self,
                statusTip="Close all the windows",
                triggered=self._mdi_area.closeAllSubWindows)

        self._tile_act = QAction("&Tile", self, statusTip="Tile the windows",
                triggered=self._mdi_area.tileSubWindows)

        self._cascade_act = QAction("&Cascade", self,
                statusTip="Cascade the windows",
                triggered=self._mdi_area.cascadeSubWindows)

        self._next_act = QAction("Ne&xt", self, shortcut=QKeySequence.NextChild,
                statusTip="Move the focus to the next window",
                triggered=self._mdi_area.activateNextSubWindow)

        self._previous_act = QAction("Pre&vious", self,
                shortcut=QKeySequence.PreviousChild,
                statusTip="Move the focus to the previous window",
                triggered=self._mdi_area.activatePreviousSubWindow)

        self._separator_act = QAction(self)
        self._separator_act.setSeparator(True)

        self._about_act = QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)

        self._about_qt_act = QAction("About &Qt", self,
                statusTip="Show the Qt library's About box",
                triggered=QApplication.instance().aboutQt)

    def create_menus(self):
        self._file_menu = self.menuBar().addMenu("&File")
        self._file_menu.addAction(self._new_act)
        self._file_menu.addAction(self._open_act)
        self._file_menu.addAction(self._save_act)
        self._file_menu.addAction(self._save_as_act)
        self._file_menu.addSeparator()
        action = self._file_menu.addAction("Switch layout direction")
        action.triggered.connect(self.switch_layout_direction)
        self._file_menu.addAction(self._exit_act)

        self._edit_menu = self.menuBar().addMenu("&Edit")
        self._edit_menu.addAction(self._cut_act)
        self._edit_menu.addAction(self._copy_act)
        self._edit_menu.addAction(self._paste_act)

        self._window_menu = self.menuBar().addMenu("&Window")
        self.update_window_menu()
        self._window_menu.aboutToShow.connect(self.update_window_menu)

        self.menuBar().addSeparator()

        self._help_menu = self.menuBar().addMenu("&Help")
        self._help_menu.addAction(self._about_act)
        self._help_menu.addAction(self._about_qt_act)

    def create_tool_bars(self):
        self._file_tool_bar = self.addToolBar("File")
        self._file_tool_bar.addAction(self._new_act)
        self._file_tool_bar.addAction(self._open_act)
        self._file_tool_bar.addAction(self._save_act)

        self._edit_tool_bar = self.addToolBar("Edit")
        self._edit_tool_bar.addAction(self._cut_act)
        self._edit_tool_bar.addAction(self._copy_act)
        self._edit_tool_bar.addAction(self._paste_act)

    def create_status_bar(self):
        self.statusBar().showMessage("Ready")

    def read_settings(self):
        settings = QSettings('QtProject', 'MDI Example')
        geometry = settings.value('geometry', QByteArray())
        if geometry.size():
            self.restoreGeometry(geometry)

    def write_settings(self):
        settings = QSettings('QtProject', 'MDI Example')
        settings.setValue('geometry', self.saveGeometry())

    def active_mdi_child(self):
        active_sub_window = self._mdi_area.activeSubWindow()
        if active_sub_window:
            return active_sub_window.widget()
        return None

    def find_mdi_child(self, fileName):
        canonical_file_path = QFileInfo(fileName).canonicalFilePath()

        for window in self._mdi_area.subWindowList():
            if window.widget().current_file() == canonical_file_path:
                return window
        return None

    def switch_layout_direction(self):
        if self.layoutDirection() == Qt.LeftToRight:
            QApplication.setLayoutDirection(Qt.RightToLeft)
        else:
            QApplication.setLayoutDirection(Qt.LeftToRight)

    def set_active_sub_window(self, window):
        if window:
            self._mdi_area.setActiveSubWindow(window)


if __name__ == '__main__':
    argument_parser = ArgumentParser(description='MDI Example',
                                     formatter_class=RawTextHelpFormatter)
    argument_parser.add_argument("files", help="Files",
                                 nargs='*', type=str)
    options = argument_parser.parse_args()

    app = QApplication(sys.argv)
    main_win = MainWindow()
    for f in options.files:
        main_win.load(f)
    main_win.show()
    sys.exit(app.exec())