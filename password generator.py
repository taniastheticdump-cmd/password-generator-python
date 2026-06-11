import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string

history = []



#_____Password Generator_____
def generate_password():
    chars=""


    if upper_var.get():
        chars += string.ascii_uppercase

    if lower_var.get():
        chars += string.ascii_lowercase

    if number_var.get():
        chars += string.digits

    if symbol_var.get():
        chars += string.punctuation

    if chars == "":
        messagebox.showwarning("Warning",
                               "select at least one character type!"
                               )
        return
    length = length_Scale.get()

    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    history.append(password)

    if len(history) > 5:
        history.pop(0)

    history_box.delete(0, tk.END)

    for p in history:
        history_box.insert(tk.END, p)

    check_strength(password)


#_____Strength checker_____
def check_strength(password):

    has_upper= any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_symbol = any(c in  string.punctuation for c in  password)

    if len(password) >= 12 and has_upper and has_lower and has_digits and has_symbol:
        strength_label.config(text="Strength:Strong",
                              fg = "lime"
                              )
        strength_bar["value"] = 100

    elif len(password) >= 8:
        strength_label.config(text="Strength: Medium",
                              fg="yellow"
                              )
        strength_bar["value"]=60

    else:
        strength_label.config(text="Strength: Weak",
                              fg="red"
                              )
        strength_bar["value"]=30


#_____COPY PASSWORD_____
def copy_password():

    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)


        messagebox.showinfo(
            "copied",
            "Password copied to clipboard!"
            )

#_____SHOW/HIDE PASSWORD_____
def toggle_password():

    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


#_____GUI_____

root = tk.Tk()
show_var = tk.BooleanVar()
root.title("PASSWORD GENERATOR")
root.geometry("700x800")
root.configure(bg="#1E1E2E")
root.resizable(True, True)


title = tk.Label(
    root,
    text=" PASSWORD GENERATOR",
    font=("Segoe UI",20,"bold"),
    bg= "#1E1E2E",
    fg="white"
    )

title.pack(pady=20)

password_entry = tk.Entry(
    root,
    font=("Consolas",20),
    justify = 'center',
    width = 30,
    bd=0
    )
password_entry.pack(pady=20)

password_entry.config(show="*")

strength_bar = ttk.Progressbar(
    root,
    length=300,
    mode="determinate"
    )
strength_bar.pack(pady=10)


length_Label= tk.Label(
    root,
    text="password length"
    )
length_Label.pack()

length_Scale = tk.Scale(
    root,
    from_ = 4,
    to = 30,
    orient = "horizontal"
    )
length_Scale.set(12)
length_Scale.pack()


upper_var =tk.BooleanVar(value=True)
lower_var =tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text = "uppercase letters",
    variable = upper_var,
    bg="#1E1E2E",
    fg="white",
    selectcolor = "#2E2E3E"
    ).pack()

tk.Checkbutton(
    root,
    text="lowercase letters",
    variable = lower_var,
    bg = "#1E1E2E",
    fg="white",
    selectcolor = "#2E2E3E"
    ).pack()

tk.Checkbutton(
    root,
    text="Numbers",
    variable=number_var,
    bg="#1E1E2E",
    fg="white",
    selectcolor ="#2E2E3E"
    ).pack()

tk.Checkbutton(
    root,
    text="symbols",
    variable=symbol_var,
    bg="#1E1E2E",
    fg = "white",
    selectcolor="#2E2E3E"
    ).pack()

show_check = tk.Checkbutton(
    root,
    text="Show Password",
    variable = show_var,
    command = toggle_password,
    bg = "#1E1E2E",
    fg = "white",
    selectcolor="#2E2E3E"
    )
show_check.pack()

generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("segoe UI", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10,
    command = generate_password,
    )


generate_btn.pack(pady=15)

copy_btn = tk.Button(
    root,
    text="copy password",
    command = copy_password,
    font=("segoe UI",14),
    bg="#2196F3",
    fg="white",
    padx=20,
    pady=10,
    )
copy_btn.pack(pady=10)

strength_label = tk.Label(
    root,
    text="Strength:",
    font=("Segoe UI", 16,"bold"),
    bg="#1E1E2E",
    fg="white"
    )
strength_label.pack(pady=20)

history_title = tk.Label(
    root,
    text="Recent Passwords",
    bg = "#1E1E2E",
    fg="white"
    )
history_title.pack(pady=5)

history_box = tk.Listbox(
    root,
    width=40,
    height=5
    )

history_box.pack()


root.mainloop()

