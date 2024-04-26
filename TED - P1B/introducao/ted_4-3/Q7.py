import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 7")

################################################################
msg_1 = customtkinter.CTkLabel(app, text="Quantidade em estoque:")
msg_1.pack(padx=10, pady=5)

quantidade_atual = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Quantidade...", textvariable=quantidade_atual)
resposta_1.pack(padx=10, pady=5)

################################################################
msg_2 = customtkinter.CTkLabel(app, text="Quantidade máxima:")
msg_2.pack(padx=10, pady=5)

quantidade_maxima = customtkinter.StringVar()
resposta_2 = customtkinter.CTkEntry(
    app, placeholder_text="Quantidade máxima...", textvariable=quantidade_maxima)
resposta_2.pack(padx=10, pady=5)

################################################################
msg_3 = customtkinter.CTkLabel(app, text="Quantidade mínima:")
msg_3.pack(padx=10, pady=5)

quantidade_minima = customtkinter.StringVar()
resposta_3 = customtkinter.CTkEntry(
    app, placeholder_text="Número da conta...", textvariable=quantidade_minima)
resposta_3.pack(padx=10, pady=5)


def calc_resultado():

    atual = float(quantidade_atual.get())
    quantidade_media = (float(quantidade_maxima.get()) +
                        float(quantidade_minima.get())) / 2

    if atual < quantidade_media:
        resultado.configure(
            text=f'Precisa repor o estoque!', text_color="#F03E74")
    else:
        resultado.configure(
            text=f'Não precisa repor o estoque!', text_color="#42DB5A")


calcular = customtkinter.CTkButton(
    app, text="Resultado", command=calc_resultado)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado:")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
