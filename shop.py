def menu():
    print('1.添加 2.查看 3.退出')


def add_item(shopping_list, item):
    shopping_list.append(item)


def show_list(shopping_list):
    for i, item in enumerate(shopping_list):
        print(f'{i + 1}.{item}')


shopping_list = []
while True:
    menu()
    choice = input('请选择：')
    if choice == '1':
        item = input('商品名：')
        add_item(shopping_list, item)
    elif choice == '2':
        show_list(shopping_list)
    elif choice == '3':
        break
