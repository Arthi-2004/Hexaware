import sys
import os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.db_connection import get_connection
from exception.InsufficientFundsException import InsufficientFundsException
from exception.InvalidPetAgeException import InvalidPetAgeException
from exception.FileHandlingException import FileHandlingException
from exception.AdoptionException import AdoptionException
from entity.pet import Pet
from entity.dog import Dog
from entity.cat import Cat

def display_pet_listings():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Pets")  # Assuming the columns are in the order: ID, Name, Age, Type, Extra (for breed/color)
        pets = cursor.fetchall()
        
        if not pets:
            print("No pets available for adoption.")
            return
        
        print("Available pets:")
        for pet in pets:
            # Debug print to ensure pets are returned correctly
            print(f"Pet ID: {pet[0]}, Name: {pet[1]}, Age: {pet[2]}, Type: {pet[3]}, Extra: {pet[4]}")
            
            if pet[3] == 'Dog':  # type column (4th column in the result)
                dog = Dog(pet[1], pet[2], pet[3], pet[4])  # Extra contains breed
                print(dog)
            elif pet[3] == 'Cat':
                cat = Cat(pet[1], pet[2], pet[3], pet[4])  # Extra contains color
                print(cat)
    except Exception as e:
        print(f"Error fetching pets: {e}")


def record_donation(donor, amount, donation_type='Cash'):
    try:
        if amount < 10:
            raise InsufficientFundsException()
            
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute(""" 
            INSERT INTO Donations (DonorName, Amount, DonationDate, ItemType, Type) 
            VALUES (?, ?, ?, ?, ?) 
        """, (donor, amount, datetime.now(), donation_type, donation_type))
        
        connection.commit()
        print(f"{donation_type} donation recorded successfully!")
        
    except InsufficientFundsException as e:
        print(e)
    except Exception as e:
        print(f"Error recording donation: {e}")

def manage_adoption_event():
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM Adoption_Events")  # Ensure correct table name
        events = cursor.fetchall()
        
        if not events:
            print("No upcoming adoption events.")
            return
            
        print("\nUpcoming Adoption Events:")
        for event in events:
            print(f"ID: {event[0]}, Event: {event[1]}, Date: {event[2]}")  # Updated to match 3 columns

        participant_name = input("Enter participant name to register: ").strip()
        if not participant_name:
            raise AdoptionException("Participant name cannot be empty")
            
        event_id = int(input("Enter event id: "))
        
        # Start transaction
        connection.autocommit = False
        
        # Verify event exists
        cursor.execute("SELECT EventID FROM Adoption_Events WHERE EventID = ?", (event_id,))
        if not cursor.fetchone():
            raise AdoptionException(f"Event with ID {event_id} does not exist")
            
        # Register participant (Use the correct column name 'Name' instead of 'ParticipantName')
        cursor.execute("""
            INSERT INTO Participants (Name, EventID)
            VALUES(?, ?)
        """, (participant_name, event_id))
        
        connection.commit()
        print("Successfully registered for the adoption event!")
        
    except ValueError:
        print("Invalid event ID. Please enter a number.")
    except AdoptionException as e:
        print(f"Adoption event error: {e}")
        if connection:
            connection.rollback()
    except Exception as e:
        print(f"Error managing event: {e}")
        if connection:
            connection.rollback()
    finally:
        if connection:
            connection.autocommit = True
            connection.close()

def add_new_pet():
    try:
        name = input("Enter pet name: ")
        age = int(input("Enter pet age: "))
        if age <= 0:
            raise InvalidPetAgeException()
            
        breed = input("Enter pet breed: ")
        pet_type = input("Enter pet type (Dog/Cat): ").capitalize()
        
        if pet_type not in ['Dog', 'Cat']:
            raise AdoptionException("Invalid pet type. Must be Dog or Cat")
            
        specific_attribute = input(f"Enter {'dog breed' if pet_type == 'Dog' else 'cat color'}: ")
        
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute("""
        INSERT INTO pets(name, age, breed, type, Extra)
        VALUES(?, ?, ?, ?, ?)
        """, (name, age, breed, pet_type, specific_attribute))

        connection.commit()
        print("Pet added successfully!")
        
    except ValueError:
        print("Invalid age. Please enter a number.")
    except InvalidPetAgeException as e:
        print(e)
    except AdoptionException as e:
        print(e)
    except Exception as e:
        print(f"Error adding pet: {e}")

if __name__ == "__main__":
    while True:
        print("\nPetPals Management System")
        print("1. Display available pets")
        print("2. Add new pet")
        print("3. Record donation")
        print("4. Manage adoption event")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            display_pet_listings()
        elif choice == '2':
            add_new_pet()
        elif choice == '3':
            donor = input("Enter donor name: ")
            try:
                amount = float(input("Enter donation amount: "))
                record_donation(donor, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '4':
            manage_adoption_event()
        elif choice == '5':
            print("Thank you for using PetPals Management System!")
            break
        else:
            print("Invalid choice. Please try again.")
