def add(P,Q):
  added =  P+Q 
  print(added)

def subtract(P,Q):
    subtracted = P-Q
    print(subtracted)

def multiply(P,Q):
    multiplied = P*Q
    print(multiplied)
    
def divide(P,Q):
    divided = P/Q
    print(divided)

print('Chose an operation: a,s,m,d')
choice = input("enter your choice")
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))

if choice == 'a':
    add(num1,num2)
if choice == 's':
    subtract(num1,num2)
if choice == 'm':
    multiply(num1,num2)
if choice == 'd':
    divide(num1,num2)

 