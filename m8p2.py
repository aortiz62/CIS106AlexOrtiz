num1 = 1
num2 = 1

print(num1)
print(num2)

for i in range (3, 21):
    nextnum = num1 + num2
    print(nextnum)
    num1 = num2
    num2 = nextnum