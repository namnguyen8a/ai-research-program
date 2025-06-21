# Exercises: Python Object-Oriented Programming

This file contains a series of exercises to practice the concepts covered in the lecture. The problems start simple and build up to a final project that integrates multiple skills.

## Topic-by-Topic Exercises

_These are focused exercises designed to test your understanding of a single topic at a time._

---

### Exercise 1: Classes and Objects
*   **Scenario:** You are building a digital library and need to represent a book. A book has a title, an author, and a number of pages.
*   **Task:** Create a `Book` class that models this information.
*   **Requirements:**
    *   The class should be named `Book`.
    *   It must have an `__init__` method that accepts `title`, `author`, and `pages` as arguments.
    *   These arguments should be stored as attributes on the object.
    *   Include a method `get_info()` that returns a formatted string: `"Title: [title], Author: [author], Pages: [pages]"`.
*   **Test Case:**
    *   **Input:** `my_book = Book("The Hobbit", "J.R.R. Tolkien", 310)` followed by `my_book.get_info()`
    *   **Expected Output:** `'Title: The Hobbit, Author: J.R.R. Tolkien, Pages: 310'`

---

### Exercise 2: Classes and Objects
*   **Scenario:** You are developing a simple banking application. A core component is the bank account, which holds a balance and allows for deposits and withdrawals.
*   **Task:** Create a `BankAccount` class.
*   **Requirements:**
    *   The `__init__` method should take an `initial_balance` (defaulting to 0) and a `account_holder_name`.
    *   Implement a `deposit(amount)` method that adds to the balance.
    *   Implement a `withdraw(amount)` method that subtracts from the balance but does not allow the balance to go below zero. If a withdrawal is invalid, the balance should not change.
    *   Implement a `get_balance()` method that returns the current balance.
*   **Test Case:**
    *   **Input:**
        ```python
        account = BankAccount("John Doe", 100)
        account.deposit(50)
        account.withdraw(80)
        account.withdraw(100) # This should fail
        print(account.get_balance())
        ```
    *   **Expected Output:** `70`

---

### Exercise 3: Classes and Objects
*   **Scenario:** You're working on a student information system. You need to model a student who has a name and a list of grades.
*   **Task:** Create a `Student` class that can store grades and calculate their average.
*   **Requirements:**
    *   The `__init__` method takes a `name` and initializes an empty list for `grades`.
    *   Create an `add_grade(grade)` method that adds an integer grade to the list.
    *   Create a `get_average_grade()` method that calculates and returns the average of the grades in the list. If there are no grades, it should return 0.
*   **Test Case:**
    *   **Input:**
        ```python
        student = Student("Jane Smith")
        student.add_grade(85)
        student.add_grade(92)
        student.add_grade(78)
        print(student.get_average_grade())
        ```
    *   **Expected Output:** `85.0`

---

### Exercise 4: Classes and Objects
*   **Scenario:** You are creating a simple graphics library and need a way to represent a rectangle.
*   **Task:** Define a `Rectangle` class with methods to calculate its area and perimeter.
*   **Requirements:**
    *   The `__init__` method should accept `width` and `height`.
    *   A method `calculate_area()` should return the area (`width * height`).
    *   A method `calculate_perimeter()` should return the perimeter (`2 * (width + height)`).
*   **Test Case:**
    *   **Input:** `rect = Rectangle(10, 5)` followed by `rect.calculate_area()` and `rect.calculate_perimeter()`
    *   **Expected Output:** `50` and `30` respectively.

---

### Exercise 5: Classes and Objects
*   **Scenario:** You're building a simulation of a car. The car has a make, model, and can be started or stopped. It also needs to track its mileage.
*   **Task:** Create a `Car` class to represent this simulation.
*   **Requirements:**
    *   `__init__` takes `make` and `model`. It should also initialize `mileage` to 0 and `is_running` to `False`.
    *   A `start_engine()` method that sets `is_running` to `True` and prints a message like `"Engine started."`.
    *   A `stop_engine()` method that sets `is_running` to `False` and prints a message like `"Engine stopped."`.
    *   A `drive(kilometers)` method that only adds to `mileage` if the engine is running (`is_running` is `True`).
*   **Test Case:**
    *   **Input:**
        ```python
        my_car = Car("Toyota", "Corolla")
        my_car.drive(50) # Should not add mileage
        my_car.start_engine()
        my_car.drive(120)
        my_car.stop_engine()
        my_car.drive(30) # Should not add mileage
        print(my_car.mileage)
        ```
    *   **Expected Output:** `120`

---

### Exercise 1: Encapsulation
*   **Scenario:** You're creating a `Person` class for an HR system. To protect privacy, a person's age should not be directly modifiable from outside the class.
*   **Task:** Create a `Person` class with a private attribute for age.
*   **Requirements:**
    *   The class `Person` has an `__init__` that takes a `name` and an initial `age`.
    *   The `age` should be stored in a private attribute (e.g., `__age`).
    *   Provide a public "getter" method `get_age()` that returns the value of the private age attribute.
    *   Do *not* provide a public "setter" method.
*   **Test Case:**
    *   **Input:**
        ```python
        p = Person("Alice", 30)
        # Attempting p.__age = 40 should not change the internal state
        print(p.get_age())
        ```
    *   **Expected Output:** `30`

