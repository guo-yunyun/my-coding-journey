def load_contact():
    contracts = {}
    try:
        with open('contact.txt', 'r', encoding='utf-8') as f:
            for line in f:
                name, phone = line.strip(',')
                contacts[name] = phone
    except FileNotFoundError:
        pass
    return contracts


def save_contacts(contacts):
    with open('contacts.txt', 'w', encoding='utf-8') as f:
        for name, phone in contacts.items():
            f.write(f'{name},{phone}\n')


contacts = load_contact()
while True:
    print('\n1.添加 2.查询 3。退出')
    choice = input('请选择')
    if choice == '1':
        name = input('姓名：')
        phone = input('电话：')
        contacts[name] = phone
        save_contacts(contacts)
        print('已保存')
    elif choice == '2':
        name = input('要查的姓名：')
        print(contacts.get(name, '没找到哦'))
    elif choice == '3':
        break
