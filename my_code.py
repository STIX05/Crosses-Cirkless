import pandas as pd

df = pd.read_csv('crosses-or-cirkless.csv')

win = input("Хотите ли узнать сколько побед у всех игроков суммарно? ")
if win == "Да" or win == "да":
    temp = (df["win"].value_counts())
    print("Побед у всех игроков:", temp["Yes"])

lose = input("Хотите ли узнать сколько поражений у всех игроков? ")
if lose == "Да" or lose == "да":
    temp = (df["lose"].value_counts())
    print("Поражений у всех игроков:", temp["Yes"])

draw = input("Хотите ли узнать сколько ничьих у всех игроков? ")
if draw == "Да" or draw == "да":
    temp = (df["draw"].value_counts())
    print("Ничьих у всех игроков:", temp["Yes"])


a = int(input("Информацию какой из 20 игр вы хотите узнать? "))
print(df.iloc[a])

b = input("Какую информацию вы хотите получить(win, lose, draw)? ")
if b == 'win':
    a = input("Информацию о каком игроке вы хотите узнать? ")
    if a == 'Adam':
        temp = (df.groupby(by = 'name')['win'].value_counts())
        print("Побед у данного игрока: ", temp[a]['Yes'])
    elif a == 'Dean':
        temp = (df.groupby(by = 'name')['win'].value_counts())
        print("Побед у данного игрока: ", temp[a]['Yes'])
    elif a == 'Eva':
        temp = (df.groupby(by = 'name')['win'].value_counts())
        print("Побед у данного игрока: ", temp[a]['Yes'])
    elif a == 'Thomas':
        temp = (df.groupby(by = 'name')['win'].value_counts())
        print("Побед у данного игрока: ", temp[a]['Yes'])
    elif a == 'Sara':
        temp = (df.groupby(by = 'name')['win'].value_counts())
        print("Побед у данного игрока: ", temp[a]['Yes'])

elif b == 'lose':
    a = input("Информацию о каком игроке вы хотите узнать? ")
    if a == 'Adam':
        temp = (df.groupby(by = 'name')['lose'].value_counts())
        print("Поражений у данного игрока: ", temp[a]['Yes'])
    elif a == 'Dean':
        temp = (df.groupby(by = 'name')['lose'].value_counts())
        print("Поражений у данного игрока: ", temp[a]['Yes'])
    elif a == 'Eva':
        temp = (df.groupby(by = 'name')['lose'].value_counts())
        print("Поражений у данного игрока: ", temp[a]['Yes'])
    elif a == 'Thomas':
        temp = (df.groupby(by = 'name')['lose'].value_counts())
        print("Поражений у данного игрока: ", temp[a]['Yes'])
    elif a == 'Sara':
        temp = (df.groupby(by = 'name')['lose'].value_counts())
        print("Поражений у данного игрока: ", temp[a]['Yes'])

elif b == 'draw':
    a = input("Информацию о каком игроке вы хотите узнать? ")
    if a == 'Adam':
        temp = (df.groupby(by = 'name')['draw'].value_counts())
        print("Ничьих у данного игрока: ", temp[a]['Yes'])
    elif a == 'Dean':
        temp = (df.groupby(by = 'name')['draw'].value_counts())
        print("Ничьих у данного игрока: ", temp[a]['Yes'])
    elif a == 'Eva':
        temp = (df.groupby(by = 'name')['draw'].value_counts())
        print("Ничьих у данного игрока: ", temp[a]['Yes'])
    elif a == 'Thomas':
        temp = (df.groupby(by = 'name')['draw'].value_counts())
        print("Ничьих у данного игрока: ", temp[a]['Yes'])
    elif a == 'Sara':
        temp = (df.groupby(by = 'name')['draw'].value_counts())
        print("Ничьих у данного игрока: ", temp[a]['Yes'])
