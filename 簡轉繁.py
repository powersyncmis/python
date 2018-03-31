import pymysql.cursors
from hanziconv import HanziConv

config = {
    'host': '192.168.0.10',
    'port': 3306,
    'user': 'root',
    'password': 'power&mis',
    'db': 'mis',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
    }
connection1 = pymysql.connect( ** config)
try:
    with connection1.cursor() as cursor1:
        sql1 = "SELECT No,SName,Spec From gs1 WHERE End_Case = '0'"
        cursor1.execute(sql1)
        row1 = cursor1.fetchone()
        print(row1)
        while row1 is not None:
            var1 = row1['SName']
            var2 = row1['Spec']
            No1 = row1['No']
            print(var1,var2,No1)
            var1 = HanziConv.toTraditional(var1)
            var2 = HanziConv.toTraditional(var2)
            print(var1,var2,No1)
            connection2 = pymysql.connect( ** config)
            try:
                with connection2.cursor() as cursor2:
                    sql2 = "UPDATE gs1 SET SName =%s, Spec=%s WHERE No=%s"
                    cursor2.execute(sql2,(var1,var2,No1))
                    connection2.commit()
            except:
                print("level_2")
            row1 = cursor1.fetchone()
        cursor2.close()
        connection2.close()
except:
    print("level_1")
finally:
    cursor1.close()
    connection1.close()