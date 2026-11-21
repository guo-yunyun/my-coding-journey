import datetime


def write_diary():
    text = input('今天想记点什么：')
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    with open('diary.txt', 'a', encoding='utf-8') as f:
        f.write(f'[{now}{text}\n]')
    print('已保存')


def show_diary():
    try:
        with open('diary.txt', 'r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print('还没写日记，先写一条吧')


while True:
    print('\n1.写日记 2.看日记 3.退出')
    choice = input('请选择：')
    if choice == '1':
        write_diary()
    elif choice == '2':
        show_diary()
    elif choice == '3':
        print('再见')
        break
