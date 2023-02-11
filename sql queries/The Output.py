import SqlQueries

Contin="yes"

while (Contin == "yes"):
    print("Input numbers from 1-10 for specific results")
    print("1- Display all users.")
    print("2- Display all owners.")
    print("3- Join dates and time.")
    print("4- Display Everyones E-mail address.")
    print("5- Display the last logged in user.")
    print("6- Display Question text For question title")
    print("7- Display Questions asked by a user.")
    print("8- Display number of questions asked by a users.")
    print("9- Display answers to a questions.")
    print("10-Display number of answers given.")
    print("11- Exit.")
    choice=int(input("Please enter your choice: "))
    if(choice==1):
        SqlQueries.allusers()# For All users
    elif(choice==2):
        SqlQueries.owners() # for all owners
    elif(choice==3):
        SqlQueries.joining() # for joining dates and time
    elif(choice==4):
        SqlQueries.email() # For emails of everyone
    elif(choice==5):
        SqlQueries.lastlogin() # for last login
    elif(choice==6):
        SqlQueries.qtxt_ques() # to get question text if question is asked
    elif(choice==7):
        SqlQueries.qsbyone() # to find questions asked by a person
    elif(choice==8):
        SqlQueries.numqs() # for number of questions asked by user
    elif(choice==9):
        SqlQueries.ans_to_qs() # to find answer asked to a question
    elif(choice==10):
        SqlQueries.num_ans() # to find number of answers given
    elif(choice==11):
        print("Thank you")
        break
    
    Contin=input("Do you want another query ")
























