"""HW3 Question 1

Please implement the Pet class below.
It contains comments describing its methods, but you should write the 
documentation and implement the methods yourself.
"""

class Pet:
    pass
    # Attributes:
    #   name: The name of the pet
    #   hunger: The current hunger level of the pet. 0 is not hungry (satisfied). No upper limit
    #   happiness: The current happiness level of the pet. 0 is default. No upper limit
    #   You may add more attributes as needed to implement the methods.

    # Constructor arguments:
    #   name: The name of the pet
    #   default_hunger: The default hunger level of the pet

    # Methods:
    #   feed(num_cans): decreases hunger by the number of cans of food given.
    #   play(hours): increases happiness and hunger by the number of hours
    #                played. E.g., if you play for 2 hours, happiness and hunger
    #                both increase by 2.
    #   sleep(): resets hunger to default level and resets happiness to 0.
    #   check_status(): returns a string "<name> is <status>!"
    #                   where <name> is the pet's name, and <status> is:
    #                       "hungry" if the pet's hunger is greater than their happiness,
    #                       "happy" if the pet's happiness is greater than their hunger, or
    #                       "content" if the pet's happiness and hunger levels are equal
