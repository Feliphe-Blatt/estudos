import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 11")

################################################################
msg_1 = customtkinter.CTkLabel(app, text="Idade:")
msg_1.pack(padx=10, pady=5)

idade = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Sua idade...", textvariable=idade)
resposta_1.pack(padx=10, pady=5)

################################################################


def calc_resultado():

    id = int(idade.get())

    if id >= 12 and id <= 60:
        resultado.configure(
            text='Valor do ingresso: R$ 25,00!')
    else:
        resultado.configure(
            text='Valor do ingresso: R$ 15,00!')


calcular = customtkinter.CTkButton(
    app, text="Resultado", command=calc_resultado)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado:")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
