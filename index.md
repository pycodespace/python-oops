```markdown
Python class names should follow the `PascalCase` convention. This means the first letter of each word in the class name should be capitalized, and there should be no spaces between words.

Here's an example of a Python class named according to this convention:

```python
class Employee:
    # defining the properties and assigning them none
    ID = None
    salary = None
    department = None

    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department


    # def __init__(self, ID=None, salary=0, department=None):
    #     self.ID = ID
    #     self.salary = salary
    #     self.department = department

    def __init__(self):
        # Initialize the class
        pass 
```

In this example, `Employee` is the class name, and it follows the `PascalCase` convention.

The class `Employee` has an `__init__` method, which is a special method in Python classes. This method is called when an instance of the class is created, and it initializes the attributes of the class. In this case, the `Employee` class does not have any attributes, so the `__init__` method is empty.

You can create an instance of the `Employee` class and use it in your Python code. For example:

```python
employee = Employee()
employee.ID = 123
employee.salary = 50000
employee.department = "IT"

# creating an object of the Employee class with default parameters
steve = Employee(3789, 2500, "Human Resources")

```

This will create an instance of the `Employee` class named `employee`. You can then use this instance to access the methods and attributes of the class.
```


In Python, properties can be defined into two parts:

Class variables
Instance variables
Class variables are defined outside the initializer and instance variables are defined inside the initializer.



#### Getters and Setters
In Python, getters and setters are not explicitly defined as in other programming languages like Java or C++. However, you can achieve similar functionality using property decorators.

Property decorators allow you to define custom behavior for accessing and modifying attributes of a class. 
There are three main property decorators: `@property`, `@<attribute>.setter`, and `@<attribute>.deleter`.

Here's an example of how to use property decorators to create getters and setters for an `Employee` class:

```python
class Employee:
    def __init__(self, ID, salary, department):
        self._ID = ID
        self._salary = salary
        self._department = department

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department
```

In this example, we define private attributes for `ID`, `salary`, and `department` using the `_` prefix. Then, we use property decorators to create getters and setters for these attributes.

Here's how you can use these getters and setters:

```python
employee = Employee(123, 50000, "IT")
print(employee.ID)  # Output: 123
employee.ID = 456
print(employee.ID)  # Output: 456

print(employee.salary)  # Output: 50000
employee.salary = 60000
print(employee.salary)  # Output: 60000

print(employee.department)  # Output: IT
employee.department = "HR"
print(employee.department)  # Output: HR
```

In this example, we access the getter methods (`ID`, `salary`, `department`) using the dot notation. We can also modify the values of these attributes using the setter methods.

By using property decorators, you can achieve similar functionality to getters and setters in Python. However, it's important to note that this approach is not as common as using public attributes directly.

##### Inheritance / Super class/Base Class 
In Python, a class can have a parent class, also known as a superclass or base class. The class that inherits or extends the superclass is called a child class or derived class.

Here's an example to illustrate the concept of parent and child classes:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!

cat = Cat("Whiskers")
print(cat.name)  # Output: Whiskers
print(cat.speak())  # Output: Meow!
```

In this example, the `Animal` class is the parent class, and the `Dog` and `Cat` classes are the child classes. The `Dog` and `Cat` classes inherit the properties and methods from the `Animal` class.

The `Dog` and `Cat` classes override the `speak` method to provide their own implementation. The `Dog` class returns "Woof!" when the `speak` method is called, and the `Cat` class returns "Meow!" when the `speak` method is called.

By using parent and child classes, you can achieve code reusability and create a hierarchical structure of classes. This helps in organizing and managing complex codebases.

### Polymorphism Using Methods


class Shape:
    def __init__(self):  # initializing sides of all shapes to 0
        self.sides = 0

    def getArea(self):
        pass


class Rectangle(Shape):  # derived from Shape class
    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area
    def getArea(self):
        return (self.width * self.height)


class Circle(Shape):  # derived from Shape class
    # initializer
    def __init__(self, radius=0):
        self.radius = radius

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of circle is:", str(shapes[1].getArea()))


### Method Overriding
* The method in the parent class is called the overridden method, The methods in the child classes are called the overriding methods.
```python
class Shape:
    def __init__(self):  # initializing sides of all shapes to 0
        self.sides = 0

    def getArea(self):
        pass


