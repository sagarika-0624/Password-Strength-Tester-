import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import re

def check_password_strength(password):
    length = len(password) >= 8
    digit = re.search(r"\d", password) is not None
    upper = re.search(r"[A-Z]", password) is not None
    lower = re.search(r"[a-z]", password) is not None
    symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    score = sum([length, digit, upper, lower, symbol])

    if score == 5:
        return "Strong Password", "green"
    elif score >= 3:
        return "Moderate Password", "orange"
    else:
        return "Weak Password", "red"

def on_key_release(event=None):
    pwd = password_entry.get()
    result, color = check_password_strength(pwd)
    result_label.config(text=result, fg=color)

def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Root window
root = tk.Tk()
root.title("Secure Password Strength Checker")
root.geometry("600x400")
root.resizable(False, False)

# Load background image
bg_image = Image.open("1.jpeg")
bg_image = bg_image.resize((600, 400))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame for form
frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=280)

# Title
tk.Label(frame, text="User Login", font=("Helvetica", 16, "bold"), bg="white").pack(pady=10)

# Username
tk.Label(frame, text="Username:", font=("Arial", 12), bg="white").pack(anchor="w", padx=20)
username_entry = tk.Entry(frame, font=("Arial", 12), width=30)
username_entry.pack(pady=5)

# Password
tk.Label(frame, text="Password:", font=("Arial", 12), bg="white").pack(anchor="w", padx=20)
password_entry = tk.Entry(frame, show="*", font=("Arial", 12), width=30)
password_entry.pack(pady=5)
password_entry.bind("<KeyRelease>", on_key_release)

# Show password checkbox
show_var = tk.BooleanVar()
tk.Checkbutton(frame, text="Show Password", variable=show_var, command=toggle_password, bg="white").pack()

# Password strength label
result_label = tk.Label(frame, text="", font=("Arial", 12, "bold"), bg="white")
result_label.pack(pady=10)

root.mainloop()
