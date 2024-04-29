import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 6")

################################################################
msg_1 = customtkinter.CTkLabel(app, text="Número da conta:")
msg_1.pack(padx=10, pady=5)

conta = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Número da conta...", textvariable=conta)
resposta_1.pack(padx=10, pady=5)

################################################################
msg_2 = customtkinter.CTkLabel(app, text="Saldo:")
msg_2.pack(padx=10, pady=5)

saldo = customtkinter.StringVar()
resposta_2 = customtkinter.CTkEntry(
    app, placeholder_text="Saldo da conta...", textvariable=saldo)
resposta_2.pack(padx=10, pady=5)

################################################################
msg_3 = customtkinter.CTkLabel(app, text="Débito:")
msg_3.pack(padx=10, pady=5)

debito = customtkinter.StringVar()
resposta_3 = customtkinter.CTkEntry(
    app, placeholder_text="Número da conta...", textvariable=debito)
resposta_3.pack(padx=10, pady=5)

################################################################
msg_4 = customtkinter.CTkLabel(app, text="Crédito:")
msg_4.pack(padx=10, pady=5)

credito = customtkinter.StringVar()
resposta_4 = customtkinter.CTkEntry(
    app, placeholder_text="Número da conta...", textvariable=credito)
resposta_4.pack(padx=10, pady=5)

################################################################


def calc_resultado():

    total = float(saldo.get()) - float(debito.get()) + float(credito.get())

    if total > 0:
        resultado.configure(
            text=f'Saldo Positivo de: R${total:.2f}!', text_color="#42DB5A")
    elif total < 0:
        resultado.configure(
            text=f'Saldo Negativo de: R${total:.2f}!', text_color="#F03E74")
    else:
        resultado.configure(
            text=f'Saldo Neutro de: R${total:.2f}!', text_color="#E0DB4A")


calcular = customtkinter.CTkButton(
    app, text="Resultado", command=calc_resultado)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado:")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
