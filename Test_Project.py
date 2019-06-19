import tkinter as tk
import csv


# ***** MAIN LOGIN WINDOW *****
class LoginWindow:
    # Create a class called Application w/ parent tk.Frame

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        # ***** Generate Users *****
        # Sets basic username/password parameters
        # Open csv file that stores user data
        with open('profiles.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            LoginWindow.users = {}
            # Create a new dictionary to hold temporary data for login

            for line in csv_reader:
                LoginWindow.users[line['user']] = line['password']
                # Read csv data into the temporary dictionary

        # ***** Create Logo *****
        # Create the logo at the top of the screen
        self.logo = tk.Label(self.frame)
        self.logo["text"] = "Login Application"
        self.logo["font"] = ('Times New Roman', 48)
        self.logo["bd"] = 1
        self.logo["relief"] = "solid"
        # ^ Adds a relief/border to the widget.
        # flat, groove, raised, ridge, solid, or sunken
        self.logo.grid(columnspan=2)

        # ***** Create Entries *****
        self.user_label = tk.Label(self.frame, text="Username:")
        self.user_label.grid(column=0, row=1)

        self.user_entry = tk.Entry(self.frame)
        self.user_entry.grid(column=1, row=1)

        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.grid(column=0, row=2)

        self.password_entry = tk.Entry(self.frame)
        self.password_entry.grid(column=1, row=2)

        # ***** Create Newuser Button *****
        self.newuser_button = tk.Button(self.frame, text="New user? Click here.", command=self.newuser)
        self.newuser_button.grid(columnspan=2, row=4)

        # ***** Pack the Frame *****
        self.frame.pack()

        # ***** Create Login Button *****
    def login(self):
        # Create a login function that checks for user input

        if self.user_entry.get() in LoginWindow.users.keys():
            if self.password_entry.get() == LoginWindow.users[self.user_entry.get()]:
                print("Logged in!")
            else:
                print("Incorrect password. Please try again.")
        else:
            print("That username doesn't exist. Please try again.")

        self.login_button = tk.Button(self.frame, text="Login", command=self.login)
        self.login_button.grid(columnspan=2, row=3)

        # ***** Create New User Button *****
    def newuser(self):
        def newuser_main():
            root = tk.Tk()
            app = NewUserWindow(root)
            root.mainloop()

        if __name__ == '__main__':
            newuser_main()


# ***** NEW USER WINDOW *****
class NewUserWindow:
    # A new window for creating a new user profile

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        # self.root = tk.Tk()
        # self.create_logo()
        # self.create_entries()
        # self.confirmation_button()
        # self.root.mainloop()

        # ***** Create Logo *****
        # Create the logo at the top of the screen
        self.logo = tk.Label(self.frame)
        self.logo["text"] = "Welcome stranger!"
        self.logo["font"] = ('Times New Roman', 36)
        self.logo["bd"] = 1
        self.logo["relief"] = "solid"
        # ^ Adds a relief/border to the widget.
        # flat, groove, raised, ridge, solid, or sunken
        self.logo.grid(columnspan=2)

        # ***** Create Entries *****
        # Creates labels and entries
        self.user_label = tk.Label(self.frame, text="Create username:")
        self.user_label.grid(column=0, row=1, sticky='E')

        self.user_entry = tk.Entry(self.frame)
        self.user_entry.grid(column=1, row=1)

        self.password_label = tk.Label(self.frame, text="Create password:")
        self.password_label.grid(column=0, row=2, sticky='E')

        self.password_entry = tk.Entry(self.frame)
        self.password_entry.grid(column=1, row=2)

        # Create the confirmation buttons
        self.confirm_button = tk.Button(self.frame, text="Confirm", command=self.confirm)
        self.confirm_button.grid(columnspan=2, row=3)
        self.frame.pack()
        # ***** Confirmation Button *****
        # Button that confirms the selection and adds the
        # entry into the dictionary

    def confirm(self):
        temp_user = self.user_entry.get()
        temp_password = self.password_entry.get()

        if temp_user in LoginWindow.users.keys():
            # Check to see if the username is already taken
            print(f"{self.user_entry.get()} already taken.")
        elif temp_user == '':
            print("You didn't enter a username ya ding dong!")
        elif temp_password == '':
            print("You didn't enter a password dummy!")
        else:
            # Add a new dictionary entry for the given input
            LoginWindow.users[temp_user] = temp_password

            with open('profiles.csv', 'a+', newline='') as new_file:
                fieldnames = ['user', 'password']

                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

                csv_writer.writerow({'user': temp_user, 'password': temp_password})

            print("New profile created successfully")
            self.master.destroy()


def main():
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()