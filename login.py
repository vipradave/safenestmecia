from tkinter import *
from PIL import ImageTk

def on_enter(event):
    if usernameEntry.get=='Username':
        usernameEntry.delete(0,END)

login_window = Tk()
login_window.geometry('900x660+50+50')
bgImage = ImageTk.PhotoImage(file='bg1.png')

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

# heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold')bg='white',fg='gray9')
# heading.place(x=605,y=120)

usernameEntry=Entry(login_window)
usernameEntry.place(x=650,y=200)
usernameEntry.insert(0,'FullName')
usernameEntry.bind('<FocusIn>',on_enter)

frame1=Frame(login_window,width=250,height=2,bg='gray9').place(x=580,y=222)

passwordEntry=Entry(login_window)
passwordEntry.place(x=650,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',on_enter)

frame2=Frame(login_window,width=250,height=2,bg='gray9').place(x=580,y=282)

forgetButton=Button(login_window,text='Forgot Password',bd=0,bg='white',activebackground='white'
                    ,cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg='black')
forgetButton.place(x=715,y=295)

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold')
                   ,fg='white',bg='black',activeforeground='white',activebackground='black',cursor='hand2',bd=0,width=19)
loginButton.place(x=578,y=350)
login_window.mainloop()