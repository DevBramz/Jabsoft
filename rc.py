for num in range(1, 101):
    if num % 3 == 0:
        print("Crackle")
        continue
    elif num % 5 == 0:
        print("Pop")
        continue
    elif (num % 5 == 0) and (num % 3 == 0):
        print("CracklePop")
        continue
    print(num)
    
    
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("CracklePop")
        continue
    elif num % 3 == 0:
        print("Cracle")
        continue
    elif num % 5 == 0:
        print("Pop")
        continue
    print(num)
    
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("CracklePop")
    elif i%3==0:
        print("Crackle")
    elif i%5==0:
        print("Pop")
    else:
        print(i)