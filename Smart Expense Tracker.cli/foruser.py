import json
def tell_budget():
    with open("info.json","r") as file:
        user=json.load(file)
        if user=={}:
            name=input("Enter your name\n")
            budget=int(input("Please input your bugdet or income\n"))
            user["name"]=name
            user["budget"]=budget
            with open("info.json","w") as file:
                json.dump(user,file)
        print(f"Welcome {user["name"].title()}, this is the Chrys Smart Expense Tracker CLI. Please chose an option by typing only the number associated with your choice")
def about():
    About="Chrys Smart Expense Tracker v1.0.0\nThis is a Smart Expense Tracker Cli that helps you track how your money is spent\nby storing all the expenses you input and providing a total whenever you want.\nYou can also view all expenses and modify whatever you want.\nPlease leave a feedback on any bugs or error."
    print(About)
def feedback():
    with open("feedback.json","r") as file:
        feedback=json.load(file)
        feedreport=input("Please enter your feedback\n")
        with open("feedback.json","w") as file:
            feedback.append(feedreport)
            json.dump(feedback,file)