import customtkinter


fonte_app = customtkinter.CTkFont(family="Helvetica", size=20)

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

app = customtkinter.CTk()
app.geometry("600x600")
app.title("nome da janela")

mensagem_inicial = customtkinter.CTkLabel(app, text='Alou Rapeize...', font=fonte_app)
mensagem_inicial.pack(padx=10, pady=10)

val_1 = customtkinter.StringVar()
input = customtkinter.CTkEntry(app, placeholder_text = 'Digite algo...', textvariable = val_1)
input.pack(padx=10, pady=10)

temporario = ''

def somar():

    #configure

botao = customtkinter.CTkButton(app, text='Calcular', command=somar)

mensagem_final = customtkinter.CTkLabel(app, text='Resultado:', font=fonte_app)
mensagem_final.pack(padx=10, pady=10)

app.mainloop()
