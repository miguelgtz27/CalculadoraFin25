import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

# Formulas para Interés Simple y Compuesto
def calcular():
    opcion = opcion_var.get()
    try:
        if opcion == "Interés":
            P = float(entry_capital.get())
            r = float(entry_tasa.get()) / 100
            t = float(entry_tiempo.get())
            interes = P * r * t
            resultado_var.set(f"El interés es: ${interes:.2f}")

        elif opcion == "Valor Futuro":
            P = float(entry_capital.get())
            r = float(entry_tasa.get()) / 100
            t = float(entry_tiempo.get())
            VF = P * (1 + r * t)
            resultado_var.set(f"El valor futuro es: ${VF:.2f}")

        elif opcion == "Valor Presente":
            VF = float(entry_valor_futuro.get())
            r = float(entry_tasa.get()) / 100
            t = float(entry_tiempo.get())
            P = VF / (1 + r * t)
            resultado_var.set(f"El valor presente es: ${P:.2f}")

        elif opcion == "Tasa de Interés":
            I = float(entry_interes.get())
            P = float(entry_capital.get())
            t = float(entry_tiempo.get())
            r = I / (P * t) * 100
            resultado_var.set(f"La tasa de interés es: {r:.2f}%")

        elif opcion == "Tiempo":
            I = float(entry_interes.get())
            P = float(entry_capital.get())
            r = float(entry_tasa.get()) / 100
            t = I / (P * r)
            resultado_var.set(f"El tiempo es: {t:.2f} años")

        elif opcion == "Valor Futuro (Compuesto)":
            P = float(entry_capital.get())
            r = float(entry_tasa.get()) / 100
            t = float(entry_tiempo.get())
            VF = P * ((1 + r) ** t)
            resultado_var.set(f"El valor futuro compuesto es: ${VF:.2f}")

        elif opcion == "Valor Presente (Compuesto)":
            VF = float(entry_valor_futuro.get())
            r = float(entry_tasa.get()) / 100
            t = float(entry_tiempo.get())
            P = VF / ((1 + r) ** t)
            resultado_var.set(f"El valor presente compuesto es: ${P:.2f}")

        elif opcion == "Tasa Efectiva":
            r_nom = float(entry_tasa.get()) / 100
            m = float(entry_periodos.get())
            r_efectiva = ((1 + r_nom / m) ** m - 1) * 100
            resultado_var.set(f"La tasa efectiva es: {r_efectiva:.2f}%")

        elif opcion == "Conversión de Tasa":
            r_efectiva = float(entry_tasa.get()) / 100
            m = float(entry_periodos.get())
            r_nom = (m * ((1 + r_efectiva) ** (1 / m) - 1)) * 100
            resultado_var.set(f"La tasa nominal equivalente es: {r_nom:.2f}%")

        elif opcion == "Tiempo (Compuesto)":
            VF = float(entry_valor_futuro.get())
            P = float(entry_capital.get())
            r = float(entry_tasa.get()) / 100
            t = math.log(VF / P) / math.log(1 + r)
            resultado_var.set(f"El tiempo compuesto es: {t:.2f} años")

    except Exception as e:
        messagebox.showerror("Error", f"Datos inválidos: {e}")

