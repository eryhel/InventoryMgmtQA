## Automated End-to-End Test for Inventory Management System

This repository contains an automated end-to-end test suite written in Python for an Inventory Management System developed in C#.

### Overview

Given that the test script and the application to be tested are implemented in different programming languages, the testing approach involves the following steps:

1. **Compilation**: The C# code is compiled into an executable.
2. **Subprocess Management**: The compiled executable is then launched as a subprocess by the Python script (`runner.py`).
3. **Input Injection and Output Monitoring**: The Python script injects input commands into the application, captures its output, and performs necessary assertions to validate the functionality.

### How It Works

1. **Compile the C# Code**: Ensure the C# application is compiled into an executable (`InventoryMgmt.exe`).
2. **Run the Python Script**: The Python script (`runner.py`) spawns the executable as a subprocess.
3. **Automated Testing**: The script sends predefined inputs to the Inventory Management System and monitors the outputs to verify the application's behavior against expected results.

### Prerequisites

- **Python**: Ensure Python is installed on your system.
- **C# Compiler**: Make sure you have a C# compiler to compile the Inventory Management System.
- **pytest**: The testing framework used to run the automated tests.

### Example Test

Below is an example test case to add a product to the Inventory Management System:

```python
def test_add_product(command_runner):
    inputs = [
        "1",            # Select "Add a product"
        "Product1",     # Enter product name
        "10",           # Enter product quantity
        "5.99"          # Enter product price
    ]
    output = command_runner.run_command(inputs)

    # Assert that the message "Product added successfully" is returned by the program
    assert output[-1] == 'Product added successfully.'
```

---

# Installation 

## Clone this repository

```bash
git clone git@github.com:eryhel/InventoryMgmtQA.git
```

## Install required packages
```bash
pip install -r requirements.txt
```

Move executable to test to `./bin/InventoryMgmt.exe` (Windows) or `./bin/InventoryMgmt` (Mac, Linux)


## Run test
```bash
pytest
```

## To run test per module
```bash
pytest test_functions.py
```

## To modify the executable path

```python
# modify this line in runner.py
command = ['./bin/InventoryMgmt']
```