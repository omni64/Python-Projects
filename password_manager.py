from tkinter import *
import json
import os
def main_screen():
    global land
    land = Tk()
    land.geometry('200x150')
    land.title("Hello World")
    Label(text = "Welcome", font = ("Calibri", 15 ),foreground = "red",  height = "2", width = "200", bg = "black").pack()
    Label(text = "").pack()
    Button(text = "Log In", command = login).pack()
    Button(text = "Register", command = register).pack()
    land.mainloop()

def register():
    global regscreen
    global username
    global passwd
    global uname
    global pwd
    username = StringVar()
    passwd = StringVar()
    regscreen = Toplevel(land)
    regscreen.title('Register')
    regscreen.geometry("220x200")
    Label(regscreen, text = "Please enter a username and password", height = "2" ).pack()
    Label(regscreen, text = "").pack()
    Label(regscreen,text = "Username*").pack()
    uname = Entry(regscreen, textvariable = username)
    uname.pack()
    Label(regscreen, text = "Password*").pack()
    pwd = Entry(regscreen, show = '*', textvariable = passwd)
    pwd.pack()
    Button(regscreen, text = "Register", command = reg_user).pack()
    

def reg_user():
    name = username.get()
    key = passwd.get()
    if os.path.exists('keys.json'):
        with open('keys.json', 'r') as f:
            chain = json.load(f)
            f.close()
            if name in chain:
                Label(regscreen, text = "Username Already Exists", foreground = 'red').pack()
            else:
                chain[name] = key
                with open('keys.json', 'w') as f:
                    jdump = json.dumps(chain)
                    f.write(jdump)
                    f.close()
                    Label(regscreen, text = "Registration Successful", fg = 'green').pack()
                uname.delete(0,END)
                pwd.delete(0,END)
    else:
        with open("keys.json", 'w') as f:
            chain = dict()
            chain[name] = key
            jdump = json.dumps(chain)
            f.write(jdump)
            f.close()
            Label(regscreen, text = "Registration Successful", fg = 'green').pack()
    

def login():
    global logscreen
    logscreen = Tk()
    logscreen.title("Log in")
    global username_in
    global passwd_in
    global uname_in
    global pwd_in
    username_in = StringVar()
    passwd_in = StringVar()
    Label(logscreen,text = "Username*").pack()
    uname_in = Entry(logscreen, textvariable = username_in)
    uname_in.pack()
    Label(logscreen, text = "Password*").pack()
    pwd_in = Entry(logscreen, show = '*', textvariable = passwd_in)
    pwd_in.pack()
    Button(logscreen, text = "Log in", command = login_user).pack()


def login_user():
    name = uname_in.get()
    key = pwd_in.get()
    if os.path.exists('keys.json'):
            with open('keys.json', 'r') as f:
                chain = json.load(f)
                f.close()
                if chain[name] == key:
                    Label(land, text = 'Access Granted', fg = 'green').pack()                    
                elif(name not in chain):
                    Label(logscreen, text = 'No user detected', fg = 'red').pack()
                elif(not (chain[name] == key)):
                    Label(logscreen, text = 'Incorrect Password!!', fg = 'red').pack()
    
main_screen()

