
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Вибір мови програмування")
window.geometry("300x250")

language = tk.StringVar(value="Python")

tk.Label(
    window,
    text="Виберіть мову програмування:"
).pack(pady=10)

tk.Radiobutton(
    window, text="Python",
    variable=language, value="Python"
).pack()

tk.Radiobutton(
    window, text="Java",
    variable=language, value="Java"
).pack()

tk.Radiobutton(
    window, text="C++",
    variable=language, value="C++"
).pack()

def confirm():
    messagebox.showinfo(
        "Підтвердження",
        f"Ви вибрали мову: {language.get()}"
    )

tk.Button(
    window,
    text="Підтвердити",
    command=confirm
).pack(pady=15)

window.mainloop()
