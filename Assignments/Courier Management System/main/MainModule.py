import sys
import os

# Add the parent folder to sys.path to access modules in 'dao' and 'exception'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.CourierServiceDb import CourierServiceDb
from exception.TrackingNumberNotFoundException import TrackingNumberNotFoundException
from exception.InvalidEmployeeIdException import InvalidEmployeeIdException
from util.DBPropertyUtil import get_db_properties

def print_header(title):
    print(f"\n{'=' * 50}")
    print(f"{title}")
    print(f"{'=' * 50}")

def print_success(message):
    print(f"✅ {message}")

def print_error(message):
    print(f"❌ {message}")

if __name__ == "__main__":
    print_header("=== Courier Service Database Operations ===")

    # Initialize database interaction class
    courier_service_db = CourierServiceDb()

    # Insert a new courier with different values
    print_header("=== Inserting New Courier ===")
    try:
        courier_service_db.insert_courier(
            sender_name="John Doe",
            sender_address="123 Main St, City, Country",
            receiver_name="Alice Brown",
            receiver_address="789 Pine St, City, Country",
            weight=5.5,
            status="In Transit",
            tracking_number="TN12346",  # Changed tracking number
            delivery_date="2025-05-01"  # Changed delivery date
        )
        print_success("Courier inserted successfully!")
    except Exception as e:
        print_error(f"Error inserting courier: {e}")

    # Update courier status
    print_header("=== Updating Courier Status ===")
    try:
        courier_service_db.update_courier_status("TN12346", "Delivered")
        print_success("Status updated successfully!")
    except Exception as e:
        print_error(f"Error updating status for tracking number TN12346: {e}")

    # Retrieve courier details
    print_header("=== Retrieving Courier Details ===")
    try:
        courier_service_db.get_courier_details("TN12346")
    except Exception as e:
        print_error(f"Error retrieving courier details: {e}")

    # Shipment Status Report
    print_header("=== Generating Shipment Status Report ===")
    try:
        courier_service_db.generate_shipment_status_report()
    except Exception as e:
        print_error(f"Error generating shipment status report: {e}")

    # Revenue Report
    print_header("=== Generating Revenue Report ===")
    try:
        courier_service_db.generate_revenue_report()
    except Exception as e:
        print_error(f"Error generating revenue report: {e}")

    # Exception Handling Demonstrations
    print_header("=== Exception Handling Demo ===")

    try:
        raise TrackingNumberNotFoundException("Tracking number 9999 not found.")
    except TrackingNumberNotFoundException as e:
        print_error(f"Error: {e}")

    try:
        raise InvalidEmployeeIdException("Employee with ID 5 not found.")
    except InvalidEmployeeIdException as e:
        print_error(f"Error: {e}")

    print_header("=== Completed Courier Service Operations ===")
