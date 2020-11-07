def foo(text, type="Quote", author: str = None, **kwargs):
    """
    text: positional
    type: optional positional or keyword, with default 'Quote'
    author: optional positional or keyword of type str with default None
    kwargs: optional keyword arguments.

    foo('Hello', 'Song', 'Oscar')
    Hello, Song, Oscar, {}

    foo(text='Hello', 'Oscar')
    >>>SyntaxError: positional argument follows keyword argument

    foo(text='Hello')
    >>>Hello, Quote, None, {}

    foo('Hello', type='Novella', year=1890)
    >>>Hello, Novella, None, {'year': 1890}
    """
    print(f"{text}, {type}, {author}, {kwargs}")


class Vehicle:
    size = "small"
    weight = 500

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model


""" 
size: class variable
weight: class variable

year: instance var
make: ...
model: ... 
"""