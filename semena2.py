#for line in file:
 #   num = line.find()
#     file.close() способы тестирования через документ-строку


string = ['a', 'e', 'i', 'o', 'u']

with open('inp.txt', 'r') as file_1:
    max_1 = ''
    for line in file_1:
        line = line[3:]
        a = line.find(' ')
        line = line[:a + 1]
        for j in string:
            m = line.find(j)
            if m != -1:
                max_1 += j
        print(line)
