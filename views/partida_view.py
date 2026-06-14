import os
import customtkinter as ctk
from PIL import Image


class PartidaView(ctk.CTkFrame):

    def __init__(
        self,
        master,
        partida,
        on_volver_menu,
        on_mostrar_resultados
    ):
        super().__init__(master)

        self.partida = partida
        self.on_volver_menu = on_volver_menu
        self.on_mostrar_resultados = on_mostrar_resultados

        self.labels_puntuacion = []

        self.crear_interfaz()
        self.actualizar_interfaz()

    def crear_interfaz(self):

        titulo = ctk.CTkLabel(
            self,
            text=f"🎯 {self.partida.modo_juego}",
            font=("Arial", 32, "bold")
        )
        titulo.pack(pady=15)

        self.label_turno = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 24, "bold")
        )
        self.label_turno.pack()

        self.label_dardo = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 18)
        )
        self.label_dardo.pack(pady=5)

        self.label_mensaje = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 18)
        )
        self.label_mensaje.pack(pady=5)

        self.frame_jugadores = ctk.CTkFrame(self)
        self.frame_jugadores.pack(fill="x", padx=20, pady=20)

        for jugador in self.partida.jugadores:

            card = ctk.CTkFrame(self.frame_jugadores)
            card.pack(side="left", padx=10, pady=10, expand=True)

            foto = self.crear_marco_foto(card, jugador)
            foto.pack(pady=10)

            nombre = ctk.CTkLabel(
                card,
                text=jugador.nombre,
                font=("Arial", 18, "bold")
            )
            nombre.pack()

            puntuacion = ctk.CTkLabel(
                card,
                text=str(jugador.puntuacion),
                font=("Arial", 30, "bold")
            )
            puntuacion.pack()

            self.labels_puntuacion.append(puntuacion)

        self.multiplicador = ctk.IntVar(value=1)

        frame_mult = ctk.CTkFrame(self)
        frame_mult.pack(pady=10)

        for texto, valor in [
            ("Simple", 1),
            ("Doble", 2),
            ("Triple", 3)
        ]:

            radio = ctk.CTkRadioButton(
                frame_mult,
                text=texto,
                variable=self.multiplicador,
                value=valor
            )

            radio.pack(side="left", padx=15)

        frame_numeros = ctk.CTkFrame(self)
        frame_numeros.pack(pady=10)

        for numero in range(1, 21):

            boton = ctk.CTkButton(
                frame_numeros,
                text=str(numero),
                width=60,
                command=lambda n=numero: self.registrar_tirada(n)
            )

            boton.grid(
                row=(numero - 1) // 10,
                column=(numero - 1) % 10,
                padx=3,
                pady=3
            )

        frame_extra = ctk.CTkFrame(self)
        frame_extra.pack(pady=10)

        ctk.CTkButton(
            frame_extra,
            text="Bull 25",
            command=lambda: self.registrar_tirada(25)
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            frame_extra,
            text="Bullseye 50",
            command=lambda: self.registrar_tirada(50)
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            frame_extra,
            text="Fallo",
            command=lambda: self.registrar_tirada(0)
        ).pack(side="left", padx=5)

    def crear_marco_foto(self, parent, jugador):

        if os.path.exists(jugador.foto):

            imagen = Image.open(jugador.foto)

            foto = ctk.CTkImage(
                light_image=imagen,
                dark_image=imagen,
                size=(100, 100)
            )

            label = ctk.CTkLabel(
                parent,
                image=foto,
                text=""
            )

            label.image = foto

            return label

        return ctk.CTkLabel(
            parent,
            text="📷",
            width=100,
            height=100
        )

    def registrar_tirada(self, numero):

        multiplicador = self.multiplicador.get()

        if numero == 0:
            multiplicador = 0

        elif numero == 25:
            multiplicador = 1

        elif numero == 50:
            multiplicador = 1

        resultado = self.partida.registrar_tirada(
            numero,
            multiplicador
        )

        self.label_mensaje.configure(
            text=resultado["mensaje"]
        )

        self.actualizar_interfaz()

        if resultado["ganador"]:
            self.on_mostrar_resultados()

    def actualizar_interfaz(self):

        jugador_actual = self.partida.jugador_actual()

        self.label_turno.configure(
            text=f"Turno de: {jugador_actual.nombre}"
        )

        self.label_dardo.configure(
            text=f"Dardo {self.partida.dardos_lanzados + 1} de 3"
        )

        for i, jugador in enumerate(self.partida.jugadores):

            self.labels_puntuacion[i].configure(
                text=str(jugador.puntuacion)
            )