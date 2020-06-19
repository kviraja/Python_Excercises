

def add(a, b):
    c = a + b
    print('The addition of ', a, 'and ', b, 'is ', c)

def subtract(a, b):
    c = a - b
    print('The difference of ', a, 'and ', b, 'is ', c)


def multiply(a, b):
    c = a * b
    print('The multiplication of ', a, 'and ', b, 'is ', c)

def divide(a, b):
    c = a / b
    print('The division of ', a, 'by ', b, 'is ', c)

x = int(input('Enter the value of a :'))
y = int(input('Enter the value of b :'))

print("Select the operation")
print('1.Addition')
print('2.Subtaction')
print('3.Multiplication')
print('4.Division')

ch=int(input())

if ch==1:
    add(x, y)
elif ch==2:
    subtract(x, y)
elif ch==3:
    multiply(x, y)
elif ch==4:
    divide(x, y)
else:
    print("Not a valid operation")
