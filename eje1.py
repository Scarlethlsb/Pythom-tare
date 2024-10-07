import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class PersonalInfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Información Personal')
        self.setGeometry(100, 100, 400, 200)

        # Fondo de la ventana
        self.setStyleSheet("background-color: #f0f0f0;")  # color de fondo

        layout = QVBoxLayout()
        layout.setSpacing(20)  # espaciado entre widgets

        self.name_label = QLabel('Nombre Completo: Oscar Ulises Ortiz Cruz')
        self.name_label.setAlignment(Qt.AlignCenter)  # centrar el texto
        self.name_label.setFont(QFont('Arial', 16, QFont.Bold))  # fuente más grande y negrita
        self.name_label.setStyleSheet("color: #2e8b57;")  # color de texto verde
        layout.addWidget(self.name_label)

        self.age_label = QLabel('Edad: 20 años')
        self.age_label.setAlignment(Qt.AlignLeft)  # Alinear el texto a la izquierda
        self.age_label.setFont(QFont('Verdana', 14, QFont.StyleItalic))  # Fuente Verdana, tamaño 14, cursiva

        self.age_label.setStyleSheet("color: #ff6347;")  # Color de texto rojo tomate

        layout.addWidget(self.age_label)

    
        self.setLayout(layout)
 
app = QApplication(sys.argv)
window = PersonalInfoWindow()
window.show()
sys.exit(app.exec_())
