import pyodbc
from util.DBConnUtil import create_connection

class CourierServiceDb:
    connection = None

    def __init__(self):
        if CourierServiceDb.connection is None:
            CourierServiceDb.connection = create_connection()

    def insert_courier(self, sender_name, sender_address, receiver_name, receiver_address, weight, status, tracking_number, delivery_date):
        """Insert a new courier if tracking number doesn't already exist."""
        if self.get_courier_by_tracking_number(tracking_number):
            print(f"❌ Error: Courier with tracking number {tracking_number} already exists!")
            return
        
        try:
            cursor = CourierServiceDb.connection.cursor()
            cursor.execute("""
                INSERT INTO Courier (SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (sender_name, sender_address, receiver_name, receiver_address, weight, status, tracking_number, delivery_date))
            CourierServiceDb.connection.commit()  # Ensure changes are committed to DB
            print(f"✅ Courier inserted successfully with tracking number {tracking_number}!")
            cursor.close()  # Close the cursor
        except Exception as e:
            print(f"❌ Error inserting courier: {e}")
            cursor.close()

    def update_courier_status(self, tracking_number, new_status):
        """Update the status of a courier."""
        try:
            cursor = CourierServiceDb.connection.cursor()
            cursor.execute("""
                UPDATE Courier
                SET Status = ?
                WHERE TrackingNumber = ?
            """, (new_status, tracking_number))
            CourierServiceDb.connection.commit()  # Ensure changes are committed to DB
            print(f"✅ Courier {tracking_number} status updated to {new_status}")
            cursor.close()  # Close the cursor
        except Exception as e:
            print(f"❌ Error updating status for tracking number {tracking_number}: {e}")
            cursor.close()

    def get_courier_details(self, tracking_number):
        """Retrieve courier details based on tracking number."""
        try:
            cursor = CourierServiceDb.connection.cursor()
            cursor.execute("""
                SELECT * FROM Courier
                WHERE TrackingNumber = ?
            """, (tracking_number,))
            result = cursor.fetchone()
            if result:
                print("✅ Courier Details:")
                print(f"CourierID: {result[0]}")
                print(f"Sender: {result[1]}, Address: {result[2]}")
                print(f"Receiver: {result[3]}, Address: {result[4]}")
                print(f"Weight: {result[5]} kg, Status: {result[6]}")
                print(f"Tracking Number: {result[7]}, Delivery Date: {result[8]}")
            else:
                print(f"❌ Courier with tracking number {tracking_number} not found.")
            cursor.close()  # Close the cursor
        except Exception as e:
            print(f"❌ Error retrieving courier details: {e}")
            cursor.close()

    def generate_shipment_status_report(self):
        """Generate a report of shipment statuses."""
        try:
            cursor = CourierServiceDb.connection.cursor()
            cursor.execute("""
                SELECT Status, COUNT(*) AS Total
                FROM Courier
                GROUP BY Status
            """)
            result = cursor.fetchall()
            print("✅ Shipment Status Report:")
            for row in result:
                print(f"Status: {row[0]} - Total: {row[1]}")
            cursor.close()  # Close the cursor
        except Exception as e:
            print(f"❌ Error generating shipment status report: {e}")
            cursor.close()

    def generate_revenue_report(self):
        """Generate a revenue report based on courier status."""
        try:
            cursor = CourierServiceDb.connection.cursor()
            cursor.execute("""
                SELECT c.Status, SUM(p.Amount) as TotalRevenue
                FROM Payment p
                JOIN Courier c ON c.CourierID = p.CourierID
                GROUP BY c.Status
            """)
            result = cursor.fetchall()
            print("✅ Revenue Report:")
            for row in result:
                print(f"Status: {row[0]}, Revenue: ${row[1]:,.2f}")
            cursor.close()  # Close the cursor
        except Exception as e:
            print(f"❌ Error generating revenue report: {e}")
            cursor.close()

    def get_courier_by_tracking_number(self, tracking_number):
        """Check if a courier with the given tracking number exists."""
        try:
            cursor = CourierServiceDb.connection.cursor()
            cursor.execute("""
                SELECT * FROM Courier
                WHERE TrackingNumber = ?
            """, (tracking_number,))
            result = cursor.fetchone()  # Fetch a single row
            cursor.close()  # Close the cursor
            return result
        except Exception as e:
            print(f"❌ Error checking courier by tracking number: {e}")
            return None
