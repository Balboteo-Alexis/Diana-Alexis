import customtkinter as ctk


class NumeroJugadoresView(ctk.CTkFrame):
    def __init__(self, master, modo_juego, on_numero_seleccionado, on_volver):
        super().__init__(master)

        titulo = ctk.CTkLabel(
            self,
            text=f"Modo seleccionado: {modo_juego}",
            font=("Arial", 34, "bold")
        )
        titulo.pack(pady=40)

        subtitulo = ctk.CTkLabel(
            self,
            text="¿Cuántos jugadores vais a jugar?",
            font=("Arial", 26)
        )
        subtitulo.pack(pady=20)

        frame_botones = ctk.CTkFrame(self)
        frame_botones.pack(pady=20)

        for numero in range(1, 9):
            boton = ctk.CTkButton(
                frame_botones,
                text=str(numero),
                width=80,
                height=60,
                font=("Arial", 24, "bold"),
                command=lambda n=numero: on_numero_seleccionado(n)
            )
            boton.grid(row=0, column=numero - 1, padx=8, pady=8)

        boton_volver = ctk.CTkButton(
            self,
            text="Volver",
            width=200,
            height=45,
            command=on_volver
        )
        boton_volver.pack(pady=40)