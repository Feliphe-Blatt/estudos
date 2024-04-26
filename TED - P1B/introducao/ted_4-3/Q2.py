import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 2")

###############################################################
msg_1 = customtkinter.CTkLabel(app, text="Numero a ser\nComparado a 50:")
msg_1.pack(padx=10, pady=5)

num_1 = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Número a comparar...", textvariable=num_1)
resposta_1.pack(padx=10, pady=5)

###############################################################


def compara():
    temp = float(num_1.get())

    if temp > 50:
        resultado.configure(text="É maior que 50!", text_color="#42DB5A")

    elif temp < 50:
        resultado.configure(text="É menor que 50!", text_color="#F03E74")

    elif temp == 50:
        resultado.configure(text="É igual a 50!", text_color="#E0DB4A")

    else:
        resultado.configure(text="Número inválido!", text_color="#FFFFFF")


calcular = customtkinter.CTkButton(app, text="Comparar", command=compara)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado:")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
