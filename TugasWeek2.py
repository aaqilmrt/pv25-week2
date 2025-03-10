import sys
from PyQt5.QtWidgets import *

def form():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Week 2 : Layout - User Registration Form")
    window.setGeometry(100, 100, 500, 500)

    layout1 = QVBoxLayout()
    kotakIdentitas = QGroupBox("Identitas (vertical box layout)")
    identitas = QVBoxLayout()
    identitas.addWidget(QLabel("Nama : Abdul Aqil Murtadho"))
    identitas.addWidget(QLabel("Nim : F1D022029"))
    identitas.addWidget(QLabel("Kelas : C"))
    kotakIdentitas.setLayout(identitas)
    layout1.addWidget(kotakIdentitas)

    kotakNav = QGroupBox("Navigation (horizontal box layout)")
    navigasi = QHBoxLayout()
    navigasi.addWidget(QPushButton("Home"))
    navigasi.addWidget(QPushButton("About"))
    navigasi.addWidget(QPushButton("Contact"))
    kotakNav.setLayout(navigasi)
    layout1.addWidget(kotakNav)

    kotakRegis = QGroupBox("User Registration (form layout)")
    registration = QFormLayout()
    registration.addRow(QLabel("Full Name:"), QLineEdit())
    registration.addRow(QLabel("Email:"), QLineEdit())
    registration.addRow(QLabel("Phone:"), QLineEdit())

    gender = QHBoxLayout()
    gender.addWidget(QRadioButton("Male"))
    gender.addWidget(QRadioButton("Female"))
    registration.addRow(QLabel("Gender:"), gender)
    
    negara = QComboBox()
    negara.addItems(["Select", "Saundi Arabia", "Turkey", "Singapura", "Indonesia"])
    registration.addRow(QLabel("Country:"), negara)
    
    kotakRegis.setLayout(registration)
    layout1.addWidget(kotakRegis)

    kotakAction = QGroupBox("Actions (horizontal box layout)")
    action = QHBoxLayout()
    action.addWidget(QPushButton("Submit"))
    action.addWidget(QPushButton("Cancel"))
    kotakAction.setLayout(action)
    layout1.addWidget(kotakAction)

    window.setLayout(layout1)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    form()