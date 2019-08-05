class Room():
    def __init__(self, room_name):
        """Initialises a room with a name, description, rooms linked to it, characters in it and items in it"""
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_character(self, character_item):
        """Sets the name of the character to the room"""
        self.character = character_item

    def get_character(self):
        """Returns the character in a room"""
        return self.character
        
    def set_description(self, room_description):
        """Sets the description of the room"""
        self.description = room_description

    def get_description(self):
        """Returns the description of the room"""
        return self.description

    def set_name(self, room_name):
        """Sets the name of the room"""
        self.name = room_name

    def get_name(self):
        """Returns the name of the room"""
        return self.name
    
    def get_item(self):
        """"Returns the item in a room"""
        return self.item
    
    def set_item(self, item_name):
        """Sets the item to the room"""
        self.item = item_name
    
    def describe(self):
        """Prints out a description of the room"""
        print( self.description )

    #Adding Link Rooms

    def link_room(self, room_to_link, direction):
        """Links a room with another room in a certain direction"""
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def get_details(self):
        """Prints out the complete details of the room"""
        print (self.name + '\n' + "--------------" + '\n')
        print(self.description + '\n')
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        """Navigates from one room to another only in a forward direction"""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("you can't go that way")
            return self
    
