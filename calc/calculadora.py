import tkinter as tk
from PIL import Image, ImageTk
import re

# Función para reproducir un GIF en bucle
def play_gif_loop(gif_path, label):
    gif = Image.open(gif_path)
    frames = []
    # Leer los cuadros del GIF
    try:
        while True:
            frame = gif.copy()
            frame = frame.convert("LA")
            frame = frame.resize((ventana.winfo_width(), ventana.winfo_height()), Image.ANTIALIAS)
            frames.append(ImageTk.PhotoImage(frame))
            gif.seek(len(frames))
    except EOFError:
        pass
    # Inicializar atributos para la reproducción del GIF
    play_gif_loop.frames = frames
    play_gif_loop.current_frame = 0
    update_gif(label)

# Función para actualizar el cuadro del GIF mostrado
def update_gif(label):
    label.config(image=play_gif_loop.frames[play_gif_loop.current_frame])
    label.image = play_gif_loop.frames[play_gif_loop.current_frame]
    play_gif_loop.current_frame = (play_gif_loop.current_frame + 1) % len(play_gif_loop.frames)
    ventana.after(100, update_gif, label)

# Cambiar esta variable al archivo de video que deseas usar
gif_path = "C:/Users/yera2/VScode/python/7gP8.gif"

# Función para calcular el resultado de la expresión ingresada
def calcular():
    try:
        # Intenta evaluar la expresión en el campo de entrada y almacenar el resultado
        resultado = eval(entry.get())
        # Habilita la modificación del widget de texto del resultado
        resultado_text.config(state='normal')
        # Borra el contenido actual del widget de texto del resultado
        resultado_text.delete(1.0, tk.END)
        # Inserta el resultado de la evaluación en el widget de texto del resultado
        resultado_text.insert(tk.END, f"{resultado}")
        # Deshabilita la modificación del widget de texto del resultado
        resultado_text.config(state='disabled')
        # Borra el contenido actual del campo de entrada
        entry.delete(0, tk.END)
        # Inserta el resultado en el campo de entrada
        entry.insert(tk.END, str(resultado))
    except Exception as error:
        # Si hay un error al evaluar la expresión, busca el mensaje de error en el objeto 'error'
        error_message = re.search(r"Error:\s(.+?)\(", str(error))
        # Si se encuentra un mensaje de error, úsalo como el texto de error
        if error_message:
            error_text = error_message.group(1)
        # De lo contrario, usa "Invalid syntax" como texto de error
        else:
            error_text = "Invalid syntax"
        # Habilita la modificación del widget de texto del resultado
        resultado_text.config(state='normal')
        # Borra el contenido actual del widget de texto del resultado
        resultado_text.delete(1.0, tk.END)
        # Inserta el texto de error en el widget de texto del resultado
        resultado_text.insert(tk.END, error_text)
        # Deshabilita la modificación del widget de texto del resultado
        resultado_text.config(state='disabled')

# Funciones para borrar caracteres
def borrar():
    entrada_actual = entry.get()
    entry.delete(len(entrada_actual) - 1, tk.END)

# Funciones para borrar todos los caracteres
def borrar_todo():
    entry.delete(0, tk.END)
    resultado_text.config(state='normal')
    resultado_text.delete(1.0, tk.END)
    resultado_text.config(state='disabled')

def main():
    global ventana, entry, resultado_text

    ventana = tk.Tk()
    ventana.title("Calculadora Futurista")
    ventana.configure(bg='black')
    ventana.attributes('-alpha', 0.95)

# Crear y colocar campo de entrada de texto
    entry = tk.Entry(
        ventana,
        width=40,
        font=("Helvetica", 20),
        borderwidth=5,
        bg="black",
        fg="green",
        insertbackground="green",
    )
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def insert_with_clear_error(text):
     if resultado_text["state"] == "normal":
        resultado_text.config(state='disabled')
        resultado_text.delete(1.0, tk.END)
        entry.delete(0, tk.END)
     entry.insert(tk.END, text)

def button_pressed(button):
    button.config(relief="sunken")

def button_released(button):
    button.config(relief="ridge")

    # Crear y colocar botones
    botones = [
        ("7", 1, 0, 1, 2), ("8", 1, 1, 1, 2), ("9", 1, 2, 1, 2), ("/", 1, 3, 1, 2),
        ("4", 2, 0, 1, 2), ("5", 2, 1, 1, 2), ("6", 2, 2, 1, 2), ("*", 2, 3, 1, 2),
        ("1", 3, 0, 1, 2), ("2", 3, 1, 1, 2), ("3", 3, 2, 1, 2), ("-", 3, 3, 1, 2),
        ("0", 4, 0, 1, 2), (".", 4, 1, 1, 2), ("=", 4, 2, 1, 2), ("+", 4, 3, 1, 2),
        ("Borrar", 5, 0, 1, 2), ("Borrar\nTodo", 5, 1, 1, 2),
    ]

    # Iterar sobre la lista de botones y sus propiedades
    for (texto, fila, columna, borderwidth, width) in botones:
        # Establecer el estilo de los botones
        estilo_boton = {
            "height": 2,  # Altura del botón en líneas de texto
            "width": width,  # Ancho del botón en caracteres
            "bd": 2,  # Ancho del borde en píxeles
            "font": ("Helvetica", 14),
            "bg": "black",
            "fg": "green",
            "activebackground": "darkgreen",
            "activeforeground": "white",
            "borderwidth": borderwidth,
            "relief": "ridge",
            "highlightthickness": 0,
            "cursor": "hand2",
        }

    # Crear un botón con el estilo y el texto especificados
        boton = tk.Button(ventana, text=texto, padx=30, pady=10, **estilo_boton)

        # Asignar la función correspondiente a cada botón según su texto
        if texto == "=":
            boton.config(command=calcular)
        elif texto == "Borrar":
            boton.config(command=borrar)
        elif texto == "Borrar\nTodo":
            boton.config(command=borrar_todo)
        else:
            boton.config(command=lambda t=texto: insert_with_clear_error(t))

        # Colocar el botón en la ventana usando grid
        boton.grid(row=fila, column=columna, ipadx=5, ipady=5)
        # Vincular eventos del mouse a las funciones para cambiar el aspecto de los botones al presionarlos
        boton.bind("<ButtonPress-1>", lambda event, b=boton: button_pressed(b))
        boton.bind("<ButtonRelease-1>", lambda event, b=boton: button_released(b))

# Agregar un label para mostrar el video
    gif_label = tk.Label(ventana, bg="black")
    gif_label.grid(row=0, column=0, rowspan=9, columnspan=4, sticky="nsew")
    gif_label.lower()

# Crear y colocar la caja de texto del resultado
    resultado_text = tk.Text(
        ventana,
        height=1,
        width=18,
        font=("Helvetica", 20),
        bd=5,
        state="disabled",
        bg="black",
        fg="green",
    )
    resultado_text.grid(row=8, column=0, columnspan=4, padx=10, pady=(10, 0))

# Agregar la etiqueta "Total" antes de la caja de texto del resultado
    total_label = tk.Label(
        ventana,
        text="Total:",
        font=("Helvetica", 20),
        bg="black",
        fg="green",
    )
    total_label.grid(row=8, column=0, columnspan=4, sticky="W", padx=10, pady=(10, 0))

    # Iniciar la ventana
    gif_label.after(100, play_gif_loop, gif_path, gif_label)
    ventana.mainloop()


if __name__ == "__main__":
    main()
