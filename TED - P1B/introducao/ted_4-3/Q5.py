import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 5")

###############################################################
msg_1 = customtkinter.CTkLabel(app, text="Número a comparar com 10:")
msg_1.pack(padx=10, pady=5)

num_1 = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Número a comparar...", textvariable=num_1)
resposta_1.pack(padx=10, pady=5)

###############################################################


def compara():
    temp_1 = float(num_1.get())

    if temp_1 > 10:
        resultado.configure(
            text=f'{temp_1} é maior que 10!', text_color="#42DB5A")
    elif temp_1 < 10:
        resultado.configure(
            text=f'{temp_1} é menor que 10!', text_color="#F03E74")
    else:
        resultado.configure(
            text=f'{temp_1} é igual a 10!', text_color="#E0DB4A")


calcular = customtkinter.CTkButton(
    app, text="Comparar com 10", command=compara)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado:")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