---

### Exercise 2: Encapsulation
*   **Scenario:** You are improving the `BankAccount` class. To prevent accidental or malicious changes, the balance must be private. All modifications should happen through `deposit` and `withdraw` methods.
*   **Task:** Refactor the `BankAccount` class to use encapsulation for the balance.
*   **Requirements:**
    *   The `balance` attribute should be private (e.g., `__balance`).
    *   The `deposit` and `withdraw` methods should correctly modify this private attribute.
    *   The `get_balance` method should return the value of the private balance.
    *   Direct access like `account.__balance = 1000000` from outside the class should not affect the balance returned by `get_balance()`.
*   **Test Case:**
    *   **Input:**
        ```python
        account = BankAccount("Bob", 500)
        account.deposit(100)
        try:
            account.__balance = 9999 # This should not work
        except AttributeError:
            pass # Expected behavior
        print(account.get_balance())
        ```
    *   **Expected Output:** `600`

---

### Exercise 3: Encapsulation
*   **Scenario:** You're designing an `Employee` class. The employee's salary is sensitive information. It should be "protected," indicating that it's for internal use or for use by subclasses, but not for general public access.
*   **Task:** Create an `Employee` class with a protected salary attribute.
*   **Requirements:**
    *   The class `Employee` takes `name` and `salary` in its constructor.
    *   Store the salary in a protected attribute (e.g., `_salary`).
    *   Create a public method `get_details()` that returns a string with the employee's name and salary.
*   **Test Case:**
    *   **Input:** `emp = Employee("Charlie", 50000)` followed by `emp.get_details()`
    *   **Expected Output:** `'Name: Charlie, Salary: 50000'`

---

### Exercise 4: Encapsulation
*   **Scenario:** You are programming a smart coffee machine. The machine has internal reservoirs for water and coffee beans, which should not be set directly. The user can only press a button to make coffee.
*   **Task:** Create a `CoffeeMachine` class that hides its internal state.
*   **Requirements:**
    *   `__init__` should initialize private attributes `__water_level` and `__beans_level` to a starting value (e.g., 1000 ml and 500 g).
    *   A public method `make_coffee()` checks if there's enough water (e.g., >50) and beans (e.g., >20).
    *   If there are enough resources, it should subtract the required amounts from the private attributes and return `"Enjoy your coffee!"`.
    *   If not, it should return `"Not enough water or beans."` without changing the levels.
*   **Test Case:**
    *   **Input:**
        ```python
        machine = CoffeeMachine() # Assume it requires 50 water, 20 beans
        # Simulate making coffee until resources run out
        for _ in range(20):
            machine.make_coffee()
        print(machine.make_coffee())
        ```
    *   **Expected Output:** `"Not enough water or beans."`

---

### Exercise 5: Encapsulation
*   **Scenario:** You're building a `SmartThermostat`. The temperature can be adjusted, but only within a safe range (e.g., 16°C to 30°C) to prevent damage or excessive energy use.
*   **Task:** Create a `SmartThermostat` class that enforces temperature limits.
*   **Requirements:**
    *   `__init__` sets an initial private temperature, `__current_temp` (e.g., 20).
    *   A public `get_temp()` method returns the current temperature.
    *   A public `set_temp(new_temp)` method that only changes `__current_temp` if `new_temp` is between 16 and 30 (inclusive). If the new temperature is outside the range, the temperature remains unchanged.
*   **Test Case:**
    *   **Input:**
        ```python
        thermo = SmartThermostat(20)
        thermo.set_temp(25)
        thermo.set_temp(35) # This should be ignored
        print(thermo.get_temp())
        ```
    *   **Expected Output:** `25`

---

### Exercise 1: Inheritance
*   **Scenario:** You are modeling the animal kingdom. All animals can eat, but specific animals have unique behaviors.
*   **Task:** Create a base `Animal` class and a `Dog` class that inherits from it.
*   **Requirements:**
    *   The `Animal` class should have a method `eat()` that prints `"This animal is eating."`.
    *   The `Dog` class should inherit from `Animal`.
    *   The `Dog` class should have its own method `bark()` that prints `"Woof!"`.
*   **Test Case:**
    *   **Input:**
        ```python
        d = Dog()
        d.eat()
        d.bark()
        ```
    *   **Expected Output:**
        ```
        This animal is eating.
        Woof!
        ```

---

### Exercise 2: Inheritance
*   **Scenario:** You are building a system to catalog vehicles. All vehicles have a brand and model, but a car is a specific type of vehicle with a certain number of doors.
*   **Task:** Create a `Vehicle` superclass and a `Car` subclass.
*   **Requirements:**
    *   `Vehicle` class `__init__` should take `brand` and `model`.
    *   `Car` class should inherit from `Vehicle`.
    *   `Car` class `__init__` should take `brand`, `model`, and `num_doors`. It must call the parent's `__init__` method to set the brand and model.
    *   `Car` should have a `get_details()` method that returns a string like `"Brand: [brand], Model: [model], Doors: [num_doors]"`.
*   **Test Case:**
    *   **Input:** `my_car = Car("Ford", "Mustang", 2)` followed by `my_car.get_details()`
    *   **Expected Output:** `'Brand: Ford, Model: Mustang, Doors: 2'`

