import math
from hanziconv import HanziConv
import pymysql.cursors
import time

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

while 1:
    starttime = time.strftime("%H:%M:%S", time.localtime()) 
    print("檢查資料庫 "+ starttime)
    while 1:
        connection1 = pymysql.connect( ** config)
        try:
            with connection1.cursor() as cursor1:
                sql1 = "SELECT No,GS1 From gs1 WHERE GS1 = (SELECT MAX(GS1) FROM gs1) AND Company ='SH'"
                cursor1.execute(sql1)
                row1 = cursor1.fetchone()
                var1 = row1['GS1']
                var1 = str(int(var1[0: 12]) + 1)
                var2 = ean13(var1)
                No1 = row1['No']
                No2 = str(int(No1)+1)
        except Exception as a:
            print("step1:" + a)
        finally:
            cursor1.close()
            connection1.close()

        connection2 = pymysql.connect(**config)
        try:
            with connection2.cursor() as cursor2:
                sql2 = "UPDATE gs1 SET GS1 = %s WHERE No = (SELECT MIN(No) From gs1 where Company='SH' AND GS1 is Null)" 
                x = cursor2.execute(sql2,var2)
                if x == 0:
                    print("上海無新資料")
                    time.sleep(60)
                    break
                else:
                    endtime = time.strftime("%H:%M:%S", time.localtime())
                    print("處理完畢！" + endtime)
                    time.sleep(60)
                    connection2.commit()
        except Exception as b:
            print("step2:" + b)
        finally:
            cursor2.close()
            connection2.close()

        connection3 = pymysql.connect( ** config)
        try:
            with connection3.cursor() as cursor3:
                sql3 = "SELECT No,GS1 From gs1 WHERE GS1 = (SELECT MAX(GS1) FROM gs1) AND Company ='TP'"
                cursor3.execute(sql3)
                row1 = cursor3.fetchone()
                var1 = row1['GS1']
                var1 = str(int(var1[0: 12]) + 1)
                var2 = ean13(var1)
                No1 = row1['No']
                No2 = str(int(No1)+1)
        except Exception as c:
            print("step3:" + c)
        finally:
            cursor3.close()
            connection3.close()

        connection4 = pymysql.connect(**config)
        try:
            with connection4.cursor() as cursor4:
                sql4 = "UPDATE gs1 SET GS1 = %s WHERE No = (SELECT MIN(No) From gs1 where Company='TP' AND GS1 is Null)" 
                x = cursor4.execute(sql4,var2)
                if x == 0:
                    print("台北無新資料")
                    time.sleep(60)
                    break
                else:
                    endtime = time.strftime("%H:%M:%S", time.localtime())
                    print("處理完畢！" + endtime)
                    time.sleep(60)
                    connection4.commit()
        except Exception as d:
            print("step4:" + d)
        finally:
            cursor4.close()
            connection4.close()
    # connection3 = pymysql.connect( ** config)
    # try:
    #     with connection3.cursor() as cursor3:
    #         sql3 = "SELECT No,SName,Spec From gs1 WHERE End_Case = '0'"
    #         cursor3.execute(sql3)
    #         row3 = cursor3.fetchone()
    #         while row3 is not None:
    #             var3 = row3['SName']
    #             var4 = row3['Spec']
    #             No2 = row3['No']
    #             # print(var3,var4,No2)
    #             # var3 = HanziConv.toTraditional(var3)
    #             # var4 = HanziConv.toTraditional(var4)
    #             # print(var3,var4,No2)
    #             connection4 = pymysql.connect( ** config)
    #             try:
    #                 with connection4.cursor() as cursor4:
    #                     sql4 = "UPDATE gs1 SET SName =%s, Spec=%s WHERE No=%s"
    #                     cursor4.execute(sql4,(var3,var4,No2))
    #                     connection4.commit()
    #             except:
    #                 print("level_3")
    #             row3 = cursor3.fetchone()
    #         cursor4.close()
    #         connection4.close()
    # except:
    #     print("level_4")
    # finally:
    #     cursor3.close()
    #     connection3.close()
    endtime = time.strftime("%H:%M:%S", time.localtime())
    print("處理完畢！ " + endtime)
    time.sleep(60)
