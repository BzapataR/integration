 #This program was made by Brian Zapata Resendiz.
 #This program was meant to help save and distribute my money
 #this will be based on the simple 50-20-30 rule. is it a good way to
 #save or not I don't know, but here we go.
 #also, information was based off the link below
 #https://www.investopedia.com/ask/answers/022916/what-502030-budget-rule.asp

 #intro and menu to calculated how much you get paid per month
import math
def intro():
    print("Hello welcome to my integration project. This will be a budget\
    calculator based on the 50-30-20 rule created by Nancy Pelosi")
    #learned how to split code from https://developer.rhino3d.com
def pay_info():
    loop = True
    while not(loop == False):
        menu_selection=input("\nHow often do you get paid?\n1.Monthly\
        \n2.Yearly\n3.Bi weekly\n")
        if menu_selection== "1":
            #all the calculations will convert how much you get paid into a monthly format
            pay_rate=float(input("How much do you make a year?"))/12
            return pay_rate
            loop=False
        elif menu_selection== "2":
            pay_rate=float(input("How much do you make a month?"))
            return pay_rate
            loop=False
        elif menu_selection=="3":
            pay_rate=float(input("How much do you make every two weeks?"))\
            *(4.34524/2)//1
            return pay_rate
            loop=False
        else:
            print("invalid input. Try again.")
    print("You're pay rate is:", pay_rate)

#4.34524 is how many weeks in a month, according to google
#kinda forced a floor division here, I don't know how to put and serve a
#purpose.
def needs(pay_rate):
    necessities= pay_rate*.50
    print("\nThis is how much money should be used on necessities: $"
    , format(necessities,".2f"),sep="")
    print("How much do you spend on these items in a month?")
    #going to add basic needs that most people pay and add them together
    rent=float(input("Rent or mortgage amount:"))
    utilities=float(input("Enter the amount for utilities:"))
    transportation=float(input("Enter the transportation cost:"))
    food=float(input("Enter food cost:"))
    debts=float(input("Enter the minimum debt payments for the month:"))
    otherN=0
    anythingE=input("Anything else? If so type 'Y' or 'N' if you're done")
    anythingE=anythingE.upper()
    while not (anythingE)=='Y' and not(anythingE)=='N':
        anythingE = input("invalid input. Type 'Y' or 'N'.")
        anythingE=anythingE.upper()
    if anythingE == 'Y':
        while anythingE =='Y':
            otherN=float(input("Enter any other needs for the month:"))
            otherN+=otherN
            anythingE=input("Anything else? if so type 'Y' or 'N'")
            anythingE =anythingE.upper()
            while not(anythingE) == 'Y' and (anythingE) != 'N':
                anythingE = input("invalid input. Type 'Y' or 'Ni'.")
                anythingE=anythingE.upper()
    combinedN=(rent+utilities+transportation+food+debts+otherN)
    if combinedN<=necessities:
        print("Good job, you're in the green!")
        if combinedN<necessities:
            leftover=str(necessities-combinedN)
            print("You have "+leftover, "left to add on to any other category")
# additionally, if you go under 50% the article implies that you could\
#improve you lifestyle and afford it.
    else:
        print("you need to allocate and sacrifice funds from needs and investments\
        or change your life style")
def want(pay_rate):
    print("\nOk lets see how much you can spend on things you want")
    #stuff you don't need to live. a lot of people have a difficult time of
    #knowing the difference between needs and wants.
    wants=pay_rate*.30
    print("Here is what you have to spend on your wants per month: $"
        ,format(wants, ".2f"), sep="")
    #going to put something that will calculate how many months you need to wait
    #before you can comfortably afford something.
    a_want=0
    while not(float(a_want)):
        try:
            a_want=float(input("How much does your next big purchase cost? "))
        except:
            print("invalid input. try again.")

    if a_want<=wants:
        print("You can already afford that item within a month")
    else:
        time_for_purchase= a_want / wants
        print("You will be able to afford this item within:",
            format(time_for_purchase,".2f"),"months")

 #now for the savings part I want this part to do the most and maybe make this
 #into its separate project to calculate the interest and profit gained.
def save(pay_rate):
    savings=pay_rate*.20
    print("\nAlright, this is how much you should save up per month: $"
          ,format(savings,".2f"),sep="")
    print("That's all she wrote, you're all set.", end="")
    print(" Happy savings!", str(":)"*3),end="")
    #learned how to do end="" through geeksforgeeks.org
def main():
    intro()
    pay=pay_info()
    needs(pay)
    want(pay)
    save(pay)

main()
print("\nI can't seems to find a use for a for statement so im going to force it in ")
y_or_n=input("Do you want to see it hit 'y' or 'n'")
y_or_n=y_or_n.lower()
while not (y_or_n)=='y' and not(y_or_n)=='n':
        y_or_n = input("invalid input. Type 'y' or 'n'.")
        y_or_n=y_or_n.lower()
if (y_or_n == "y") or (y_or_n =="n"):
    if y_or_n=='n':
        print("well you're going to see it anyway")
    rows=int(input("enter a number"))
    rows+=1
    for x in range (rows,0,-1):
        for y in range (0,x-1):
            print('( ͡° ͜ʖ ͡°)'," ", end="")
        print()