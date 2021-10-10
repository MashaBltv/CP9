def popadanie(a,b,c,d,e):
    if(c-a) ** 2 + (d-b) ** 2 <= e ** 2:
        return 1
    else:
        return 0
try:
    X0 = float(input('введите координату центра X0:'))
    Y0 = float(input('введите координату центра Y0:'))
    X = float(input('введите координату X:'))
    Y = float(input('введите координату Y:'))
    R = float(input('введите радиус R:'))
    if R > 0:
        if popadanie(X0,Y0,X,Y,R) == 1:
            print('попал')
        else:
            print('не попал')
    else:
        print('радиус не может быть неположительным. введите другое значение')
except ValueError:
    print('это не число. введите число')