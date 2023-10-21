from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
from main_handle import MAIN_HANDLE
import time

# class ThreadClass(QThread):
#     any_signal = pyqtSignal

class My_Ui(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.mainUI = QMainWindow()
        self.mainHandle = MAIN_HANDLE(self.mainUI)
        self.mainUI.show()
        
        
        self.mainHandle.Button_Upgrade_Tab_1.clicked.connect(self.mainHandle.Open_Upgrade_File_1)
        self.mainHandle.Button_File_Tab_1.clicked.connect(self.mainHandle.Open_DEUI_File_1)
        self.mainHandle.Button_Upgrade_Tab_2.clicked.connect(self.mainHandle.Open_Upgrade_File_2)
        self.mainHandle.Button_File_Tab_3.clicked.connect(self.mainHandle.Open_DEUI_File_3)
        self.mainHandle.Button_Start_Tab_1.clicked.connect(self.run1)
        self.mainHandle.Button_Setting_Tab_3.clicked.connect(self.Verify)
        self.mainHandle.Button_Start_Tab_3.clicked.connect(self.run3)
        self.mainHandle.Button_Start_Tab_2.clicked.connect(self.run2)

    def run1(self):
        self.mainHandle.Button_Start_Tab_1.setEnabled(False)
        self.mainHandle.Button_Stop_Tab_1.setEnabled(True)
        for i in range(100):   
            time.sleep(0.1)
            self.mainHandle.progressBar_Tab_1.setValue(i+1)
        self.mainHandle.Button_Start_Tab_1.setEnabled(True)
    
    def run2(self):
        self.mainHandle.Button_Start_Tab_2.setEnabled(False)
        self.mainHandle.Button_Stop_Tab_2.setEnabled(True)
        for i in range(100):   
            time.sleep(0.1)
            self.mainHandle.progressBar_Tab_2.setValue(i+1)
        self.mainHandle.Button_Start_Tab_2.setEnabled(True)

    def Verify(self):
        self.mainHandle.Button_Start_Tab_3.setEnabled(True)
        
        
    def run3(self):
        self.mainHandle.Button_Start_Tab_3.setEnabled(False)
        self.mainHandle.Button_Stop_Tab_3.setEnabled(True)
        for i in range(100):   
            time.sleep(0.1)
            self.mainHandle.progressBar_Tab_3.setValue(i+1)
        self.mainHandle.Button_Start_Tab_3.setEnabled(True)

if __name__ == "__main__":
    app = QApplication([])
    Run_UI = My_Ui()
    app.exec_()