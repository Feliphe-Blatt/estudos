import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 10")

################################################################
msg_1 = customtkinter.CTkLabel(app, text="Primeiro lado:")
msg_1.pack(padx=10, pady=5)

lado_1 = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Lado 1...", textvariable=lado_1)
resposta_1.pack(padx=10, pady=5)

################################################################
msg_2 = customtkinter.CTkLabel(app, text="Segundo lado:")
msg_2.pack(padx=10, pady=5)

lado_2 = customtkinter.StringVar()
resposta_2 = customtkinter.CTkEntry(
    app, placeholder_text="Lado 2...", textvariable=lado_2)
resposta_2.pack(padx=10, pady=5)

################################################################
msg_3 = customtkinter.CTkLabel(app, text="Terceiro lado:")
msg_3.pack(padx=10, pady=5)

lado_3 = customtkinter.StringVar()
resposta_3 = customtkinter.CTkEntry(
    app, placeholder_text="Lado 3...", textvariable=lado_3)
resposta_3.pack(padx=10, pady=5)

################################################################


def calc_resultado():

    lad_1 = float(lado_1.get())
    lad_2 = float(lado_2.get())
    lad_3 = float(lado_3.get())

    if lad_1 == lad_2 and lad_1 == lad_3:
        resultado.configure(
            text='Triângulo Equilátero!')
    elif lad_1 == lad_2 or lad_1 == lad_3 or lad_2 == lad_3:
        resultado.configure(
            text='Triângulo Isósceles!')
    else:
        resultado.configure(
            text='Triângulo Escaleno!')


calcular = customtkinter.CTkButton(
    app, text="Resultado", command=calc_resultado)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado:")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
