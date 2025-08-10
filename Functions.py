
#function definition
# !!! The function ends instantly after completion. !!!
def sum(a,b): #sum(parameters)   # This is a whole function, and it ends as soon as the last line is reached
    return(a+b)    # which is this.     


sum(2,5) # This particular call has the value 7 stored in it.
total_sum = sum(8,6) # function call;arguments
# the whole above defined function is ran here again just with numbers or different values so
print(sum(2,3),'hello')

print('')

def greet():
    return  "Nice to meet you !"

print(f'Hey Sam,\n{greet()}')

print('')

def print_random():
    name = (input('Enter your name: '))
    print('Hello,',name)
    return name

print('Could you introduce yourself',print_random(),'?')

print('')

# write a function to print avg of 3 numbers.

def calc_avg():
    x = int(input('Enter a number:'))
    y = int(input('Enter a number:'))
    z = int(input('Enter a number:'))
    print(f'The average of {x},{y} and {z} is {(x+y+z)/3}.')
    

calc_avg()

print('')

def calc_multi(p=3,q=3): #default parameter assigned, works when no arguments are passed with the function when called.
    print(p*q)
    return p*q

calc_multi() # multiplies default value i.e 3*3
calc_multi(4,5) # since arguments passed so it will be 4*5











