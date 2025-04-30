import pyodbc

def get_connection():
    try:
        # Update with your correct database and SQL Server details
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DELL;"  # Update with your SQL Server name or IP
            "DATABASE=petpals;"  # Database name updated to petpals
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
        if result:
            print("✅ Connection Successful!")
        else:
            print("❌ Connection Failed!")
        return conn  # Return the connection object
        
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return None  # Return None if connection fails

# Execute the function to test connection
if __name__ == "__main__":
    get_connection()