# Ocultar campos 
def actualizar_campos(event):
    for widget in frame_entradas.winfo_children():
        widget.grid_forget()

    opcion = opcion_var.get()

    if opcion in ["Interés", "Valor Futuro"]:
        lbl_capital.grid(row=0, column=0, sticky="e")
        entry_capital.grid(row=0, column=1)
        lbl_tasa.grid(row=1, column=0, sticky="e")
        entry_tasa.grid(row=1, column=1)
        lbl_tiempo.grid(row=2, column=0, sticky="e")
        entry_tiempo.grid(row=2, column=1)

    elif opcion == "Valor Presente":
        lbl_valor_futuro.grid(row=0, column=0, sticky="e")
        entry_valor_futuro.grid(row=0, column=1)
        lbl_tasa.grid(row=1, column=0, sticky="e")
        entry_tasa.grid(row=1, column=1)
        lbl_tiempo.grid(row=2, column=0, sticky="e")
        entry_tiempo.grid(row=2, column=1)

    elif opcion == "Tasa de Interés":
        lbl_interes.grid(row=0, column=0, sticky="e")
        entry_interes.grid(row=0, column=1)
        lbl_capital.grid(row=1, column=0, sticky="e")
        entry_capital.grid(row=1, column=1)
        lbl_tiempo.grid(row=2, column=0, sticky="e")
        entry_tiempo.grid(row=2, column=1)

    elif opcion == "Tiempo":
        lbl_interes.grid(row=0, column=0, sticky="e")
        entry_interes.grid(row=0, column=1)
        lbl_capital.grid(row=1, column=0, sticky="e")
        entry_capital.grid(row=1, column=1)
        lbl_tasa.grid(row=2, column=0, sticky="e")
        entry_tasa.grid(row=2, column=1)

    elif opcion in ["Valor Futuro (Compuesto)"]:
        lbl_capital.grid(row=0, column=0, sticky="e")
        entry_capital.grid(row=0, column=1)
        lbl_tasa.grid(row=1, column=0, sticky="e")
        entry_tasa.grid(row=1, column=1)
        lbl_tiempo.grid(row=2, column=0, sticky="e")
        entry_tiempo.grid(row=2, column=1)

    elif opcion == "Tiempo (Compuesto)":
        lbl_valor_futuro.grid(row=0, column=0, sticky="e")
        entry_valor_futuro.grid(row=0, column=1)
        lbl_capital.grid(row=1, column=0, sticky="e")
        entry_capital.grid(row=1, column=1)
        lbl_tasa.grid(row=2, column=0, sticky="e")
        entry_tasa.grid(row=2, column=1)

    elif opcion == "Valor Presente (Compuesto)":
        lbl_valor_futuro.grid(row=0, column=0, sticky="e")
        entry_valor_futuro.grid(row=0, column=1)
        lbl_tasa.grid(row=1, column=0, sticky="e")
        entry_tasa.grid(row=1, column=1)
        lbl_tiempo.grid(row=2, column=0, sticky="e")
        entry_tiempo.grid(row=2, column=1)

    elif opcion in ["Tasa Efectiva", "Conversión de Tasa"]:
        lbl_tasa.grid(row=0, column=0, sticky="e")
        entry_tasa.grid(row=0, column=1)
        lbl_periodos.grid(row=1, column=0, sticky="e")
        entry_periodos.grid(row=1, column=1)

# --------------------------- Interfaz ------------------------- 
root = tk.Tk()
root.title("$mart Fin")
root.geometry("520x450")

opcion_var = tk.StringVar()
resultado_var = tk.StringVar()

# Sección de Interés Simple
frame_simple = ttk.LabelFrame(root, text="Interés Simple")
frame_simple.pack(padx=10, pady=5, fill="x")

combo_opciones_simple = ttk.Combobox(frame_simple, textvariable=opcion_var, state="readonly",
    values=["Interés", "Valor Futuro", "Valor Presente", "Tasa de Interés", "Tiempo"])
combo_opciones_simple.pack(padx=5, pady=5)
combo_opciones_simple.bind("<<ComboboxSelected>>", actualizar_campos)

# Sección de Interés Compuesto
frame_compuesto = ttk.LabelFrame(root, text="Interés Compuesto")
frame_compuesto.pack(padx=10, pady=5, fill="x")

combo_opciones_compuesto = ttk.Combobox(frame_compuesto, textvariable=opcion_var, state="readonly",
    values=["Valor Futuro (Compuesto)", "Valor Presente (Compuesto)", "Tasa Efectiva",
            "Conversión de Tasa", "Tiempo (Compuesto)"])
combo_opciones_compuesto.pack(padx=5, pady=5)
combo_opciones_compuesto.bind("<<ComboboxSelected>>", actualizar_campos)

frame_entradas = ttk.Frame(root)
frame_entradas.pack(pady=10)

# ------------------------------------------- Otros campos ----------------------------------------------
lbl_capital = ttk.Label(frame_entradas, text="Principal (P)")
entry_capital = ttk.Entry(frame_entradas)

lbl_tasa = ttk.Label(frame_entradas, text="Tasa de interés (r) [%]")
entry_tasa = ttk.Entry(frame_entradas)

lbl_tiempo = ttk.Label(frame_entradas, text="Tiempo o Periodo (t)")
entry_tiempo = ttk.Entry(frame_entradas)

lbl_interes = ttk.Label(frame_entradas, text="Interés (I)")
entry_interes = ttk.Entry(frame_entradas)

lbl_valor_futuro = ttk.Label(frame_entradas, text="Valor Futuro (VF)")
entry_valor_futuro = ttk.Entry(frame_entradas)

lbl_periodos = ttk.Label(frame_entradas, text="No de períodos por año (m)")
entry_periodos = ttk.Entry(frame_entradas)

btn_calcular = ttk.Button(root, text="Calcular", command=calcular)
btn_calcular.pack(pady=10)

lbl_resultado = ttk.Label(root, textvariable=resultado_var, font=("Arial", 12, "bold"))
lbl_resultado.pack(pady=10)

root.mainloop()
