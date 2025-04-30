import pyodbc

def create_connection():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DELL;"  # Update with your SQL Server name or IP
            "DATABASE=EcommerceDB;"  # Database name updated to EcommerceDB
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
    create_connection()
