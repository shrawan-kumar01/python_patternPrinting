'''
30. to print pyramid pattern with fixed digit in every row 
'''

n = 5
for i in range(n):
    print(" " * (n-i-1) + (str(i+1)+ " ")*(i+1))

