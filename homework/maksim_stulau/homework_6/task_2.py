for i in range(1, 100):
    if i % 5 == 0:
        if i % 3 == 0:
            print('FuzzBuzz')
    if i % 3 == 0:
        if i % 5 != 0:
            print('Fuzz')
    elif i % 5 == 0:
        if i % 3 != 0:
            print('Buzz')
    else:
        print(i)