import customtkinter as ctk


class MenuJuegosView(ctk.CTkFrame):
    def __init__(self, master, on_modo_seleccionado, on_volver_intro):
        super().__init__(master)

        self.on_modo_seleccionado = on_modo_seleccionado
        self.on_volver_intro = on_volver_intro

        titulo = ctk.CTkLabel(
            self,
            text="🎯 ELIGE MODO DE JUEGO",
            font=("Arial", 38, "bold")
        )
        titulo.pack(pady=50)

        modos = ["301", "501", "Cricket", "Around the Clock"]

        for modo in modos:
            boton = ctk.CTkButton(
                self,
                text=modo,
                width=320,
                height=55,
                font=("Arial", 20),
                command=lambda m=modo: self.on_modo_seleccionado(m)
            )
            boton.pack(pady=10)

        boton_volver = ctk.CTkButton(
            self,
            text="Volver a la intro",
            width=220,
            height=45,
            font=("Arial", 16),
            command=self.on_volver_intro
        )
        boton_volver.pack(pady=35)