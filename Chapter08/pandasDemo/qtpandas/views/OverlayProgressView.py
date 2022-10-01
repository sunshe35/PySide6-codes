from qtpandas.compat import QtCore, QtGui, Qt, Signal, Slot

class OverlayProgressWidget(QtGui.QFrame):
    def __init__(self, parent, workers=[], debug=True, margin=0):
        super(OverlayProgressWidget, self).__init__(parent)
        self._debug = debug
        self._workers = workers
        self._detailProgressBars = []
        self._addedBars = 0
        self._minHeight = 50
        self._width = parent.width() * 0.38
        self._margin = margin
        self._totalProgress = 0

        self.initUi()

        for worker in workers:
            self._addProgressBar(worker)


    def initUi(self):
        self.sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)

        self._pbHeight = 30

        self.setMinimumWidth(self._width)
        #self.setMaximumWidth(self._width)
        self.setMinimumHeight(self._minHeight)

        self.glayout = QtGui.QGridLayout(self)

        self.totalProgressBar = QtGui.QProgressBar(self)
        self.totalProgressBar.setMinimumHeight(self._pbHeight)
        self.totalProgressBar.setMaximumHeight(self._pbHeight)

        self.toggleButton = QtGui.QPushButton('Details', self)
        self.toggleButton.setCheckable(True)
        self.toggleButton.toggled.connect(self.showDetails)
        self.glayout.addWidget(self.totalProgressBar, 0, 0, 1, 1)
        self.glayout.addWidget(self.toggleButton, 0, 1, 1, 1)

        #styleSheet = """.QProgressBar {
            #border: none;
            #border-radius: 3px;
            #text-align: center;
            #background-color: rgba(37, 37, 37, 50%);
            #color: white;
            #margin: 1px;
            #border-bottom-left-radius:5px;
            #border-top-left-radius:5px;
        #}

        #.QProgressBar::chunk {
            #background-color: #05B8CC;
            #border-radius: 3px;
        #}

        #.OverlayProgressWidget {
            #background-color: white;
        #}

        #"""
        ## set stylesheet for all progressbars in this widget
        #self.setStyleSheet(styleSheet)

        parent = self.parent()
        xAnchor = parent.width() - self._width - self._margin
        yAnchor = self._margin
        self.setGeometry(xAnchor, yAnchor, self._width, self._minHeight)

    @Slot(bool)
    def showDetails(self, toggled):
        for (progressBar, label) in self._detailProgressBars:
            progressBar.setVisible(toggled)
            label.setVisible(toggled)
        self.resizeFrame()


    def _addProgressBar(self, worker):
        progressBar = QtGui.QProgressBar(self)
        progressBar.setMinimumHeight(self._pbHeight - 5)
        progressBar.setMaximumHeight(self._pbHeight - 5)
        label = QtGui.QLabel(worker.name, self)
        if not self.toggleButton.isChecked():
            progressBar.hide()
            label.hide()
        row = self._addedBars + 1
        self.glayout.addWidget(progressBar, row, 0, 1, 1)
        self.glayout.addWidget(label, row, 1, 1, 1)
        self._addedBars += 1
        self._detailProgressBars.append((progressBar, label))
        worker.progressChanged.connect(progressBar.setValue)
        worker.progressChanged.connect(self.calculateTotalProgress)
        
        worker.progressChanged.connect(self.debugProgressChanged)
        
    def debugProgressChanged(self, value):
        print(("debugProgressChanged", value))

    def addWorker(self, worker):
        self._workers.append(worker)
        self._addProgressBar(worker)
        self.resizeFrame()

    def resizeFrame(self):
        size = self.glayout.sizeHint()
        self.resize(size.width(), size.height())

    @Slot()
    def calculateTotalProgress(self):
        bars = len(self._detailProgressBars)
        if bars:
            progress = 0
            for (progressBar, label) in self._detailProgressBars:
                value = progressBar.value()
                progress += value
            progress = progress / bars
        else:
            progress = 100

        self.totalProgressBar.setValue(progress)
