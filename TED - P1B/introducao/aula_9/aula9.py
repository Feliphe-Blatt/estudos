import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

app = customtkinter.CTk()
app.geometry("600x600")
app.title("nome da janela")

mensagem_inicial = customtkinter.CTkLabel(app, text='Alou Rapeize...')
mensagem_inicial.pack(padx=10, pady=10)

app.mainloop()