import math

def is_pair(x):
    return not x%2

def check_code_ean13(number):

    oddsum = 0
    evensum = 0
    total = 0
    eanvalue = number
    reversevalue = eanvalue[:-14:-1]
    finalean = reversevalue[0:]
    for i in range(len(finalean)):
        if is_pair(i):
            oddsum += int(finalean[i])
        else:
            evensum += int(finalean[i])
    total=(oddsum * 3) + evensum

    check = int(10 - math.ceil(total % 10.0)) %10

    return check

if __name__ == "__main__":
    x=695130332436
    for i in range(0,19):
        print(str(x+i)+str(check_code_ean13(str(x+i))))
