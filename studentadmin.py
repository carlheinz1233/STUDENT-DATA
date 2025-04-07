from tkinter import *
from tkinter import messagebox
import os
import sqlite3

Student_Data_fm=Tk()
Student_Data_fm.geometry('925x500+300+200')
Student_Data_fm.title('Student Data')
Student_Data_fm.state("zoomed")
Student_Data_fm.bind('<Button-1>',lambda a: print(a.x,a.y))

#background color
bg_color='#323233'


#Image icon
login_icon=PhotoImage(file='icon/icon.png')
qr_img=PhotoImage(file='icon/login.png')
eye_icon1=PhotoImage(file='icon/eyeicon1.png')
eye_icon2=PhotoImage(file='icon/eyeicon2.png')
back1_btn=PhotoImage(file='icon/back.png')
forward1_btn=PhotoImage(file='icon/forward.png')
logout1_btn=PhotoImage(file='icon/logout.png')
submit1_btn=PhotoImage(file='icon/submit.png')
cancel1_btn=PhotoImage(file='icon/cancel.png')


#Checking initial database
def init_database():
    if os.path.exists("students_accounts.db"):
        connections=sqlite3.connect("students_accounts.db")
        cursor=connections.cursor()
        cursor.execute(""" Select * From data """)
        connections.commit()
        print(cursor.fetchall())
        connections.close()

    else:
        connections=sqlite3.connect("students_accounts.db")

        #Database Table
        cursor=connections.cursor()
        cursor.execute("""CREATE TABLE data(
        Username text, 
        Password text, 
        Name text, 
        Age text, 
        Date of Birth text, 
        Address text, 
        Contact No text, 
        Guardian's Name text, 
        Guardian's Contact No text, 
        Elementary text, 
        High School text, 
        Senior High School text, 
        College text, 
        Semester text, 
        Subjects Name text, 
        Subject Description text, 
        Credit Units text)""")
        connections.commit()
        connections.close()


#Creating Data
def create_data(Username,Password,Name,Age,Date_of_Birth,Address,Contact_No,Guardians_Name,Guardians_Contact_No,Elementary,High_School,Senior_High_School,College,Semester,Subjects_Name,Subjects_Description,Credits_Units):
    connection=sqlite3.connect("list_accounts.db")

    #Database Table
    cursor=connection.cursor()
    cursor.execute(f"""INSERT INTO data VALUES("{Username}","{Password}","{Name}","{Age}","{Date_of_Birth}","{Address}","{Contact_No}","{Guardians_Name}","{Guardians_Contact_No}","{Guardians_Contact_No}","{Elementary}","{High_School}","{Senior_High_School}","{College}","{Semester}","{Subjects_Name}","{Subjects_Description}","{Credits_Units})""")
    connection.commit()
    connection.close()


#Confirmation box for exiting or not
def confirmation_box(message):

    #Can store true or false in variable
    answer=BooleanVar()
    answer.set(False)

    #Getting the answer of the user(if Yes or No)
    def action(ans):
        answer.set(ans)
        confirmation_box_fm.destroy()

    #Frame of its content
    confirmation_box_fm=Frame(Student_Data_fm,highlightbackground=bg_color,highlightthickness=3)
    confirmation_box_fm.place(x=620,y=190,width=320,height=320)

    #Message on its box
    message_lb=Label(confirmation_box_fm,text=message,font=('Bold',15))
    message_lb.pack(padx=20)

    #No button on its box
    no_btn=Button(confirmation_box_fm,text='No',font=('Bold',15),bd=0,bg='#1e1ee4',fg='white',command=lambda: action(False))
    no_btn.place(x=50,y=160,width=80)

    #Yes button on its box
    yes_btn=Button(confirmation_box_fm,text='Yes',font=('Bold',15),bd=0,bg='#1e1ee4',fg='white',command=lambda: action(True))
    yes_btn.place(x=190,y=160,width=80)

    #Waiting until user press any button
    Student_Data_fm.wait_window(confirmation_box_fm)
    
    return answer.get()


def message_box(message):

    #Frame of its content
    message_box1_fm=Frame(Student_Data_fm,highlightbackground=bg_color,highlightthickness=3)
    message_box1_fm.place(x=620,y=190,width=320,height=320)

    #Close/Exit button
    close_btn=Button(message_box1_fm,text='X',bd=0,font=('Bold', 13), fg=bg_color,command=lambda: message_box1_fm.destroy())
    close_btn.place(x=290,y=5)

    message_lb=Label(message_box1_fm,text=message,font=('Bold',15))
    message_lb.pack(pady=50)


