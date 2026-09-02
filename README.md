# Python Employee Management

A command-line employee management application built with Python. The program allows users to create departments, register employees, assign department managers, and view employee and department information.

## Features

* Create and manage departments
* Add employees with:

  * Name
  * Salary
  * Department
* Add department managers
* View all registered employees
* Search for information about a specific employee
* View the manager of a department
* Validate that employees and managers belong to existing departments
* Organize the application using Python classes and inheritance

## Technologies

* Python
* Object-Oriented Programming (OOP)
* Classes
* Inheritance
* `super()`
* Dictionaries
* Lists
* Functions
* User input and validation
* Multiple Python modules

## Project Structure

```text
python-employee-management/
│
├── main.py
├── klasser.py
└── README.md
```

The project separates the classes from the main program logic.

The `Allmän` class represents an employee, while the `Chefer` class inherits from `Allmän` and adds manager-specific functionality.

## Object-Oriented Programming

The project uses inheritance to create specialized employee objects.

`Chefer` inherits attributes and functionality from `Allmän` using `super()` and adds information about the manager.

## What I Learned

Through this project, I practiced:

* Creating classes and objects in Python
* Using inheritance
* Using `super()` to initialize inherited attributes
* Separating classes into a separate Python module
* Working with lists and dictionaries
* Creating functions to organize program logic
* Validating user input
* Building an interactive command-line application

## How to Run

1. Make sure Python 3 is installed.
2. Clone the repository.
3. Open the project folder in your code editor.
4. Run the main program:

```bash
python main.py
```

Follow the instructions displayed in the terminal to interact with the application.
