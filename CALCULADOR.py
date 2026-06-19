import tkinter as tk

# Funciones
def click(valor):
    entrada.insert(tk.END, valor)

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def cambiar_tema(tema):
    temas = {
        "Claro": {
            "bg": "#f0f0f0",
            "fg": "black",
            "btn": "#ffffff"
        },
        "Oscuro": {
            "bg": "#2b2b2b",
            "fg": "white",
            "btn": "#444444"
        },
        "Azul": {
            "bg": "#1e3a5f",
            "fg": "white",
            "btn": "#3b6ea5"
        },
        "Verde": {
            "bg": "#1b5e20",
            "fg": "white",
            "btn": "#43a047"
        }
    }

    config = temas[tema]

    ventana.config(bg=config["bg"])
    entrada.config(
        bg=config["btn"],
        fg=config["fg"],
        insertbackground=config["fg"]
    )

    for boton in botones:
        boton.config(
            bg=config["btn"],
            fg=config["fg"],
            activebackground=config["bg"]
        )

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora con Temas")
ventana.geometry("350x450")
ventana.resizable(False, False)

# Entrada
entrada = tk.Entry(
    ventana,
    font=("Arial", 20),
    justify="right",
    bd=5
)
entrada.pack(fill="x", padx=10, pady=10)

# Selector de tema
tema_var = tk.StringVar(value="Claro")

menu_tema = tk.OptionMenu(
    ventana,
    tema_var,
    "Claro",
    "Oscuro",
    "Azul",
    "Verde",
    command=cambiar_tema
)
menu_tema.pack(pady=5)

# Marco de botones
frame = tk.Frame(ventana)
frame.pack()

# Botones
botones = []

disposicion = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for fila in disposicion:
    fila_frame = tk.Frame(frame)
    fila_frame.pack()

    for texto in fila:
        if texto == "=":
            comando = calcular
        elif texto == "C":
            comando = limpiar
        else:
            comando = lambda t=texto: click(t)

        boton = tk.Button(
            fila_frame,
            text=texto,
            width=8,
            height=2,
            font=("Arial", 14),
            command=comando
        )
        boton.pack(side="left", padx=2, pady=2)
        botones.append(boton)

# Aplicar tema inicial
cambiar_tema("Claro")

ventana.mainloop()