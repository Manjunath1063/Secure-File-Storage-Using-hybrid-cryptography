import tkinter as tk
from tkinter import *
from tkinter import ttk

from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw

import pickle
from tkinter import messagebox

import os
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

class GraphicalPasswordApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, RegistrationPage, LoginPage, PasswordPageOne, PasswordPageTwo,
                  PasswordPageThree, PasswordPageFour, PasswordPageFive, HomePage, LoginPageOne,
                  LoginPageTwo, LoginPageThree, LoginPageFour, LoginPageFive):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        label = tk.Label(frame, bg="white", text="GRAPHICAL PASSWORD AUTHENTICATION SYSTEM", font=("Arial", 30), pady=30)
        label.pack(pady=10,padx=10)

        canvas = tk.Canvas(frame, width=200, height=200)
        canvas.pack(pady=20)
        
        logo = Image.open('logo.png').resize((200, 200))

        logo = ImageTk.PhotoImage(logo)
        canvas.background = logo
        canvas.create_image(0, 0, anchor="nw", image=logo)

        button1 = tk.Button(frame, text="REGISTER NOW", width=20, height=2, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(RegistrationPage))
        button1.pack(pady=20)

        button2 = tk.Button(frame, text="LOGIN", width=20, height=2, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(LoginPage))
        button2.pack(pady=5)


class RegistrationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button1 = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=20, anchor='w', padx=10)

        label = tk.Label(frame, bg="white", text="REGISTER NEW USER HERE", font=("Arial", 30), pady=30)
        label.pack(pady=10,padx=10)

        label2 = tk.Label(frame, text = "USERNAME", bg="white")
        label2.pack()

        username = tk.Entry(frame, bd=2)
        username.pack(pady=5,ipadx=50, ipady=5)

        label3 = tk.Label(frame, text = "PASSWORD", bg="white")
        label3.pack()
        
        password = tk.Entry(frame, bd=2, show = "*")
        password.pack(pady=5,ipadx=50, ipady=5)

        label4 = tk.Label(frame, text = "CONFIRM PASSWORD", bg="white")
        label4.pack()
        
        confirmpassword = tk.Entry(frame, bd=2, show = "*")
        confirmpassword.pack(pady=5,ipadx=50, ipady=5)

        def callback():

            current_user_dict = {}
            registered_user_dict = {}
            
            registered_users = []
            
            username_data = username.get()
            username.delete(0,END)
            username.insert(0,"")
            
            password_data = password.get()
            password.delete(0,END)
            password.insert(0,"")
            
            confirmpassword_data = confirmpassword.get()
            confirmpassword.delete(0,END)
            confirmpassword.insert(0,"")
            
            try:
                pickle_in = open("usersdata.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                current_user_dict = pickledata.get('current_user_dict')

                pickle_in = open("registeredusers.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                registered_user_dict = pickledata.get('registered_user_dict')

                for i in registered_user_dict:
                    registered_users.append(i)
            except:
                pass

            
            if username_data == "":
                messagebox.showinfo("Alert!", "Please enter username!")

            elif password_data == "":
                messagebox.showinfo("Alert!", "Please enter password!")

            elif confirmpassword_data == "":
                messagebox.showinfo("Alert!", "Please enter confirm password!")

            else:
                if username_data not in registered_users:
                    if password_data != confirmpassword_data:
                        messagebox.showinfo("Alert!", "Please check your password!")
                    else:
                        current_user_dict["currentuser"] = {"username": username_data,
                                                               "password": password_data,
                                                               "image_one": "NA",
                                                               "image_two": "NA",
                                                               "image_three": "NA",
                                                               "image_four": "NA",
                                                               "image_five": "NA"}

                        pickle_out = open("usersdata.pickle", "wb")
                        pickledata = {'current_user_dict': current_user_dict}
                        pickle.dump(pickledata, pickle_out)
                        pickle_out.close()

                        controller.show_frame(PasswordPageOne)
                else:
                    messagebox.showinfo("Alert!", "Account with this username already exist!")
                    

        button2 = tk.Button(frame, text="SUBMIT", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=callback)
        button2.pack(pady=20, padx=10)

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button1 = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=20, anchor='w', padx=10)

        label = tk.Label(frame, bg="white", text="LOGIN HERE", font=("Arial", 30), pady=30)
        label.pack(pady=10,padx=10)

        label2 = tk.Label(frame, text = "USERNAME", bg="white")
        label2.pack()

        username = tk.Entry(frame, bd=2)
        username.pack(pady=5,ipadx=50, ipady=5)

        label3 = tk.Label(frame, text = "PASSWORD", bg="white")
        label3.pack()
        
        password = tk.Entry(frame, bd=2, show = "*")
        password.pack(pady=5,ipadx=50, ipady=5)

        def callback():

            registered_user_dict = {}
            current_user_dict = {}
            
            registered_users = []
            
            username_data = username.get()
            username.delete(0,END)
            username.insert(0,"")
            
            password_data = password.get()
            password.delete(0,END)
            password.insert(0,"")

            try:
                pickle_in = open("registeredusers.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                registered_user_dict = pickledata.get('registered_user_dict')

                pickle_in = open("usersdata.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                current_user_dict = pickledata.get('current_user_dict')

                for i in registered_user_dict:
                    registered_users.append(i)
            except:
                pass

            if username_data == "":
                messagebox.showinfo("Alert!", "Please enter username!")

            elif password_data == "":
                messagebox.showinfo("Alert!", "Please enter password!")

            else:
                if username_data not in registered_users:
                    messagebox.showinfo("Alert!", "Please create your account first!")
                else:
                    user_password = registered_user_dict.get(username_data)["password"]

                    if user_password == password_data:

                        
                        user_password = registered_user_dict.get(username_data)["password"]
                        user_image_one = registered_user_dict.get(username_data)["image_one_code"]
                        user_image_two = registered_user_dict.get(username_data)["image_two_code"]
                        user_image_three = registered_user_dict.get(username_data)["image_three_code"]
                        user_image_four = registered_user_dict.get(username_data)["image_four_code"]
                        user_image_five = registered_user_dict.get(username_data)["image_five_code"]

                        current_user_dict["currentuser"].update({"username":username_data,
                                                                 "password":user_password,
                                                                 "image_one":user_image_one,
                                                                 "image_two":user_image_two,
                                                                 "image_three":user_image_three,
                                                                 "image_four":user_image_four,
                                                                 "image_five":user_image_five})

                        pickle_out = open("usersdata.pickle", "wb")
                        pickledata = {'current_user_dict': current_user_dict}
                        pickle.dump(pickledata, pickle_out)
                        pickle_out.close()
                        
                        controller.show_frame(LoginPageOne)
                    else:
                        messagebox.showinfo("Alert!", "Please check your passsword!")

        button2 = tk.Button(frame, text="SUBMIT", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=callback)
        button2.pack(pady=20, padx=10)

                
class PasswordPageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(RegistrationPage))
        button.pack(pady=20, padx=10, anchor='w')

        label = tk.Label(frame, bg="white", text="Select Point On Image To Create Your Password", font=("Arial", 25))
        label.pack(pady=10,padx=10)

        def printcoords(event):

            current_user_dict = {}
            
            try:
                pickle_in = open("usersdata.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                current_user_dict = pickledata.get('current_user_dict')

            except:
                pass

            count_x = 0
            count_y = 0
            
            for i in range(1,25):
                if event.x <= i*20:
                    count_x+=1

                if event.y <= i*20:
                    count_y+=1

            current_user_dict["currentuser"].update({"image_one": str(abs(count_y-25))+str(abs(count_x-25))})

            pickle_out = open("usersdata.pickle", "wb")
            pickledata = {'current_user_dict': current_user_dict}
            pickle.dump(pickledata, pickle_out)
            pickle_out.close()
            
            controller.show_frame(PasswordPageTwo)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        canvas = tk.Canvas(frame, width=500, height=500)
        canvas.pack()

        img = Image.open('image1.jpg').resize((500, 500))
        
        draw = ImageDraw.Draw(img)
        for i in range(1,25):
            draw.line((0,i*20, 500,i*20), fill=256)
        for i in range(1,25):
            draw.line((i*20,0 , i*20, 500), fill=256)

        img = ImageTk.PhotoImage(img)
        canvas.background = img
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.bind("<Button 1>",printcoords)

class PasswordPageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(PasswordPageOne))
        button.pack(pady=20, padx=10, anchor='w')

        label = tk.Label(frame, bg="white", text="Select Point On Image To Create Your Password", font=("Arial", 25))
        label.pack(pady=10,padx=10)

        def printcoords(event):
            
            current_user_dict = {}
            
            try:
                pickle_in = open("usersdata.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                current_user_dict = pickledata.get('current_user_dict')

            except:
                pass
            
            count_x = 0
            count_y = 0
            
            for i in range(1,25):
                if event.x <= i*20:
                    count_x+=1

                if event.y <= i*20:
                    count_y+=1
                    
            current_user_dict["currentuser"].update({"image_two": str(abs(count_y-25))+str(abs(count_x-25))})

            pickle_out = open("usersdata.pickle", "wb")
            pickledata = {'current_user_dict': current_user_dict}
            pickle.dump(pickledata, pickle_out)
            pickle_out.close()
            
            controller.show_frame(PasswordPageThree)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        canvas = tk.Canvas(frame, width=500, height=500)
        canvas.pack()

        img = Image.open('image2.jpg').resize((500, 500))
        
        draw = ImageDraw.Draw(img)
        for i in range(1,25):
            draw.line((0,i*20, 500,i*20), fill=256)
        for i in range(1,25):
            draw.line((i*20,0 , i*20, 500), fill=256)

        img = ImageTk.PhotoImage(img)
        canvas.background = img
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.bind("<Button 1>",printcoords)

class PasswordPageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(PasswordPageOne))
        button.pack(pady=20, padx=10, anchor='w')

        label = tk.Label(frame, bg="white", text="Select Point On Image To Create Your Password", font=("Arial", 25))
        label.pack(pady=10,padx=10)

        def printcoords(event):

            current_user_dict = {}
            
            try:
                pickle_in = open("usersdata.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                current_user_dict = pickledata.get('current_user_dict')

            except:
                pass
            
            count_x = 0
            count_y = 0
            
            for i in range(1,25):
                if event.x <= i*20:
                    count_x+=1

                if event.y <= i*20:
                    count_y+=1
                    
            current_user_dict["currentuser"].update({"image_three": str(abs(count_y-25))+str(abs(count_x-25))})

            pickle_out = open("usersdata.pickle", "wb")
            pickledata = {'current_user_dict': current_user_dict}
            pickle.dump(pickledata, pickle_out)
            pickle_out.close()
            
            controller.show_frame(PasswordPageFour)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        canvas = tk.Canvas(frame, width=500, height=500)
        canvas.pack()

        img = Image.open('image3.jpg').resize((500, 500))
        
        draw = ImageDraw.Draw(img)
        for i in range(1,25):
            draw.line((0,i*20, 500,i*20), fill=256)
        for i in range(1,25):
            draw.line((i*20,0 , i*20, 500), fill=256)

        img = ImageTk.PhotoImage(img)
        canvas.background = img
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.bind("<Button 1>",printcoords)

class PasswordPageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(PasswordPageThree))
        button.pack(pady=20, padx=10, anchor='w')

        label = tk.Label(frame, bg="white", text="Select Point On Image To Create Your Password", font=("Arial", 25))
        label.pack(pady=10,padx=10)

        def printcoords(event):

            current_user_dict = {}
            
            try:
                pickle_in = open("usersdata.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                current_user_dict = pickledata.get('current_user_dict')

            except:
                pass
            
            count_x = 0
            count_y = 0
            
            for i in range(1,25):
                if event.x <= i*20:
                    count_x+=1

                if event.y <= i*20:
                    count_y+=1
                    
            current_user_dict["currentuser"].update({"image_four": str(abs(count_y-25))+str(abs(count_x-25))})

            pickle_out = open("usersdata.pickle", "wb")
            pickledata = {'current_user_dict': current_user_dict}
            pickle.dump(pickledata, pickle_out)
            pickle_out.close()
            
            controller.show_frame(PasswordPageFive)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        canvas = tk.Canvas(frame, width=500, height=500)
        canvas.pack()

        img = Image.open('image4.jpg').resize((500, 500))
        
        draw = ImageDraw.Draw(img)
        for i in range(1,25):
            draw.line((0,i*20, 500,i*20), fill=256)
        for i in range(1,25):
            draw.line((i*20,0 , i*20, 500), fill=256)

        img = ImageTk.PhotoImage(img)
        canvas.background = img
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.bind("<Button 1>",printcoords)

class PasswordPageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(PasswordPageFour))
        button.pack(pady=20, padx=10, anchor='w')

        label = tk.Label(frame, bg="white", text="Select Point On Image To Create Your Password", font=("Arial", 25))
        label.pack(pady=10,padx=10)

        def printcoords(event):

            current_user_dict = {}

            registered_user_dict = {}
            
            try:
                pickle_in = open("usersdata.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                current_user_dict = pickledata.get('current_user_dict')

                pickle_in = open("registeredusers.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                registered_user_dict = pickledata.get('registered_user_dict')

            except:
                pass
            
            count_x = 0
            count_y = 0
            
            for i in range(1,25):
                if event.x <= i*20:
                    count_x+=1

                if event.y <= i*20:
                    count_y+=1
                    
            current_user_dict["currentuser"].update({"image_five": str(abs(count_y-25))+str(abs(count_x-25))})

            pickle_out = open("usersdata.pickle", "wb")
            pickledata = {'current_user_dict': current_user_dict}
            pickle.dump(pickledata, pickle_out)
            pickle_out.close()

            newusername = current_user_dict["currentuser"].get("username")
            newpassword = current_user_dict["currentuser"].get("password")
            
            image_one_code = current_user_dict["currentuser"].get("image_one")
            image_two_code = current_user_dict["currentuser"].get("image_two")
            image_three_code = current_user_dict["currentuser"].get("image_three")
            image_four_code = current_user_dict["currentuser"].get("image_four")
            image_five_code = current_user_dict["currentuser"].get("image_five")

            registered_user_dict[newusername] = {"username": newusername,
                                                 "password": newpassword,
                                                 "image_one_code": image_one_code,
                                                 "image_two_code": image_two_code,
                                                 "image_three_code": image_three_code,
                                                 "image_four_code": image_four_code,
                                                 "image_five_code": image_five_code}

            pickle_out = open("registeredusers.pickle", "wb")
            pickledata = {'registered_user_dict': registered_user_dict}
            pickle.dump(pickledata, pickle_out)
            pickle_out.close()
            
            messagebox.showinfo("Alert!", "Registration Successful !")
            
            controller.show_frame(LoginPage)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        canvas = tk.Canvas(frame, width=500, height=500)
        canvas.pack()

        img = Image.open('image5.jpg').resize((500, 500))
        
        draw = ImageDraw.Draw(img)
        for i in range(1,25):
            draw.line((0,i*20, 500,i*20), fill=256)
        for i in range(1,25):
            draw.line((i*20,0 , i*20, 500), fill=256)

        img = ImageTk.PhotoImage(img)
        canvas.background = img
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.bind("<Button 1>",printcoords)

class LoginPageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(LoginPage))
        button.pack(pady=20, padx=10, anchor='w')

        label = tk.Label(frame, bg="white", text="Select Point On Image To Create Your Password", font=("Arial", 25))
        label.pack(pady=10,padx=10)

        def printcoords(event):

            current_user_dict = {}
            
            count_x = 0
            count_y = 0
            
            for i in range(1,25):
                if event.x <= i*20:
                    count_x+=1

                if event.y <= i*20:
                    count_y+=1

            try:
                pickle_in = open("usersdata.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                current_user_dict = pickledata.get('current_user_dict')

            except:
                pass

            if current_user_dict["currentuser"].get("image_one") == str(abs(count_y-25))+str(abs(count_x-25)):                
                controller.show_frame(LoginPageTwo)
            else:
                messagebox.showinfo("Alert!", "Please select correct point!")

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        canvas = tk.Canvas(frame, width=500, height=500)
        canvas.pack()

        img = Image.open('image1.jpg').resize((500, 500))
        
        draw = ImageDraw.Draw(img)
        for i in range(1,25):
            draw.line((0,i*20, 500,i*20), fill=256)
        for i in range(1,25):
            draw.line((i*20,0 , i*20, 500), fill=256)

        img = ImageTk.PhotoImage(img)
        canvas.background = img
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.bind("<Button 1>",printcoords)

class LoginPageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(LoginPageOne))
        button.pack(pady=20, padx=10, anchor='w')

        label = tk.Label(frame, bg="white", text="Select Point On Image To Create Your Password", font=("Arial", 25))
        label.pack(pady=10,padx=10)

        def printcoords(event):

            current_user_dict = {}
            
            count_x = 0
            count_y = 0
            
            for i in range(1,25):
                if event.x <= i*20:
                    count_x+=1

                if event.y <= i*20:
                    count_y+=1
                    
            try:
                pickle_in = open("usersdata.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                current_user_dict = pickledata.get('current_user_dict')
            except:
                pass

            if current_user_dict["currentuser"].get("image_two") == str(abs(count_y-25))+str(abs(count_x-25)):
                controller.show_frame(LoginPageThree)
            else:
                messagebox.showinfo("Alert!", "Please select correct point!")

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        canvas = tk.Canvas(frame, width=500, height=500)
        canvas.pack()

        img = Image.open('image2.jpg').resize((500, 500))
        
        draw = ImageDraw.Draw(img)
        for i in range(1,25):
            draw.line((0,i*20, 500,i*20), fill=256)
        for i in range(1,25):
            draw.line((i*20,0 , i*20, 500), fill=256)

        img = ImageTk.PhotoImage(img)
        canvas.background = img
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.bind("<Button 1>",printcoords)

class LoginPageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(LoginPageTwo))
        button.pack(pady=20, padx=10, anchor='w')

        label = tk.Label(frame, bg="white", text="Select Point On Image To Create Your Password", font=("Arial", 25))
        label.pack(pady=10,padx=10)

        def printcoords(event):

            current_user_dict = {}
            
            count_x = 0
            count_y = 0
            
            for i in range(1,25):
                if event.x <= i*20:
                    count_x+=1

                if event.y <= i*20:
                    count_y+=1
            try:
                pickle_in = open("usersdata.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                current_user_dict = pickledata.get('current_user_dict')
            except:
                pass

            if current_user_dict["currentuser"].get("image_three") == str(abs(count_y-25))+str(abs(count_x-25)):
                controller.show_frame(LoginPageFour)
            else:
                messagebox.showinfo("Alert!", "Please select correct point!")


        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        canvas = tk.Canvas(frame, width=500, height=500)
        canvas.pack()

        img = Image.open('image3.jpg').resize((500, 500))
        
        draw = ImageDraw.Draw(img)
        for i in range(1,25):
            draw.line((0,i*20, 500,i*20), fill=256)
        for i in range(1,25):
            draw.line((i*20,0 , i*20, 500), fill=256)

        img = ImageTk.PhotoImage(img)
        canvas.background = img
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.bind("<Button 1>",printcoords)

class LoginPageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(LoginPageThree))
        button.pack(pady=20, padx=10, anchor='w')

        label = tk.Label(frame, bg="white", text="Select Point On Image To Create Your Password", font=("Arial", 25))
        label.pack(pady=10,padx=10)

        def printcoords(event):

            current_user_dict = {}
            
            count_x = 0
            count_y = 0
            
            for i in range(1,25):
                if event.x <= i*20:
                    count_x+=1

                if event.y <= i*20:
                    count_y+=1
                    
            try:
                pickle_in = open("usersdata.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                current_user_dict = pickledata.get('current_user_dict')

            except:
                pass

            if current_user_dict["currentuser"].get("image_four") == str(abs(count_y-25))+str(abs(count_x-25)):
                controller.show_frame(LoginPageFive)
            else:
                messagebox.showinfo("Alert!", "Please select correct point!")

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        canvas = tk.Canvas(frame, width=500, height=500)
        canvas.pack()

        img = Image.open('image4.jpg').resize((500, 500))
        
        draw = ImageDraw.Draw(img)
        for i in range(1,25):
            draw.line((0,i*20, 500,i*20), fill=256)
        for i in range(1,25):
            draw.line((i*20,0 , i*20, 500), fill=256)

        img = ImageTk.PhotoImage(img)
        canvas.background = img
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.bind("<Button 1>",printcoords)

class LoginPageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        button = tk.Button(frame, text="BACK", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(LoginPageFour))
        button.pack(pady=20, padx=10, anchor='w')

        label = tk.Label(frame, bg="white", text="Select Point On Image To Create Your Password", font=("Arial", 25))
        label.pack(pady=10,padx=10)

        def printcoords(event):

            current_user_dict = {}
            
            count_x = 0
            count_y = 0
            
            for i in range(1,25):
                if event.x <= i*20:
                    count_x+=1

                if event.y <= i*20:
                    count_y+=1
                    
            try:
                pickle_in = open("usersdata.pickle", "rb")
                pickledata = pickle.load(pickle_in)
                current_user_dict = pickledata.get('current_user_dict')

            except:
                pass

            if current_user_dict["currentuser"].get("image_five") == str(abs(count_y-25))+str(abs(count_x-25)):
                messagebox.showinfo("Alert!", "Login Successful!")
                controller.show_frame(HomePage)
            else:
                messagebox.showinfo("Alert!", "Please select correct point!")

        frame = tk.Frame(self,bg="white")
        frame.pack(fill="both",expand=True)

        canvas = tk.Canvas(frame, width=500, height=500)
        canvas.pack()

        img = Image.open('image5.jpg').resize((500, 500))
        
        draw = ImageDraw.Draw(img)
        for i in range(1,25):
            draw.line((0,i*20, 500,i*20), fill=256)
        for i in range(1,25):
            draw.line((i*20,0 , i*20, 500), fill=256)

        img = ImageTk.PhotoImage(img)
        canvas.background = img
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.bind("<Button 1>",printcoords)

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        frame = tk.Frame(self, bg="white")
        frame.pack(fill="both", expand=True)

        button = tk.Button(frame, text="LOGOUT", width=10, height=1, bg = "firebrick", foreground = "white",
                            command=lambda: controller.show_frame(StartPage))
        button.pack(pady=20, padx=10, anchor='w')

        label = tk.Label(frame, text="Home Page - File Encryption/Decryption", bg="white", font=("Arial", 20))
        label.pack(pady=20)

        # Buttons
        self.upload_button = tk.Button(frame, text="Upload File", command=self.upload_file, width=20, height=2, bg="firebrick", foreground="white")
        self.upload_button.pack(pady=20)

        self.restore_button = tk.Button(frame, text="Restore File", command=self.restore_file, width=20, height=2, bg="firebrick", foreground="white")
        self.restore_button.pack(pady=20)

        # Key file selection
        self.key_file_label = tk.Label(frame, text="Key File (optional):", bg="white")
        self.key_file_label.pack(pady=10)

        self.key_file_entry = tk.Entry(frame, width=50)
        self.key_file_entry.pack(pady=5)

        self.browse_key_button = tk.Button(frame, text="Browse Key File", command=self.browse_key_file, bg="firebrick", foreground="white")
        self.browse_key_button.pack(pady=5)

    def upload_file(self):
        file_path = filedialog.askopenfilename(title="Select a File")
        if not file_path:
            messagebox.showwarning("No File", "Please select a file to upload.")
            return

        # Generate encryption key
        key = Fernet.generate_key()
        cipher = Fernet(key)

        # Encrypt the file
        with open(file_path, "rb") as file:
            data = file.read()
        encrypted_data = cipher.encrypt(data)

        # Save the encrypted file to the server folder
        SERVER_FOLDER = "server_storage"
        os.makedirs(SERVER_FOLDER, exist_ok=True)
        encrypted_file_name = os.path.basename(file_path) + ".enc"
        encrypted_file_path = os.path.join(SERVER_FOLDER, encrypted_file_name)
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        # Save key to a file
        key_file_path = filedialog.asksaveasfilename(
            defaultextension=".key",
            filetypes=[("Key Files", "*.key")],
            title="Save Encryption Key"
        )
        if key_file_path:
            with open(key_file_path, "wb") as key_file:
                key_file.write(key)
            messagebox.showinfo("Success", f"File uploaded and key saved at:\n{key_file_path}")
        else:
            messagebox.showwarning("Key Not Saved", "File uploaded, but the key was not saved.")

    def restore_file(self):
        encrypted_file_name = filedialog.askopenfilename(
            title="Select Encrypted File to Restore",
            filetypes=[("Encrypted Files", "*.enc")],
            initialdir="server_storage"
        )
        if not encrypted_file_name:
            messagebox.showwarning("No File", "Please select an encrypted file to restore.")
            return

        key_file_path = self.key_file_entry.get() or filedialog.askopenfilename(
            title="Select Encryption Key File",
            filetypes=[("Key Files", "*.key")]
        )
        if not key_file_path:
            messagebox.showerror("No Key", "Encryption key is required to restore the file.")
            return

        # Load the encryption key
        try:
            with open(key_file_path, "rb") as key_file:
                key = key_file.read()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read the key file: {e}")
            return

        cipher = Fernet(key)

        # Read the encrypted file
        try:
            with open(encrypted_file_name, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read the encrypted file: {e}")
            return

        # Decrypt the file
        try:
            decrypted_data = cipher.decrypt(encrypted_data)
        except Exception as e:
            messagebox.showerror("Decryption Error", "Invalid key or corrupted file.")
            return

        # Save the decrypted file
        save_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("All Files", "*.*")],
            title="Save Decrypted File"
        )
        if save_path:
            with open(save_path, "wb") as file:
                file.write(decrypted_data)
            messagebox.showinfo("Success", f"File restored and saved at:\n{save_path}")
        else:
            messagebox.showwarning("Save Canceled", "Restoration canceled by the user.")

    def browse_key_file(self):
        key_file_path = filedialog.askopenfilename(title="Select Key File", filetypes=[("Key Files", "*.key")])
        if key_file_path:
            self.key_file_entry.delete(0, tk.END)
            self.key_file_entry.insert(0, key_file_path)

        

app = GraphicalPasswordApp()
app.title('Graphical Password Authentication System')
app.geometry('1600x800+0+0')
app.mainloop()
