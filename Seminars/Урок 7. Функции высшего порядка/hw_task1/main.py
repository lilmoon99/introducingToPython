# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                       Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам      Парам пам-пам

import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QIcon
from vonni_ui import Ui_MainWindow

class vonni_rhythm(QtWidgets.QMainWindow):
    def __init__(self):
        super(vonni_rhythm,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    def init_UI(self):
        self.setWindowTitle("Проверка рифмы от Вонни")
        self.setWindowIcon(QIcon('vonni.png'))
        self.ui.text_box.setPlaceholderText("Введите фразу для проверки")
        self.ui.check_botton.clicked.connect(self.rhythm_identifier)
        
    def rhythm_identifier(self):
        words = self.ui.text_box.toPlainText()
        words = words.split()
        syllables_list = []
        for i in words:
            syllables_list.append(syllable_finder(i))
        if max(syllables_list) == min(syllables_list):
            self.ui.answer.setText(str('Парам пам-пам'))
        else:
            self.ui.answer.setText(str('Пам парам'))
    
def syllable_finder(word):
    vowel_rus = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
        # consonant_rus = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'x', 'ш', 'щ', 'ч']
    vowel_count = 0
    for i in range(len(word)):
        if word[i] in vowel_rus:
            vowel_count += 1
    return vowel_count
    
app = QtWidgets.QApplication([])
application = vonni_rhythm()
application.show()

sys.exit(app.exec())



    


input_string = 'па-ра-ра-рам рам-пам-па-пам па-ра-па-дам'
print(rhythm_identifier(input_string))