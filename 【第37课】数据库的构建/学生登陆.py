import win32com.client

is_login = 0

conn = win32com.client.Dispatch(r"ADODB.Connection")
DSN = 'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = 图书借阅管理.mdb'  # Access2007及以后
conn.Open(DSN)
# 打开一个记录集Recordset
rs = win32com.client.Dispatch(r'ADODB.Recordset')


student_number= input("输入学号：")
if not student_number:
    print("学号输入无效！")
    exit()
# 查询语句
sql = "SELECT 学号,密码 FROM student WHERE 学号='{}'".format(student_number)
rs.Open(sql, conn, 1, 1)


if rs.RecordCount:
    student_password = input("输入密码：")
    # 判断查询结果中的密码和输入的密码是否一致
    while not rs.EOF:
        if student_password == rs.Fields(1).Value:
            is_login = 1  # 登陆成功
            break
        rs.MoveNext()
    else:
        print("密码错误！")
else:
    print("查无此人！")

if is_login:
    pass


conn.Close()