class Rectangle(Shape):  # derived form Shape class
    # initializer
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    # method to calculate Area
    def getArea(self):
        return (self.width * self.height)


class Circle(Shape):  # derived form Shape class
    # initializer
    def __init__(self, radius=0):
        self.radius = radius

    # method to calculate Area
    def getArea(self):
        return (self.radius * self.radius * 3.142)


shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of circle is:", str(shapes[1].getArea()))

```

#### Operator overloading 
Operator overloading is a feature in Python that allows you to define custom behavior for operators such as addition, subtraction, multiplication, and others. By using operator overloading, you can make your classes more intuitive and expressive.

Here's an example to illustrate operator overloading in Python:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)  # Output: Vector(4, 6)
print(v1 - v2)  # Output: Vector(2, 2)
print(v1 * 2)  # Output: Vector(6, 8)
```

In this example, we define a `Vector` class that represents a 2D vector. We overload the addition (`+`), subtraction (`-`), and multiplication (`*`) operators to perform vector operations.

The `__add__`, `__sub__`, and `__mul__` methods are special methods in Python that are called when the corresponding operators are used. These methods allow us to define custom behavior for the operators.

The `__str__` method is also overridden to provide a string representation of the `Vector` object.

By using operator overloading, we can make our classes more intuitive and expressive. In this example, we can perform vector operations using the familiar addition, subtraction, and multiplication operators.

Operator overloading is a powerful feature in Python that allows you to extend the behavior of built-in operators to work with custom classes. It enables you to create more expressive and intuitive code, making your classes more versatile and reusable.

#### Abstract Base Class

Abstract Base Classes (ABCs) are a feature in Python that allows you to create a blueprint for other classes. They are used to define a common interface or behavior for a set of related classes. ABCs cannot be instantiated directly, but they can be subclassed to create concrete classes.

An ABC is defined by creating a class that inherits from the `abc` module's `ABC` class. Inside the ABC, you can define abstract methods, which are methods that must be implemented by any subclass. Abstract methods are declared using the `@abstractmethod` decorator.

Here's an example of an ABC in Python:

```python
import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        print("Eating...")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


dog = Dog()
dog.make_sound()  # Output: Woof!
dog.eat()  # Output: Eating...

cat = Cat()
cat.make_sound()  # Output: Meow!
cat.eat()  # Output: Eating...
```

In this example, we define an ABC called `Animal` that has an abstract method called `make_sound`. We then create two subclasses, `Dog` and `Cat`, that implement the `make_sound` method. Both subclasses can be instantiated and used interchangeably with the `Animal` ABC.

Using ABCs, you can enforce a common interface or behavior for a set of related classes, making your code more modular and easier to maintain. They also help to prevent errors by ensuring that all subclasses implement the required methods.

In summary, Abstract Base Classes (ABCs) in Python allow you to create a blueprint for other classes, defining a common interface or behavior. They can be used to enforce a consistent interface and promote code reusability.


####  Relationships between classes

There are three main class relationships :
**IS A**
**Part-of**
**Has-a (Association)**


IS A (Inheritance): A class inherits properties and behaviors from another class.
Part-of (Composition): A class is composed of other classes, allowing for code reusability and flexibility.
Has-a (Association): A class has a reference to another class, allowing for more flexibility and code reusability.
Aggregation: A class is composed of other classes, but the ownership and lifecycle of the aggregated objects are not tied to the owner class.

1. IS A (Inheritance): This relationship occurs when a class inherits properties and behaviors from another class. In the given example, the `Dog` and `Cat` classes inherit from the `Animal` class. This relationship allows the `Dog` and `Cat` classes to reuse the code defined in the `Animal` class.

