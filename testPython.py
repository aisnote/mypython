import abc

def print_result(func):
    def modified_fun(*args, **kwargs):
        print func(*args, **kwargs)
    return modified_fun

@print_result
def add(*tup):
    return sum(tup)

"""
@print_result
def power(base, exp):
    return base ** exp
"""

def test_var_args(farg, *args):
    print "formal arg:", farg
    for arg in args:
        print "another arg:", arg

class Cat:
    def __init__(self, name):
        self.name = name
    
    def shout(self):
        print 'Meow'

class Pizza(object):
    radius = 42
    @classmethod
    def get_radius(cls):
        return cls.radius

class BasePizza(object):
    __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def get_radius(self):
         """Method that should do something."""

class ChildPizza(BasePizza):
    def get_radius(self):
        print "childPizza"


if __name__ == '__main__':
    test_var_args(1, "two", 3)
    
    my_cat = Cat('Kittly')
    my_cat.shout()

    add(1,2,3,4)

    print Pizza.get_radius()

    bp = ChildPizza()
    bp.get_radius()