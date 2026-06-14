import customtkinter as ctk


class ConfirmacionPartidaView(ctk.CTkFrame):
    def __init__(
        self,
        master,
        modo_juego,
        jugadores,
        on_comenzar,
        on_volver
    ):
        super().__init__(master)

        titulo = ctk.CTkLabel(
            self,
            text="Confirmar partida",
            font=("Arial", 34, "bold")
        )
        titulo.pack(pady=25)

        modo = ctk.CTkLabel(
            self,
            text=f"Modo de juego: {modo_juego}",
            font=("Arial", 24)
        )
        modo.pack(pady=10)

        jugadores_label = ctk.CTkLabel(
            self,
            text="Jugadores:",
            font=("Arial", 24, "bold")
        )
        jugadores_label.pack(pady=(20, 10))

        frame_jugadores = ctk.CTkFrame(self)
        frame_jugadores.pack(pady=10)

        for jugador in jugadores:
            etiqueta = ctk.CTkLabel(
                frame_jugadores,
                text=jugador["nombre"],
                font=("Arial", 20)
            )
            etiqueta.pack(pady=5)

        boton_comenzar = ctk.CTkButton(
            self,
            text="🎯 Comenzar partida",
            width=300,
            height=55,
            command=on_comenzar
        )
        boton_comenzar.pack(pady=25)

        boton_volver = ctk.CTkButton(
            self,
            text="Volver",
            width=200,
            height=45,
            command=on_volver
        )
        boton_volver.pack()