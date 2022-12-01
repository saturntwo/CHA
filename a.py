log = ''
passw = ''
def autorization(log, passw):
    for a in range(3):
        log = input('Введите ваш логин: ')
        passw = input('Введите ваш пароль: ')
        with open('autorize.txt', 'r') as file:
            mass = file.readlines()
            print(mass[0][0:-1])
        for i in range(len(mass)):
            if log == mass[i][0:-1]:
                if passw == mass[i+1][0:-1]:
                    print('Вы вошли в аккаунт')
                    break
                
                else:
                    print('Неверный пароль')
                    log = '-1'
                    break
            elif log not in mass:
                print('Такой учётной записи пока нет, но сейчас я её создам')
                with open('autorize.txt', 'a') as file:
                    file.write('\n' + log)
                    file.write('\n' + passw)
                    break
        return(log)
log1 = autorization(log, passw)
print(log1)

