def find_max(a,b,c):
    if(a>b and c):
        return a
    elif(b>c):
        return b
    else:
        return c
    


max_num = find_max(50, 20, 10)
print(f"The maximum number is: {max_num}")  

max_num2 = find_max(100, 300, 50)
print(f"The maximum number is: {max_num2}")

print('')

# function to take 2 strings and print them together just separated by a space

def fullname(a, b):
    return (f'{a} {b}')

print(f'Your full name is {fullname('Attri','De.')}')

print('')

# Age validator

def adultcheck():
    age = int(input('Enter your age: '))
    if (age<18 or age>120):
        return False
    else:
        print('Valid Age')
        return True


adultcheck()

print('')

# check if number positive

def positive_check():
    a = int(input('Enter a number: '))
    if a >0:
        return (f'{a} positive')
    else:
        return "Error"
    
print(positive_check())

#This is to check github upload. 