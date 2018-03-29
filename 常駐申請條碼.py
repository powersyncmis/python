import math

import pymysql.cursors


def is_pair(x):
    return not x % 2


def ean13(number):

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
    total = (oddsum * 3) + evensum

    check = int(10 - math.ceil(total % 10.0)) % 10

    return number + str(check)


config = {
    'host': '192.168.0.10',
    'port': 3306,
    'user': 'root',
    'password': 'power&mis',
    'db': 'mis',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

connection1 = pymysql.connect(**config)

try:
    with connection1.cursor() as cursor1:
        sql1 = "SELECT MAX(GS1) From gs1 "
        cursor1.execute(sql1)
        row1 = cursor1.fetchone()
        while row1 is not None:
            var1 = row1['MAX(GS1)']
            var1 = str(int(var1[0:12]) + 1)
            var2 = ean13(var1)

            print(var2)
            row1 = cursor1.fetchone()
except Exception as f:
    print(f.args[0], f.args[1])
finally:
    connection1.close()
