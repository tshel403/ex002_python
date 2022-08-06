num0 = 0
num1 = 1
print(num0)
print(num1)
while True:
    if (num1 + num0) > 10000:
        break
    num2 = num1 + num0
    print(num2)
    num0 = num1
    num1 = num2
