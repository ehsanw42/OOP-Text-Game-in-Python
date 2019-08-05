class Character():

    def __init__(self, char_name, char_description):
        """Iniliases the character with a name and description"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """DPrints out a description of the character"""
        print( self.name + " is here!" )
        print( self.description )

    def set_conversation(self, conversation):
        """Sets what this character will say when talked to"""
        self.conversation = conversation

    def talk(self):
        """If this character has a conversation attribute, prints it out"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        """Prints a message syanig you cannot fight with this character"""
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    enemies_defeated = 0
    
    def __init__(self, char_name, char_description):
        """Inilialises the Enemy with a name, description and weakness"""

        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        """Sets this Enemy's weakness"""
        self.weakness = item_weakness

    def get_weakness(self):
        """Returns this Enemy's weakness"""
        return self.weakness

    def set_defeated(self, number_defeated):
        """Sets the number of enemies defeated so far in this game. Not required for most games as this is incremented automatically when a fight is won"""
        Enemy.enemies_defeated = number_defeated

    def get_defeated(self):
        """Returns the number of enemies defeated so far in this game"""
        return Enemy.enemies_defeated
        
        
    # FIght with an Enemy
    def fight(self, combat_item):
        """Checks the combat_item against the weakness to determine if the fight is won or lost"""
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            Enemy.enemies_defeated += 1
            return True
        else:
            print(self.name + " Crushes you, punny adventurer!")
            return False

    def steal(self):
        """A dummy method to demonstrate adding new methods"""
        print("You steal from " + self.name)
        #Decide what character has to steal

class Friend(Character):
    def __init__(self, char_name, char_description):
        """Initialises a friend character"""
        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        """A dummy mthod for the friend character"""
        print(self.name + " hugs you back!")
