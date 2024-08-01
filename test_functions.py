from runner import command_runner

"""Testing functions"""

def test_add_product(command_runner):

    # Prompt, product name, quantity, price
    inputs = [
        "1",
        "Apple",
        "10",
        "5.99"
    ]
    output = command_runner.run_command(inputs)
    assert output[-1] == "Product added successfully."


def test_get_total_value(command_runner):
    
        # Prompt
        inputs = [
            "4"
        ]
        output = command_runner.run_command(inputs)
        assert output[-1] == "Total value of inventory: 59.90"

def test_list_all_products(command_runner):

    # Prompt
    inputs = [
        "5"
    ]
    output = command_runner.run_command(inputs)

    assert output[-1] == '{"ProductID":1,"Name":"Apple","QuantityInStock":10,"Price":5.99}'


def test_modify_product(command_runner):

    # Prompt, product id, new quantity
    inputs = [
        "3",
        "1",
        "100",
    ]
    output = command_runner.run_command(inputs)
    assert output[-1] == "Product updated successfully."

    # check product list to verify the quantity has been updated
    inputs = [
        "5"
    ]
    output = command_runner.run_command(inputs)
    assert output[-1] == '{"ProductID":1,"Name":"Apple","QuantityInStock":100,"Price":5.99}'
    

def test_remove_product(command_runner):

    # Prompt, product ID
    inputs = [
        "2",
        "1",
    ]
    output = command_runner.run_command(inputs)
    assert output[-1] == "Product removed successfully."
