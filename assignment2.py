x = input("Please enter feeding map as a list:")
x = eval(x)
arr = (x)

commands = input("Please enter direction of movements as a list:")
commands= eval(commands)



print("Your board is:")
for r in arr:
    for c in r:
        print(c, end=" ")
    print()

puan = 0
Apple = 5
Carrot = 10
Meat = 5
isTrue = True

def rabbit_position():
    row = -1
    column = -1
    for i in arr:
        row = row+1
        for j in i:
            column = column+1
            if(j.__eq__("*")):

                return(str(row)+","+ str(column - (row * (len(arr[0])))))
def goRight():
    isTrue = True
    global puan
    divv = rabbit_position().split(",")
    b = int(divv[0])
    k = int(divv[1])


    if(k == len(arr[0])-1 or arr[b][k + 1].__eq__('W')):
        pass
    else:
        if(arr[b][k + 1].__eq__('A')):
            puan += Apple
            arr[b][k], arr[b][k + 1] = arr[b][k], "X"
        if(arr[b][k + 1].__eq__('C')):
            puan += Carrot
            arr[b][k], arr[b][k + 1] = arr[b][k], "X"
        if(arr[b][k + 1].__eq__('M')):
            puan -= Meat
            arr[b][k], arr[b][k + 1] = arr[b][k], "X"
        if (arr[b][k + 1].__eq__('P')):
            arr[b][k], arr[b][k + 1] = arr[b][k], "X"

            isTrue = False
        else:
            arr[b][k], arr[b][k + 1] = arr[b][k + 1], arr[b][k]
def goLeft():
    global puan
    isTrue = True
    divv = rabbit_position().split(",")
    b = int(divv[0])
    k = int(divv[1])
    if (k == 0 or arr [b][k - 1].__eq__('W')):
        pass
    else:
        if (arr[b][k-1].__eq__('A')):
            puan += Apple
            arr[b][k], arr[b][k - 1] = arr[b][k] , "X"
        if (arr[b][k -1].__eq__('C')):
            puan += Carrot

            arr[b][k], arr[b][k - 1] =  arr[b][k] , "X"
        if (arr [b][k-1].__eq__('M')):
            puan -= Meat

            arr[b][k], arr[b][k -1] =  arr[b][k] , "X"
        if (arr[b][k-1].__eq__('P')):
            arr[b][k], arr[b][k-1] = arr[b][k] , "X"
            isTrue = False
        else:
            arr[b][k], arr[b][k - 1] = arr[b][k - 1], arr[b][k]
def goUp():
    global puan
    isTrue = True
    divv = rabbit_position().split(",")
    b = int(divv[0])
    k = int(divv[1])
    if (b == 0 or arr [b-1][k].__eq__('W')):
        pass
    else:
        if (arr[b - 1][k].__eq__('A')):
            puan += Apple
            arr[b][k], arr[b - 1][k] =  arr[b][k] , 'X'

        if (arr[b - 1][k].__eq__('C')):
            puan += Carrot
            arr[b][k], arr[b - 1][k] = arr[b][k] , 'X'
        if (arr[b - 1][k].__eq__('M')):
            puan -= Meat
            arr[b][k], arr[b - 1][k] =  arr[b][k] , 'X'
        if (arr[b - 1][k].__eq__('P')):
            arr[b][k], arr[b - 1][k] =  arr[b][k] , 'X'
            isTrue = False


        else:
            arr[b][k], arr[b - 1][k] = arr[b - 1][k], arr[b][k]

def goDown():
    global puan
    isTrue = True
    divv = rabbit_position().split(",")
    b = int(divv[0])
    k = int(divv[1])

    if(b == len(arr)-1 or arr[b+1][k].__eq__('W')):
        pass
    else:
        if (arr[b + 1][k].__eq__('A')):
            puan += Apple

            arr[b][k], arr[b + 1][k] = arr[b][k] , 'X'
        if (arr[b + 1][k].__eq__('C')):
            puan += Carrot
            arr[b][k], arr[b + 1][k] = arr[b][k] , 'X'
        if (arr[b + 1][k].__eq__('M')):
            puan -= Meat
            arr[b][k], arr[b + 1][k] = arr[b][k] , 'X'
        if (arr[b + 1][k].__eq__('P')):
            arr[b][k], arr[b + 1][k] = arr[b][k], 'X'
            isTrue = False


        else:
            arr[b][k], arr[b + 1][k] = arr[b + 1][k], arr[b][k]

def Hareket():

    for eleman in commands:
        if(isTrue):
            if (eleman == "R"):
                goRight()


            if (eleman == "L"):
                goLeft()


            if (eleman == "U"):
                goUp()

            if (eleman == "D"):
                goDown()


        else:
            pass
Hareket()
print("Your output should be like this:",)
for r in arr:
    for c in r:
        print(c, end=" ")
    print()
print("Your score is:", puan)