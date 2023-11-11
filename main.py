from PyQt5.Widgets import (QApplicatition, QWidget, QPushButton, QLabel, QListWitget,
QlineEdit, QTextEdit, QInputDialog, QHBoxLayout)

app = QApplicatition([])
'''Інтерфейс програми'''
notes_win = QWidget()
notes_win.setWindowTittle('"Розумні замітки"')
notes_win.resize(900, 600)
notes win.show()
app.exes_()
list_notes = QListWitget()
list_notes_label = QLabel('Cписок заміток')
button_notes_del = QPushButton('Видалити замітку')
button_notes_create = QPushButton('Створити замiтку')
button_notes_save = QPushButton('Зберегти замітку')

frield_tag = QlineEdit('')
frield_tag.setPlaceholdertext('введiть тег...')
frield_text
