import customtkinter as ctk


class IntroView(ctk.CTkFrame):
    def __init__(self, master, on_click):
        super().__init__(master)

        self.on_click = on_click

        self.titulo = ctk.CTkLabel(
            self,
            text="🎯 Torneo de dardos \n trabajadores muy trabajadores",
            font=("Arial", 46, "bold")
        )
        self.titulo.pack(expand=True)

        self.texto_click = ctk.CTkLabel(
            self,
            text="Haz click para empezar",
            font=("Arial", 22)
        )
        self.texto_click.pack(pady=40)

        self.bind("<Button-1>", self.click_pantalla)
        self.titulo.bind("<Button-1>", self.click_pantalla)
        self.texto_click.bind("<Button-1>", self.click_pantalla)

    def click_pantalla(self, event):
        self.on_click()