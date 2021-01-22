# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text_for_3.txt', 'r', encoding='utf-8') as f:
    data = [f]
    for workers in f:
        workers.split()
        workers_dict = {workers.split()[0]: float(workers.split()[1])}
        # average = (sum(workers_dict.values()) / len(workers_dict)) #вроде формула верная, но что-то не удалось
        # print(f'средняя зп {average}')
        for salary in workers_dict.items():
            result = []
            if salary[1] < 20000.00:
                result.append(salary[0])
                print(f'зарплата менее 20000: {result}')
