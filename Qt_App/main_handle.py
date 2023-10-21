from OTA_App import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog



class MAIN_HANDLE(Ui_MainWindow):
    
    def __init__(self,mainwindow):
        self.setupUi(mainwindow)
        self.tabWidget.setCurrentWidget(self.OTA_Update)
        self.Button_Stop_Tab_1.setEnabled(False)
        self.Button_Stop_Tab_2.setEnabled(False)
        self.Button_Stop_Tab_3.setEnabled(False)
        self.Button_Start_Tab_3.setEnabled(False)

        self.Set_Bar()
        
        # self.progressBar_Tab_1.setMaximum(100)
    
    def Open_Upgrade_File_1(self):
        self.file_name = QFileDialog.getOpenFileName(None, "Open a upgrade files", "","Excel files(*.bin)")
        if self.file_name[0] != '':
            self.TextBrowser_Tab_1.setText(self.file_name[0])
    
    def Open_DEUI_File_1(self):
        self.file_name = QFileDialog.getOpenFileName(None, "Open a DEUI files", "", "Excel files(*.txt)")
        if self.file_name[0] != '':
            self.TextBrowser_Tab_1.setText(self.file_name[0])
    
    def Open_Upgrade_File_2(self):
        self.file_name = QFileDialog.getOpenFileName(None, "Open a upgrade files", "","Excel files(*.bin)")
        if self.file_name[0] != '':
            self.textBrowser_Tab_2.setText(self.file_name[0])
    
    def Open_DEUI_File_3(self):
        self.file_name = QFileDialog.getOpenFileName(None, "Open a DEUI files", "","Excel files(*.txt)")
        if self.file_name[0] != '':
            self.textBrowser_Tab_3.setText(self.file_name[0])

    def Set_Bar(self):
        self.progressBar_Tab_1.setValue(0)
        self.progressBar_Tab_2.setValue(0)
        self.progressBar_Tab_3.setValue(0)
        self.progressBar_Tab_1.setMinimum(0)
        self.progressBar_Tab_2.setMinimum(0)
        self.progressBar_Tab_3.setMinimum(0)
        self.progressBar_Tab_1.setMaximum(100)
        self.progressBar_Tab_2.setMaximum(100)
        self.progressBar_Tab_3.setMaximum(100)
    #---------------------