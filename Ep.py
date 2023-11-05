import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class RefractionSimulator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def calculate_reflection_transmission(self):
        try:
            n1 = float(self.n1_input.text())
            n2 = float(self.n2_input.text())
            angle_incidence_degrees = float(self.angle_input.text())

            # Check for valid input ranges
            if n1 <= 0 or n2 <= 0 or angle_incidence_degrees < 0 or angle_incidence_degrees > 90:
                raise ValueError("Invalid input values. Ensure n1, n2 are positive and 0 <= angle <= 90 degrees.")

            angle_incidence_radians = math.radians(angle_incidence_degrees)
            sin_i = math.sin(angle_incidence_radians)
            sin_t = (n1 / n2) * sin_i
            if abs(sin_t) > 1:
                raise ValueError("Invalid input values. Ensure 0 <= angle <= 90 degrees and valid refractive indices.")

            angle_transmission_radians = math.asin(sin_t)

            reflection = ((n1 * math.cos(angle_incidence_radians) - n2 * math.cos(angle_transmission_radians)) /
                          (n1 * math.cos(angle_incidence_radians) + n2 * math.cos(angle_transmission_radians))) ** 2
            transmission = 1 - reflection

            result_text = f'Reflection: {reflection * 100:.2f}%\nTransmission: {transmission * 100:.2f}%'
            self.result_label.setText(result_text)
        except ValueError as e:
            self.result_label.setText(str(e))
        except Exception as e:
            self.result_label.setText("Math Error")

    def init_ui(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Refraction Simulator')

        layout = QVBoxLayout()

        # Create labels and input fields
        self.n1_label = QLabel('Refractive Index of Medium 1 (n1):', self)
        layout.addWidget(self.n1_label)

        self.n1_input = QLineEdit(self)
        layout.addWidget(self.n1_input)

        self.n2_label = QLabel('Refractive Index of Medium 2 (n2):', self)
        layout.addWidget(self.n2_label)

        self.n2_input = QLineEdit(self)
        layout.addWidget(self.n2_input)

        self.angle_label = QLabel('Angle of Incidence (degrees):', self)
        layout.addWidget(self.angle_label)

        self.angle_input = QLineEdit(self)
        layout.addWidget(self.angle_input)

        # Create labels for displaying results
        self.result_label = QLabel('', self)
        layout.addWidget(self.result_label)

        # Create the Calculate button
        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.clicked.connect(self.calculate_reflection_transmission)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RefractionSimulator()
    window.show()
    sys.exit(app.exec_())