---

### Exercise 3: Inheritance
*   **Scenario:** In an HR system, a Manager is a type of Employee. They share common attributes like name and salary, but a Manager also gets a bonus.
*   **Task:** Create an `Employee` superclass and a `Manager` subclass that extends it.
*   **Requirements:**
    *   `Employee` class `__init__` takes `name` and `salary`. It has a method `get_annual_salary()` that returns the salary.
    *   `Manager` class inherits from `Employee`.
    *   `Manager` class `__init__` takes `name`, `salary`, and `bonus`.
    *   `Manager` should override the `get_annual_salary()` method to return the sum of the salary and the bonus.
*   **Test Case:**
    *   **Input:** `mgr = Manager("David", 80000, 15000)` followed by `mgr.get_annual_salary()`
    *   **Expected Output:** `95000`

---

### Exercise 4: Inheritance
*   **Scenario:** You need to model different types of staff at a school. There are general `Staff` members, `Teachers` who are a type of staff, and a `Principal` who is a type of teacher.
*   **Task:** Implement a multi-level inheritance chain: `Staff` -> `Teacher` -> `Principal`.
*   **Requirements:**
    *   `Staff` has an `__init__` with `staff_id` and a method `work()`.
    *   `Teacher` inherits from `Staff`, adds a `subject` attribute, and has a method `teach()`.
    *   `Principal` inherits from `Teacher` and has a method `manage_school()`.
    *   An instance of `Principal` should have access to methods from all three levels (`work`, `teach`, `manage_school`).
*   **Test Case:**
    *   **Input:** `p = Principal("P001", "Math")` followed by `p.work()`, `p.teach()`, and `p.manage_school()`.
    *   **Expected Output:** The corresponding print statements from each method should execute without error. (e.g., `Principal is working`, `Principal is teaching Math`, `Principal is managing the school`).

---

### Exercise 5: Inheritance
*   **Scenario:** In a fantasy game, some creatures can fly, and some can swim. A Griffin is a mythical creature that can do both.
*   **Task:** Use multiple inheritance to create a `Griffin` class.
*   **Requirements:**
    *   Create a `FlyingCreature` class with a `fly()` method.
    *   Create a `MythicalCreature` class with a `roar()` method.
    *   Create a `Griffin` class that inherits from *both* `FlyingCreature` and `MythicalCreature`.
    *   The `Griffin` object should be able to call both `fly()` and `roar()`.
*   **Test Case:**
    *   **Input:**
        ```python
        g = Griffin()
        g.fly()
        g.roar()
        ```
    *   **Expected Output:** The print statements from both `fly()` and `roar()` methods should be displayed.

---

### Exercise 1: Polymorphism and Method Overriding
*   **Scenario:** You are modeling different shapes for a drawing application. All shapes can be drawn, but the way they are drawn is different.
*   **Task:** Demonstrate polymorphism using a `Shape` superclass and two subclasses, `Circle` and `Square`.
*   **Requirements:**
    *   The `Shape` class has a method `draw()` that prints `"Drawing a shape"`.
    *   The `Circle` class inherits from `Shape` and overrides `draw()` to print `"Drawing a circle"`.
    *   The `Square` class inherits from `Shape` and overrides `draw()` to print `"Drawing a square"`.
    *   Create a function `render(shape_object)` that takes any shape object and calls its `draw()` method.
*   **Test Case:**
    *   **Input:**
        ```python
        shapes = [Circle(), Square()]
        for shape in shapes:
            render(shape)
        ```
    *   **Expected Output:**
        ```
        Drawing a circle
        Drawing a square
        ```

---

### Exercise 2: Polymorphism and Method Overriding
*   **Scenario:** A document processing system handles different file types. Each file type needs to be opened, but the process might differ.
*   **Task:** Create a `Document` class and two subclasses, `PdfDocument` and `WordDocument`, to show polymorphic behavior.
*   **Requirements:**
    *   `Document` class has a method `open()` that raises a `NotImplementedError`.
    *   `PdfDocument` overrides `open()` to print `"Opening PDF document..."`.
    *   `WordDocument` overrides `open()` to print `"Opening Word document..."`.
    *   Create a list containing an instance of `PdfDocument` and `WordDocument` and loop through it, calling `open()` on each.
*   **Test Case:**
    *   **Input:**
        ```python
        docs = [PdfDocument(), WordDocument()]
        for doc in docs:
            doc.open()
        ```
    *   **Expected Output:**
        ```
        Opening PDF document...
        Opening Word document...
        ```

---

### Exercise 3: Polymorphism and Method Overriding
*   **Scenario:** A payroll system needs to calculate the weekly pay for different types of employees. Salaried employees get a fixed weekly amount, while hourly employees are paid based on hours worked.
*   **Task:** Design `Employee`, `SalariedEmployee`, and `HourlyEmployee` classes.
*   **Requirements:**
    *   The `Employee` base class has an `__init__` with a `name` and a `calculate_pay()` method.
    *   `SalariedEmployee` inherits from `Employee`, takes a `weekly_salary` in its `__init__`, and overrides `calculate_pay()` to return this fixed salary.
    *   `HourlyEmployee` inherits from `Employee`, takes an `hourly_rate` and `hours_worked` in its `__init__`, and overrides `calculate_pay()` to return `hourly_rate * hours_worked`.
