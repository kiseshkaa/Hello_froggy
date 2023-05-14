def change_record(points = 0) -> list:
    file = open('records.txt')
    spisok = file.readlines()
    for i in range(len(spisok)):
        spisok[i] = int(spisok[i])
    spisok.append(points)
    spisok.sort(reverse= True)
    file.close()
    return spisok[ : -1]

def add_record(points : int) -> None:
    lst = change_record(points)
    file = open('records.txt', 'w')
    file.write('')
    file.close()
    file = open('records.txt', 'a')
    for i in lst:
        file.write(str(i) + '\n')
    file.close()

def clear_records() -> None:
    file = open('records.txt', 'w')
    file.write('')
    file = open('records.txt', 'a')
    for i in range(10):
        file.write(str(0) + '\n')
    file.close()

def get_coins() -> str:
    file = open('coins.txt')
    coin = file.readline()
    file.close()
    return coin

def set_coins(coins : int) -> None:
    file = open('coins.txt', 'w')
    file.write(str(coins))
    file.close()