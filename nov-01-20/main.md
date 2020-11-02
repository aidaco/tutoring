# Review

## Variables
- Store objects or primitive type data
- Create a variable and assign a value to it with the following syntax:
    {VARIABLE NAME} = {EXPRESSION}

## Functions
- Encapsulate functionality, allowing portability and re-use
- Declared with the following syntax:
    def {FUNCTION NAME}([args, ...], [kwargs, ...]):
        {FUNCTION BODY}
        [return {EXPRESSION}]
- Arguments (args) are values passed into the function by position, for ex.:
    def foo(data1, data2):
        print(data1)
        print(data2)
    
    >>>foo(1, 2) # data1 = 1 and data2 = 2 due to the position
- Keyword Arguments (kwargs) are values passed in by keyword (eg. name)
    def foo(data1, data2):
        print(data1)
        print(data2)
    
    >>>foo(data2 = 2, data1 = 1) # Note position doesn't matter, only the keyword.
- We can mix positional and keyword arguments together, however all positional
arguments *must* come before the keyword arguments:
    def foo(data1, data2):
        print(data1)
        print(data2)
    
    >>>foo(1, data2 = 2) # data1 = 1 by position, data2 = 2 by keyword
    >>>foo(data2 = 2, 1) # SyntaxError: positional argument after keyword argument
- Python allows us to specify default values, allowing arguments to be optional:
    def bar(num1, num2 = 2):
        print(num1+num2)
    
    >>>bar(2, 3) # num1 = 2 by position, num2 = 3 by position
    5
    >>>bar(2) # num1 = 2 by position, num2 = 2 by default
    4
- Optionally, we can specify a type for an argument:
    def bar(num1: float, num2: float = 2):
        print(num1+num2)
    
    >>>bar(2, 3) # num1 = 2 by position, num2 = 3 by position
    5
    >>>bar(2) # num1 = 2 by position, num2 = 2 by default
    4
    >>>bar('hello', 'world') # num1 = 'hello', num2 = 'world'. The type is *not checked*,
                             # Only adds additional information, *not functionality*,
                             # Python interpreters that *do* check types are available.
    'hello world'
- Functions in python can accept a variable number of arguments, functions of this
category are called 'variadic'. Declaration is as follows:
    def {FUNCTION NAME}(*args):
        {FUNCTION BODY}

    def average(*args):
        return sum(args) / len(args)

    >>>average(1, 4)
    2.5
    >>>average(1, 4, 6)
    ...
    >>>average(1, 2, 3, 4, 5, 6, 7, 8, 9)
    ...
The args object is a list-like store of all positional arguments.
Note: does not have to be named args, *must* have the asterisk (*)
- We can do similar to accept a variable of keyword arguments:
    def display_grades(**kwargs):
        for student, score in kwargs.items():
            print(f"{student} scored {score}%")
    >>>display_grades(aidan=96, albert=97, rowan=34, theresa=55)
    "aidan scored 96%"
    "albert scored 97%"
    ...
The kwargs object is a dict-like store mapping keyword to value
for all keyword arguments.
Note: does not have to be named kwargs, *must* have the double asterisk (**)
- Of course, we can have a function with variadic positional and keyword arguments:
    def foo(*args, **kwargs):
        print(f'Args: {args}')
        print(f'Kwargs: {kwargs}')

We can also have a mix of positional, keyword, and variadic arguments. However,
they *must* follow this order:
    Positional, *args, Keyword, **kwargs
For example:
    def foo(num, date, *args, is_test = False, **kwargs):
        print(f'num: {num}')
        print(f'date: {date}')
        print(f'Args: {args}')
        print(f'is_test: {is_test}')
        print(f'Kwargs: {kwargs}')

## Classes
- Encapsulate an object with both functionality and state
- Declare a new class with the following syntax:
    class {CLASS NAME}[(PARENT CLASSES, ...)]:
        {CLASS BODY}
- The class itself is a 'blueprint' for creating new instances of that type,
ex. class List, used to create various types of lists. While working with classes,
the instance is typically referred to as *self*, while the class is referred to as *cls*.
- ### Storing data in a Class
- Classes store data in two ways: class variables and instance variables. This distinction
depends on where the variable is declared and how it is to be used.
- Class Variables reside in the class itself, each instance contains a reference to the *same*
value.
    class Foo:
        version = 'WINDOWS'
    >>>Foo.version # variable lives inside the class
    'WINDOWS'
    >>>f = Foo() # Intantiate a new Foo object
    >>>f.version # Refers to the variable stored in the class, not the instance.
    'WINDOWS'
- Instance variables contain values specific to each instance. These are declared
when you assign a value to the self object:
    self.{VARIABLE NAME} = {EXPRESSION}

    class Foo:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2
    
    >>>f = Foo(1, 2)
    >>>f.num1 # Instance variable lives on the instance.
    1
    >>>Foo.num1 # AttributeError, no reference to the variable exists in the class.
- ### Adding functionality to a class
- When we declare a function inside a class, that function is special and considered
a *method*.
- Methods require a special variable, self, to be the first argument of the function:
    class Number:
        def add(self, other):
            return self + other
    >>>n = Number(1)
    >>>o = Number(2)
    >>>n.add(o) # self is *automatically* passed into the *add* method.
    3
- self allows us to access the current instance of the class containing the method.
- When we call a method, it works like this under the hood:
    >>>n = Number(1)
    >>>o = Number(2)
    >>>n.add(o) # self is *automatically* passed into the *add* method.
    >>>Number.add(n, o) # Equivalent to the preceeding line.
- Methods can take input other than the current instance.
- Methods that operate on the class are called class methods.
    class Number:
        precision = 4
        @classmethod
        def set_precision(cls, prec = 4):
            cls.precision = prec
    >>>n1 = Number(4)
    >>>n1.precision
    4
    >>>Number.set_precision(8)
    >>>n1.precision # *precision* is a class variable, so calling set_precision
                    # changes the value for *all instances*.
    8
    >>>n2 = Number(3)
    >>>n2.precision
    8
- Methods can take *no* references to the class or instance, we call these static methods:
    class Number:
        @staticmethod
        def average(num1, num2):
            return (num1 + num2) / 2
    >>>n1 = Number(4)
    >>>n2 = Number(3)
    >>>Number.average(n1, n2) # Function accessed from the class
    3.5
- Classes also provide a way to extend functionality: inheritance. For example,
suppose we had a class *ConnectionManager* for handling device communication. If we
wanted to add bluetooth capability, we might create a new class 
*BluetoothConnectionManager* which inherits the functionality of *ConnectionManager*
and adds only the new code required to enable blutooth.
Note: inheritance is a tricky concept, often times *composition* of objects is
better.
Syntax:
    class {CLASS NAME}[({PARENT CLASS1}, {PARENT CLASS 2}, ...)]:
        {CLASS BODY}
- Class instantiation is controlled by the __init__ method, which we can override
to customize functionality:
    class {CLASS NAME}[(PARENT CLASSES, ...)]:
        {CLASS BODY}
        def __init__(self [, args, kwargs, ...]):