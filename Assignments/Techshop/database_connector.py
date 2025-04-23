import pyodbc

class DatabaseConnector:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            # Establish a connection to the SQL Server database with Windows Authentication
            self.connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=DELL;'  # Replace with your server name
                'DATABASE=TECHSHOP_NEW1;'  # Replace with your database name
                'Trusted_Connection=yes;'
            )
            self.cursor = self.connection.cursor()
            print("Database connection established successfully.")
        except Exception as e:
            print(f"Error in connection: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
