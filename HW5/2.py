# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text_for_2.txt', 'r') as f:
    line = 0
    word = 0
    for lines in open('text_for_2.txt', 'r'):
        line += 1
        words = str(lines).split()
        word += len(words)
    print(line)
    print(word)



