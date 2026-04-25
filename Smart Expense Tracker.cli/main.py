from pathlib import Path
from expense import Expense
import foruser
import json
foruser.tell_budget()
expense=Expense()
with open("info.json","r") as file:
    user=json.load(file)
    name=user["name"]
while True:
    menu=int(input("1. Add Expense\n2. Delete Expense\n3. View expenses\n4. Edit expense\n5. Show total expenses\n6. Change name\n7. Change bugdet\n8. About\n9. Leave a feedback\n10. Quit CLI\n"))
    if menu==1:
        category=input("Please input category money was spent on\n")
        amount=int(input("Please input amount spent\n"))
        expense.add_expenses(category,amount)
        print(f"All done {name.title()}. Would you like to.....")
    if menu==2:
        tobe_deleted=input("Please input the category to be deleted\n")
        expense.delete_expense(tobe_deleted)
        print(f"All done {name.title()}. Would you like to.....")
    if menu==3:
        currency=input("Please input currency symbol\n")
        expense.view_expense(currency)
        print(f"All done {name.title()}. Would you like to.....")
    if menu==4:
        chosen_category=input("Please input category to be edited\n")
        new_amount=int(input("Please input new amount\n"))
        expense.edit_expense(chosen_category,new_amount)
        print(f"All done {name.title()}. Would you like to.....")
    if menu==5:
        expense.show_total()
        print(f"All done {name.title()}. Would you like to.....")
    if menu==6:
        new_name=input("Please input your new name\n")
        with open("info.json","r") as file:
            user=json.load(file)
            user["name"]=new_name
        with open("info.json","w") as file:
            json.dump(user,file)
        print(f"All done {name.title()}. Would you like to.....")
    if menu==7:
        new_budget=int(input("Please input new budget amount"))
        with open("info.json","r") as file:
            user=json.load(file)
            user["budget"]=new_budget
        with open("info.json","w") as file:
            json.dump(user,file)
        print(f"All done {name.title()}. Would you like to.....")
    if menu==8:
        foruser.about()
        print(f"All done {name.title()}. Would you like to.....")
    if menu==9:
        foruser.feedback()
        print(f"All done {name.title()}. Would you like to.....")
    if menu==10:
        print("Thank you for using Chrys Smart Expense Tracker CLI. *-*")
        break