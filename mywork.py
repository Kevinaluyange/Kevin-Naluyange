STUDENT_NAME = "Replace_Your_Name_Here"
REG_NO = "Replace_Your_Registration_Number_Here"
STUDENT_NO = "Replace_Your_Student_Number_Here"

class Room:
    def __init__(self, room_number, room_type, price):
        '''
        Implement this method to instantiate a Room.
        Possible room types: 'Single', 'Double', and 'Suite'.
        A Room should also have a private attribute __guest_id to track the guest occupying the room
        '''
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.__guest_id = None

    def book(self, guest_id):
        """Set the guest ID for the room when booked by a guest."""
        if self.__guest_id is None:
            self.__guest_id = guest_id
            return True
        return False

    def checkout(self):
        """Clear the guest ID, indicating the room is unoccupied."""
        self.__guest_id = None

    def get_info(self):
        """Return a dictionary with room information.
        Expected dictionary keys: 'room', 'type', 'price', and 'occupant'"""
        return {
            'room': self.room_number,
            'type': self.room_type,
            'price': self.price,
            'occupant': self.__guest_id if self.__guest_id else 0
        }

    def get_occupant(self):
        """Return the guest ID of the current occupant."""
        return self.__guest_id


class Guest:
    _guest_id_counter = 1

    def __init__(self, name, contact_info):
        '''
        Implement this method that instatiates a Guest. In addition, a guest should have the following attributes
        guest_id: an automatically generated unique integer for the guest
        name: a string representing the guest's name
        contact_info:  a string for contact details (phone and email)
        booked_room: an instance of Room (initially set to None).
        '''
        self.guest_id = Guest._guest_id_counter
        Guest._guest_id_counter += 1
        self.name = name
        self.contact_info = contact_info
        self.booked_room = None

    def reserve_room(self, room):
        """
            - This method must receive an instance of a room (a room Object)
            - Books the specified room and set it as occupied by this guest.
            - Precondition: The room must NOT be occupied before it can be reserved.
            - Method should return True on Success and False otherwise
        """
        if room.book(self.guest_id):
            self.booked_room = room
            return True
        return False

    def cancel_reservation(self):
        """Cancel the current reservation and free up the room.
        """
        if self.booked_room:
            self.booked_room.checkout()
            self.booked_room = None


class Hotel:
    def __init__(self, name):
        '''
        Initialize a hotel with specified name. The hotel must maintain a list of Room instances in the hotel
        '''
        self.name = name
        self.rooms = []

    def add_room(self, room):
        """Add a Room instance to the hotel. This method receives a Room instance as room. """
        self.rooms.append(room)

    def find_available_room(self, room_type):
        """Find the first available room of the specified type. A room is available if it's not occupied.
        - Return the first instance of available Room of specified type
        """
        for room in self.rooms:
            if room.room_type == room_type and room.get_occupant() is None:
                return room
        return None

    def list_rooms(self):
        """
            - Return a list containing dictionaries of information about all rooms in the hotel.
            - Format of the list should be similar to sample below:
                [
                    {'room': 101, 'type': 'Single', 'price': 100, 'occupant': 0},
                    {'room': 102, 'type': 'Double', 'price': 200, 'occupant': 4}
                ]

        """
        return [room.get_info() for room in self.rooms]
