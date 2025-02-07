import sys
from PyQt5.QtWidgets import QApplication,QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QTimer, Qt, QTime

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.init()

    def init(self):
        self.setWindowTitle("Stopwatch")
        vbox = QVBoxLayout()

        vbox.addWidget(self.time_label)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.setLayout(vbox)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.start_button.setObjectName("startButton")
        self.stop_button.setObjectName("stopButton")
        self.reset_button.setObjectName("resetButton")

        self.setStyleSheet("""
            QPushButton {
                padding: 20px;
                font-weight: bold;
                font-size: 50px;
                border-radius: 10px;
            }
            QPushButton#startButton {
                background-color: #4CAF50;  
                border: 3px solid #388E3C;  
            }
            QPushButton#stopButton {
                background-color: #F44336; 
                border: 3px solid #D32F2F;  
            }
            QPushButton#resetButton {
                background-color: #2196F3;
                border: 3px solid #1976D2;  
            }
            QLabel {
                background-color: #7f60bf;
                font-size: 150px;
                border-radius: 20px;
                border: 5px solid #4a4a4a;
            }
        """)
        
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format(self.time))
        self.stop()

    def format(self, time):
        hours = time.hour()
        mins = time.minute()
        secs = time.second()
        millisec = time.msec()
        return f"{hours:02}:{mins:02}:{secs:02}:{millisec // 10:02}"

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Stopwatch()
    window.show()
    sys.exit(app.exec_())