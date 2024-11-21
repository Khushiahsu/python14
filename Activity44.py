#Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print('Please select the operation:')
print('f. Addition')
print('g. Subtraction')
print('h. Multiplication')
print('i. Division')
c = input('Enter your choice (f/g/h/i):')
d = int(input('Enter the number you chose'))
e = int(input('Now select two numbers for your chosen operation'))


if c=='f':
    print(add(d,e))
   
elif c=='g':
    print(sub(d,e))
    
elif c=='h':
    print(mul(d,e))
    
elif c=='i':
    print(div(d,e))
    
else:
    print('Invalid Output')