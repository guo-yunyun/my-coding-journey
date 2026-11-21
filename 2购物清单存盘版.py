def load_list():
    try:
        with open('shopping.txt', 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []


def save_list(shopping_list):
    with open('shopping.txt', 'w', encoding='utf-8') as f:
        for item in shopping_list:
            f.write(item + '\n')


shopping_list = load_list()
while True:
    print('\n1.查看 2.添加 3.删除 4.退出')
    choice = input('请选择：')
    if choice == '1':
        for i, item in enumerate(shopping_list, 1):
            print(f'{i}.{item}')
    elif choice == '2':
        item = input('商品名：')
        shopping_list.append(item)
        save_list(shopping_list)
        print('已保存')
    elif choice == '3':
        item = input('要删除的')
        if item in shopping_list:
            shopping_list.remove(item)
            save_list(shopping_list)
            print('已删除并保存')
    elif choice == '4':
        break
