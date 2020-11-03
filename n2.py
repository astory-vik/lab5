import random
name1 = ["Стоит", "Танцует", "Спит", "Читает", "Кричит", "Кушает", "Плачет"]
name2 = ["Смешно", "Красиво", "Медлено", "Громко", "Безупречно", "Внимательно", "Тихо"]
name3 = ["Стол", "Торт", "Шкаф", "Человек", "Студент", "Машина", "Табурет"]
list = [name1, name2, name3]
def Random():
    int1 = random.randint(0, len(list)-1)
    print(list[int1][random.randint(0, len(list[int1])-1)])
    list.pop(int1)
    int2 = random.randint(0, len(list) - 1)
    print(list[int2][random.randint(0, len(list[int2])-1)])
    list.pop(int2)
    int3 = random.randint(0, len(list) - 1)
    print(list[int3][random.randint(0, len(list[int3])-1)])
Random()



