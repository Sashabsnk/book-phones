
book_phones = {
    # Напиши код тут
    'андрей':"-79899899889",
    'Михаил':'112',
    'аня':'1',
    'лия':'+09998765432',
    'ЭДУАРД':'0'
}
print(len(book_phones))
for a in book_phones.values():

    print(a)
action = input('Что хочешь сделать: 1 - показать, 2 - добавить, 3 - изменить, 4 - удалить контакт, 5 - Показать все имена в книге, 6 - Показать все номера в книге? -> ')

if  action == '1':
    name = input('имя ')
    if name in book_phones:
        print(book_phones [name])
    else:
        print('нет такого телефоного номера')
elif action == '2' or action == '3':
    name = input('имя ')
    phone = input('телефон ')
    book_phones [name] = phone
    for key in book_phones:
        print(f'{key}: {book_phones[key]}')
elif action == '4':
    name = input('имя ')
    if name in book_phones:
        del book_phones [name]
    for key in book_phones:
        print(f'{key}: {book_phones[key]}')
elif action == "5":
    for a in book_phones:
        print(a)
elif action == '6':
    for b in book_phones.values():
        print(b)

else:
    print('нет такого телефоного номера')
