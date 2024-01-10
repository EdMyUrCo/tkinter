import tkinter as tk

def calcular():
    try:
        # Obtener los valores de los campos de entrada
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        # Realizar la operación seleccionada
        if operacion.get() == "Suma":
            resultado = num1 + num2
        elif operacion.get() == "Resta":
            resultado = num1 - num2
        elif operacion.get() == "Multiplicación":
            resultado = num1 * num2
        elif operacion.get() == "División":
            resultado = num1 / num2
        else:
            resultado = "Error"

        # Mostrar el resultado en la etiqueta
        label_resultado.config(text=f"Resultado: {resultado}", fg="green")

    except ValueError:
        # Manejar errores de entrada no válida
        label_resultado.config(text="Error: Entrada no válida", fg="red")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x200")
ventana.configure(bg="lightblue")

# Variables de control
operacion = tk.StringVar()
operacion.set("Suma")

# Campos de entrada
entry_num1 = tk.Entry(ventana, width=10, font=("Arial", 12))
entry_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(ventana, width=10, font=("Arial", 12))
entry_num2.grid(row=0, column=1, padx=10, pady=10)

# Menú desplegable para seleccionar la operación
menu_operaciones = tk.OptionMenu(ventana, operacion, "Suma", "Resta", "Multiplicación", "División")
menu_operaciones.configure(font=("Arial", 12), bg="yellow", fg="black", highlightbackground="lightblue", width=15)

menu_operaciones.grid(row=0, column=2, padx=10, pady=10)

# Botón para realizar el cálculo
btn_calcular = tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12), bg="green", fg="black", highlightbackground="lightblue", highlightcolor="green")
btn_calcular.grid(row=1, column=0, columnspan=3, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 14), bg="#f0f0f0")
label_resultado.grid(row=2, column=0, columnspan=3, pady=10)

# Iniciar el bucle principal
ventana.mainloop()
