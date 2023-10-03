class Pup():
    # Step #1: constructor
    def __init__(self, name, wags_tail, is_good_boy = True):
        self._name = name
        self._wags_tail = wags_tail
        self.is_good_boy = is_good_boy # is_good_boy is merely an attribute so doesn't need the leading underscore

    # Step #2: make name property using decorators (preferred method)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and len(new_name) > 3:
            self._name = new_name 
        else:
            raise Exception("Name must be a string with more than 3 characters!")

    # Step #3: make wags_tail property using the old method
    def get_wags_tail(self):
        return self._wags_tail
    
    def set_wags_tail(self, wags_tail):
        if wags_tail == True or wags_tail == False:
            self._wags_tail = wags_tail
        else:
            print("Tail wagging can be a Boolean value only!")

    wags_tail = property(get_wags_tail, set_wags_tail)

    # use an instance method to make summon_pup
    def summon_pup(self):
        print(f"Come here, {self.name}!")


    # str magic method
    def __str__(self):
        return f"Name: {self.name}"

herschel = Pup("Herschel", True)
zero = Pup("Zero", True, False)
skipper = Pup("Skipper", False, True)

# skipper.wags_tail = "Yes"
# print(skipper.wags_tail)