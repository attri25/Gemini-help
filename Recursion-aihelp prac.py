# Recursion - When a function calls itself repeateadly

def steps(number):
    if number == 0:
        return 
    else:
        steps(number-1)
        print('Step number:',number)
        

steps(75)

# def show(n):

#     if n ==  0:  # similar to stopping conditions in loops
#         return n
#     print(n)
#     show(n-1)
#     if  n == 1:
#         print('This is 1')
#     if n == 2:
#         print('This is 2')
#     if n==3:
#         print('This is 3')      #call stack when a function is called on top of a previous function
    
# show(3)

# # n! through recursion

# def fact(n):
#     if (n == 0 or n==1):
#         return
#     else:
#         return n * fact(n-1)

# fact(5)






