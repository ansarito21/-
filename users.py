import tkinter as tk
from tkinter import ttk  


root = tk.Tk()


users_tree = ttk.Treeview(root)  
users_tree.pack()  


users_frame = tk.Frame(root)
users_frame.pack()  


def add_user():
    def submit_user():
        USERS.append(
            {
                "id": len(USERS) + 1,
                "name": name_var.get(),
                "role": role_var.get(),
            }
        )
        display_data(users_tree, get_users())  
        add_user_window.destroy()

  
    add_user_window = tk.Toplevel(root)
    add_user_window.title("Добавить пользователя")
    add_user_window.geometry("300x200")

  
    tk.Label(add_user_window, text="Имя:").pack()
    name_var = tk.StringVar()
    tk.Entry(add_user_window, textvariable=name_var).pack()

 
    tk.Label(add_user_window, text="Роль:").pack()
    role_var = tk.StringVar()
    tk.Entry(add_user_window, textvariable=role_var).pack()


    tk.Button(add_user_window, text="Добавить", command=submit_user).pack()


USERS = []

def display_data(tree, users):
    pass 

def get_users():
    return USERS


tk.Button(users_frame, text="Добавить пользователя", command=add_user).pack()

root.mainloop()
