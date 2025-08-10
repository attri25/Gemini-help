# # WAF to print the length of a list.

# def print_len(a):
#     print(len(a))
#     return len(a)

# x = ['This','is','a','list.']
# print_len(x)
# print(x)
# print('')

# # WAF to print the elements of a list in single line

# a = ['This','is','another','list.']

# def print_list(list):
#     for el in list:
#         print(el,end=' ')


# print_list(a)

# print('\n','')

# # WAF to find the factorial of n 

# def print_fact():
#     n = int(input("Enter the number u want factorial of: "))
#     i= 1
#     for el in range(1,n+1):
#         i*= el
#     print(i)
#     return(i)

# print_fact()

# print_fact()

# print('')

# # WAF to convert usd to inr

# def usd_inr():
#     usd = float(input('Dollar: '))
#     print('The value of inr is ',usd*87.20,'INR')
#     return 

# usd_inr()


# # WAF to where we take input from user and determine that it is odd or even



def eve_odd():
    num = float(input('Enter a number:'))
    if num%2==0:
        print('EVEN')
    else:
        print('ODD')

eve_odd()




