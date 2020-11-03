import os


reader = []
scs = []
b = []


def SortByLow():
    scs.sort(key=int)
    for k in scs:
        for i in reader:
            if i.find(k) != -1:
                b.append(i)


def SortByHight():
    scs.sort(key=int)
    scs.reverse()
    for k in scs:
        for i in reader:
            if i.find(k) != -1:
                b.append(i)


path = input("Enter Path")
directory = os.listdir(path)
print(directory)
print("Choice file")
filePath = input("Enter the file name with type")
ch = input("Выберите действие 1)Прочитать файл 2) Дополнить файл 3)отсортировать файл")
if ch == "1":
    file = open(f"{path}{filePath}", 'r', encoding='utf8')
    reader = file.readlines()
    print(reader)
elif ch == '2':
    file = open(f"{path}{filePath}", 'a')
    text = input("Append text: ")
    file.write(text)
    file.close()
elif ch == '3':
    sort = input("1)По возростанию 2)По убиванию")
    file = open(f"{path}{filePath}", 'r', encoding='utf8')
    file2 = open(f"{path}new{filePath}", 'w', encoding='utf8')
    reader = file.readlines()

    for i in reader:
        scs.append(i.split()[2])
    if sort == '1':
        SortByLow()
        for i in b:
            file2.write(i)
    elif sort == '2':
        SortByHight()
        for i in b:
            file2.write(i)
    file2.close()
