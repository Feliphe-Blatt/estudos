import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 1")

################################################################
titulo = customtkinter.CTkLabel(app, text="Digite um número:")
titulo.pack(padx=10, pady=2)

num = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Velocidade...", textvariable=num)
resposta_1.pack(padx=10, pady=5)

################################################################


def compara_numero():

    temp = float(num.get())

    if temp >= 0:
        resultado.configure(
            text='Número positivo!', text_color="#42DB5A")
    else:
        resultado.configure(
            text='Número negativo!', text_color="#F03E74")


comparar = customtkinter.CTkButton(
    app, text="Comparar", command=compara_numero)
comparar.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado...")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
