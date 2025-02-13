import tkinter as tk
from tkinter import simpledialog, messagebox

class LoginWindow(tk.Toplevel):
    def __init__(self, parent, on_success):
        super().__init__(parent)
        self.title("Logowanie")
        self.geometry("300x200")
        self.on_success = on_success
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self, text="Login:").pack(pady=5)
        self.login_entry = tk.Entry(self)
        self.login_entry.pack(pady=5)
        tk.Label(self, text="Hasło:").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        tk.Button(self, text="Zaloguj", command=self.attempt_login).pack(pady=10)

    def attempt_login(self):
        username = self.login_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "password":
            self.on_success(username)
            self.destroy()
        else:
            messagebox.showerror("Błąd", "Niepoprawne dane logowania!")
