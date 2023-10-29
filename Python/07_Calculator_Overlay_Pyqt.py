# Import libraries
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout

# App erzeugen
app = QApplication(sys.argv)

# Top-Level Window erzeugen
window = QWidget()
window.setWindowTitle("Taschenrechner von Merdan")

# Buttons erzeugen
btn_1 = QPushButton("1")
btn_2 = QPushButton("2")
btn_3 = QPushButton("3")
btn_4 = QPushButton("4")
btn_5 = QPushButton("5")
btn_6 = QPushButton("6")
btn_7 = QPushButton("7")
btn_8 = QPushButton("8")
btn_9 = QPushButton("9")
btn_rad_deg = QPushButton("Rad   |   Deg")
btn_nichtx = QPushButton("x!")
btn_klammerauf = QPushButton("(")
btn_klammerzu = QPushButton(")")
btn_prozent = QPushButton("%")
btn_ac = QPushButton("AC")
btn_inv = QPushButton("Inv")
btn_sin = QPushButton("sin")
btn_ln = QPushButton("ln")
btn_geteiltdurch = QPushButton("/")
btn_tt = QPushButton("TT")
btn_cos = QPushButton("cos")
btn_log = QPushButton("log")
btn_mal = QPushButton("x")
btn_e = QPushButton("e")
btn_tan = QPushButton("tan")
btn_V = QPushButton("V")
btn_minus = QPushButton("-")
btn_ans = QPushButton("Ans")
btn_exp = QPushButton("EXP")
btn_xhoch = QPushButton("x²")
btn_plus = QPushButton("+")
btn_0 = QPushButton("0")
btn_punkt = QPushButton(".")
btn_istgleich = QPushButton("=")


# Farbe
gruen = QPalette()
gruen.setColor(QPalette.ButtonText, Qt.green)


# QLine mit default Wert 0
eingabe = QLineEdit("0")

btn_istgleich.setPalette(gruen)



# Layout definieren
layout = QGridLayout()

# First Row QLineEdit 
layout.addWidget(eingabe, 0, 0, 1, 7)

# 2nd Row
layout.addWidget(btn_rad_deg, 1, 0, 1, 2)
layout.addWidget(btn_nichtx, 1, 2)
layout.addWidget(btn_klammerauf, 1, 3)
layout.addWidget(btn_klammerzu, 1, 4)
layout.addWidget(btn_prozent, 1, 5)
layout.addWidget(btn_ac, 1, 6)

# 3rd Row
layout.addWidget(btn_inv, 2, 0)
layout.addWidget(btn_sin, 2, 1)
layout.addWidget(btn_ln, 2, 2)
layout.addWidget(btn_7, 2, 3)
layout.addWidget(btn_8, 2, 4)
layout.addWidget(btn_9, 2, 5)
layout.addWidget(btn_geteiltdurch, 2, 6)

# 4th Row
layout.addWidget(btn_tt, 3, 0)
layout.addWidget(btn_cos, 3, 1)
layout.addWidget(btn_log, 3, 2)
layout.addWidget(btn_4, 3, 3)
layout.addWidget(btn_5, 3, 4)
layout.addWidget(btn_6, 3, 5)
layout.addWidget(btn_mal, 3, 6)

# 5th Row
layout.addWidget(btn_e, 4, 0)
layout.addWidget(btn_tan, 4, 1)
layout.addWidget(btn_V, 4, 2)
layout.addWidget(btn_1, 4, 3)
layout.addWidget(btn_2, 4, 4)
layout.addWidget(btn_3, 4, 5)
layout.addWidget(btn_minus, 4, 6)

# 6th Row
layout.addWidget(btn_ans, 5, 0)
layout.addWidget(btn_exp, 5, 1)
layout.addWidget(btn_xhoch, 5, 2)
layout.addWidget(btn_0, 5, 3)
layout.addWidget(btn_punkt, 5, 4)
layout.addWidget(btn_istgleich, 5, 5)
layout.addWidget(btn_plus, 5, 6)

app.setStyle('Black')  # 'Fusion', 'windows', 'windowsVista', 'Machintosh'

# Layout setzen mit methode setLayout()
window.setLayout(layout)

# Zeigt das Fenster
window.show()

# App ausführen und einen Loop für die User Interaktionen starten
app.exec()



