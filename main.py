#Import statements:
import sys 
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
#End of import statements 

#Class declaration for all pages:
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("loginRegisterPage.ui",self)
        self.login_button.clicked.connect(self.gotologin_page)
        self.register_button.clicked.connect(self.gotoregister_page)

    def gotologin_page(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoregister_page(self):
        widget.setCurrentIndex(widget.currentIndex() + 2)





class login_page(QMainWindow):
    def __init__(self):
        super(login_page,self).__init__()
        loadUi("loginPage.ui",self)
        self.pushbutton_login.clicked.connect(self.login_button_pressed)
    def login_button_pressed(self):
        if self.lineedit_username.text() == "" or self.lineedit_password.text() == "":
            print("empty")
        
        else:
            widget.setCurrentIndex(widget.currentIndex()+2)
    
        

class register_page(QMainWindow):
    def __init__(self):
        super(register_page, self).__init__()
        loadUi("registerPage.ui", self)
        self.pushbutton_register.clicked.connect(self.register_button_pressed)
    def register_button_pressed(self):
        if self.lineEdit_email.text() == "" or self.lineEdit_phnumber.text() == "" or self.lineEdit_password.text() == "" or self.lineEdit_repeatpassword.text() == "":
            print("empty")
        else:
            widget.setCurrentIndex(widget.currentIndex()+1)

class buy_page(QMainWindow):
    def __init__(self) -> None:
        super(buy_page, self).__init__()
        loadUi("buy_page.ui", self)

#main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(800)
widget.setFixedHeight(600)
main_window = MainWindow()
loginpage = login_page()
buypage = buy_page()
registerpage = register_page()
widget.addWidget(main_window) #1
widget.addWidget(loginpage)   #2
widget.addWidget(registerpage)#3
widget.addWidget(buypage)     #4

widget.show()




try:
    sys.exit(app.exec_())

except:
    print("Exiting")
