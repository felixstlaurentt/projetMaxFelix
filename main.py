import sys
from PyQt5.QtWidgets import QApplication
from mainWidget import mainWidget


app = QApplication(sys.argv)

main = mainWidget()
main.show()

sys.exit(app.exec_())
