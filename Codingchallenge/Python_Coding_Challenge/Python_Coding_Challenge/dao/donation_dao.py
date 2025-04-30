from util.db_connection import get_connection
from exception.InsufficientFundsException import InsufficientFundsException
from datetime import datetime

class DonationDAO:
    @staticmethod
    def record_donation(donor_name, amount, donation_type='Cash'):
        if amount < 10:
            raise InsufficientFundsException()
            
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO donations (donor_name, amount)
                VALUES (?, ?)
            """, (donor_name, amount))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error recording donation: {e}")
            return False
