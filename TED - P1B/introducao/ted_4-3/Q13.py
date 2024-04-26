import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 13")

################################################################
titulo = customtkinter.CTkLabel(app, text="Candidatos:")
titulo.pack(padx=10, pady=2)


candidatos = customtkinter.CTkLabel(
    app, text="1 - Candidato A\n2 - Candidato B\n3 - Candidato C")
candidatos.pack(padx=10, pady=2)

voto = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Sua intenção de voto...", textvariable=voto)
resposta_1.pack(padx=10, pady=5)

################################################################


def calc_resultado():

    temp = int(voto.get())

    match temp:
        case 1:
            resultado.configure(text='Intenção de voto no Candidato A!')
        case 2:
            resultado.configure(text='Intenção de voto no Candidato B!')
        case 3:
            resultado.configure(text='Intenção de voto no Candidato C!')
        case _:
            resultado.configure(text='Intenção de voto NULO (inválido)!')


calcular = customtkinter.CTkButton(
    app, text="Resultado", command=calc_resultado)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado...")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
