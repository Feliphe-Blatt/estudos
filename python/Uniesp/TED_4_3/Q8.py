import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 8")

################################################################
msg_1 = customtkinter.CTkLabel(app, text="Valor da compra:")
msg_1.pack(padx=10, pady=5)

valor_inicial = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Valor da compra...", textvariable=valor_inicial)
resposta_1.pack(padx=10, pady=5)

################################################################

valor_descontado = 0.0


def calc_desconto():

    atual = float(valor_inicial.get())

    if atual > 100:

        valor_descontado = atual - ((atual / 100) * 10)

        resultado.configure(
            text=f'10% de desconto, TOTAL: R$ {valor_descontado:.2f}', text_color="#42DB5A")

    elif atual <= 100 and atual >= 50:

        valor_descontado = atual - ((atual / 100) * 5)

        resultado.configure(
            text=f'5% de desconto, TOTAL: R$ {valor_descontado:.2f}', text_color="#42DB5A")
    else:
        valor_descontado = atual
        resultado.configure(
            text=f'Sem desconto, TOTAL: R$ {valor_descontado:.2f}', text_color="#F03E74")


calcular = customtkinter.CTkButton(
    app, text="Resultado", command=calc_desconto)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado:")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