*   **Test Case:**
    *   **Input:**
        ```python
        salaried = SalariedEmployee("Alice", 1000)
        hourly = HourlyEmployee("Bob", 20, 45)
        print(salaried.calculate_pay())
        print(hourly.calculate_pay())
        ```
    *   **Expected Output:**
        ```
        1000
        900
        ```

---

### Exercise 4: Polymorphism and Method Overriding
*   **Scenario:** You're building a notification system that can send alerts via email or SMS. The core action is `send`, but the implementation details vary.
*   **Task:** Create a `Notification` base class and `EmailNotification` and `SMSNotification` subclasses.
*   **Requirements:**
    *   `Notification` has a method `send(message)`.
    *   `EmailNotification` overrides `send(message)` to print `"Sending email: [message]"`.
    *   `SMSNotification` overrides `send(message)` to print `"Sending SMS: [message]"`.
    *   Create a function `send_alert(notification_channel, message)` that calls the `send` method on the provided channel object.
*   **Test Case:**
    *   **Input:**
        ```python
        email_channel = EmailNotification()
        sms_channel = SMSNotification()
        send_alert(email_channel, "System critical error!")
        send_alert(sms_channel, "Maintenance window at 2 AM.")
        ```
    *   **Expected Output:**
        ```
        Sending email: System critical error!
        Sending SMS: Maintenance window at 2 AM.
        ```

---

### Exercise 5: Polymorphism and Method Overriding
*   **Scenario:** In a video game, different character classes (Warrior, Mage) can perform a special attack. The attack's name and effect are unique to each class.
*   **Task:** Model this with a `Character` class and `Warrior` and `Mage` subclasses.
*   **Requirements:**
    *   `Character` base class has a `special_attack()` method.
    *   `Warrior` overrides `special_attack()` to return `"Whirlwind Strike!"`.
    *   `Mage` overrides `special_attack()` to return `"Fireball!"`.
    *   Create a function `trigger_special_move(character)` that takes any character object and prints the result of its `special_attack()` method.
*   **Test Case:**
    *   **Input:**
        ```python
        grom = Warrior()
        jaina = Mage()
        trigger_special_move(grom)
        trigger_special_move(jaina)
        ```
    *   **Expected Output:**
        ```
        Whirlwind Strike!
        Fireball!
        ```

---

### Exercise 1: Abstraction
*   **Scenario:** You need to define a contract for what a "database connection" must be able to do, without worrying about whether it's MySQL, PostgreSQL, or SQLite.
*   **Task:** Create an abstract base class `Database` using the `abc` module.
*   **Requirements:**
    *   Import `ABC` and `abstractmethod` from the `abc` module.
    *   Define an abstract class `Database` that inherits from `ABC`.
    *   Inside `Database`, define two abstract methods: `connect()` and `disconnect()`.
    *   Create a concrete class `MySQLConnection` that inherits from `Database` and implements both methods with simple print statements.
*   **Test Case:**
    *   **Input:** Attempting to instantiate the abstract class `db = Database()`
    *   **Expected Output:** `TypeError: Can't instantiate abstract class Database with abstract methods connect, disconnect`

---

### Exercise 2: Abstraction
*   **Scenario:** You're building an e-commerce platform that supports multiple payment gateways (like Stripe, PayPal). You want to ensure any new gateway you add has the same standard methods.
*   **Task:** Create a `PaymentGateway` abstract base class.
*   **Requirements:**
    *   Use the `abc` module.
    *   Define an abstract class `PaymentGateway`.
    *   Define an abstract method `process_payment(amount)`.
    *   Create a concrete class `StripeGateway` that implements `process_payment` to print `"Processing ${amount} payment with Stripe."`.
    *   Create another concrete class `PayPalGateway` that implements `process_payment` to print `"Processing ${amount} payment with PayPal."`.
*   **Test Case:**
    *   **Input:**
        ```python
        stripe = StripeGateway()
        paypal = PayPalGateway()
        stripe.process_payment(100)
        paypal.process_payment(75)
        ```
    *   **Expected Output:**
        ```
        Processing $100 payment with Stripe.
        Processing $75 payment with PayPal.
        ```

---

### Exercise 3: Abstraction
*   **Scenario:** You are modeling media players. All players should be able to `play`, `pause`, and `stop`, but the underlying logic is different for an `AudioPlayer` vs. a `VideoPlayer`.
*   **Task:** Create a `MediaPlayer` ABC to enforce this structure.
*   **Requirements:**
    *   Define a `MediaPlayer` ABC.
    *   It should have three abstract methods: `play()`, `pause()`, and `stop()`.
    *   Create a concrete class `AudioPlayer` that inherits from `MediaPlayer` and implements all three methods with print statements (e.g., `"Playing audio..."`).
*   **Test Case:**
    *   **Input:** Create an `AudioPlayer` instance and call its `play()` method.
    *   **Expected Output:** `"Playing audio..."`

---

