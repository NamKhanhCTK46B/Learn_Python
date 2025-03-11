import pyodbc

# print (pyodbc.drivers())

connection_string = '''DRIVER={ODBC Driver 18 for SQL Server};
                        SERVER=Admin-PC\SQLEXPRESS;
                        DATABASE=QLMonAn;
                        Trusted_Connection=yes;
                        Encrypt=no'''

def get_connection():
    conn = pyodbc.connect(connection_string)
    return conn

def close_connection (conn):
    if conn:
        conn.close ()

def get_all_food_types():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM NhomMonAn")
    result = cursor.fetchall()
    conn.close()
    return result

def get_all_food():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MonAn")
    result = cursor.fetchall()
    conn.close()
    return result

def get_food_by_type(ma_nhom):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MonAn WHERE Nhom = ?", (ma_nhom,))
    result = cursor.fetchall()
    conn.close()
    return result

def get_food_by_id(food_id):
    conn = get_connection ()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MonAn WHERE MaMonAn = ?", (food_id,))
    food = cursor.fetchone()
    conn.close()
    return food

def add_update_delete_food(ma, ten, dvt, gia, nhom, thaotac):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("{CALL ThemXoaSua_MonAn (?, ?, ?, ?, ?, ?)}", (ma, ten, dvt, gia, nhom, thaotac))
    conn.commit()
    success = cursor.rowcount > 0
    conn.close()
    return success
