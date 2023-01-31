""" Function call-by-value """
no1, no2 = int(input('Enter 2 numbers :')), int(input())
print('Inputted numbers are :')
print('No1 :', no1, ', No2 :', no2)
def noIncrement(n1, n2):
    """ Number incrementation """
    print('Numbers inside the function :')
    print('N1 :', n1, ', N2 :', n2)
    n1 += 1
    n2 += 1
    print('Numbers inside the function, after incrementation :')
    print('N1 :', n1, ', N2 :', n2)
    return
print('Calling the function.')
noIncrement(no1, no2)
print('After returning from the function :')
print('No1 :', no1, ', No2 :', no2)
print('Thank you.')
