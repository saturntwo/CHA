from random import randint
from time import sleep

col = ['6p', '7p', '8p', '9p', '10p', 'vp', 'dp', 'kp', 'tp',
       '6k', '7k', '8k', '9k', '10k', 'vk', 'dk', 'kk', 'tk',
       '6b', '7b', '8b', '9b', '10b', 'vb', 'db', 'kb', 'tb',
       '6c', '7c', '8c', '9c', '10c', 'vc', 'dc', 'kc', 'tc']
print(*col)

def peremeshat(col1):
    b = 0
    x = ''
    for i in range(len(col1)):
        a = randint(0, 35)
        x = col1[a]
        col1[a] = col1[i]
        col1[i] = x
    return (col1)

col = peremeshat(col)

def veskart(col2):
    for i in range(len(col2)):
        if '6' in col2[i]: col2[i] = '6'
        elif '7' in col2[i]: col2[i] = '7'
        elif '8' in col2[i]: col2[i] = '8'
        elif '9' in col2[i]: col2[i] = '9'
        elif '10' in col2[i]: col2[i] = '10'
        elif 'v' in col2[i]: col2[i] = '2'
        elif 'd' in col2[i]: col2[i] = '3'
        elif 'k' in col2[i]: col2[i] = '4'
        elif 't' in col2[i]: col2[i] = '11'
    return(col2)
print(*col)



def hod_compa(col3):
    vibor = False
    print('Компьютеру выпали', col3[0], 'и', col3[1])
    col3 = veskart(col3)
    kart4 = col3.pop(1)
    kart3 = col3.pop(0)
    summc = int(kart4) + int(kart3)
    print('Сумма очков у компьютера: ', summc)
    print('Я думаю...')
    sleep(3)
    if summc == 21:
        print('Компьютер победил!')
    if summc > 18:
        return(summc)
    elif summc <15:
        vibor = True
    elif summc >= 15 or summc <= 18:
        ver = randint(1,summc-15+2)
        if ver == 1:
            vibor == True
    if vibor == True:
        summc = summc + int(col3[0])
        print('Компьютеру выпала ещё одна карта. Это ', col3[0])
        col3.remove(col3[0])
        print('Теперь сумма очков у компьютера:', summc)
        if summc == 21:
            print('Компьютер победил!')
    return(summc)
def hod_igroka(col):
    kart2 = col.pop(1)
    kart1 = col.pop(0)
    summ = int(kart1)+int(kart2)
    print('Сумма очков у вас: ', summ)
    if summ == 21:
        print('Вы победили!')
    else:
        print('Это пока меньше 21. Можем взять ещё карту. Если хотите, введите "1". Если нет, введите "0"')
        otvet = input()
        if otvet == '1':
            summ = summ + int(col[0])
            print('Вам выпала ещё одна карта. Это ', col[0])
            print('Теперь сумма очков у вас: ', summ)
            col.remove(col[0])
    return(summ)
def sravnenie(summ, summc):
    if summc < summ and summ < 22 or summ == 21:
        print('Вы победили! А комп лошара')
    elif summc == summ or (summc > 21 and summ > 21):
        print('Ничья!')
    else:
        print('Компьютер победил. Вы проиграли')
log = ''
passw = ''
def autorization(log, passw):
    cand = '0'
    for a in range(3):
        log = input('Введите ваш логин: ')
        passw = input('Введите ваш пароль: ')
        with open('autorize.txt', 'r') as file:
            mass = file.readlines()
        for i in range(len(mass)):
            if log == mass[i][0:-1]:
                if passw == mass[i+1][0:-1]:
                    print('Вы вошли в аккаунт')
                    cand = '1'
                    break
                else:
                    print('Неверный пароль')
                    log = '-1'
                    cand = '1'
                    break
        if cand == '0':
            print('Такой учётной записи пока нет, но сейчас я её создам')
            with open('autorize.txt', 'a') as file:
                file.write(log + '\n')
                file.write(passw +'\n')
        return(log)
anws = ''
x = 1
while anws != 'НЕТ':
    log1 = autorization(log, passw)
    if log1 == '-1':
        quit()
    col = veskart(col)
    summ = hod_igroka(col)
    summc = hod_compa(col)
    sravnenie(summ, summc)

    with open('gameresults.txt', 'a') as file:
        file.write('\n' + str(log1))
        file.write('\n'+ str(summ))
        file.write('\n'+ str(summc))
    anws = input(('Хотите сыграть ещё раз? Если хотите, введите "Да", если же нет - "Нет": '))
    anws = anws.upper()
    x+=1