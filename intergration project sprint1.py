""" This program was meant to help save and distribute my money
this will be based on the simple 50-20-30 rule. Is it a good way to
save? I don't know, but here we go.

"""

__author__ = "Brian Zapata Resendiz"


# also, information was based off the link below
# https://www.investopedia.com/ask/answers/022916/what-502030-budget-rule.asp


def requirement():
    """This part of the program included all the required code for past runs
    and serves no real function.
    """
    print("\nI can't seem to find a use if or for statement so im going to "
          "force it in ")
    y_or_n = input("Do you want to see it hit 'y' or 'n'")
    y_or_n = y_or_n.lower()
    while not y_or_n == 'y' and not y_or_n == 'n':
        y_or_n = input("invalid input. Type 'y' or 'n'.")
        y_or_n = y_or_n.lower()
    if (y_or_n == "y") or (y_or_n == "n"):
        if y_or_n == 'n':
            print("well you're going to see it anyway")
        rows = int(check_float("enter a number"))
        rows += 1
        for x in range(1, rows, +1):
            for y in range(1, x + 1):
                print('( ͡° ͜ʖ ͡°)', " ", end="")
            print()


def check_float(prompt):
    """Checks input if it's a positive float.
     Input is what ever the function is attached to
     output.
     Output is the inputted number if it's a positive integer.
     """
    a_float = 0
    valid = False
    while not valid:
        try:
            a_float = float(input(prompt))
            valid = True
        except:
            print("Invalid positive float. Try again.")
        if a_float < 0:
            valid = False
            print("Please try a positive float.")
    return a_float


def intro():
    """
    Displays intro text.
    """
    print("Hello welcome to my integration project. This will be a budget\
    calculator based on the 50-30-20 rule created by Nancy Pelosi")
    # learned how to split code from https://developer.rhino3d.com


def pay_info():
    """
    This gathers the pay information that will be used for the rest of the
    program.
    The input is the pay a person receives bi-weekly monthly or yearly.
    No output but changes the pay into a monthly figure.
    """
    pay_rate = 0
    loop = True
    while loop:
        menu_selection = input("\nHow often do you get paid?\n1.Monthly\
        \n2.Yearly\n3.Bi weekly\n")
        if menu_selection == "1":
            # all the calculations will convert how much you get paid into a
            # monthly format
            pay_rate = check_float("How much do you make a year?") / 12
            loop = False
        elif menu_selection == "2":
            pay_rate = check_float("How much do you make a month?")
            loop = False
        elif menu_selection == "3":
            pay_rate = check_float(
                "How much do you make every two weeks?") * (4.34524 / 2) // 1
            loop = False
        else:
            print("invalid input. Try again.")

    print("You're monthly pay rate is:", pay_rate)
    return pay_rate


# 4.34524 is how many weeks in a month, according to google
# kinda forced a floor division here, I don't know how to put and serve a
# purpose.
def needs(pay_rate):
    """
    Needs functions calculates all your needs for the month and sees
    if you are spending over or under 50% of your budget.
    Takes in pay-rate from before.
    """
    necessities = pay_rate * .50
    print("\nThis is how much money should be used on necessities: $",
          format(necessities, ".2f"), sep="")
    print("How much do you spend on these items in a month?")
    rent = check_float("Rent or mortgage amount:")
    utilities = check_float("Enter the amount for utilities:")
    transportation = check_float("Enter the transportation cost:")
    food = check_float("Enter food cost:")
    debts = check_float("Enter the minimum debt payments for the month:")
    other_nums = 0
    anything_e = input("Anything else? If so type 'Y' or 'N' if you're done")
    anything_e = anything_e.upper()
    while not anything_e == 'Y' and not anything_e == 'N':
        anything_e = input("invalid input. Type 'Y' or 'N'.")
        anything_e = anything_e.upper()
    if anything_e == 'Y':
        while anything_e == 'Y':
            other_nums = check_float("Enter any other needs for the month:")
            other_nums += other_nums
            anything_e = input("Anything else? if so type 'Y' or 'N'")
            anything_e = anything_e.upper()
            while not anything_e == 'Y' and anything_e != 'N':
                anything_e = input("invalid input. Type 'Y' or 'N'.")
                anything_e = anything_e.upper()
    combined_num = (
            rent + utilities + transportation + food + debts + other_nums)
    if combined_num <= necessities:
        print("Good job, you're in the green!")
        if combined_num < necessities:
            leftover = str(necessities - combined_num)
            print("You have " + leftover,
                  "left to add on to any other category")
    # additionally, if you go under 50% the article implies that you could\
    # improve you lifestyle and afford it.
    else:
        print("you need to allocate and sacrifice funds from needs and"
              "investments or change your life style")


def want(pay_rate):
    """
    Calculates if a want of yours is within your budget for the month.
    Input is pay_rate.
    """
    print("\nOk lets see how much you can spend on things you want")
    # stuff you don't need to live. a lot of people have a difficult time of
    # knowing the difference between needs and wants.
    wants = pay_rate * .30
    print("Here is what you have to spend on your wants per month: $",
          format(wants, ".2f"), sep="")
    # going to put something that will calculate how many months you need to
    # wait before you can comfortably afford something.
    a_want = check_float("How much does your next big purchase cost?")
    if a_want <= wants:
        print("You can already afford that item within a month")
    else:
        time_for_purchase = a_want / wants
        print("You will be able to afford this item within:",
              format(time_for_purchase, ".2f"), "months")


# now for the savings part I want this part to do the most and maybe make this
# into its separate project to calculate the interest and profit gained.
def save(pay_rate):
    """
    Save, just calculates how much of your monthly earnings you should
    use to invest.
    Input is pay_rate.
    """
    savings = pay_rate * .20
    print("\nAlright, this is how much you should save up per month: $",
          format(savings, ".2f"), sep="")
    print("That's all she wrote, you're all set.", end="")
    print(" Happy savings!", str(":)" * 3),
          end="")  # learned how to do end="" through geeksforgeeks.org


def main():
    """
    Calls all functions together to make the program.Unnecessary, but only
    to meet the requirements for the past sprints.
    """
    intro()
    pay = pay_info()
    needs(pay)
    want(pay)
    save(pay)


if __name__ == "__main__":
    main()
