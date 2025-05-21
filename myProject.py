# This file should be saved in the format yourFirstName.yourStudentNumber.py

STUDENT_NAME = "Replace_Your_Name_Here"
REG_NO = "Replace_Your_Registration_Number_Here"
STUDENT_NO = "Replace_Your_Student_Number_Here"

class Guest:
    # Class variable to keep track of guest IDs
    _next_guest_id = 1
    
    def __init__(self, name, contact_info):
        """Initialize a new guest with automatically generated ID."""
        self.guest_id = Guest._next_guest_id
        Guest._next_guest_id += 1
        self.name = name
        self.contact_info = contact_info
        self.booked_room = None
    
    def reserve_room(self, room):
        """
        Books the specified room for the guest.
        
        Args:
            room: An instance of Room to be booked
            
        Returns:
            bool: True if reservation is successful, False otherwise
        """
        if room.get_occupant() == 0:  # Check if room is unoccupied
            room.book(self.guest_id)
            self.booked_room = room
            return True
        return False
    
    def cancel_reservation(self):
        """Cancels the current reservation and frees up the room."""
        if self.booked_room:
            self.booked_room.checkout()
            self.booked_room = None

class Room:
    def __init__(self, room_number, room_type, price):
        """
        Initialize a new room.
        
        Args:
            room_number: Integer representing unique room number
            room_type: String - one of 'Single', 'Double', or 'Suite'
            price: Integer representing price per night
        """
        if room_type not in ["Single", "Double", "Suite"]:
            raise ValueError("Invalid room type. Must be 'Single', 'Double', or 'Suite'")
            
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self._guest_id = 0  # Private attribute to track occupant, 0 means unoccupied
    
    def book(self, guest_id):
        """
        Set the guest ID for the room when booked.
        
        Args:
            guest_id: Integer representing the unique ID of the guest
        """
        self._guest_id = guest_id
    
    def checkout(self):
        """Clear the guest ID, marking the room as unoccupied."""
        self._guest_id = 0
    
    def get_info(self):
        """
        Return a dictionary with room information.
        
        Returns:
            dict: Contains room number, type, price, and current occupant
        """
        return {
            'room': self.room_number,
            'type': self.room_type,
            'price': self.price,
            'occupant': self._guest_id
        }
    
    def get_occupant(self):
        """
        Return the guest ID of the current occupant.
        
        Returns:
            int: Guest ID of current occupant (0 if unoccupied)
        """
        return self._guest_id

# Testing the implementation
def test_hotel_booking_system():
    print("Testing Hotel Booking System...")
    print("-" * 50)
    
    # Create rooms
    room1 = Room(101, "Single", 100)
    room2 = Room(202, "Double", 150)
    room3 = Room(303, "Suite", 300)
    
    # Create guests
    guest1 = Guest("John Doe", "john@email.com, +1234567890")
    guest2 = Guest("Jane Smith", "jane@email.com, +0987654321")
    
    # Test 1: Check room information
    print("Test 1: Room Information")
    print(f"Room 1 info: {room1.get_info()}")
    print(f"Room 2 info: {room2.get_info()}")
    print(f"Room 3 info: {room3.get_info()}")
    print()
    
    # Test 2: Room reservation
    print("Test 2: Room Reservation")
    success = guest1.reserve_room(room1)
    print(f"Guest 1 ({guest1.name}) booking Room 1: {'Success' if success else 'Failed'}")
    print(f"Room 1 occupant: {room1.get_occupant()}")
    print(f"Updated Room 1 info: {room1.get_info()}")
    print()
    
    # Test 3: Attempt to book already occupied room
    print("Test 3: Double Booking Test")
    success = guest2.reserve_room(room1)
    print(f"Guest 2 ({guest2.name}) booking Room 1: {'Success' if success else 'Failed'}")
    print()
    
    # Test 4: Cancel reservation
    print("Test 4: Cancellation Test")
    guest1.cancel_reservation()
    print(f"Guest 1 cancelled reservation")
    print(f"Room 1 occupant after cancellation: {room1.get_occupant()}")
    print(f"Room 1 info after cancellation: {room1.get_info()}")
    print()
    
    # Test 5: Book previously cancelled room
    print("Test 5: Booking After Cancellation")
    success = guest2.reserve_room(room1)
    print(f"Guest 2 booking Room 1 after cancellation: {'Success' if success else 'Failed'}")
    print(f"Final Room 1 info: {room1.get_info()}")

if __name__ == "__main__":
    test_hotel_booking_system()
