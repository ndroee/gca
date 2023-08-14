import pyodbc

# Konfigurasi koneksi ke database SQL Server
server = "HPZ6PKPEKSPL1\LOCALSQL"
database = "GB_TIMAH_DATA"
username = "sa"
password = "P@ssw0rd123"

connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

try:
    connection = pyodbc.connect(connection_string)
    print("Berhasil terhubung ke database SQL Server")

    # Lakukan operasi yang diperlukan di sini

except pyodbc.Error as e:
    print("Gagal terhubung ke database SQL Server:", e)

finally:
    # Menutup koneksi jika sudah selesai
    if 'connection' in locals():
        connection.close()