def Student_Data():
    
    #Forwarding to Login and Deleting Student Data1's content
    def forward_to_Login():
        Student_Data1_fm.destroy()
        Login()

    #Forwarding to Admin and Deleting Student Data1's content
    def forward_to_Admin():
        Student_Data1_fm.destroy()
        Admin()

    #Forwarding to Sign Up and Deleting Student Data1's content
    def forward_to_Sign_up():
        Student_Data1_fm.destroy()
        Sign_up()

    #Frame of its container
    Student_Data1_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #heading of Student Data
    heading_lb=Label(Student_Data1_fm,text='STUDENT DATA',bg=bg_color,fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.place(x=35,y=0,width=325)

    #Student button
    student_login_btn=Button(Student_Data1_fm,text='LOGIN',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_Login)
    student_login_btn.place(x=100,y=100,width=200)

    #Admin button
    admin_login_btn=Button(Student_Data1_fm,text='ADMIN',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_Admin)
    admin_login_btn.place(x=100,y=200,width=200)

    #Sign up button
    sign_up_login_btn=Button(Student_Data1_fm,text='SIGN UP',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_Sign_up)
    sign_up_login_btn.place(x=100,y=300,width=200)

    #Frame of its container
    Student_Data1_fm.pack(pady=30)
    Student_Data1_fm.pack_propagate(False)
    Student_Data1_fm.place(x=570,y=180)
    Student_Data1_fm.configure(width=400,height=420)


def Login():

    #Calling Student_Data and Destroying its Frame(Going Back)
    def forward_to_Student_Data():
        Student_Data2_fm.destroy()
        Student_Data()

    #Calling enter button to go to Login1
    def forward_to_Login1():
        Student_Data2_fm.destroy()
        Login1()

    #Frame of its container
    Student_Data2_fm = Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of Login
    heading_lb=Label(Student_Data2_fm,text='LOGIN',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.place(x=403,y=100,width=325)

    #Image icon 
    login_icon_lb=Label(Student_Data2_fm, image=login_icon,bd=0)
    login_icon_lb.place(x=515,y=150,width=100,height=100)
    
    #Lock and unlock password function
    def unlock():
        if password_ent['show'] == '*':
            password_ent.config(show='')
            eye_icon_btn.config(image=eye_icon2)
        else:
            password_ent.config(show='*')
            eye_icon_btn.config(image=eye_icon1)  

    #Insert and delete of username
    def on_enter(e):
        username_ent.delete(0,'end')

    def on_leave(e):
        name=username_ent.get()
        if name=='':
            username_ent.insert(0,'Username')

    #Username
    username_ent=Entry(Student_Data2_fm,font=('Franklin Gothic Demi (Headings)',18),justify=CENTER)
    username_ent.place(x=425,y=280)

    #Placeholder of Username
    username_ent.insert(0,'Username')
    username_ent.bind('<FocusIn>', on_enter)
    username_ent.bind('<FocusOut>', on_leave)
    
    #Insert and delete of password
    def on_enter(e):
        password_ent.delete(0,'end')

    def on_leave(e):
            name=password_ent.get()
            if name=='':
                password_ent.insert(0,'Password')

    #Password
    password_ent=Entry(Student_Data2_fm,font=('Franklin Gothic Demi (Headings)',18),justify=CENTER,)
    password_ent.place(x=425,y=330)

    #Placeholder of Password
    password_ent.insert(0,'Password')
    password_ent.bind('<FocusIn>', on_enter)
    password_ent.bind('<FocusOut>', on_leave)
    
    #Enter button
    enter_btn=Button(Student_Data2_fm,text="Enter",font=('Franklin Gothic Demi (Headings)',18),justify=CENTER,width=5,bg='#6aa84f',fg='white',relief=RAISED,command=forward_to_Login1)
    enter_btn.place(x=520,y=370)

    #Back button icon
    back_btn=Button(Student_Data2_fm, image=back1_btn,bd=0,bg='#323233',command=forward_to_Student_Data)
    back_btn.place(x=30,y=510)

    #Eye icon(lock)
    eye_icon_btn=Button(Student_Data2_fm,image=eye_icon1,bd=0,relief=RAISED,command=unlock)
    eye_icon_btn.place(x=700,y=330)

    #Frame of its container
    Student_Data2_fm.pack(pady=100)
    Student_Data2_fm.pack_propagate(False)
    Student_Data2_fm.configure(width=1100,height=620)


def Admin():

    #Forwarding to Student_Data and Deleting the content of Admin
    def forward_to_Student_Data():
        Student_Data3_fm.destroy()
        Student_Data()

    #Forwarding to Student_Data and Deleting the content of Admin1
    def forward_to_Admin1():
        Student_Data3_fm.destroy()
        Admin1()

    #Frame of its container
    Student_Data3_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of Admin
    heading_lb=Label(Student_Data3_fm,text='ADMIN',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.place(x=403,y=100,width=325)

    #Image icon 
    login1_icon_lb=Label(Student_Data3_fm, image=login_icon,bd=0)
    login1_icon_lb.place(x=515,y=150,width=100,height=100)

    #Insert and delete of username
    def on_enter(e):
        username1_ent.delete(0,'end')

    def on_leave(e):
        name=username1_ent.get()
        if name=='':
            username1_ent.insert(0,'Username')
    
    #Username
    username1_ent=Entry(Student_Data3_fm,font=('Franklin Gothic Demi (Headings)',18),justify=CENTER)
    username1_ent.place(x=425,y=280)

    #Placeholder of Username
    username1_ent.insert(0,'Username')
    username1_ent.bind('<FocusIn>', on_enter)
    username1_ent.bind('<FocusOut>', on_leave)
    
    #Insert and delete of password
    def on_enter(e):
        password1_ent.delete(0,'end')

    def on_leave(e):
            name=password1_ent.get()
            if name=='':
                password1_ent.insert(0,'Password')

    #Password
    password1_ent=Entry(Student_Data3_fm,font=('Franklin Gothic Demi (Headings)',18),justify=CENTER,)
    password1_ent.place(x=425,y=330)

    #Placeholder of Password
    password1_ent.insert(0,'Password')
    password1_ent.bind('<FocusIn>', on_enter)
    password1_ent.bind('<FocusOut>', on_leave)

    #Enter Button
    enter1_btn=Button(Student_Data3_fm,text="Enter",font=('Franklin Gothic Demi (Headings)',18),justify=CENTER,width=5,bg='#6aa84f',fg='white',relief=RAISED,command=forward_to_Admin1)
    enter1_btn.place(x=520,y=370)

    #Back button icon
    back_btn=Button(Student_Data3_fm, image=back1_btn,bd=0,bg='#323233',command=forward_to_Student_Data)
    back_btn.place(x=30,y=510)

    #Frame to its container
    Student_Data3_fm.pack(pady=100)
    Student_Data3_fm.pack_propagate(False)
    Student_Data3_fm.configure(width=1100,height=620)


def Sign_up():

    #Forwarding to Student Data and deleting the content of Sign Up
    def forward_to_Student_Data():
        Student_Data4_fm.destroy()
        Student_Data()

    #Forwarding to Foward_Button
    def forward_to_Foward_Button():
        Student_Data4_fm.destroy()
        Forward_Button()

    #Frame of its container
    Student_Data4_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Signup frame label
    student_login_lb=Label(Student_Data4_fm,text='SIGN UP',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED)
    student_login_lb.place(x=455,y=50,width=200)

    #Heading of Username 
    user_lb=Label(Student_Data4_fm,text='Username:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    user_lb.place(x=55,y=150,width=325)

    #Framebox of Username 
    frame_box=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box.place(x=270,y=150)

    #Heading of Password
    pass_lb=Label(Student_Data4_fm,text='Password:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    pass_lb.place(x=55,y=210,width=325)

    #Framebox of Password
    frame_box1=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box1.place(x=270,y=210)

    #Heading of Name
    name_lb=Label(Student_Data4_fm,text='Name:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    name_lb.place(x=70,y=270,width=325)

    #Framebox of Name
    frame_box2=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box2.place(x=270,y=270,width=150)

    #Heading of Age
    age_lb=Label(Student_Data4_fm,text='Age:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    age_lb.place(x=75,y=330,width=325)

    #Framebox of Age
    frame_box3=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box3.place(x=270,y=330)

    #Heading of Date of Birth
    birth_lb=Label(Student_Data4_fm,text='Date of Birth:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    birth_lb.place(x=40,y=390,width=325)

    #Framebox of Date of Birth
    frame_box4=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box4.place(x=270,y=390)

    #Heading of Address
    address_lb=Label(Student_Data4_fm,text='Address:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    address_lb.place(x=55,y=450,width=325)

    #Framebox of Address
    frame_box5=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box5.place(x=270,y=450)

    #Heading of Contact Number
    number_lb=Label(Student_Data4_fm,text='Contact Number:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    number_lb.place(x=475,y=150,width=325)

    #Framebox of Contact Number
    frame_box6=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box6.place(x=715,y=150)

    #Heading of Guardian's Name
    guardiansname_lb=Label(Student_Data4_fm,text="Guardian's Name:",bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    guardiansname_lb.place(x=470,y=210,width=325)

    #Framebox of Guardian's Name
    frame_box7=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box7.place(x=715,y=210)

    #Heading of Guardian's Contact Number
    guardianCN_lb=Label(Student_Data4_fm,text="Guardian's Contact Number:",bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    guardianCN_lb.place(x=430,y=270,width=325)

    #Framebox of Guardian's Contact Number
    frame_box8=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box8.place(x=715,y=270)

    #Back button icon
    back_btn=Button(Student_Data4_fm, image=back1_btn,bd=0,bg='#323233',command=forward_to_Student_Data)
    back_btn.place(x=30,y=510)

    #Forward button icon
    forward_btn=Button(Student_Data4_fm, image=forward1_btn,bd=0,bg='#323233',command=forward_to_Foward_Button)
    forward_btn.place(x=1020,y=510)

    #Frame to its container
    Student_Data4_fm.pack(pady=100)
    Student_Data4_fm.pack_propagate(False)
    Student_Data4_fm.configure(width=1100,height=620)


def Forward_Button(): 

    #Calling Sing Up and Deleting the content of Forward Button
    def forward_to_Sign_up():
        Student_Data5_fm.destroy()
        Sign_up()


    #Forwarding to student data and confirming if the user want to exit or not
    def forward_to_Student_Data():

        ans = confirmation_box(message='DO you want to leave\nSign Up form?')
        if ans:
            Student_Data5_fm.destroy()
            Student_Data()


    #Checking the inputs if the user already input something
    def check_input_validation():
        if frame_box9.get() == '':
            message_box(message='Elementary is required')     


    #Frame of its container
    Student_Data5_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Forward frame label
    forward1_lb=Label(Student_Data5_fm,text='SIGN UP',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED)
    forward1_lb.place(x=455,y=50,width=200)

    #Heading of Elementary
    elementary_lb=Label(Student_Data5_fm,text='Elementary:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    elementary_lb.place(x=45,y=150,width=325)

    #Framebox of Elementary
    frame_box9=Entry(Student_Data5_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box9.place(x=270,y=150)

    #Heading of High School
    highschool_lb=Label(Student_Data5_fm,text='High School:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    highschool_lb.place(x=40,y=210,width=325)

    #Framebox of High School
    frame_box10=Entry(Student_Data5_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box10.place(x=270,y=210)
    
    #Heading of Senior High School
    seniorhigh_lb=Label(Student_Data5_fm,text='Senior High School:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    seniorhigh_lb.place(x=15,y=270,width=325)

    #Framebox of Senior High School
    frame_box11=Entry(Student_Data5_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box11.place(x=270,y=270)

    #Heading of College
    college_lb=Label(Student_Data5_fm,text='College:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    college_lb.place(x=60,y=330,width=325)

    #Framebox of College
    frame_box12=Entry(Student_Data5_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box12.place(x=270,y=330)

    #Heading of Semester
    semester_lb=Label(Student_Data5_fm,text='Semester:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    semester_lb.place(x=55,y=390,width=325)

    #Framebox of Semester
    frame_box13=Entry(Student_Data5_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box13.place(x=270,y=390)

    #Heading of Subjects Name
    subjectname_lb=Label(Student_Data5_fm,text='Subjects Name:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    subjectname_lb.place(x=30,y=450,width=325)

    #Framebox of Subjects Name
    frame_box14=Entry(Student_Data5_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box14.place(x=270,y=450)

    #Heading of Subjects Description
    subjectD_lb=Label(Student_Data5_fm,text='Subjects Description:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    subjectD_lb.place(x=475,y=150,width=325)

    #Framebox of Subjects Description
    frame_box15=Entry(Student_Data5_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box15.place(x=740,y=150)

    #Heading of Credit Units
    credits_lb=Label(Student_Data5_fm,text="Credit Units:",bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    credits_lb.place(x=510,y=210,width=325)

    #Framebox of Credit Units
    frame_box16=Entry(Student_Data5_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box16.place(x=740,y=210)

    #Back button icon
    back_btn=Button(Student_Data5_fm, image=back1_btn,bd=0,bg='#323233',command=forward_to_Sign_up)
    back_btn.place(x=30,y=510)

    #Cancel button
    cancel_btn=Button(Student_Data5_fm, image=cancel1_btn,bd=0,bg='#323233',command=forward_to_Student_Data)
    cancel_btn.place(x=720,y=240,width=110)

    #Submit button
    submit_btn=Button(Student_Data5_fm, image=submit1_btn,bd=0,bg='#323233',command=check_input_validation)
    submit_btn.place(x=860,y=240,width=110)

    #Frame to its container
    Student_Data5_fm.pack(pady=100)
    Student_Data5_fm.pack_propagate(False)
    Student_Data5_fm.configure(width=1100,height=620)


def Login1():

    #Calling Student Data and Deleting the content of Login1
    def forward_to_Student_Data():
        Student_Data6_fm.destroy()
        Student_Data()

    #Frame of its container
    Student_Data6_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of Student
    heading_lb=Label(Student_Data6_fm,text='STUDENT',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.place(x=455,y=50,width=200)

    #Image icon 
    login_icon_lb=Label(Student_Data6_fm, image=login_icon,bd=0)
    login_icon_lb.place(x=500,y=100,width=100,height=100)

    #1st year button
    firstyear_btn=Button(Student_Data6_fm,text='FIRST YEAR',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED)
    firstyear_btn.place(x=450,y=220,width=200)

    #2nd year button
    secondyear_btn=Button(Student_Data6_fm,text='SECOND YEAR',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED)
    secondyear_btn.place(x=450,y=300,width=200)

    #3rd year button
    thirdyear_btn=Button(Student_Data6_fm,text='THIRD YEAR',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED)
    thirdyear_btn.place(x=450,y=380,width=200)

    #4th year button
    fourthyear_btn=Button(Student_Data6_fm,text='FOURTH YEAR',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED)
    fourthyear_btn.place(x=450,y=460,width=200)

    #logout button
    logout_btn=Button(Student_Data6_fm,image=logout1_btn,bd=0,bg='#323233',relief=RAISED,command=forward_to_Student_Data)
    logout_btn.place(x=940,y=520,width=120)

    #Frame of its container
    Student_Data6_fm.pack(pady=100)
    Student_Data6_fm.pack_propagate(False)
    Student_Data6_fm.configure(width=1100,height=620)


def Admin1():

    #Calling Student Data and Deleting the content of Admin1
    def forward_to_Student_Data():
        Student_Data7_fm.destroy()
        Student_Data()

    #Frame of its container
    Student_Data7_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of Student
    heading_lb=Label(Student_Data7_fm,text='ADMIN',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.place(x=453,y=50,width=200)

    #Image icon 
    login_icon_lb=Label(Student_Data7_fm, image=login_icon,bd=0)
    login_icon_lb.place(x=500,y=100,width=100,height=100)

    #View students info button
    firstyear_btn=Button(Student_Data7_fm,text="VIEW STUDENT'S INFO",bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED)
    firstyear_btn.place(x=400,y=220,width=300)

    #Edit students info button
    secondyear_btn=Button(Student_Data7_fm,text="EDIT STUDENT'S INFO",bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED)
    secondyear_btn.place(x=400,y=300,width=300)

    #Print students info button
    thirdyear_btn=Button(Student_Data7_fm,text="PRINT STUDENT'S INFO",bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED)
    thirdyear_btn.place(x=400,y=380,width=300)

    #View student by year level button
    fourthyear_btn=Button(Student_Data7_fm,text="VIEW STUDENT BY YEAR LEVEL",bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED)
    fourthyear_btn.place(x=350,y=460,width=400)

    #logout button
    logout_btn=Button(Student_Data7_fm,image=logout1_btn,bd=0,bg='#323233',relief=RAISED,command=forward_to_Student_Data)
    logout_btn.place(x=940,y=520,width=120)

    #Frame of its container
    Student_Data7_fm.pack(pady=100)
    Student_Data7_fm.pack_propagate(False)
    Student_Data7_fm.configure(width=1100,height=620)


Forward_Button()
Student_Data_fm.mainloop()