### Exercise 4: Abstraction
*   **Scenario:** You are designing a system that can export data into different formats (CSV, JSON). You want a standard interface for all data exporters.
*   **Task:** Create a `DataExporter` abstract base class.
*   **Requirements:**
    *   Define a `DataExporter` ABC.
    *   It must have one abstract method `export(data)`, which should take a dictionary as an argument.
    *   Create a `JsonExporter` class that implements `export` to convert the dictionary to a JSON string and return it.
    *   Create a `CsvExporter` class that implements `export` to convert the dictionary into a simple comma-separated string `key,value\nkey,value` and return it.
*   **Test Case:**
    *   **Input:**
        ```python
        data = {'name': 'John', 'age': 30}
        json_exporter = JsonExporter()
        print(json_exporter.export(data))
        ```
    *   **Expected Output:** `{"name": "John", "age": 30}` (or an equivalent JSON string)

---

### Exercise 5: Abstraction
*   **Scenario:** You are creating a framework for building robots. Every robot must have a way to report its status and perform a primary function, but the details depend on the robot's type.
*   **Task:** Create a `Robot` ABC and a `CleaningRobot` implementation.
*   **Requirements:**
    *   The `Robot` ABC should have a regular `__init__` that takes a `name`.
    *   It should have one abstract method `perform_task()`.
    *   It should have one *concrete* method `report_status()` that prints `"Robot [name] is operational."`.
    *   The `CleaningRobot` class should inherit from `Robot`, implement `perform_task()` to print `"Cleaning the floor..."`, and be able to use the `report_status()` method from the parent.
*   **Test Case:**
    *   **Input:**
        ```python
        roomba = CleaningRobot("Roomba-9000")
        roomba.report_status()
        roomba.perform_task()
        ```
    *   **Expected Output:**
        ```
        Robot Roomba-9000 is operational.
        Cleaning the floor...
        ```

---

### Exercise 1: Static and Class Methods
*   **Scenario:** You need a simple utility class for mathematical operations that doesn't require an instance to be created.
*   **Task:** Create a `Calculator` class with a static method for addition.
*   **Requirements:**
    *   Define a class `Calculator`.
    *   Inside it, define a `staticmethod` called `add` that takes two arguments, `a` and `b`, and returns their sum.
    *   You should be able to call this method directly on the class without creating a `Calculator` object.
*   **Test Case:**
    *   **Input:** `Calculator.add(5, 7)`
    *   **Expected Output:** `12`

---

### Exercise 2: Static and Class Methods
*   **Scenario:** You are building a system that needs to validate user data. You want to group validation functions inside a `Validator` class.
*   **Task:** Create a `Validator` class with a static method to check if an email is valid (in a very simple way).
*   **Requirements:**
    *   Define a class `Validator`.
    *   Create a `staticmethod` called `is_valid_email` that takes an email string as input.
    *   The method should return `True` if the string contains an `@` symbol and a `.` symbol, and `False` otherwise.
*   **Test Case:**
    *   **Input:** `Validator.is_valid_email("test@example.com")` and `Validator.is_valid_email("invalid-email")`
    *   **Expected Output:** `True` and `False` respectively.

---

### Exercise 3: Static and Class Methods
*   **Scenario:** You have a `User` class. You want to provide an alternative way to create a `User` object, not just from their age, but from their birth year.
*   **Task:** Add a class method to the `User` class to instantiate it from a birth year.
*   **Requirements:**
    *   The `User` class has a standard `__init__(self, name, age)`.
    *   Create a `classmethod` called `from_birth_year`.
    *   This method should accept the class itself (`cls`), a `name`, and a `birth_year`.
    *   Inside the method, calculate the age (e.g., `current_year - birth_year`) and return a new instance of the class by calling `cls(name, calculated_age)`.
*   **Test Case:**
    *   **Input:** `user = User.from_birth_year("Alice", 1990)` (assuming current year is 2023)
    *   **Expected Output:** The `user` object will have its `age` attribute set to `33`.

---

### Exercise 4: Static and Class Methods
*   **Scenario:** A `Product` class needs to keep track of a global discount rate that applies to all products. This rate should be part of the class, not individual instances.
*   **Task:** Use a class attribute and a class method to manage a global discount.
*   **Requirements:**
    *   The `Product` class should have a class attribute `_discount_rate` initialized to `0.0`.
    *   The `__init__` should take `name` and `price`.
    *   Create a `classmethod` called `set_discount_rate(cls, rate)` that updates the `_discount_rate`.
    *   Create a regular instance method `get_discounted_price()` that returns `self.price * (1 - cls._discount_rate)`.
*   **Test Case:**
    *   **Input:**
        ```python
        p1 = Product("Laptop", 1000)
        Product.set_discount_rate(0.1) # 10% discount
        print(p1.get_discounted_price())
        ```
    *   **Expected Output:** `900.0`

---

### Exercise 5: Static and Class Methods
*   **Scenario:** Your application needs to count how many `User` objects have been created in total.
*   **Task:** Use a class attribute and a class method to track the total number of instances.
*   **Requirements:**
    *   The `User` class should have a class attribute `_total_users` initialized to `0`.
    *   In the `__init__` method, increment `User._total_users` every time a new object is created.
    *   Create a `classmethod` called `get_total_users(cls)` that returns the value of `_total_users`.
*   **Test Case:**
    *   **Input:**
        ```python
        u1 = User("Alice")
        u2 = User("Bob")
        u3 = User("Charlie")
        print(User.get_total_users())
        ```
    *   **Expected Output:** `3`

---

