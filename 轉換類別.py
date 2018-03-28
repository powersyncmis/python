import pymysql.cursors

config = {
    'host':'192.168.0.10',
    'port':3306,
    'user':'root',
    'password':'power&mis',
    'db':'mis',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor,
    }
# Connect to the database
connection = pymysql.connect(**config)
connection1 = pymysql.connect(**config)
connection2 = pymysql.connect(**config)
try:
    with connection.cursor() as cursor:
    # 执行sql语句，插入记录
        sql = 'SELECT No,SNo,Class,Product,company FROM service_log WHERE company="TP"'
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in  result:
            a = i['SNo']
            d = i['No']
            try:
                with connection1.cursor() as cursor1:
                    sql1 = "SELECT * FROM ss WHERE SNo = '%s';" % (a)
                    cursor1.execute(sql1)
                    result1 = cursor1.fetchall()
                    for j in result1:
                        b = j['type']
                        c = j['product']
                        try:
                            with connection2.cursor() as cursor2:
                                sql2 = "UPDATE service_log SET class='%s', product='%s' WHERE SNo='%s' and No='%s';" % (b,c,a,d)
                                cursor2.execute(sql2)
                                connection2.commit()
                        except Exception as f:
                            print(f.args[0],f.args[1])
                    connection1.commit()
            except Exception as e:
                print(e.args[0],e.args[1])
        connection.commit()
finally:
  connection.close()
