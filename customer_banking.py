# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    
    # savings balance prompt. check that balance is a number.
    while True: 
        try:
            savings_balance = float(input("What is your savings account balance? "))
            break
        except ValueError:
            print("Balance must be a number. ")
            pass


    # savings interest prompt. check that input is a float and non-negative number
    while True: 
        try:
            savings_interest = float(input("What is your savings account's interest rate (APR)? "))
            if savings_interest < 0:
                print("Interest rate cannot be a negative number. ")
                pass
            else:
               break
        except ValueError:
            print("Provide APR as a decimal. Example: '5%' interest rate = 0.05. ")
            pass
    
    # savings maturity prompt. cehck that input is a non-negative number.
    while True: 
        try:
            savings_maturity = int(input("What is your savings account's maturity (months)? "))
            if savings_maturity < 0:
                print("Maturity cannot be a negative number. ")
                pass
            else:
                break
        except ValueError:
            print("Maturity must be given as a full integer. ")
            pass       


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    
    # formatting values that were output by the create_savings_account function
    updated_savings_balance = format(updated_savings_balance, ".2f")
    interest_earned = format(interest_earned, ".2f")


    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE 
    print (f"Your new savings account balance is ${updated_savings_balance}.\nYou earned ${interest_earned} in interest.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    
    # cd balance prompt. check that input is a non-negative number.
    while True: 
        try:
            cd_balance = float(input("What is your CD account balance? "))
            break
        except ValueError:
            print("Balance must be a number. ")
            pass

    # cd interest prompt. check that input is a non-negative number, and provided as a decimal. 
    while True: 
        try:
            cd_interest = float(input("What is your CD account's interest rate (APR)? "))
            if cd_interest < 0:
                print("Interest rate cannot be a negative number. ")
                pass
            else:
               break
        except ValueError:
            print("Provide APR as a decimal. Example: '5%' interest rate = 0.05. ")
            pass
    
    # cd maturity prompt. check that input is a non-negative integer
    while True: 
        try:
            cd_maturity = int(input("What is your CD account's maturity (months)? "))
            if cd_maturity < 0:
                print("Maturity cannot be a negative number. ")
                pass
            else:
                break            
        except ValueError:
            print("Maturity must be given as a full integer. ")
            pass 


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    
    # format values output from create_cd_account function
    updated_cd_balance = format(updated_cd_balance, ".2f")
    interest_earned = format(interest_earned, ".2f")

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print (f"Your new CD account balance is ${updated_cd_balance}. \nYou earned ${interest_earned} in interest.")

if __name__ == "__main__":
    # Call the main function.
    main()