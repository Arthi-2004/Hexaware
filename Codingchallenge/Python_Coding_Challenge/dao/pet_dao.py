from util.db_connection import get_connection

class PetDAO:
    @staticmethod
    def add_pet(name, age, breed, pet_type, specific_attribute):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO pets (name, age, breed, type, additional_details)
                VALUES (?, ?, ?, ?, ?)
            """, (name, age, breed, pet_type, specific_attribute))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error adding pet: {e}")
            return False

    @staticmethod
    def get_all_pets():
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor()
            # Get only pets that are available (not adopted)
            cursor.execute("SELECT * FROM pets WHERE adoption_status = 'AVAILABLE'")
            pets = cursor.fetchall()
            return pets
        except Exception as e:
            print(f"Error fetching pets: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
