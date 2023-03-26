'''
print the * in a row as mainy staras user want 
'''

# a = int(input("enter the no to be printed :~ "))
# print()
# print("* "*a)

#  USING FOR LOOP 
# n = int(input("enter the no to be printed :~ "))
# for i in range(n):
    # print("*",end=' ')

'''
take input from user and print the square shape of * using for loop 
'''
# n = int(input("enter the no to be printed :~ "))
# for i in range(n):
#     print(" * " * n)

    # for j in range(n):
        # print("*",end=" ")


'''
pattern 3. to print square pattern with provided fixed digit. 
'''

# n = int(input("enter the no to be printed :~ "))
# n_str = str(n)
# for i in range(n):
#     print(f" {n_str} " * n)

'''
pattern4.   print square pattern with provided fixed digit in every row.
'''

# n = int(input("enter the no to be printed :~ "))
# for i in range(n):
#     n_str = str(n)
#     print(f"{n_str}" * n)
#     n -= i


#     ******************************** sol2
# for i in range(n):
#     print((str(i+1)+ " ")*n)


'''
to print square pattern with a fixed alphabet symbol
'''

# a = input("enter the alphabet  to be printed :~ ")
# n = int(input("ener the no of alphabet to be printed :~ "))
# for  i in range(n):
    # print((a+" ") *n )

'''
to print right triangle pattern with fixed alphabet symball in every row .
'''

# a = input("enter the alphabet  to be printed :~ ")
# n = int(input("ener the no of alphabet to be printed :~ "))

# for i in range(n):
#     print((chr(65+i) + " ") * (i+1))

'''
to print inverted right angle triangle pattern with * symbols
'''

# n = int(input("ener the no to be printed :~ "))

# for i in range(n):
#     print(" * "* n )
#     n-=1
'''
pritn pattern inverted rifght angled triangle pattern with digits in ascending order in every row 
'''


            # if within the row element cghanges than nested loop is require
n = int(input("ener the no to be printed :~ "))
for i in range(n):
    for j in range(n-i):     # (n-i) is the no of element in each row .
        print(j+1 , end=" ")    # (n-j) is the name of the element
    print()

































































