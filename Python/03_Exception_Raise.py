# num2 should be higher than 5 

# Solution 1
num1 = int (input('Enter Num1: '))
num2 = int (input('Enter Num2: '))


if num2 > 5:
    total = num1 + num2
    print(total)

else:
    print("Num2 muss größer als 5 sein")


# Solution 2
try:
    num1 = int (input('Enter Num1: '))
    num2 = int (input('Enter Num2: '))

    if num2 < 6:
       raise ValueError(num2) # Trigger, start the exception handler

except ValueError as e:
    print('[ErrorNr: 1001] Only digits from 0-9 are allowed and num2 should be greater than 5')
    print(e.args)

else: 
    total = num1 + num2
    print(total)
    print("Num2 muss größer als 5 sein")



