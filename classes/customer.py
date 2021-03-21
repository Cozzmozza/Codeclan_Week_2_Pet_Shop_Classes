
# Parameters
    # name : string
    # Cash : int
    # pets : [Pet]

# Methods
    # add_pet(pet):
    # pet_count(): int
    # remove_cash(amount):

class Customer:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.pets = []
        # This is our assumption. That all the customers have no pets to start with
    
    def reduce_cash(self, amount):
        self.cash -= amount

    def pet_count(self):
        return len(self.pets)

    def add_pet(self, new_pet):
        self.pets.append(new_pet)

    def get_total_value_of_pets(self):
        total = 0
        for pet in self.pets:
            total += pet.price
            # Normally we'd do pets['price'] for a dictionary, or find it in the list etc
            # But pets is an object. So to access it we use pet.price
        return total