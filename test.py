with open('cities.txt', 'r', encoding='utf-8') as file:
    txt = file.readlines()
    txt2 = []
    for u in txt:
        txt2.append(u[:-2])
    print(txt2)
while True:
    city = input('enter your city: ')
    for a in txt2:
        if a == city:
            print('Элемент найден')
            letter = a[-1]
            print(letter)
            from random import randint
            

            
        else:
            print('Такого элемента нету')
            break

            

     