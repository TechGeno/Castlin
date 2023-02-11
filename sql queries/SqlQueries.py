import mysql.connector
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="baLaji$123",
    database="simpleqna")
mycursor = mydb.cursor()


def allusers():
    mycursor.execute("select username from auth_user")
    data = mycursor.fetchall()
    for i in data:
        print(i)


def owners():
    mycursor.execute("select username from auth_user where is_superuser= 1")
    data = mycursor.fetchall()
    for i in data:
        print(i)


def joining():
    mycursor.execute("select date_joined from auth_user ")
    data = mycursor.fetchall()
    for i in data:
        print(i)


def email():
    mycursor.execute("select email from auth_user ")
    data = mycursor.fetchall()
    for i in data:
        print(i)


def lastlogin():
    mycursor.execute("select last_login from auth_user ")
    data = mycursor.fetchall()
    for i in data:
        print(i)
# to get question text if question is asked


def qtxt_ques():
    x = input("Enter Question ")
    mycursor.execute("select question_text from questions_question where question_title=('%s')" % x)
    data = mycursor.fetchone()
    print(data)


# for selecting special stuff
# to find questions asked by a person   
def qsbyone():
    x = input("Enter Username ")
    mycursor.execute(
        'select question_title from auth_user, questions_question where auth_user.id= questions_question.posted_by_id and username= ("%s")' % x)
    data = mycursor.fetchall()
    for i in data:
        print(i)

# to find number of questions asked by one


def numqs():
    x = input("Enter Username ")
    mycursor.execute(
        'select count(question_title) from auth_user, questions_question where auth_user.id= questions_question.posted_by_id and username= ("%s")' % x)
    data = mycursor.fetchone()
    print(data)


# to find answer asked to a question

def ans_to_qs():
    x = input("Enter Question ")
    mycursor.execute(
        'select answer_text from questions_answer, questions_question where questions_answer.qid_id = questions_question.qid  and question_title= ("%s")' % x)
    data = mycursor.fetchall()
    for i in data:
        print(i)

# to find number of answers given


def num_ans():
    x = input("Enter Question ")
    mycursor.execute(
        'select count(answer_text) from questions_answer, questions_question where questions_answer.qid_id = questions_question.qid  and question_title= ("%s")' % x)
    data = mycursor.fetchone()
    print(data)
