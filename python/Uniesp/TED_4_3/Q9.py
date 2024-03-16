import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 9")

################################################################
msg_1 = customtkinter.CTkLabel(app, text="Quantidade de horas extras:")
msg_1.pack(padx=10, pady=5)

horas_extra = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Quantidade de horas...", textvariable=horas_extra)
resposta_1.pack(padx=10, pady=5)

################################################################
msg_2 = customtkinter.CTkLabel(app, text="Quantidade de horas que faltaram:")
msg_2.pack(padx=10, pady=5)

horas_falta = customtkinter.StringVar()
resposta_2 = customtkinter.CTkEntry(
    app, placeholder_text="Quantidade que falta...", textvariable=horas_falta)
resposta_2.pack(padx=10, pady=5)

################################################################


def calc_resultado():

    extra = float(horas_extra.get())
    limite = float(horas_falta.get()) + (float(horas_falta.get()) / 2)

    if extra > limite:
        resultado.configure(
            text='Bônus de R$ 500,00!', text_color="#42DB5A")
    else:
        resultado.configure(
            text='Sem bônus!', text_color="#F03E74")


calcular = customtkinter.CTkButton(
    app, text="Resultado", command=calc_resultado)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado:")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
