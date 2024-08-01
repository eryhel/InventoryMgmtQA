from runner import command_runner

"""Negative testing"""

# Incorrect product ID
def test_remove(command_runner):
    
    #Prompt, product ID
    inputs = [
        "2",
        "10",
    ]
    output = command_runner.run_command(inputs)
    assert output[-1] == "Product not found, please try again."

# Incorrect product ID
def test_modify(command_runner):
    
    #Prompt, product ID, new quantity
    inputs = [
        "3",
        "Banana",
        "10"
    ]

    output = command_runner.run_command(inputs)
    assert output[-1] == "Invalid input, please try again."


# Add a product with a negative quantity
def test_add_negative_quantity(command_runner):
    
    # Prompt, product name, quantity, price
    inputs = [
        "1",
        "Apple"
        "-10",
        "5.99"
    ]

    output = command_runner.run_command(inputs)
    assert output[-1] == "Invalid input, please try again."


# Add a product with a negative price
def test_add_negative_price(command_runner):
    
    # Prompt, product name, quantity, price
    inputs = [
        "1",
        "Apple"
        "10",
        "-5.99"
    ]

    output = command_runner.run_command(inputs)
    assert output[-1] == "Invalid input, please try again."


# Modify a product with a negative quantity
def test_modify_negative_quantity(command_runner):
    
    # Prompt, product name, quantity, price
    inputs = [
        "1",
        "Apple"
        "1",
        "5.99"
    ]

    #Prompt, product ID, new quantity
    inputs = [
        "3",
        "1",
        "-10"
    ]

    output = command_runner.run_command(inputs)
    assert output[-1] == "Invalid input, please try again."
