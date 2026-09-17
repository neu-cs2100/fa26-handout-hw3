"""HW3 Question 1

Please implement the Pet class below.
It contains comments describing its methods and attributes, but you should write the 
documentation and implement the methods yourself.
"""

class Pet:
    pass
    # Attributes:
    #   name (str): The name of the pet
    #   hunger (int): The current hunger level of the pet
    #   happiness (int): The current happiness level of the pet
    #   You may add more attributes as needed to implement the methods.

    # Constructor arguments:
    #   name (str): The name of the pet
    #   default_hunger (int): The default hunger level of the pet

    # Methods:
    #   feed(num_cans: int) -> None: decreases hunger by the number of cans of food given.
    #   play(hours: int) -> None: increases happiness and hunger by the number of hours
    #                             played. E.g., if you play for 2 hours, happiness and hunger
    #                             both increase by 2.
    #   sleep() -> None: resets hunger to default level and happiness to 0.
    #   check_status() -> str: returns a string based on current hunger and happiness levels.
    #                          If hunger > happiness, it should return "{name} is hungry!"
    #                          If happiness > hunger, it should return "{name} is happy!"
    #                          If hunger == happiness, it should return "{name} is content."
