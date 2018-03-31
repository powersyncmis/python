import os
import openpyxl
import pymysql.cursors

config = {
    'host': '192.168.0.10',
    'port': 3306,
    'user': 'root',
    'password': 'power&mis',
    'db': 'mis',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
    }

filename = "D:\\pcpong\\國際條碼\\條碼確認檔-網路新增-201711215.xlsx"
if(filename):
    wb = openpyxl.load_workbook(filename, keep_vba=True, data_only=True)
    ws = wb.get_sheet_by_name('2018上海')    
    row_all=ws.max_row
    for i in range(6, row_all):
        if ws.cell(row=i, column=1).value is None:
            break
        var1 = ws.cell(row=i, column=4).value # 條碼
        var2 = ws.cell(row=i, column=6).value # 規格
        var3 = ws.cell(row=i, column=7).value # 包裝方式
        # print(var1,var2,var3)
        connection4 = pymysql.connect( ** config)
        try:
            with connection4.cursor() as cursor4:
                sql4 = "UPDATE gs1 SET SName = %s, Spec = %s WHERE GS1 = %s"
                cursor4.execute(sql4,(var2,var3,var1))
                connection4.commit()
        except:
            print("level_3")
        finally:
            cursor4.close()
            connection4.close()