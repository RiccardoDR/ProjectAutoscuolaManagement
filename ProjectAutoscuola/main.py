import sys

from PyQt5.QtWidgets import QApplication

from ProgettoAutoscuola.Home.View.VistaAccesso import VistaAccesso

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stylesheet = """
                QPushButton{
                    background-color: transparent;
                }
                
                QTextEdit{
                    background-color: white;
                    border: 2px solid #dfdfdf
                }

                QPushButton::pressed{
                    border-radius: 10px;
                    background-color: grey;
                }

                QTableWidget{
                    border-radius: 0px
                    background-color: white;
                }

                QLabel{
                    background-color: white;
                    color: #444444; 
                }
                
                QMessageBox{
                    background-color: blue;
                }
                
                QToolButton{
                    background-color: white;
                    border: 1px solid #9c9c9c;
                    border-radius: 10px;
                }
                
                QToolButton::Pressed{
                    background-color: grey;
                }
                
                QComboBox{
                    border: 1px solid grey;
                    color: black;
                }
                
                QFont{
                    font-family: cursive;
                }
                
                QLineEdit{
                    background-color: white;
                    border: 2px solid #dfdfdf
                }
                
                QCalendarWidget QToolButton{
                    background-color : lightblue;
                }
                QCalendarWidget QWidget{
                    background-color : lightblue;
                }
    """

    app.setStyleSheet(stylesheet)
    vista_accesso = VistaAccesso()
    vista_accesso.show()
    sys.exit(app.exec_())
