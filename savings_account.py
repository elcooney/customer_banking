"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE


## import class type 'Account' from file Account
from Account import Account 


# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    interest = 0
    savings_account = Account(balance, interest)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    # note from liz: I ask for the interest rate as a decimal in customer_banking.py, so I do not divide by 100 in the formula below
    interest_new = balance * (interest_rate * (months/12))

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    balance_new = balance + interest_new
    

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_balance(balance_new)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings_account.set_interest(interest_new)

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    return  balance_new, interest_new