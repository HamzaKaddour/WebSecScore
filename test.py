import pymysql

try:
    connection = pymysql.connect(
        host="127.0.0.1",
        user="root",
        # password="123456789",
        database="websecscore",
        port=3306  # Adjust if needed
    )
    print("Connection successful!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'connection' in locals():
        connection.close()