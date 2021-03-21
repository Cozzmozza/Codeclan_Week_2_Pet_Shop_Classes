# Parameters:
    # name : string
    # total_cash : int
    # pets_sold : int
    # pets : [Pet]

# Methods:
    # stock_count(): int
    # increase_cash(amount):
    # increase_pets_sold(amount):

class PetShop:
    def __init__(self, name, pets, total_cash):
        self.name = name
        self.pets = pets
        self.total_cash = total_cash
        self.pets_sold = 0
        # Again assuming this is 0 to start off with every time
    
    def stock_count(self):
        return len(self.pets)
    
    def increase_pets_sold(self):
        self.pets_sold += 1

    def increase_total_cash(self, amount):
        self.total_cash += amount

    def remove_pet(self,pet_to_remove):
        self.pets.remove(pet_to_remove)

    def find_pet_by_name(self, name):
        for pet in self.pets:
            if pet.name == name:
                return pet
        return None

    def sell_pet_to_customer(self, pet_name, customer):
        pet = self.find_pet_by_name(pet_name)
        customer.reduce_cash(pet.price)
            # This way, this will only happen, if the reduce_cash method exists
            # Meaning if we in future get rid of the reduce_cash method, in the Customer Class, it won't still take away cash
        customer.add_pet(pet)
        self.increase_total_cash(pet.price)
        self.increase_pets_sold()
        self.remove_pet(pet)
        # Does not matter which order these are all in