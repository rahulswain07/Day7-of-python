import tkinter as tk
from tkinter import messagebox

# Predefined credentials
correct_username = "rahul"
correct_password = "1234"

# Function to check login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == correct_username and password == correct_password:
        messagebox.showinfo("Login", "Login Successful ✅")
    else:
        messagebox.showerror("Login", "Invalid Username or Password ❌")

# Create GUI window
window = tk.Tk()
window.title("Instagram Login")
window.geometry("300x250")
window.configure(bg="#fafafa")

# Instagram style label
tk.Label(window, text="Instagram", font=("Helvetica", 20, "bold"), bg="#fafafa").pack(pady=10)

# Username field
tk.Label(window, text="Username", bg="#fafafa").pack()
username_entry = tk.Entry(window)
username_entry.pack(pady=5)

# Password field
tk.Label(window, text="Password", bg="#fafafa").pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=5)

# Login button
tk.Button(window, text="Log In", command=login, bg="#3897f0", fg="white", width=20).pack(pady=15)

window.mainloop()
