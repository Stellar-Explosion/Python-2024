# Создайте класс, который при инициализации принимает параметр «путь
# до файла». Если файл не существует (проверка с помощью модуля os), то его
# необходимо создать при инициализации объекта данного класса. В атрибут
# words должен быть помещен список всех слов из текста. У класса должны быть
# следующие методы:
# 1) delete_word – должен удалить слово, которое было передано в вызов
# данного метода.
# 2) update_source – сохраняет все слова обратно в файл.

import os

class TextSearch:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                pass

        self.words = self._read_words_from_file()

    def _read_words_from_file(self):
        with open(self.file_path, 'r') as file:
            text = file.read()
        words = text.split()
        return words

    def delete_word(self, word):
        self.words = [w for w in self.words if w != word]

    def update_source(self):
        with open(self.file_path, 'w') as file:
            file.write(' '.join(self.words))
            
