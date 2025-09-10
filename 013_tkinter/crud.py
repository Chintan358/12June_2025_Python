import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql, base64
from io import BytesIO
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


# ---------- Database Connection ----------
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306,
        database="12jun_python"
    )

# ---------- CRUD Operations ----------
def insert_data():
    uname, email, phone = entry_username.get(), entry_email.get(), entry_phone.get()
    if not uname or not email or not phone:
        messagebox.showerror("Error", "All fields are required!")
        return

    con = get_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO users(username, email, phone) VALUES(%s, %s, %s)", (uname, email, phone))
    con.commit()
    con.close()
    messagebox.showinfo("Success", "Record Inserted Successfully")
    fetch_data()
    clear_data()

def fetch_data():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    if rows:
        tree.delete(*tree.get_children())
        for i, row in enumerate(rows):
            tag = "oddrow" if i % 2 else "evenrow"
            tree.insert("", tk.END, values=row, tags=(tag,))
    con.close()

def clear_data():
    entry_username.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def get_selected_row(event):
    selected = tree.focus()
    values = tree.item(selected, "values")
    if values:
        entry_username.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_username.insert(tk.END, values[1])
        entry_email.insert(tk.END, values[2])
        entry_phone.insert(tk.END, values[3])

def update_data():
    selected = tree.focus()
    values = tree.item(selected, "values")
    if not values:
        messagebox.showerror("Error", "No record selected!")
        return
    uid = values[0]

    uname, email, phone = entry_username.get(), entry_email.get(), entry_phone.get()

    con = get_connection()
    cur = con.cursor()
    cur.execute("UPDATE users SET username=%s, email=%s, phone=%s WHERE id=%s", (uname, email, phone, uid))
    con.commit()
    con.close()
    messagebox.showinfo("Success", "Record Updated Successfully")
    fetch_data()
    clear_data()

def delete_data():
    selected = tree.focus()
    values = tree.item(selected, "values")
    if not values:
        messagebox.showerror("Error", "No record selected!")
        return
    uid = values[0]

    con = get_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (uid,))
    con.commit()
    con.close()
    messagebox.showinfo("Success", "Record Deleted Successfully")
    fetch_data()
    clear_data()

# ---------- Helper: Load Base64 Icon ----------
def load_icon(base64_str, size=(18, 18)):
    img_data = base64.b64decode(base64_str)
    img = Image.open(BytesIO(img_data)).resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)




# ---------- GUI ----------
root = tk.Tk()
root.title("User Management System")
root.geometry("750x550")
root.config(bg="#f7f9fc")

# Title Label
title = tk.Label(root, text="User Management System", font=("Segoe UI", 20, "bold"), bg="#f7f9fc", fg="#2b2d42")
title.pack(pady=10)

# Frame for form
form_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
form_frame.place(x=30, y=70, width=350, height=200)

tk.Label(form_frame, text="Username:", font=("Segoe UI", 11), bg="#ffffff").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_username = tk.Entry(form_frame, font=("Segoe UI", 11), bg="#f1f3f6")
entry_username.grid(row=0, column=1, padx=10, pady=10)

tk.Label(form_frame, text="Email:", font=("Segoe UI", 11), bg="#ffffff").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_email = tk.Entry(form_frame, font=("Segoe UI", 11), bg="#f1f3f6")
entry_email.grid(row=1, column=1, padx=10, pady=10)

tk.Label(form_frame, text="Phone:", font=("Segoe UI", 11), bg="#ffffff").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_phone = tk.Entry(form_frame, font=("Segoe UI", 11), bg="#f1f3f6")
entry_phone.grid(row=2, column=1, padx=10, pady=10)



# Buttons Frame
btn_frame = tk.Frame(root, bg="#f7f9fc")
btn_frame.place(x=420, y=80)

tk.Button(
    btn_frame, text="✔ Add", compound="left", bg="#4caf50", fg="white",
    font=("Segoe UI", 10, "bold"), relief="flat", padx=10, command=insert_data
).grid(row=0, column=0, padx=10, pady=10)

tk.Button(
    btn_frame, text="✏ Update", compound="left", bg="#2196f3", fg="white",
    font=("Segoe UI", 10, "bold"), relief="flat", padx=10, command=update_data
).grid(row=0, column=1, padx=10, pady=10)

tk.Button(
    btn_frame, text="🗑 Delete", compound="left", bg="#f44336", fg="white",
    font=("Segoe UI", 10, "bold"), relief="flat", padx=10, command=delete_data
).grid(row=1, column=0, padx=10, pady=10)

tk.Button(
    btn_frame, text="🔄 Clear", compound="left", bg="#9e9e9e", fg="white",
    font=("Segoe UI", 10, "bold"), relief="flat", padx=10, command=clear_data
).grid(row=1, column=1, padx=10, pady=10)

# Table Frame
table_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
table_frame.place(x=30, y=300, width=680, height=220)

tree = ttk.Treeview(table_frame, columns=("id", "username", "email", "phone"), show="headings", height=10)
tree.heading("id", text="ID")
tree.heading("username", text="Username")
tree.heading("email", text="Email")
tree.heading("phone", text="Phone")

tree.column("id", width=50, anchor="center")
tree.column("username", width=150)
tree.column("email", width=200)
tree.column("phone", width=120, anchor="center")

# Styling Treeview
style = ttk.Style()
style.configure("Treeview", font=("Segoe UI", 10), rowheight=25, background="#fefefe", fieldbackground="#fefefe")
style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#e0e0e0")

tree.tag_configure("oddrow", background="#f1f1f1")
tree.tag_configure("evenrow", background="#ffffff")

tree.pack(fill=tk.BOTH, expand=True)
tree.bind("<ButtonRelease-1>", get_selected_row)

fetch_data()
root.mainloop()
