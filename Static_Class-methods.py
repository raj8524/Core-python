#static methods dont need access class specific data or cant modify it. its used for utility function which perforrm task in isolation.
#They should be completely self-contained, and only work with data passed in as arguments.
class DecoratorExample:
    """ Example Class """

    def __init__(self):
        """ Example Setup """
        print('Hello, World!')

    @staticmethod
    def example_function():
        """ This method is a static method! """
        print('I\'m a static method!')


de = DecoratorExample
de.example_function()

#--------------------class methods--------
#They can't access specific instance data(which can be accessed through instance method), but they can call other static methods.Can modify class specific details.
class DecoratorExample:
    """ Example Class """

    def __init__(self):
        """ Example Setup """
        print('Hello, World!')

    @classmethod
    def example_function(cls):
        """ This method is a class method! """
        print('I\'m a class method!')
        cls.some_other_function()

    @staticmethod
    def some_other_function():
        print('Hello!')


de = DecoratorExample()
de.example_function()
