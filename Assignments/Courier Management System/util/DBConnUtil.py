# util/DBConnUtil.py
import pyodbc
from util.DBPropertyUtil import get_db_properties

def create_connection():
    try:
        # Try connecting to the database
        conn = pyodbc.connect(
            'Driver={ODBC Driver 17 for SQL Server};'
            'Server=DELL;'
            'Database=CMS;'
            'Trusted_Connection=yes'
        )
        print("✅ Database connection successful!")

        # Verify the connection by executing a simple query
        cursor = conn.cursor()
        cursor.execute("SELECT 1")  # Test query to check if the connection is active
        result = cursor.fetchone()
        
        if result:
            print("✅ Connection Successful!")
        else:
            print("❌ Connection Failed!")
            return None
        
        return conn  # Return the connection object if successful

    except Exception as e:
        print(f"❌ Error connecting to the database: {e}")
        return None  # Return None if connection fails
    
create_connection()
