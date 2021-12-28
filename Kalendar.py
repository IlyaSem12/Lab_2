
Days =[0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


date=int(input("Введите день:"))
Month = int(input("Введите месяц:"))
Year =  int(input("Введите год:"))
CD= int(input('Количество дней: '))

if Year % 4 == 0 and (Year % 400 == 0 or Year % 100 != 0):
    Days[2] = 29
else:
    Days[2] = 28


print("начальная дата: ", date,'-',Month,'-',Year,"\n")
while CD > 0:
    date += 1
    if date > Days[Month]:
        Month += 1
        if Month > 12:
            Year += 1
            if Year % 4 == 0 and (Year % 400 == 0 or Year % 100 != 0):
                Days[2] = 29
            else:
                Days[2] = 28
            Month = 1
        date = 1
    CD -= 1
print("конечная дата: ", date,'-',Month,'-',Year,"\n")