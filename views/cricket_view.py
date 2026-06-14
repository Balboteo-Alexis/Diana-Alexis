import os
import customtkinter as ctk
from PIL import Image


class CricketView(ctk.CTkFrame):
    def __init__(self, master, partida, on_volver_menu, on_mostrar_resultados):
        super().__init__(master)

        self.partida = partida
        self.on_volver_menu = on_volver_menu
        self.on_mostrar_resultados = on_mostrar_resultados

        self.objetivos = [20, 19, 18, 17, 16, 15, "BULL"]

        self.labels_puntuacion = {}
        self.labels_marcas = {}
        self.labels_nombre_cards = {}
        self.label_foto_turno = None
        self.label_ronda = None
        self.imagen_turno = None

        self.crear_interfaz()
        self.actualizar_interfaz()

    def crear_interfaz(self):
        self.crear_cabecera()
        self.crear_zona_principal()
        self.crear_controles_inferiores()

    def crear_cabecera(self):
        titulo = ctk.CTkLabel(
            self,
            text="🎯 CRICKET",
            font=("Arial", 34, "bold")
        )
        titulo.pack(pady=(8, 4))

        frame_turno = ctk.CTkFrame(self)
        frame_turno.pack(pady=4)

        self.label_foto_turno = ctk.CTkLabel(
            frame_turno,
            text="📷",
            width=70,
            height=70,
            font=("Arial", 34),
            fg_color="#333333",
            corner_radius=12
        )
        self.label_foto_turno.pack(side="left", padx=12, pady=8)

        frame_textos_turno = ctk.CTkFrame(frame_turno)
        frame_textos_turno.pack(side="left", padx=12, pady=8)

        self.label_turno = ctk.CTkLabel(
            frame_textos_turno,
            text="",
            font=("Arial", 24, "bold")
        )
        self.label_turno.pack(anchor="w")

        self.label_dardo = ctk.CTkLabel(
            frame_textos_turno,
            text="",
            font=("Arial", 18)
        )
        self.label_dardo.pack(anchor="w", pady=2)

        self.label_mensaje = ctk.CTkLabel(
            self,
            text="Marca un número de Cricket",
            font=("Arial", 18)
        )
        self.label_mensaje.pack(pady=(4, 8))

    def crear_zona_principal(self):
        zona_principal = ctk.CTkFrame(self)
        zona_principal.pack(fill="both", expand=True, padx=20, pady=8)

        self.frame_izquierda = ctk.CTkFrame(zona_principal)
        self.frame_izquierda.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10),
            pady=8
        )

        self.frame_tabla = ctk.CTkFrame(zona_principal)
        self.frame_tabla.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10,
            pady=8
        )

        self.frame_derecha = ctk.CTkFrame(zona_principal)
        self.frame_derecha.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=(10, 0),
            pady=8
        )

        zona_principal.grid_columnconfigure(0, weight=1)
        zona_principal.grid_columnconfigure(1, weight=3)
        zona_principal.grid_columnconfigure(2, weight=1)
        zona_principal.grid_rowconfigure(0, weight=1)

        self.crear_jugadores_laterales()
        self.crear_tabla_central()

    def crear_jugadores_laterales(self):
        mitad = (len(self.partida.jugadores) + 1) // 2

        for indice, jugador in enumerate(self.partida.jugadores):
            if indice < mitad:
                parent = self.frame_izquierda
            else:
                parent = self.frame_derecha

            card = ctk.CTkFrame(parent, height=115)
            card.pack(pady=14, padx=10, fill="x")
            card.pack_propagate(False)

            foto = self.crear_marco_foto(card, jugador, 85)
            foto.pack(side="left", padx=14, pady=10)

            frame_info = ctk.CTkFrame(card)
            frame_info.pack(side="left", fill="both", expand=True, padx=8, pady=10)

            nombre = ctk.CTkLabel(
                frame_info,
                text=jugador.nombre,
                font=("Arial", 19, "bold")
            )
            nombre.pack(anchor="w", pady=(8, 2))

            puntuacion = ctk.CTkLabel(
                frame_info,
                text=str(jugador.puntuacion),
                font=("Arial", 32, "bold")
            )
            puntuacion.pack(anchor="w", pady=(0, 6))

            self.labels_puntuacion[jugador.nombre] = puntuacion
            self.labels_nombre_cards[jugador.nombre] = card

    def crear_tabla_central(self):
        titulo_tabla = ctk.CTkLabel(
            self.frame_tabla,
            text="Marcador Cricket",
            font=("Arial", 28, "bold")
        )
        titulo_tabla.pack(pady=(18, 12))

        tabla = ctk.CTkFrame(self.frame_tabla)
        tabla.pack(fill="both", expand=True, padx=18, pady=18)

        ctk.CTkLabel(
            tabla,
            text="Jugador",
            font=("Arial", 20, "bold"),
            width=150
        ).grid(row=0, column=0, padx=8, pady=12)

        for col, objetivo in enumerate(self.objetivos, start=1):
            ctk.CTkLabel(
                tabla,
                text=str(objetivo),
                font=("Arial", 20, "bold"),
                width=80
            ).grid(row=0, column=col, padx=8, pady=12)

        ctk.CTkLabel(
            tabla,
            text="Pts",
            font=("Arial", 20, "bold"),
            width=80
        ).grid(row=0, column=len(self.objetivos) + 1, padx=8, pady=12)

        for fila, jugador in enumerate(self.partida.jugadores, start=1):
            ctk.CTkLabel(
                tabla,
                text=jugador.nombre,
                font=("Arial", 19, "bold"),
                width=150
            ).grid(row=fila, column=0, padx=8, pady=10)

            self.labels_marcas[jugador.nombre] = {}

            for col, objetivo in enumerate(self.objetivos, start=1):
                label = ctk.CTkLabel(
                    tabla,
                    text="-",
                    font=("Arial", 28, "bold"),
                    width=80
                )
                label.grid(row=fila, column=col, padx=8, pady=10)

                self.labels_marcas[jugador.nombre][objetivo] = label

            label_puntos = ctk.CTkLabel(
                tabla,
                text="0",
                font=("Arial", 25, "bold"),
                width=80
            )
            label_puntos.grid(
                row=fila,
                column=len(self.objetivos) + 1,
                padx=8,
                pady=10
            )

            self.labels_puntuacion[jugador.nombre + "_tabla"] = label_puntos

        for col in range(len(self.objetivos) + 2):
            tabla.grid_columnconfigure(col, weight=1)

        for fila in range(len(self.partida.jugadores) + 1):
            tabla.grid_rowconfigure(fila, weight=1)

    def crear_controles_inferiores(self):
        frame_controles = ctk.CTkFrame(self, height=90)
        frame_controles.pack(fill="x", padx=20, pady=(8, 16))
        frame_controles.pack_propagate(False)

        self.multiplicador = ctk.IntVar(value=1)

        frame_mult = ctk.CTkFrame(frame_controles)
        frame_mult.pack(side="left", padx=18, pady=16)

        for texto, valor in [("Simple", 1), ("Doble", 2), ("Triple", 3)]:
            radio = ctk.CTkRadioButton(
                frame_mult,
                text=texto,
                variable=self.multiplicador,
                value=valor,
                font=("Arial", 18)
            )
            radio.pack(side="left", padx=14, pady=10)

        frame_numeros = ctk.CTkFrame(frame_controles)
        frame_numeros.pack(side="left", padx=16, pady=16)

        for numero in [20, 19, 18, 17, 16, 15]:
            boton = ctk.CTkButton(
                frame_numeros,
                text=str(numero),
                width=80,
                height=52,
                font=("Arial", 20, "bold"),
                command=lambda n=numero: self.registrar_tirada(n)
            )
            boton.pack(side="left", padx=5)

        frame_extra = ctk.CTkFrame(frame_controles)
        frame_extra.pack(side="left", padx=16, pady=16)

        boton_bull = ctk.CTkButton(
            frame_extra,
            text="Bull 25",
            width=125,
            height=52,
            font=("Arial", 16, "bold"),
            command=lambda: self.registrar_tirada(25)
        )
        boton_bull.pack(side="left", padx=5)

        boton_centro = ctk.CTkButton(
            frame_extra,
            text="Centro 50",
            width=125,
            height=52,
            font=("Arial", 16, "bold"),
            command=lambda: self.registrar_tirada(50)
        )
        boton_centro.pack(side="left", padx=5)

        boton_fallo = ctk.CTkButton(
            frame_extra,
            text="Fallo",
            width=110,
            height=52,
            font=("Arial", 16, "bold"),
            command=lambda: self.registrar_tirada(0)
        )
        boton_fallo.pack(side="left", padx=5)

        boton_menu = ctk.CTkButton(
            frame_controles,
            text="Menú",
            width=100,
            height=52,
            font=("Arial", 16, "bold"),
            command=self.on_volver_menu
        )
        boton_menu.pack(side="right", padx=18, pady=16)

    def crear_marco_foto(self, parent, jugador, size):
        if os.path.exists(jugador.foto):
            imagen = Image.open(jugador.foto)

            foto = ctk.CTkImage(
                light_image=imagen,
                dark_image=imagen,
                size=(size, size)
            )

            label = ctk.CTkLabel(
                parent,
                image=foto,
                text="",
                width=size + 10,
                height=size + 10
            )
            label.image = foto

        else:
            label = ctk.CTkLabel(
                parent,
                text="📷",
                font=("Arial", int(size / 2)),
                width=size + 10,
                height=size + 10,
                fg_color="#333333",
                corner_radius=12
            )

        return label

    def actualizar_foto_turno(self, jugador):
        if os.path.exists(jugador.foto):
            imagen = Image.open(jugador.foto)

            self.imagen_turno = ctk.CTkImage(
                light_image=imagen,
                dark_image=imagen,
                size=(65, 65)
            )

            self.label_foto_turno.configure(
                image=self.imagen_turno,
                text=""
            )

        else:
            self.label_foto_turno.configure(
                image=None,
                text="📷"
            )

    def registrar_tirada(self, numero):
        multiplicador = self.multiplicador.get()

        if numero == 0:
            multiplicador = 0
        elif numero == 25:
            multiplicador = 1
        elif numero == 50:
            multiplicador = 1

        resultado = self.partida.registrar_tirada(numero, multiplicador)

        self.label_mensaje.configure(text=resultado["mensaje"])
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

        self.actualizar_foto_turno(jugador_actual)
        self.resaltar_jugador_actual(jugador_actual)

        for jugador in self.partida.jugadores:
            self.labels_puntuacion[jugador.nombre].configure(
                text=str(jugador.puntuacion)
            )

            self.labels_puntuacion[jugador.nombre + "_tabla"].configure(
                text=str(jugador.puntuacion)
            )

            if hasattr(jugador, "cricket_marcas"):
                for objetivo in self.objetivos:
                    marcas = jugador.cricket_marcas[objetivo]

                    self.labels_marcas[jugador.nombre][objetivo].configure(
                        text=self.convertir_marcas(marcas)
                    )

    def resaltar_jugador_actual(self, jugador_actual):
        for jugador in self.partida.jugadores:
            if jugador.nombre in self.labels_nombre_cards:
                card = self.labels_nombre_cards[jugador.nombre]

                if jugador == jugador_actual:
                    card.configure(border_width=3)
                else:
                    card.configure(border_width=0)

    def convertir_marcas(self, marcas):
        texto = "-"

        if marcas == 1:
            texto = "/"

        elif marcas == 2:
            texto = "X"

        elif marcas >= 3:
            texto = "✅"

        return texto