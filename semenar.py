# относительные пути доступа к файлу, иначе файл должен находиться там же, где был загружен.
# или open('../input.dat') - нет. Но КОНТЕКСТНЫЕ МЕНЕДЖЕРЫ : with open('input.txt','r') as file_in:
# with open('inp.txt', 'w') as input_file:
#     for i in range(101):
#         print(i, file=out_file, end=' ')
#             if i % 10 == 0:
#                 print(file=out_file)
# методы чтения.
# with open('inp.txt') as inp_file:
#     list_file = inp_file.readlenes()
# for line in list_file:
#     print(line)
# Все файлы обязательно закрывать. Режимы доступа.
# file = open('my_file.txt', 'r')
# with open('inp.txt') as inp_file:
#     print(inp_file.read)
with open('inp.txt') as input_file:
    for line in input_file:
        print(line[0])

for i in range(10):
    file_name = 'simple' + str(i) + '.txt'
    with open(file_name, 'w') as out_file:
        out_file.write('It\'s me.') # создать 10 файлов .

# исключения : ошибки\события .
file_name1 = input('vvedite:')
number = input('wvedu:')
number = int(number)
try:
    with open(file_name1, 'r') as input_file1:
        counter = 1
        for line in input_file1:
            if counter == number:
                print(line)
                break
            counter += 1
        else:
            print('nety')
except FileNotFoundError:  # исключение ,которое мы прописываем. Указывать вид ошибки обязательно!
    print("failnot")  # действия в случае ошибки.
except ValueError:
    print('hdfjfhjsh')

