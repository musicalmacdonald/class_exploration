"""An exploration of python classes using dogs and cats

Basic class format:

class Class_name:
    pass

    OR

    def __init__(self, variables): #this initializes the class variables
        self._variables = variables #use _ for arguments you don't want the user to have access to

    def class_function(self, variables):
        class_function acts on variables
        return result

"""

class Dog:

    def __init__(self, size):

        self.size = size

        if size == 'large':
            print("WOOF!")
        elif size == 'medium':
            print("Bork!")
        elif size == 'small':
            print("yipyipyipyipyipyip!")
        else:
            print("Error: Dog size must be 'small', 'medium' or 'large'.")

    def chase_cat(self):
        print("The Dog is chasing that cat! Snarl! Yowwwwl!")


class Cat:

    def __init__(self):

        print("Meow!")
