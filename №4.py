while True:
    a = int(input())
    b = 0
    if a > 1000:
        b = 10
    elif a > 500:
        b = 5
    else:
        b = 0
    print( (a*(100-b))/100 )
