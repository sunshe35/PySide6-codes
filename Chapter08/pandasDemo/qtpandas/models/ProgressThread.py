from qtpandas.compat import QtCore, QtGui, Qt, Signal, Slot


class ProgressWorker(QtCore.QObject):

    progressChanged = Signal(int)       # set value of OverlayProgressView
    finished = Signal()

    def __init__(self, name):
        """Worker object that will be passed to the thread.

        Args:
            name (str): name shown in progress ui.

        """
        super(ProgressWorker, self).__init__()
        self.name = name

    @Slot()
    def doWork(self):
        """start the thread"""
        self.run()
        # emit the result of the operation?
        self.finished.emit()

    def run(self):
        """Implement your job here. This is what the thread will do.

        """
        raise NotImplementedError



def createThread(parent, worker, deleteWorkerLater=False):
    """Create a new thread for given worker.

    Args:
        parent (QObject): parent of thread and worker.
        worker (ProgressWorker): worker to use in thread.
        deleteWorkerLater (bool, optional): delete the worker if thread finishes.

    Returns:
        QThread

    """
    thread = QtCore.QThread(parent)
    thread.started.connect(worker.doWork)
    worker.finished.connect(thread.quit)
    if deleteWorkerLater:
        thread.finished.connect(worker.deleteLater)

    worker.moveToThread(thread)
    worker.setParent(parent)
    return thread
