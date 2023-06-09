# The program will allow the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.
# Import math library for compound interest calculation

import math 
print("""Investment - to calculate the amount of interest you'll earn on your investment
Bond       - to calculate the amount you'll have to payon a home loan""")

# .lower() function convert the choice in lowercase, the user can input a mixture of capital or lower case.

user_input = (input("Enter either investment or bond from the menu above to proceed : ")).lower()

# If statement will determine the path based on the user input choices.
if user_input == "investment" :
    # Getting information from the user
    amount_dep  = int(input("What is the value of the money you want to deposit : "))
    interest_rate = int(input("Enter interest rate value (as a percentage) : ")) /100
    number_years = int(input("Enter the number of years you plan to invest : "))
    sc_interest = input("Do you want simple or compound interest :").lower()
    if sc_interest == "simple" :
        # Calculate simple interest
        # The total amount when simple interest is applied is calculated as follows: 𝐴 = 𝑃(1 + 𝑟 × 𝑡) or ""A = P*(1 + r*t)""
        # In the formulae above:
        # ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08
        # ‘P’ is the amount that the user deposits
        # ‘t’ is the number of years that the money is being invested
        # ‘A’ is the total amount once the interest has been applied
        total_amount = (amount_dep * (1 + interest_rate * number_years))
         # Display the results to the user
        print(f"Your total amount after {number_years} years at {interest_rate * 100} % interest it will be {total_amount:,.2F}")

    elif sc_interest == "compound" :
        # Calculate compound interest
        # The total amount when compound interest is applied is calculated as follows: 𝐴 = 𝑃(1 + 𝑟)𝑡 or ""A = P * math.pow((1+r),t)""
        # In the formulae above value are taken as simple interest value
        total_amount = amount_dep * math.pow((1 + interest_rate), number_years)
        # # Display the results to the user
        print(f"Your total amount after {number_years} years at {interest_rate * 100} % interest it will be {total_amount:,.2F}")

    else :
        # If the user choose enter invalid answer the following message will appear
        print ("Invalid answer, please choose either simple or compound.")
    
elif user_input == "bond" :
     # Getting information from the user
    house_value = int(input("What is the present value of the house? "))
    interest_rate = int(input("Enter interest rate value : "))
    interest_rate_percentage_month = (interest_rate / 100) / 12
    bond_repay = int(input("What is the number of months are you plan to take to repay the bond : "))
    # Calculate monthly repayment
    # The amount that a person will have to be repaid on a home loan each month is calculated as follows: 𝑟𝑒𝑝𝑎𝑦𝑚𝑒𝑛𝑡 = (𝑖 × 𝑃)/(1− (1+𝑖)−𝑛)or ""repayment = (i * P)/(1 - (1 + i)**(-n))""
    # In the formula above:
    # ‘P’ is the present value of the house
    # ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12
    # ‘n’ is the number of months over which the bond will be repaid
    bond_repayment = int((interest_rate_percentage_month * house_value) / (1 - (1 + interest_rate_percentage_month)**(- bond_repay)))
    # Display the results to the user
    print(f"The amount of money you have to repay each month is : {bond_repayment:,.2F}")

else :
    print (" Invalid answer, please choose either investment or bond : ")