### Exercise 1: Operator Overloading
*   **Scenario:** You're working on a 2D graphics library and need to represent points or vectors. A common operation is adding two vectors together.
*   **Task:** Create a `Vector2D` class and overload the `+` operator.
*   **Requirements:**
    *   The `Vector2D` class `__init__` takes `x` and `y` coordinates.
    *   Implement the `__add__(self, other)` method. It should return a *new* `Vector2D` object whose `x` is the sum of the `x`'s and whose `y` is the sum of the `y`'s.
*   **Test Case:**
    *   **Input:**
        ```python
        v1 = Vector2D(2, 3)
        v2 = Vector2D(4, 1)
        v3 = v1 + v2
        print(v3.x, v3.y)
        ```
    *   **Expected Output:** `6 4`

---

### Exercise 2: Operator Overloading
*   **Scenario:** You are creating a `ShoppingCart` class and want to be able to use the built-in `len()` function to find out how many items are in the cart.
*   **Task:** Implement the `__len__` method for a `ShoppingCart` class.
*   **Requirements:**
    *   The `ShoppingCart` class should have an `__init__` that initializes a private list of items.
    *   An `add_item(item)` method adds an item to the list.
    *   Implement the `__len__(self)` method to return the number of items in the list.
*   **Test Case:**
    *   **Input:**
        ```python
        cart = ShoppingCart()
        cart.add_item("Apple")
        cart.add_item("Banana")
        print(len(cart))
        ```
    *   **Expected Output:** `2`

---

### Exercise 3: Operator Overloading
*   **Scenario:** You have a custom `Order` class and you want to be able to compare two orders to see if they are equal based on their order ID.
*   **Task:** Create an `Order` class and overload the `==` operator.
*   **Requirements:**
    *   The `Order` class `__init__` takes an `order_id` and a list of `items`.
    *   Implement the `__eq__(self, other)` method. It should return `True` if `self.order_id` is the same as `other.order_id`, and `False` otherwise.
*   **Test Case:**
    *   **Input:**
        ```python
        order1 = Order(123, ["book", "pen"])
        order2 = Order(123, ["stapler"])
        order3 = Order(456, ["book", "pen"])
        print(order1 == order2)
        print(order1 == order3)
        ```
    *   **Expected Output:**
        ```
        True
        False
        ```

---

### Exercise 4: Operator Overloading
*   **Scenario:** You're modeling a music playlist. You want to be able to get a nicely formatted string representation of the playlist just by printing the object.
*   **Task:** Implement the `__str__` method for a `Playlist` class.
*   **Requirements:**
    *   The `Playlist` class `__init__` takes a `name` and initializes an empty list of `songs`.
    *   An `add_song(song)` method adds a song title to the list.
    *   Implement the `__str__(self)` method to return a string like `"Playlist: [name]\n- [song1]\n- [song2]"`.
*   **Test Case:**
    *   **Input:**
        ```python
        pl = Playlist("My Favorites")
        pl.add_song("Bohemian Rhapsody")
        pl.add_song("Stairway to Heaven")
        print(pl)
        ```
    *   **Expected Output:**
        ```
        Playlist: My Favorites
        - Bohemian Rhapsody
        - Stairway to Heaven
        ```

---

### Exercise 5: Operator Overloading
*   **Scenario:** You are building a `Time` class to represent a duration in hours and minutes. You want to be able to add two `Time` objects together, and have the minutes and hours correctly roll over.
*   **Task:** Create a `Time` class and overload the `+` operator to handle time arithmetic.
*   **Requirements:**
    *   The `Time` class `__init__` takes `hours` and `minutes`.
    *   Implement the `__add__(self, other)` method.
    *   The method should calculate the total minutes, then convert that back into hours and minutes (e.g., 80 minutes becomes 1 hour and 20 minutes).
    *   It should return a new `Time` object with the final calculated hours and minutes.
*   **Test Case:**
    *   **Input:**
        ```python
        t1 = Time(2, 45)
        t2 = Time(1, 30)
        total_time = t1 + t2
        # Assume a __str__ or other way to see the result
        print(f"{total_time.hours} hours, {total_time.minutes} minutes")
        ```
    *   **Expected Output:** `4 hours, 15 minutes`

---

### Exercise 1: Composition
*   **Scenario:** You are modeling a car. A car is not a type of engine, but it "has an" engine. This is a classic "has-a" relationship, perfect for composition.
*   **Task:** Create an `Engine` class and a `Car` class that contains an `Engine` object.
*   **Requirements:**
    *   Create an `Engine` class with a `start()` method that prints `"Engine starting..."`.
    *   Create a `Car` class. Its `__init__` method should create an instance of the `Engine` class and store it as an attribute (e.g., `self.engine`).
    *   The `Car` class should have a `start_car()` method that calls the `start()` method on its `engine` object.
*   **Test Case:**
    *   **Input:**
        ```python
        my_car = Car("Toyota")
        my_car.start_car()
        ```
    *   **Expected Output:** `"Engine starting..."`

---

