import numpy as np
import matplotlib.pyplot as plt
import tkinter.messagebox as MessageBox
from tkinter import *
import mysql.connector
import csv


# If you will use database on your pc, you should change the information near the default values.

mydb = mysql.connector.connect(
    host="bxyirtxmghqcognim1ms-mysql.services.clever-cloud.com", # localhost
    user="u4mrzk8mb8x3sqm6",                                 # root
    passwd="BlbBPwwiWUJai75kgH4z",                         # 12345678
    database="bxyirtxmghqcognim1ms"                         # DB
)

def signup():
    name = e_name.get()
    surname = e_surname.get()
    email = e_email.get()
    password = e_password.get()

    if name=="" or surname=="" or email=="" or password=="":
        MessageBox.showinfo("Sign-Up Status", "Please fill all fields!")

    else:
        cursor = mydb.cursor()
        cursor.execute("insert into user values ('"+name+"','"+surname+"','"+email+"','"+password+"')")
        mydb.commit()

        e_name.delete(0,"end")
        e_surname.delete(0,"end")
        e_email.delete(0,"end")
        e_password.delete(0,"end")
        MessageBox.showinfo("Sign-Up Status", "Sign-Up Succesfully")



def login():

    sql = "SELECT * FROM user WHERE BINARY Email = '%s' AND Password = '%s'" % (e_emailLogin.get(), e_passwordLogin.get())
    cursor = mydb.cursor()
    cursor.execute(sql)
    rootLogin1 = Tk()

    if cursor.fetchone():
        MessageBox.showinfo("Login Status", "Login Successfully!")
        rootLogin.destroy()

        rootLogin1.geometry("600x300")
        rootLogin1.title("See-It Login")

        filePath = Label(rootLogin1, text="Enter a CSV or XML file path on your computer.", font=("bold", 10))
        filePath.place(x=20, y=30)

        colNum = Label(rootLogin1, text="Enter index of column header and column number\nthat you will use with space. EX: '1 3'", font=("bold", 9))
        colNum.place(x=350, y=30)

        colNumPlace = Entry(rootLogin1, textvariable=StringVar)
        colNumPlace.place(x=350,y=60)

        e_filePath = Entry(rootLogin1, textvariable=StringVar)
        e_filePath.place(x=20,y=50)


        text1 = Label(rootLogin1, text="*Be sure that you wrote a valid path. For Ex: /Users/admin/Desktop/test.csv", font=("light", 7))
        text1.place(x=20, y=80)

        text = Label(rootLogin1, text="Select a chart type that you want to create.", font=("light", 10))
        text.place(x=20, y=120)

        OPTIONS = [
           "Pie Chart",
           "Bar Chart",
           "Scatter Chart"]




        def pie_chart():

            colNumAndInfo = []
            colNumPlace_splitted = colNumPlace.get().split(" ")
            for i in colNumPlace_splitted:
                i = int(i)
                colNumAndInfo.append(i)

            a = colNumAndInfo[0]
            b = colNumAndInfo[1]


            y = []
            mylabels = []
            with open(e_filePath.get(),'r') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                for row in lines:
                    mylabels.append(row[a])
                    y.append(int(row[b]))

            fig1, ax1 = plt.subplots()
            ax1.pie(y, labels=mylabels, autopct='%1.1f%%',
                    shadow=False, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            plt.show()


            pass


        def bar_chart():
            x = []
            y = []

            colNumAndInfo = []
            colNumPlace_splitted = colNumPlace.get().split(" ")
            for i in colNumPlace_splitted:
                i = int(i)
                colNumAndInfo.append(i)

            a = colNumAndInfo[0]
            b = colNumAndInfo[1]
            with open(e_filePath.get(),'r') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                for row in lines:
                    x.append(row[a])
                    y.append(int(row[b]))

            plt.bar(x, y, color = 'g', width = 0.72, label = " ")
            plt.xlabel(' ')
            plt.ylabel(' ')
            plt.title('Bar Chart')
            plt.legend()
            plt.show()
            pass

        def scatter_chart():
            x = []
            y = []

            colNumAndInfo = []
            colNumPlace_splitted = colNumPlace.get().split(" ")
            for i in colNumPlace_splitted:
                i = int(i)
                colNumAndInfo.append(i)

            a = colNumAndInfo[0]
            b = colNumAndInfo[1]
            with open(e_filePath.get(),'r') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                for row in lines:
                    x.append(int(row[a]))
                    y.append(int(row[b]))

            x=np.array(x)
            y=np.array(y)
            plt.plot(x, y, 'o')

            m, b = np.polyfit(x, y, 1)

            plt.plot(x, m*x + b)
            plt.show()
            pass


        def picker():
            if variable.get() == "Pie Chart":
                pie_chart()
            if variable.get() == "Bar Chart":
                bar_chart()
            if variable.get() == "Scatter Chart":
                scatter_chart()




        variable = StringVar(rootLogin1)
        variable.set(OPTIONS[0])

        selectList = OptionMenu(rootLogin1, variable, *OPTIONS)
        selectList.place(x=20,y=150)


        submitButton = Button(rootLogin1, text="Create a Chart", font=("bold",14), bg="white", command=lambda: picker())
        submitButton.place(x=300, y=250)

    else:
        MessageBox.showinfo("Login Status", "Incorrect email or password!")
        e_emailLogin.delete(0,"end")
        e_passwordLogin.delete(0,"end")
        rootLogin1.destroy()
        pass


def destroyro():
    root.destroy()



root = Tk()
root.geometry("600x300")
root.title("See-It Sign-Up")


name = Label(root, text="Name", font=("bold", 10))
name.place(x=20, y=30)

surname = Label(root, text="Surname", font=("bold", 10))
surname.place(x=20, y=60)

email = Label(root, text="Email", font=("bold", 10))
email.place(x=20, y=90)

password = Label(root, text="Password", font=("bold", 10))
password.place(x=20, y=120)

text = Label(root, text="*If you have already an account, you can click the login button", font=(10))
text.place(x=20, y=180)


e_name = Entry(root, textvariable=StringVar)
e_name.place(x=150,y=30)

e_surname = Entry(root, textvariable=StringVar)
e_surname.place(x=150,y=60)

e_email = Entry(root, textvariable=StringVar)
e_email.place(x=150,y=90)

e_password = Entry(root, textvariable=StringVar, show="*")
e_password.place(x=150,y=120)

signupButton = Button(root, text="Sign-Up", font=("bold", 11), activebackground="blue", activeforeground="white", command=signup)
signupButton.place(x=150, y=150)

loginPageButton = Button(root, text="Login", font=("bold", 11), bg="white", command=destroyro)
loginPageButton.place(x=250, y=150)

root.mainloop()

rootLogin = Tk()
rootLogin.geometry("600x300")
rootLogin.title("See-It Login")

email = Label(rootLogin, text="Email", font=("bold", 10))
email.place(x=20, y=30)

password = Label(rootLogin, text="Password", font=("bold", 10))
password.place(x=20, y=60)

e_emailLogin = Entry(rootLogin, textvariable=StringVar)
e_emailLogin.place(x=150,y=30)

e_passwordLogin = Entry(rootLogin, textvariable=StringVar, show="*")
e_passwordLogin.place(x=150,y=60)

loginButton = Button(rootLogin, text="Login", font=("bold", 11), bg="white", command=login)
loginButton.place(x=180, y=90)

rootLogin.mainloop()