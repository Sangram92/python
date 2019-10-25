- **What is the difference between `__init__` and `__call__`?**

Defining a custom `__call__()` method in the meta-class allows the class's instance to be called as a function, not always modifying the instance itself.
```
In [1]: class A:
   ...:     def __init__(self):
   ...:         # constructor
   ...:         print "init"
   ...:         
   ...:     def __call__(self):
   ...:         #  implements function call operator.
   ...:         print "call"
   ...:         
   ...:         

In [2]: a = A()
init

In [3]: a()
call
```