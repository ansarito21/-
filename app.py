import tkinter as tk
from tkinter import ttk
from mock_data import get_users, get_bookings, get_payments

def display_data(tree, data):
    """Обновление данных в Treeview"""
    tree.delete(*tree.get_children())
    for item in data:
        tree.insert("", "end", values=list(item.values()))


root = tk.Tk()
root.title("Управление системой")
root.geometry("800x600")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)


users_frame = ttk.Frame(notebook)
notebook.add(users_frame, text="Пользователи")
users_tree = ttk.Treeview(users_frame, columns=("id", "name", "role"), show="headings")
users_tree.pack(fill="both", expand=True)
for col in ("id", "name", "role"):
    users_tree.heading(col, text=col.capitalize())


bookings_frame = ttk.Frame(notebook)
notebook.add(bookings_frame, text="Бронирования")
bookings_tree = ttk.Treeview(bookings_frame, columns=("id", "user_id", "details", "status"), show="headings")
bookings_tree.pack(fill="both", expand=True)
for col in ("id", "user_id", "details", "status"):
    bookings_tree.heading(col, text=col.capitalize())


payments_frame = ttk.Frame(notebook)
notebook.add(payments_frame, text="Платежи")
payments_tree = ttk.Treeview(payments_frame, columns=("id", "user_id", "amount", "status"), show="headings")
payments_tree.pack(fill="both", expand=True)
for col in ("id", "user_id", "amount", "status"):
    payments_tree.heading(col, text=col.capitalize())


display_data(users_tree, get_users())
display_data(bookings_tree, get_bookings())
display_data(payments_tree, get_payments())


root.mainloop()
