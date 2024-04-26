import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 12")

################################################################
msg_1 = customtkinter.CTkLabel(app, text="Temperatura atual:")
msg_1.pack(padx=10, pady=5)

temperatura = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Temperatura...", textvariable=temperatura)
resposta_1.pack(padx=10, pady=5)

################################################################


def calc_resultado():

    temp = int(temperatura.get())

    if temp < 15:
        resultado.configure(
            text='Tá frio!')
    elif temp >= 15 and temp <= 25:
        resultado.configure(
            text='Tá ameno!')
    else:
        resultado.configure(
            text='Tá quente!')


calcular = customtkinter.CTkButton(
    app, text="Resultado", command=calc_resultado)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado:")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
