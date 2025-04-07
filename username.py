from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

#The root of the system
root=Tk()
root.title('Student Data')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable


def login():
       username=user.get()
       password=code.get()

       if username=='admin' and password=='1234':
              screen=Toplevel(root)
              screen.title("Student Data")
              screen.geometry('925x500+300+200')
              screen.config(bg="white")

              Label(screen,text='LOGIN',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold')).pack(expand=True)
              

              screen.mainloop()

       elif username!='admin' and password!='1234':
              messagebox.showerror("Invalid","invalid username and password")

       elif password!="1234":
              messagebox.showerror("Invalid","invalid password")
       elif username!='admin':
              messagebox.showerror("Invalid","invalid username")

#QR code
'''img=PhotoImage(file='login.png') 
Label(root,image=img,bg='white').place(x=50,y=50)
'''
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

#Heading of LOGIN
heading=Label(frame,text='LOGIN',fg='#217982',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=5)


def on_enter(e):
        user.delete(0,'end')

def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')

#Username           
user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


def on_enter(e):
        code.delete(0,'end')

def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')


#Password
code=Entry(frame,width=25,fg='black',border=0,bg="white",show='*',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


#Show password command
#may problema pa sa pag show password
entry=Entry(root,show='*')

def show_password():
       if entry.cget('show') == '*':
              entry.config(show='')
       else:
              entry.config(show='*')

check_button=Checkbutton(root, text="show password",command=show_password)
check_button.place(x=505,y=250)

#Button of LOGIN
Button(frame,width=39,pady=7,text='Login',bg='#217982',fg='white',border=0,command=login).place(x=35,y=206)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

#Sign-up Button
sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#217982')
sign_up.place(x=215,y=270)



root.mainloop()