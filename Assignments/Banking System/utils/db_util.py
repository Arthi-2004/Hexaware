import pyodbc

class DBUtil:
    @staticmethod
    def get_db_conn():
        try:
            # Server and database information
            server = 'SHRUTHI'  # e.g., 'localhost', '127.0.0.1', or your server's name
            database = 'HMBank'  # Your database name

            # Connection string for Windows Authentication
            conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

            # Establish connection
            conn = pyodbc.connect(conn_str)
            
            # Check if the connection was successful
            print("Database connection established successfully!")
            return conn
        
        except Exception as e:
            print(f"Error while connecting to the database: {e}")
            return None