### Exercise 2: Composition
*   **Scenario:** You are creating an application for a library. A book is written by an author. A `Book` object should contain information about its `Author`.
*   **Task:** Create `Author` and `Book` classes where `Book` is composed of an `Author`.
*   **Requirements:**
    *   Create an `Author` class with `name` and `birth_year` attributes.
    *   Create a `Book` class. Its `__init__` should take a `title` and an `author_object` (which will be an instance of the `Author` class).
    *   The `Book` class should have a `get_book_info()` method that returns a string like `"[title] by [author_name]"` by accessing the author object's attributes.
*   **Test Case:**
    *   **Input:**
        ```python
        tolkien = Author("J.R.R. Tolkien", 1892)
        hobbit = Book("The Hobbit", tolkien)
        print(hobbit.get_book_info())
        ```
    *   **Expected Output:** `'The Hobbit by J.R.R. Tolkien'`

---

### Exercise 3: Composition
*   **Scenario:** You are modeling a computer. A computer is composed of several parts, such as a CPU and RAM.
*   **Task:** Create `CPU`, `RAM`, and `Computer` classes.
*   **Requirements:**
    *   Create a `CPU` class with a `model` attribute.
    *   Create a `RAM` class with a `size_gb` attribute.
    *   Create a `Computer` class. Its `__init__` should instantiate and store a `CPU` object and a `RAM` object.
    *   The `Computer` class should have a `get_specs()` method that returns a formatted string detailing its components.
*   **Test Case:**
    *   **Input:**
        ```python
        computer = Computer("Intel i7", 16)
        print(computer.get_specs())
        ```
    *   **Expected Output:** `'Computer Specs: CPU - Intel i7, RAM - 16GB'`

---

### Exercise 4: Composition
*   **Scenario:** You're building a system to manage employee data. An employee has a role and a home address. These can be modeled as separate objects.
*   **Task:** Create `Address` and `Employee` classes, where `Employee` contains an `Address` object.
*   **Requirements:**
    *   Create an `Address` class with `street`, `city`, and `zip_code` attributes.
    *   Create an `Employee` class. Its `__init__` should take `name` and an `address_object`.
    *   The `Employee` class should have a `get_full_address()` method that delegates the formatting to the `Address` object (or formats it itself).
*   **Test Case:**
    *   **Input:**
        ```python
        home_address = Address("123 Main St", "Anytown", "12345")
        employee = Employee("John Doe", home_address)
        print(employee.get_full_address())
        ```
    *   **Expected Output:** `'123 Main St, Anytown, 12345'`

---

### Exercise 5: Composition
*   **Scenario:** You are creating a quiz application. A quiz consists of a collection of questions.
*   **Task:** Create `Question` and `Quiz` classes, where a `Quiz` is composed of a list of `Question` objects.
*   **Requirements:**
    *   Create a `Question` class with `text` and `answer` attributes.
    *   Create a `Quiz` class. Its `__init__` should initialize an empty list to hold `Question` objects.
    *   The `Quiz` class should have an `add_question(question_object)` method.
    *   The `Quiz` class should have a `run_quiz()` method that iterates through its questions, prints the question text, and then reveals the answer.
*   **Test Case:**
    *   **Input:**
        ```python
        q1 = Question("What is the capital of France?", "Paris")
        q2 = Question("What is 2+2?", "4")
        quiz = Quiz()
        quiz.add_question(q1)
        quiz.add_question(q2)
        # Running quiz.run_quiz() should print the questions and answers sequentially.
        ```
    *   **Expected Output:** The console output should show the text and answer for each question in the quiz.

---

### Exercise 1: Design Patterns (Singleton)
*   **Scenario:** You need a single configuration object for your entire application to hold settings like the database URL or API keys. Creating multiple configuration objects would be redundant and could lead to inconsistencies.
*   **Task:** Create a simple `AppConfig` class that implements the Singleton pattern.
*   **Requirements:**
    *   The `AppConfig` class should ensure that only one instance of it can ever be created.
    *   Subsequent calls to its constructor should return the already existing instance.
    *   You can store some sample configuration data in it, like `self.settings = {'api_key': 'abc-123'}`.
*   **Test Case:**
    *   **Input:**
        ```python
        config1 = AppConfig()
        config2 = AppConfig()
        print(config1 is config2) # Check if they are the same object in memory
        ```
    *   **Expected Output:** `True`

---

### Exercise 2: Design Patterns (Singleton)
*   **Scenario:** Your application needs a logging mechanism. You want all parts of your code to write to the same log file through a single `Logger` instance.
*   **Task:** Create a `Logger` class using the Singleton pattern.
*   **Requirements:**
    *   Implement the Singleton pattern for the `Logger` class.
    *   The `Logger` should have a `log(message)` method that prints the message to the console (simulating writing to a file).
*   **Test Case:**
    *   **Input:**
        ```python
        # In one part of the app
        logger1 = Logger()
        logger1.log("Starting service...")

        # In another part of the app
        logger2 = Logger()
        logger2.log("Service is running.")

        print(logger1 is logger2)
        ```
    *   **Expected Output:**
        ```
        Starting service...
        Service is running.
        True
        ```

---

### Exercise 3: Design Patterns (Singleton)
*   **Scenario:** To manage database connections efficiently, you want to ensure there is only one `DatabaseConnection` pool object throughout your application's lifecycle.
*   **Task:** Implement a `DatabaseConnection` Singleton that manages a mock connection state.
*   **Requirements:**
    *   Implement the Singleton pattern for the `DatabaseConnection` class.
    *   In the `__init__`, add an attribute `self.connection_id` and set it to a random number to simulate a unique connection.
    *   Add a `connect()` method that prints the `connection_id`.
    *   Verify that no matter how many times you instantiate the class, the `connection_id` remains the same.
