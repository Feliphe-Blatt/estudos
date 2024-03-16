import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("600x600")
app.title("Questão 15")

################################################################
titulo = customtkinter.CTkLabel(app, text="Velocidade atual:")
titulo.pack(padx=10, pady=2)

velocidade = customtkinter.StringVar()
resposta_1 = customtkinter.CTkEntry(
    app, placeholder_text="Velocidade...", textvariable=velocidade)
resposta_1.pack(padx=10, pady=5)

################################################################


def calc_ir():

    temp = float(velocidade.get())

    if temp < 80:
        resultado.configure(
            text='Abaixo do limite (80km/h)!', text_color="#42DB5A")
    elif temp == 80:
        resultado.configure(
            text='No limite (80km/h)!', text_color="#E0DB4A")
    else:
        multa = (temp - 80) * 5
        resultado.configure(
            text=f'Acima do limite (80km/h), Multa de R$ {multa:.2f}!\n(+R$ 5,00 para cada Km a mais!)', text_color="#F03E74")


calcular = customtkinter.CTkButton(
    app, text="Resultado", command=calc_ir)
calcular.pack(padx=10, pady=20)

###############################################################
resultado = customtkinter.CTkLabel(app, text="Resultado...")
resultado.pack(padx=10, pady=2)

###############################################################
app.mainloop()
