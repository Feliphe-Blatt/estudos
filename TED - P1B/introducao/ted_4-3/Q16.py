import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 16")

################################################################
titulo = customtkinter.CTkLabel(app, text="Digite a senha:")
titulo.pack(padx=10, pady=2)

senha = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Velocidade...", textvariable=senha)
resposta_1.pack(padx=10, pady=5)

################################################################

senha_oficial = "Python123"


def compara_senha():

    temp = senha.get()

    if temp == senha_oficial:
        resultado.configure(
            text='Acesso concedido!', text_color="#42DB5A")
    else:
        resultado.configure(
            text='Acesso negado!', text_color="#F03E74")


acessar = customtkinter.CTkButton(
    app, text="Acessar", command=compara_senha)
acessar.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado...")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
