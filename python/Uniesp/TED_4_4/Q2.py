import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 2")

################################################################
titulo = customtkinter.CTkLabel(app, text="Quantas maçãs?")
titulo.pack(padx=10, pady=2)

quantidade = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Velocidade...", textvariable=quantidade)
resposta_1.pack(padx=10, pady=5)

################################################################


def compara_quantidade():

    temp = int(quantidade.get())

    if temp < 12:
        preco_final = float(temp * 1.3)
        resultado.configure(
            text=f'Valor unitário: R$ 1.30\nValor TOTAL: R$ {preco_final:.2f}...')
    elif temp >= 12:
        resultado.configure(
            text=f'Valor unitário: R$ 1.00\nValor TOTAL: R$ {temp:.2f}...')


comparar = customtkinter.CTkButton(
    app, text="Calcular", command=compara_quantidade)
comparar.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado...")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
