import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection():
        connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DELL;"  # Update with your SQL Server name or IP
            "DATABASE=SISDB1;"  # Database name updated to EcommerceDB
            "Trusted_Connection=yes;"
        )
        return connection
