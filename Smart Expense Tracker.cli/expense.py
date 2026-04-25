import json
class Expense:
    def __init__(self):
        self.expenses=[]
    def add_expenses(self,category,amount):
        self.new_expense={}
        self.new_expense[category]=amount
        try:
            with open("data.json","r") as file:
                self.expenses=json.load(file)
                self.expenses.append(self.new_expense)
                with open("data.json","w") as file:
                    json.dump(self.expenses,file)
        except:
            self.expenses==[]
            with open("data.json","w") as file:
                self.expenses.append(self.new_expense)
                json.dump(self.expenses,file)
    def delete_expense(self,tobe_deleted):
        with open("data.json","r") as file:
            self.expenses=json.load(file)
            if self.expenses==[]:
                print("Empty list")
        for dictions in self.expenses:
            if tobe_deleted in dictions.keys():
                del dictions[tobe_deleted]
            else:
                print(f"Category {tobe_deleted} not found")
        with open("data.json","w") as file:
            json.dump(self.expenses,file)
    def view_expense(self,currency):
        with open("data.json","r") as file:
            self.expenses=json.load(file)
            if self.expenses==[]:
                print("Empty list")
        for empty_dicts in self.expenses:
            if empty_dicts=={}:
                del empty_dicts 
            for diction in self.expenses:               
                for catg,amt in diction.items():
                    all_expense=f"{catg.title()}= {currency}{amt}"
                    print(all_expense)
    def edit_expense(self,chosen_category,new_amount):
        with open ("data.json","r") as file:
            self.expenses=json.load(file)
            if self.expenses==[]:
                print("Empty list or category does not exist")
        for to_edit in self.expenses:
            if chosen_category in to_edit.keys():
                to_edit[chosen_category]=new_amount
            with open("data.json","w") as file:
                json.dump(self.expenses,file)
    def show_total(self):
        currency=input("Please input your currency in words\n")
        expenditure=[]
        with open("data.json","r") as file:
            self.expenses=json.load(file)
            if self.expenses==[]:
                print("Empty list")
                total=0
        for dictionay in self.expenses:
            for items in dictionay.values():
                expenditure.append(items)
                total=sum(expenditure)
        with open("info.json","r") as file:
                user=json.load(file)
        print(f"Your total is: {total} {currency.lower()} against your budget of {user["budget"]} {currency.lower()}")
    