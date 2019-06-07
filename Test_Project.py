import tkinter as tk
import csv


# ***** MAIN LOGIN WINDOW *****
class LoginWindow(tk.Frame):
    # Create a class called Application w/ parent tk.Frame

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.generate_users()
        self.create_logo()
        self.create_entries()
        self.create_login_button()
        self.create_newuser_button()
        # Generate EVERYTHING

    def generate_users(self):
        # Sets basic username/password parameters

        # Open csv file that stores user data
        with open('profiles.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            LoginWindow.users = {}
            # Create a new dictionary to hold temporary data for login

            for line in csv_reader:
                LoginWindow.users[line['user']] = line['password']
                # Read csv data into the temporary dictionary

    def create_logo(self):
        # Create the logo at the top of the screen
        self.logo = tk.Label(self)
        self.logo["text"] = "Login Application"
        self.logo["font"] = ('Times New Roman', 48)
        self.logo["bd"] = 1
        self.logo["relief"] = "solid"
        # ^ Adds a relief/border to the widget.
        # flat, groove, raised, ridge, solid, or sunken
        self.logo.grid(columnspan=2)

    def create_entries(self):
        self.user_label = tk.Label(self, text="Username:")
        self.user_label.grid(column=0, row=1)

        self.user_entry = tk.Entry(self)
        self.user_entry.grid(column=1, row=1)

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(column=0, row=2)

        self.password_entry = tk.Entry(self)
        self.password_entry.grid(column=1, row=2)

    def create_login_button(self):

        def login(event):
            # Create a login function that checks for user input

            if self.user_entry.get() in LoginWindow.users.keys():
                if self.password_entry.get() == LoginWindow.users[self.user_entry.get()]:
                    print("Logged in!")
                else:
                    print("Incorrect password. Please try again.")
            else:
                print("That username doesn't exist. Please try again.")

        self.login_button = tk.Button(self, text="Login")
        self.login_button.bind("<Button-1>", login)
        self.login_button.grid(columnspan=2, row=3)

    def create_newuser_button(self):

        def newuser(event):
            root1 = tk.Tk()
            app1 = NewUserWindow(master=root1)
            app1.mainloop()

        self.newuser_button = tk.Button(self, text="New user? Click here.")
        self.newuser_button.bind("<Button-1>", newuser)
        self.newuser_button.grid(columnspan=2, row=4)


# ***** NEW USER WINDOW *****
class NewUserWindow(tk.Frame):
    # A new window for creating a new user profile

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_logo()
        self.create_entries()
        self.confirmation_button()

    def create_logo(self):
        # Create the logo at the top of the screen

        self.logo = tk.Label(self)
        self.logo["text"] = "Welcome stranger!"
        self.logo["font"] = ('Times New Roman', 36)
        self.logo["bd"] = 1
        self.logo["relief"] = "solid"
        # ^ Adds a relief/border to the widget.
        # flat, groove, raised, ridge, solid, or sunken
        self.logo.grid(columnspan=2)

    def create_entries(self):
        # Creates labels and entries

        self.user_label = tk.Label(self, text="Create username:")
        self.user_label.grid(column=0, row=1, sticky='E')

        self.user_entry = tk.Entry(self)
        self.user_entry.grid(column=1, row=1)

        self.password_label = tk.Label(self, text="Create password:")
        self.password_label.grid(column=0, row=2, sticky='E')

        self.password_entry = tk.Entry(self)
        self.password_entry.grid(column=1, row=2)

    def confirmation_button(self):
        # Button that confirms the selection and adds the
        # entry into the dictionary

        def confirm(event):
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
                # Need to add a line containing user entry to the profiles.csv file
                # and then call the generate_users function from the LoginWindow class
                # in order to regenerate the dictionary that the program looks at to
                # verify if a user is in the system or not

        # Create the confirmation buttons
        self.confirm_button = tk.Button(self, text="Confirm")
        self.confirm_button.bind("<Button-1>", confirm)
        self.confirm_button.grid(columnspan=2, row=3)

root0 = tk.Tk()
app0 = LoginWindow(master=root0)
app0.mainloop()
# Run the program