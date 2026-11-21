def load_records():
    records = []
    try:
        with open('account.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    amount, note = line.split(',', 1)
                    records.append((float(amount), note))
    except FileNotFoundError:
        pass
    return records


def save_records(records):
    with open('account.txt', 'w', encoding='utf-8') as f:
        for amount, nite in records:
            f.write(f'{amount},{note}\n')


records = load_records()
while True:
    print('\n1.记一笔 2.看细明 3.看总额 4.退出')
    choice = input('请选择：')
    if choice == '1':
        try:
            amount = float(input('金额：'))
            note = input('备注：')
            records.append((amount, note))
            save_records(records)
            print('已记录')
        except ValueError:
            print('金额必须是数字，这条没记上')
    elif choice == '2':
        if records:
            for i, (amount, note) in enumerate(records, 1):
                print(f'{i}.{amount}元-{note}')
        else:
            print('还没有记录')
    elif choice == '3':
        total = sum(amount for amount, note in records)
        print(f'总支出{total}元')
    elif choice == '4':
        print('再见')
        break
