import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 1: Calculadora de média")

###############################################################
msg_1 = customtkinter.CTkLabel(app, text="Primeira nota:")
msg_1.pack(padx=10, pady=5)

nota_1 = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="1ª nota...", textvariable=nota_1)
resposta_1.pack(padx=10, pady=5)

###############################################################
msg_2 = customtkinter.CTkLabel(app, text="Segunda nota:")
msg_2.pack(padx=10, pady=5)

nota_2 = customtkinter.StringVar()
resposta_2 = customtkinter.CTkEntry(
    app, placeholder_text="2ª nota...", textvariable=nota_2)
resposta_2.pack(padx=10, pady=5)


###############################################################
def media():
    med = (float(nota_1.get()) + float(nota_2.get())) / 2

    resposta_media.configure(text=f'Média: {med:.1f}')

    if med <= 10 and med >= 6:

        resposta_final.configure(text="Aprovado!", text_color="#42DB5A")

    elif med < 6 and med >= 0:

        resposta_final.configure(text="Reprovado!", text_color="#F03E74")

    else:

        resposta_final.configure(text="Média inválida!", text_color="#E0DB4A")


calcular = customtkinter.CTkButton(app, text="Calcular Média", command=media)
calcular.pack(padx=10, pady=20)

###############################################################
resposta_media = customtkinter.CTkLabel(app, text="Media:")
resposta_media.pack(padx=10, pady=2)
resposta_final = customtkinter.CTkLabel(app, text="Situação final")
resposta_final.pack(padx=10, pady=2)

###############################################################
app.mainloop()
