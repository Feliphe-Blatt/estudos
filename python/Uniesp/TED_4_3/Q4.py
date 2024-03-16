import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 4")

###############################################################
msg_1 = customtkinter.CTkLabel(app, text="Primeiro número:")
msg_1.pack(padx=10, pady=5)

num_1 = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Número a comparar...", textvariable=num_1)
resposta_1.pack(padx=10, pady=5)

###############################################################
msg_2 = customtkinter.CTkLabel(app, text="Segundo número:")
msg_2.pack(padx=10, pady=5)

num_2 = customtkinter.StringVar()
resposta_2 = customtkinter.CTkEntry(
    app, placeholder_text="Número a comparar...", textvariable=num_2)
resposta_2.pack(padx=10, pady=5)

###############################################################


def compara():
    temp_1 = float(num_1.get())
    temp_2 = float(num_2.get())

    if temp_1 < temp_2:
        resultado.configure(text=f'Em Ordem crescente: {temp_1}, {temp_2}.')
    else:
        resultado.configure(text=f'Em Ordem crescente: {temp_2}, {temp_1}.')


calcular = customtkinter.CTkButton(app, text="Comparar", command=compara)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado:")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
