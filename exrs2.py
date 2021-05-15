#Exercise 2- Faulty Calculator
#45 * 3 = 555, 56 + 9 = 77, 56/6 = 4
#Design a calculator which will correctly solve all the problems except
#The Following ones:
#45 * 3 = 555, 56 + 9 = 77, 56/6 = 4
#Your programs should take operator and the two numbers as input from the user and then return the result


while(True):
    num1 = int(input("Enter Number1: "))
    num2 = int(input("Enter Number2: "))
    operation = input("Operation (+,-,x,/): ")
    if operation == '+':
        if num1 == 56 and num2 == 9:
            print("56+9 = 77")
            print("You are disqualified")
            break;
        else:
            res1 = num1 + num2
            print(num1, "+", num2, "=", res1)
            continue

    if operation == 'x':
        if num1 == 45 and num2 == 3:
            print("45x3 = 555")
            print("You are disqualified")
            break;
        else:
            res2 = num1 * num2
            print(num1, "x", num2, "=", res2)
            continue

    if operation == '-':
        if num1 == 72 and num2 == 28:
            print("72-28 = 72")
            print("You are disqualified")
            break;
        else:
            res3 = num1 - num2
            print(num1, "-", num2, "=", res3)
            continue

    if operation == '/':
        if num1 == 56 and num2 == 6:
            print("56/6 = 4")
            print("You are disqualified")
            break;
        else:
            res2 = num1 / num2
            print(num1, "/", num2, "=", res2)
            continue
