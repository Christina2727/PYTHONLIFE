print(abs(10))
print(abs(-10))

steps = -3
if abs(steps) > 0:
    print('character is moving')


dir(['a', 'short', 'list'])
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: C:/Users/Christina/Desktop/PYTHONLIFE/NOV1-30/nov 30 PM.py ====
10
10
>>> 
==== RESTART: C:/Users/Christina/Desktop/PYTHONLIFE/NOV1-30/nov 30 PM.py ====
10
10
character is moving
>>> 
==== RESTART: C:/Users/Christina/Desktop/PYTHONLIFE/NOV1-30/nov 30 PM.py ====
10
10
character is moving
>>> dir(['a', 'short', 'list'])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> popcorn = 'I love popcorn'
>>> dir(popcorn)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(popcorn.upper)
Help on built-in function upper:

upper(...) method of builtins.str instance
    S.upper() -> str
    
    Return a copy of S converted to uppercase.

>>> help(for)
SyntaxError: invalid syntax
>>> help(keywords)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    help(keywords)
NameError: name 'keywords' is not defined
>>> eval('10*5')
50
>>> print('10*5')
10*5
>>> your_calculation = input('Enter a calculation')
Enter a calculation12*52
>>> eval(your_calculation)
624
>>> my_small_function = '''print('ham')
print('sandwhich')'''
>>> exec(my_small_program)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    exec(my_small_program)
NameError: name 'my_small_program' is not defined
>>> my_small_program = '''print('ham')
print('sandwhich')'''
>>> exec(my_small_program)
ham
sandwhich
>>> float('12')
12.0
>>> float('123.456789')
123.456789
>>> your_age = input('Enter your age: ')
Enter your age: 20
>>> age = float(your_age)
>>> if age > 13:
	print('you are %s years too old' %  (age -13))

	
you are 7.0 years too old
>>> int(123.456)
123
>>> int('123')
123
>>> int('123.456')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int('123.456')
ValueError: invalid literal for int() with base 10: '123.456'
>>> len('this is a test')
14
>>> len('this is a test string')
21
>>> 
