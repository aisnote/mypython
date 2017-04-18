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


if __name__ == '__main__':
    test_var_args(1, "two", 3)
    
    my_cat = Cat('Kittly')
    my_cat.shout()

    add(1,2,3,4)