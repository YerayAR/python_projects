import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv
import datetime
import os
import random
import string

# Configuración de estilos
window_bg_color = "#f9f9f9"
frame_bg_color = "#ffffff"
button_bg_color = "#4c86b8"
button_fg_color = "#ffffff"
button_hover_bg_color = "#416d98"
entry_bg_color = "#ffffff"
entry_fg_color = "#333333"
label_fg_color = "#333333"
font_family = "Arial"
font_size = 12
#Variables
ruta = "password_genNsave/contraseñas.csv"
SUCCESS = "Éxito"
APP_TB = "App.TButton"
APP_TE = "App.TEntry"

def set_styles():
    # Estilos personalizados para botones
    style = ttk.Style()
    style.configure(APP_TB, background=button_bg_color, foreground="#00FFFF", font=(font_family, font_size, "bold"))
    style.map(APP_TB,
              background=[("active", button_hover_bg_color), ("disabled", button_bg_color)],
              foreground=[("disabled", button_fg_color)])

    # Estilos personalizados para la entrada de texto
    style.configure(APP_TE, fieldbackground=entry_bg_color, foreground=entry_fg_color, font=(font_family, font_size))
    style.map(APP_TE,
              fieldbackground=[("disabled", entry_bg_color)],
              foreground=[("disabled", entry_fg_color)])

def generate_password():
    length = 12  # Longitud de la contraseña

    # Define los caracteres permitidos para la contraseña
    characters = string.ascii_letters + string.digits + string.punctuation

    # Genera la contraseña aleatoria
    password = ''.join(random.choice(characters) for _ in range(length))

    # Muestra la contraseña en el cuadro de texto correspondiente
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def save_password():
    password = password_entry.get()
    name = name_entry.get()

    if name == "":
        messagebox.showerror("Error", "Debes proporcionar un nombre para guardar la contraseña.")
        return

    with open(ruta, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, password, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

    messagebox.showinfo(SUCCESS, "La contraseña ha sido guardada correctamente.")

def open_passwords_window():
    passwords_window = tk.Toplevel(window)
    passwords_window.title("Contraseñas Guardadas")
    passwords_window.geometry("750x500")
    passwords_window.config(bg=window_bg_color)

    passwords_frame = tk.Frame(passwords_window, bg=frame_bg_color)
    passwords_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Configurar el desplazamiento vertical para el marco de contraseñas
    scrollbar = tk.Scrollbar(passwords_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    passwords_listbox = tk.Listbox(passwords_frame, yscrollcommand=scrollbar.set, bg=frame_bg_color, fg=label_fg_color, font=(font_family, font_size))
    passwords_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=passwords_listbox.yview)

    with open(ruta, "r") as file:
        reader = csv.reader(file)
        passwords = list(reader)

        if passwords:
            for password in passwords:
                if len(password) >= 3:
                    name, password, creation_date = password
                else:
                    name, password = password
                    creation_date = "Fecha desconocida"

                passwords_listbox.insert(tk.END, f"Nombre: {name}, Contraseña: {password}, Fecha de creación: {creation_date}")

        else:
            passwords_listbox.insert(tk.END, "No hay contraseñas guardadas.")

def edit_password():
    selected_password = passwords_listbox.curselection()

    if not selected_password:
        messagebox.showerror("Error", "Debes seleccionar una contraseña para editar.")
        return

    selected_password = selected_password[0]

    password_window = tk.Toplevel(window)
    password_window.title("Editar Contraseña")
    password_window.config(bg=window_bg_color)

    name_label = tk.Label(password_window, text="Nombre:", bg=window_bg_color, fg=label_fg_color, font=(font_family, font_size))
    name_label.grid(row=0, column=0, padx=5, pady=5)

    name_entry = tk.Entry(password_window, bg=entry_bg_color, fg=entry_fg_color, font=(font_family, font_size))
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = tk.Label(password_window, text="Contraseña:", bg=window_bg_color, fg=label_fg_color, font=(font_family, font_size))
    password_label.grid(row=1, column=0, padx=5, pady=5)

    password_entry = tk.Entry(password_window, bg=entry_bg_color, fg=entry_fg_color, font=(font_family, font_size))
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    with open(ruta, "r") as file:
        reader = csv.reader(file)
        passwords = list(reader)

        if len(passwords) >= selected_password + 1:
            password_data = passwords[selected_password]

            name_entry.insert(tk.END, password_data[0])
            password_entry.insert(tk.END, password_data[1])

    save_button = tk.Button(password_window, text="Guardar", command=lambda: save_edited_password(selected_password, name_entry.get(), password_entry.get(), password_window), bg=button_bg_color, fg=button_fg_color, font=(font_family, font_size, "bold"))
    save_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

def save_edited_password(selected_password, new_name, new_password, password_window):
    if new_name == "":
        messagebox.showerror("Error", "Debes proporcionar un nombre para guardar la contraseña.")
        return

    with open(ruta, "r") as file:
        reader = csv.reader(file)
        passwords = list(reader)

    if len(passwords) >= selected_password + 1:
        passwords[selected_password][0] = new_name
        passwords[selected_password][1] = new_password
        passwords[selected_password][2] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ruta, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(passwords)

    password_window.destroy()
    messagebox.showinfo(SUCCESS, "La contraseña ha sido actualizada correctamente.")

def delete_password():
    selected_password = passwords_listbox.curselection()

    if not selected_password:
        messagebox.showerror("Error", "Debes seleccionar una contraseña para eliminar.")
        return

    selected_password = selected_password[0]

    response = messagebox.askyesno("Confirmar Eliminación", "¿Estás seguro de que deseas eliminar esta contraseña?")

    if response == tk.YES:
        with open(ruta, "r") as file:
            reader = csv.reader(file)
            passwords = list(reader)

        if len(passwords) >= selected_password + 1:
            passwords.pop(selected_password)

        with open(ruta, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(passwords)

        messagebox.showinfo(SUCCESS, "La contraseña ha sido eliminada correctamente.")
        passwords_listbox.delete(selected_password)

# Crear la ventana principal
def main():
    global window, passwords_listbox

    window = tk.Tk()
    window.title("Generador de Contraseñas")
    window.geometry("400x200")
    window.config(bg=window_bg_color)

    # Establecer estilos
    set_styles()

    # Cuadro de texto para mostrar la contraseña generada
    password_entry = ttk.Entry(window, style=APP_TE)
    password_entry.pack(pady=10)

    # Cuadro de texto para ingresar el nombre de la contraseña
    name_entry = ttk.Entry(window, style=APP_TE)
    name_entry.pack(pady=10)

    # Botón para generar una contraseña
    generate_button = ttk.Button(
        window,
        text="Generar Contraseña",
        command=generate_password,
        style=APP_TB,
    )
    generate_button.pack(pady=5)

    # Botón para guardar la contraseña
    save_button = ttk.Button(
        window,
        text="Guardar Contraseña",
        command=save_password,
        style=APP_TB,
    )
    save_button.pack(pady=5)

    # Botón para abrir la ventana de contraseñas guardadas
    open_passwords_button = ttk.Button(
        window,
        text="Contraseñas Guardadas",
        command=open_passwords_window,
        style=APP_TB,
    )
    open_passwords_button.pack(pady=5)

# Crear la lista de contraseñas
    passwords_listbox = None

    # Ejecutar el bucle principal de la interfaz gráfica
    window.mainloop()


if __name__ == "__main__":
    main()
