# Sistema de Registro de Estudiantes con interfaz gráfica

import tkinter as tk
from tkinter import messagebox, ttk


# Lista donde se almacenan los estudiantes
estudiantes = []


# Registrar estudiante
def registrar_estudiante():
    nombre = entrada_nombre.get().strip()
    carrera = entrada_carrera.get().strip()
    edad = entrada_edad.get().strip()

    # Validar campos vacíos
    if nombre == "" or carrera == "" or edad == "":
        messagebox.showwarning(
            "Campos incompletos",
            "Complete todos los datos."
        )
        return

    # Validar que la edad sea un número
    try:
        edad = int(edad)

        if edad <= 0:
            messagebox.showwarning(
                "Edad incorrecta",
                "La edad debe ser mayor que cero."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Error",
            "La edad debe ser un número."
        )
        return

    estudiante = {
        "nombre": nombre,
        "carrera": carrera,
        "edad": edad
    }

    estudiantes.append(estudiante)

    # Agregar estudiante a la tabla
    tabla.insert(
        "",
        "end",
        values=(nombre, carrera, edad)
    )

    # Limpiar los campos
    entrada_nombre.delete(0, tk.END)
    entrada_carrera.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)

    messagebox.showinfo(
        "Registro exitoso",
        "Estudiante registrado correctamente."
    )


# Buscar estudiante
def buscar_estudiante():
    nombre_buscar = entrada_buscar.get().strip()

    if nombre_buscar == "":
        messagebox.showwarning(
            "Buscar",
            "Ingrese el nombre del estudiante."
        )
        return

    for estudiante in estudiantes:

        if estudiante["nombre"].lower() == nombre_buscar.lower():

            messagebox.showinfo(
                "Estudiante encontrado",
                "Nombre: " + estudiante["nombre"] +
                "\nCarrera: " + estudiante["carrera"] +
                "\nEdad: " + str(estudiante["edad"])
            )
            return

    messagebox.showwarning(
        "Resultado",
        "Estudiante no encontrado."
    )


# ---------------- VENTANA PRINCIPAL ----------------

ventana = tk.Tk()

ventana.title("Sistema de Registro de Estudiantes")
ventana.geometry("750x600")
ventana.resizable(False, False)

ventana.configure(bg="#eef2f7")


# ---------------- ENCABEZADO ----------------

encabezado = tk.Frame(
    ventana,
    bg="#243447",
    height=100
)

encabezado.pack(fill="x")


# Logo sencillo
logo = tk.Label(
    encabezado,
    text="🎓",
    font=("Arial", 30),
    bg="#243447",
    fg="white"
)

logo.place(x=35, y=20)


titulo = tk.Label(
    encabezado,
    text="Sistema de Registro de Estudiantes",
    font=("Arial", 20, "bold"),
    bg="#243447",
    fg="white"
)

titulo.place(x=100, y=22)


subtitulo = tk.Label(
    encabezado,
    text="Gestión básica de información académica",
    font=("Arial", 10),
    bg="#243447",
    fg="#d6e2ee"
)

subtitulo.place(x=102, y=60)


# ---------------- FORMULARIO ----------------

formulario = tk.Frame(
    ventana,
    bg="white",
    padx=30,
    pady=20
)

formulario.pack(
    padx=40,
    pady=25,
    fill="x"
)


tk.Label(
    formulario,
    text="Registrar nuevo estudiante",
    font=("Arial", 14, "bold"),
    bg="white"
).grid(
    row=0,
    column=0,
    columnspan=2,
    pady=(0, 15)
)


# Nombre
tk.Label(
    formulario,
    text="Nombre:",
    bg="white",
    font=("Arial", 10)
).grid(
    row=1,
    column=0,
    sticky="w",
    pady=6
)

entrada_nombre = tk.Entry(
    formulario,
    width=45,
    font=("Arial", 10)
)

entrada_nombre.grid(
    row=1,
    column=1,
    padx=10
)


# Carrera
tk.Label(
    formulario,
    text="Carrera:",
    bg="white",
    font=("Arial", 10)
).grid(
    row=2,
    column=0,
    sticky="w",
    pady=6
)

entrada_carrera = tk.Entry(
    formulario,
    width=45,
    font=("Arial", 10)
)

entrada_carrera.grid(
    row=2,
    column=1,
    padx=10
)


# Edad
tk.Label(
    formulario,
    text="Edad:",
    bg="white",
    font=("Arial", 10)
).grid(
    row=3,
    column=0,
    sticky="w",
    pady=6
)

entrada_edad = tk.Entry(
    formulario,
    width=45,
    font=("Arial", 10)
)

entrada_edad.grid(
    row=3,
    column=1,
    padx=10
)


# Botón registrar
btn_registrar = tk.Button(
    formulario,
    text="✓ Registrar estudiante",
    bg="#2da44e",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    padx=15,
    pady=7,
    command=registrar_estudiante
)

btn_registrar.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=15
)


# ---------------- BUSCADOR ----------------

zona_buscar = tk.Frame(
    ventana,
    bg="#eef2f7"
)

zona_buscar.pack()


entrada_buscar = tk.Entry(
    zona_buscar,
    width=35,
    font=("Arial", 10)
)

entrada_buscar.pack(
    side="left",
    padx=5
)


btn_buscar = tk.Button(
    zona_buscar,
    text="🔍 Buscar estudiante",
    bg="#0969da",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    command=buscar_estudiante
)

btn_buscar.pack(
    side="left",
    padx=5
)


# ---------------- TABLA ----------------

tabla = ttk.Treeview(
    ventana,
    columns=("Nombre", "Carrera", "Edad"),
    show="headings",
    height=8
)

tabla.heading(
    "Nombre",
    text="Nombre"
)

tabla.heading(
    "Carrera",
    text="Carrera"
)

tabla.heading(
    "Edad",
    text="Edad"
)


tabla.column(
    "Nombre",
    width=230
)

tabla.column(
    "Carrera",
    width=270
)

tabla.column(
    "Edad",
    width=100,
    anchor="center"
)


tabla.pack(
    padx=40,
    pady=20
)


# ---------------- PIE ----------------

pie = tk.Label(
    ventana,
    text="Construcción de Software  •  Python  •  Git & GitHub",
    bg="#eef2f7",
    fg="#667085",
    font=("Arial", 9)
)

pie.pack(
    side="bottom",
    pady=10
)


ventana.mainloop()