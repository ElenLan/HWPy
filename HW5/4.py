# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
from googletrans import Translator

file_translate = Translator()
with open('text_for_4.txt', 'r') as f:
    data = f.readlines()
    result = Translator.translate(str(data), src='en', dest='ru')
    print(result.text)
    with open('text_for_4/2', 'w') as wr:
        wr.write(result.text)