The relationship between the `Dog` and `Cat` classes in the given example is an "IS A" relationship. This means that the `Dog` and `Cat` classes inherit from the `Animal` class. In other words, a `Dog` is an `Animal`, and a `Cat` is also an `Animal`. This relationship allows the `Dog` and `Cat` classes to reuse the code defined in the `Animal` class, such as the `eat` method.

The "IS A" relationship is a fundamental concept in object-oriented programming (OOP) that helps to model real-world relationships between objects. It allows you to create a hierarchical structure of classes, where each class inherits from a parent class and can be used interchangeably with its parent class.

In summary, the "IS A" relationship in the given example demonstrates the inheritance feature of Python. The `Dog` and `Cat` classes inherit from the `Animal` class, allowing them to reuse the code defined in the `Animal` class. This relationship helps to create a more modular and organized codebase, making it easier to maintain and extend.

2. Part-of (Composition): This relationship occurs when a class is composed of other classes. In the given example, the `Employee` class has attributes that are instances of other classes (`ID`, `salary`, and `department`). This relationship allows the `Employee` class to reuse the code defined in the other classes.

Certainly! Here's an example to illustrate the "Part-of" (Composition) relationship:

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine started with {self.horsepower} horsepower.")


class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def start(self):
        print(f"Starting {self.make} {self.model} {self.year}.")
        self.engine.start()


engine = Engine(200)
car = Car("Toyota", "Corolla", 2022, engine)
car.start()
```

In this example, the `Engine` class represents an engine with a certain horsepower. The `Car` class represents a car, which is composed of an engine. The `Car` class has an attribute called `engine`, which is an instance of the `Engine` class.

When the `start` method of the `Car` class is called, it also calls the `start` method of the `Engine` class. This demonstrates the "Part-of" (Composition) relationship, where the `Car` class is composed of the `Engine` class.

By using composition, you can create more complex and flexible systems by combining different classes together. In this example, the `Car` class can have any type of engine, as long as it is an instance of the `Engine` class. This allows for code reusability and flexibility.



3. Has-a (Association): This relationship occurs when a class has a reference to another class. In the given example, the `Rectangle` and `Circle` classes have attributes that are instances of the `Vector` class. This relationship allows the `Rectangle` and `Circle` classes to use the code defined in the `Vector` class.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, position, width, height):
        self.position = position
        self.width = width
        self.height = height


class Circle:
    def __init__(self, position, radius):
        self.position = position
        self.radius = radius


# Creating instances of Vector, Rectangle, and Circle classes
vector = Vector(1, 2)
rectangle = Rectangle(vector, 5, 10)
circle = Circle(vector, 3)

# Accessing attributes of the Rectangle and Circle classes
print(rectangle.position.x, rectangle.position.y)  # Output: 1 2
print(circle.position.x, circle.position.y)  # Output: 1 2
```

In the provided code, we define three classes: `Vector`, `Rectangle`, and `Circle`. The `Rectangle` and `Circle` classes have attributes that are instances of the `Vector` class, demonstrating the "Has-a" (Association) relationship.

We create instances of the `Vector`, `Rectangle`, and `Circle` classes, and then access the attributes of the `Rectangle` and `Circle` classes to showcase the relationship. The output confirms that the `Rectangle` and `Circle` classes have attributes that are instances of the `Vector` class.

### Aggregation
Aggregation allows for more flexibility and code reusability compared to composition. It allows the owner class to have a reference to the aggregated objects, but the ownership and lifecycle of the aggregated objects are not tied to the owner class
``` python
class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population = population

    def printDetails(self):
        print("Country Name:", self.name)
        print("Country Population", self.population)


class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Person Name:", self.name)
        self.country.printDetails()


c = Country("Wales", 1500)
p = Person("Joe", c)
p.printDetails()

# deletes the object p
del p
print("")
c.printDetails()
```
As we can see, the Country object c lives on even after we delete the Person object p. This creates a weaker relationship between the two classes.