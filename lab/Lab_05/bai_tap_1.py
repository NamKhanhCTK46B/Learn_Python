import pyodbc

# print (pyodbc.drivers())

connection_string = '''DRIVER={ODBC Driver 18 for SQL Server};
                        SERVER=Admin-PC\SQLEXPRESS;DATABASE=QLSinhVien;
                        Trusted_Connection=yes;Encrypt=no'''

def get_connection ():
    conn = pyodbc.connect (connection_string)
    return conn

def close_connection (conn):
    if conn:
        conn.close ()

def get_all_class ():
    try:
        conn = get_connection ()
        cursor = conn.cursor()

        select_query = """select * from Lop"""
        cursor.execute(select_query)
        records = cursor.fetchall()

        print(f"Danh sách các lớp")
        for row in records:
            print ("*"*50)
            print("Mã lớp: ", row[0])
            print ("Tên lớp: ", row[1])
        close_connection (conn)
    except (Exception, pyodbc.Error) as error:
        print ("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

def get_all_student ():
    try:
        conn = get_connection ()
        cursor = conn.cursor ()

        select_query = """
                            select	sv.ID, HoTen, l.ID, TenLop
                            from	Lop l, SinhVien sv
                            where	l.ID = sv.MaLop
                        """
        cursor.execute(select_query)
        records = cursor.fetchall ()

        print (f"Danh sách sinh viên\n")
        print (f'{"Mã số":<10}{"Họ tên":<40}{"Mã lớp":<10}{"Tên lớp":<20}')
        for row in records:
            print (f'{row[0]:<10}{row[1]:<40}{row[2]:<10}{row[3]:<20}')
        
        close_connection (conn)
    except (Exception, pyodbc.Error) as error:
        print ("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)


def get_class_by_id (class_id):
    try:
        conn = get_connection ()
        cursor = conn.cursor()

        select_query = "select * from Lop where ID = ?"

        params = (class_id,)
        cursor.execute(select_query, params)

        record = cursor.fetchall ()

        print (f"Thông tin lớp có id = {class_id}")
        print ("Mã lớp", record[0][0])
        print ("Tên lớp", record[0][1])

        close_connection(conn)
    except (Exception, pyodbc.Error) as error:
        print ("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

def get_student_by_id (student_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        select_query = "select * from SinhVien where ID = ?"

        params = (student_id,)
        cursor.execute(select_query, params)

        record = cursor.fetchall ()

        print (f"Thông tin sinh viên có mssv = {student_id}")
        print ("Mã số sinh viên", record[0][0])
        print ("Họ và tên sinh viên: ", record[0][1])
        print ("Mã lớp", record[0][2])

        close_connection (conn)
    except (Exception, pyodbc.Error) as error:
        print ("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error) 

def get_student_by_class (class_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        select_query = "select * from SinhVien where MaLop = ?"
        params = (class_id,)
        cursor.execute(select_query, params)

        records = cursor.fetchall()

        print(f"Danh sách sinh viên lớp có mã {class_id}:")
        print(f"{'Mã số':<10}{'Họ tên':<40}{'Mã lớp':<8}")
        for row in records:
            print(f"{row[0]:<10}{row[1]:<40}{row[2]:<8}")
        
        close_connection (conn)
    except (Exception, pyodbc.Error) as error:
        print ("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

def find_student (class_id, name):
    try:
        conn = get_connection ()
        cursor = conn.cursor()

        select_query = "select * from SinhVien where MaLop = ? and HoTen like ?"
        params = (class_id, f"%{name}%")
        cursor.execute (select_query, params)

        records = cursor.fetchall()

        print (f"Danh sách sinh viên lớp có mã {class_id} và tên {name}")
        print(f"{'Mã số':<10}{'Họ tên':<40}{'Mã lớp':<8}")
        for row in records:
            print(f"{row[0]:<10}{row[1]:<40}{row[2]:<8}")
        
        close_connection (conn)
    except(Exception, pyodbc.Error) as error:
        print ("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

def insert_class (class_id, class_name):
    try:
        conn = get_connection ()
        cursor = conn.cursor()

        query = "insert into Lop (ID, TenLop) values (?, ?)"
        cursor.execute (query, (class_id, class_name,))

        conn.commit ()

        print ("Đã thêm thành công")

        close_connection ()
    except(Exception, pyodbc.Error) as error:
        print ("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)  

insert_class (5, "CTK46B")
get_all_class ()
# get_all_student ()
# get_class_by_id (1)
# get_student_by_id (2)
# get_student_by_class (2)
# find_student (3, "Trung")