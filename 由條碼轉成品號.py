import pymysql.cursors
import pyodbc


config = {
    'host':'192.168.0.10',
    'port':3306,
    'user':'root',
    'password':'power&mis',
    'db':'mis',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor,
    }

# 連接鼎新ERP
server = '192.168.0.5'
database = 'SH'
username = 'sa'
password = 'dsc@54302158'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor2 = cnxn.cursor()

# Connect to the database
connection1 = pymysql.connect(**config)
connection3 = pymysql.connect(**config)
try:
    with connection1.cursor() as cursor1:
        sql1 = "SELECT GS1 From gs1"
        cursor1.execute(sql1)
        row1 = cursor1.fetchone()
        while row1 is not None:
            var1 = row1['GS1']
            cursor2.execute("SELECT RTRIM(MB001) FROM INVMB WHERE MB013 = '%s'" % (var1))
            row2 = cursor2.fetchone()
            if row2 is not None:

                try:
                    with connection3.cursor() as cursor3:
                        sql3 = "UPDATE gs1 SET SNo = '%s' WHERE GS1 = '%s'" % (row2[0], var1)
                        cursor3.execute(sql3)
                        print(row2[0])
                    connection3.commit()
                except Exception as f:
                    print(f.args[0],f.args[1])
            row1 = cursor1.fetchone()
except Exception as f:
    print(f.args[0],f.args[1])
finally:
    connection1.close()
