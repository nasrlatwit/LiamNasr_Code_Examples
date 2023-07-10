#Login Page example, USE 'admin' and 'password' as username and password to test my system
import tkinter as tk
from tkinter import messagebox

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login System")
        self.geometry("300x200")
        
        self.login_frame = LoginFrame(self)
        self.home_frame = HomeFrame(self)
        self.profile_frame = ProfileFrame(self)
        
        self.show_login_frame()
        
    def show_login_frame(self):
        self.login_frame.pack()
        self.home_frame.pack_forget()
        self.profile_frame.pack_forget()
        
    def show_home_frame(self):
        self.login_frame.pack_forget()
        self.home_frame.pack()
        self.profile_frame.pack_forget()
        
    def show_profile_frame(self):
        self.login_frame.pack_forget()
        self.home_frame.pack_forget()
        self.profile_frame.pack()
        

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = tk.Label(self, text="Login Page")
        self.label.pack(pady=10)
        
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()
        
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)
        
    def login(self):
        username = self.username_entry.get() 
        password = self.password_entry.get()
        
        # Perform login validation here (e.g., check against a database)
        # For simplicity, we'll use a dummy check
        if username == "admin" and password == "password":
            self.master.show_home_frame()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")


class HomeFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = tk.Label(self, text="Home Page")
        self.label.pack(pady=10)
        
        self.profile_button = tk.Button(self, text="View Profile", command=self.view_profile)
        self.profile_button.pack(pady=5)
        
        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack(pady=5)
        
    def view_profile(self):
        self.master.show_profile_frame()
        
    def logout(self):
        self.master.show_login_frame()


class ProfileFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = tk.Label(self, text="Profile Page")
        self.label.pack(pady=10)
        
        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=5)
        
    def go_back(self):
        self.master.show_home_frame()


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
