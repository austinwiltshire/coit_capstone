"""User module contains all of the components necessary for the User
class.
"""
import name
import car
import user_id

class User(object):
    """A User class object has 3 string attributes: user ID, given
    name, and family name. It also has one list attribute: cars. A User
    object can return each of its attributes.
    """
    def __init__(self, given_name, family_name, cars):
        """Take in 2 strings (a given name and a family name) and 1
        list (cars). Using the given name and family name, create a
        user_id. Set all for elements as attributes of the object.
        """
        assert name.is_valid(given_name), "User objects require a valid given name."
        self._given_name = given_name.lower()

        assert name.is_valid(family_name), "User objects require a valid family name."
        self._family_name = family_name.lower()

        self._user_id = user_id.create(given_name, family_name)

        assert car.are_valid(cars), "User objects require a valid list of car names."
        self._cars = cars

    def get_user_id(self):
        """Return User object's user ID as a string."""
        return self._user_id

    def get_given_name(self):
        """Return User object's given name as a string."""
        return self._given_name

    def get_family_name(self):
        """Return User Object's family name as a string."""
        return self._family_name

    def get_cars(self):
        """Return a list of the User Object's cars."""
        return self._cars
