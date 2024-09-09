def custom_write(file_name, strings):
    dic = {}
    count = 0
    file = open(file_name, 'a', encoding='utf-8')
    if file.writable() == False:
        file = open(file_name, 'w' , encoding='utf-8')
    for i in strings:
        count += 1
        tell_first = file.tell()
        file.write(i + '\n')
        key = (count, tell_first)
        item = i
        dic[key] = (i)
    file.close()
    return dic


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
