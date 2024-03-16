import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 14")

################################################################
titulo = customtkinter.CTkLabel(app, text="Salário:")
titulo.pack(padx=10, pady=2)

salario = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Seus ganhos...", textvariable=salario)
resposta_1.pack(padx=10, pady=5)

################################################################


def calc_ir():

    temp = float(salario.get())

    if temp <= 2000:
        resultado.configure(text='Isento de imposto!')
    elif temp > 2000 and temp <= 3500:
        calc = (temp / 100) * 10
        resultado.configure(text=f'10% de imposto! +RS {calc:.2f}...')
    else:
        calc = (temp / 100) * 15
        resultado.configure(text=f'15% de imposto! +RS {calc:.2f}...')


calcular = customtkinter.CTkButton(
    app, text="Resultado", command=calc_ir)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado...")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
