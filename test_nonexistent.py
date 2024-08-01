from runner import command_runner

"""Testing products that does not exist"""

def test_remove(command_runner):

    #Prompt, product ID
    inputs = [
        "2",
        "5",
    ]
    output = command_runner.run_command(inputs)
    assert output[-1] == "Product not found, please try again."


def test_modify(command_runner):
    
    #Prompt, product ID, new quantity
    inputs = [
        "3",
        "5",
        "10"
    ]

    output = command_runner.run_command(inputs)
    assert output[-1] == "Product not found, please try again."


def test_total_value(command_runner):
    
    #Prompt
    inputs = [
        "4"
    ]

    output = command_runner.run_command(inputs)
    assert output[-1] == "Total value of inventory: 0.00"


def test_get_list(command_runner):
    
    #Prompt
    inputs = [
        "5"
    ]

    output = command_runner.run_command(inputs)
    assert output[-1] == "No products in here."