*   **Test Case:**
    *   **Input:**
        ```python
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        print(db1.connection_id == db2.connection_id)
        ```
    *   **Expected Output:** `True`

---

### Exercise 4: Design Patterns (Singleton)
*   **Scenario:** You have a `GameManager` class that holds the global state of a game (e.g., score, level). This state must be unique and globally accessible.
*   **Task:** Create a `GameManager` Singleton.
*   **Requirements:**
    *   Implement `GameManager` as a Singleton.
    *   Initialize `score` to 0 in its constructor.
    *   Add a method `add_points(points)` to increase the score.
    *   Add a method `get_score()` to return the current score.
*   **Test Case:**
    *   **Input:**
        ```python
        manager1 = GameManager()
        manager1.add_points(10)

        manager2 = GameManager()
        manager2.add_points(5)

        print(manager2.get_score())
        ```
    *   **Expected Output:** `15`

---

### Exercise 5: Design Patterns (Singleton)
*   **Scenario:** You need a thread-safe singleton for a `Cache` class, where multiple concurrent threads might try to create an instance at the same time.
*   **Task:** Implement a thread-safe Singleton pattern for a `Cache` class.
*   **Requirements:**
    *   Implement the Singleton pattern, but use a `threading.Lock` to protect the part of the code where the instance is created. This ensures that even with multiple threads, only one instance is ever created.
    *   The `Cache` class should have a simple dictionary `self.data` to store cached items.
*   **Test Case:**
    *   **Input:** This is harder to test deterministically without writing a multi-threaded script. The primary check is still identity.
        ```python
        cache1 = Cache()
        cache2 = Cache()
        print(cache1 is cache2)
        ```
    *   **Expected Output:** `True`

## Final Project

_This is a larger capstone project that requires combining multiple concepts from the topics above into a single, cohesive solution._

---

### Final Project: Online Course Management System
*   **Objective:** Design and implement the core backend object model for an online learning platform. The system needs to manage courses, instructors, and student enrollments, ensuring data integrity and logical relationships between entities.
*   **Background Scenario:** You are a backend developer for "EduSphere," a new online education platform. The first step is to build a robust and scalable object-oriented model that will serve as the foundation for the entire application. This model needs to handle different types of users, courses with specific instructors, and a flexible enrollment process.
*   **Core Tasks:**
    1.  **Task 1 (Core Classes, Inheritance & Encapsulation):**
        *   Create an abstract base class `User` with `name` and a private `__password` attribute.
        *   Create `Student` and `Instructor` classes that **inherit** from `User`.
        *   The `Instructor` class should have an additional private `__salary` attribute. Use **encapsulation** to provide a public `get_profile()` method but prevent direct access to sensitive data.
        *   Create a `Course` class with `course_title` and `course_code`.
    2.  **Task 2 (Composition & Abstraction):**
        *   Modify the `Course` class to use **composition**. Each `Course` instance must be associated with exactly one `Instructor` object upon creation.
        *   Create an **abstract base class** called `EnrollmentRule` with an abstract method `can_enroll(student, course)`.
        *   Create two concrete implementations:
            *   `OpenEnrollment`: The `can_enroll` method always returns `True`.
            *   `LevelPrerequisiteRule`: The `__init__` takes a required `level`. The `can_enroll` method returns `True` only if the student's `level` attribute is greater than or equal to the required level. (You'll need to add a `level` attribute to the `Student` class).
    3.  **Task 3 (Integration, Polymorphism & Singleton):**
        *   Create a `Platform` class that acts as the central hub. Implement it as a **Singleton** to ensure there's only one platform manager.
        *   The `Platform` should manage lists of courses and students.
        *   Implement a method `enroll_student_in_course(student, course)`. This method should demonstrate **polymorphism**: it will use the `EnrollmentRule` object associated with the course to check if the student is eligible before adding the student to the course's roster (a list of students in the `Course` class).
*   **Deliverable:** A single Python script (`.py` file) containing all the class definitions (`User`, `Student`, `Instructor`, `Course`, `EnrollmentRule` and its subclasses, `Platform`). The script should also include a small demonstration block under `if __name__ == "__main__":` that creates instances of these classes and showcases the enrollment process.
*   **Verification / Success Criteria:**
    *   **Check 1:** An `Instructor` object can call methods defined in the `User` class, demonstrating inheritance.
    *   **Check 2:** Attempting to directly access `instructor.__salary` or `student.__password` from outside the class raises an `AttributeError`.
    *   **Check 3:** A `Course` object must have a valid `Instructor` object as an attribute, accessible via `course.instructor`.
    *   **Check 4:** The `Platform.enroll_student_in_course` method successfully enrolls a level 1 student into a course that uses the `OpenEnrollment` rule.
    *   **Check 5:** The same method prevents a level 1 student from enrolling in a course that uses a `LevelPrerequisiteRule` requiring level 5.
    *   **Check 6:** Creating two instances of the `Platform` class results in the exact same object in memory (`platform1 is platform2` should be `True`).