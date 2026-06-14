import os
import customtkinter as ctk
from PIL import Image


class ResultadosView(ctk.CTkFrame):
    def __init__(self, master, partida, on_menu_principal):
        super().__init__(master)

        self.partida = partida
        self.on_menu_principal = on_menu_principal
        self.objetivos_cricket = [20, 19, 18, 17, 16, 15, "BULL"]

        self.crear_interfaz()

    def crear_interfaz(self):
        ganador = self.partida.ganador

        self.crear_zona_ganador(ganador)
        self.crear_zona_inferior()

       

    def crear_zona_ganador(self, ganador):
        frame_superior = ctk.CTkFrame(self)
        frame_superior.pack(fill="x", padx=30, pady=(20, 10))

        titulo = ctk.CTkLabel(
            frame_superior,
            text="🏆 RESULTADOS",
            font=("Arial", 40, "bold")
        )
        titulo.pack(pady=(15, 10))

        foto = self.crear_foto_ganador(frame_superior, ganador)
        foto.pack(pady=10)

        nombre = ctk.CTkLabel(
            frame_superior,
            text=f"Ganador: {ganador.nombre}",
            font=("Arial", 32, "bold")
        )
        nombre.pack(pady=5)

        puntuacion = ctk.CTkLabel(
            frame_superior,
            text=f"Puntuación: {ganador.puntuacion}",
            font=("Arial", 24, "bold")
        )
        puntuacion.pack(pady=(0, 15))

    def crear_zona_inferior(self):
        frame_inferior = ctk.CTkFrame(self)
        frame_inferior.pack(fill="both", expand=True, padx=30, pady=10)

        frame_inferior.grid_columnconfigure(0, weight=1)
        frame_inferior.grid_columnconfigure(1, weight=3)
        frame_inferior.grid_rowconfigure(0, weight=1)

        frame_clasificacion = ctk.CTkFrame(frame_inferior)
        frame_clasificacion.grid(row=0, column=0, sticky="nsew", padx=(0, 12), pady=10)

        frame_tabla = ctk.CTkFrame(frame_inferior)
        frame_tabla.grid(row=0, column=1, sticky="nsew", padx=(12, 0), pady=10)

        self.crear_clasificacion(frame_clasificacion)
        self.crear_tabla_partida(frame_tabla)

    def crear_clasificacion(self, parent):
        titulo = ctk.CTkLabel(
            parent,
            text="Clasificación",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=(18, 12))

        jugadores_ordenados = sorted(
            self.partida.jugadores,
            key=lambda jugador: jugador.puntuacion,
            reverse=True
        )

        for posicion, jugador in enumerate(jugadores_ordenados, start=1):
            texto = f"{posicion}. {jugador.nombre} - {jugador.puntuacion} pts"

            if jugador == self.partida.ganador:
                texto = "🏆 " + texto

            label = ctk.CTkLabel(
                parent,
                text=texto,
                font=("Arial", 20, "bold" if jugador == self.partida.ganador else "normal")
            )
            label.pack(anchor="w", padx=25, pady=8)
        boton_menu = ctk.CTkButton(
            parent,
            text="Volver al menú principal",
            width=260,
            height=50,
            font=("Arial", 17, "bold"),
            command=self.on_menu_principal
        )
        boton_menu.pack(pady=(30, 15))

    def crear_tabla_partida(self, parent):
        titulo = ctk.CTkLabel(
            parent,
            text="Tabla de la partida",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=(18, 12))

        if self.partida.modo_juego == "Cricket":
            self.crear_tabla_cricket(parent)
        else:
            self.crear_tabla_normal(parent)

    def crear_tabla_cricket(self, parent):
        tabla = ctk.CTkFrame(parent)
        tabla.pack(fill="both", expand=True, padx=20, pady=15)

        ctk.CTkLabel(
            tabla,
            text="Jugador",
            font=("Arial", 20, "bold"),
            width=150
        ).grid(row=0, column=0, padx=8, pady=10)

        for col, objetivo in enumerate(self.objetivos_cricket, start=1):
            ctk.CTkLabel(
                tabla,
                text=str(objetivo),
                font=("Arial", 20, "bold"),
                width=80
            ).grid(row=0, column=col, padx=8, pady=10)

        ctk.CTkLabel(
            tabla,
            text="Pts",
            font=("Arial", 20, "bold"),
            width=90
        ).grid(row=0, column=len(self.objetivos_cricket) + 1, padx=8, pady=10)

        for fila, jugador in enumerate(self.partida.jugadores, start=1):
            ctk.CTkLabel(
                tabla,
                text=jugador.nombre,
                font=("Arial", 19, "bold"),
                width=150
            ).grid(row=fila, column=0, padx=8, pady=8)

            for col, objetivo in enumerate(self.objetivos_cricket, start=1):
                marcas = 0

                if hasattr(jugador, "cricket_marcas"):
                    marcas = jugador.cricket_marcas[objetivo]

                label = ctk.CTkLabel(
                    tabla,
                    text=self.convertir_marcas(marcas),
                    font=("Arial", 28, "bold"),
                    width=80
                )
                label.grid(row=fila, column=col, padx=8, pady=8)

            ctk.CTkLabel(
                tabla,
                text=str(jugador.puntuacion),
                font=("Arial", 24, "bold"),
                width=90
            ).grid(
                row=fila,
                column=len(self.objetivos_cricket) + 1,
                padx=8,
                pady=8
            )

        for col in range(len(self.objetivos_cricket) + 2):
            tabla.grid_columnconfigure(col, weight=1)

        for fila in range(len(self.partida.jugadores) + 1):
            tabla.grid_rowconfigure(fila, weight=1)

    def crear_tabla_normal(self, parent):
        tabla = ctk.CTkFrame(parent)
        tabla.pack(fill="both", expand=True, padx=20, pady=15)

        ctk.CTkLabel(
            tabla,
            text="Jugador",
            font=("Arial", 22, "bold"),
            width=200
        ).grid(row=0, column=0, padx=10, pady=12)

        ctk.CTkLabel(
            tabla,
            text="Puntuación final",
            font=("Arial", 22, "bold"),
            width=200
        ).grid(row=0, column=1, padx=10, pady=12)

        ctk.CTkLabel(
            tabla,
            text="Tiradas registradas",
            font=("Arial", 22, "bold"),
            width=200
        ).grid(row=0, column=2, padx=10, pady=12)

        for fila, jugador in enumerate(self.partida.jugadores, start=1):
            ctk.CTkLabel(
                tabla,
                text=jugador.nombre,
                font=("Arial", 20, "bold"),
                width=200
            ).grid(row=fila, column=0, padx=10, pady=10)

            ctk.CTkLabel(
                tabla,
                text=str(jugador.puntuacion),
                font=("Arial", 20),
                width=200
            ).grid(row=fila, column=1, padx=10, pady=10)

            ctk.CTkLabel(
                tabla,
                text=str(len(jugador.historial)),
                font=("Arial", 20),
                width=200
            ).grid(row=fila, column=2, padx=10, pady=10)

        tabla.grid_columnconfigure(0, weight=1)
        tabla.grid_columnconfigure(1, weight=1)
        tabla.grid_columnconfigure(2, weight=1)

    def crear_foto_ganador(self, parent, ganador):
        if os.path.exists(ganador.foto):
            imagen = Image.open(ganador.foto)

            foto = ctk.CTkImage(
                light_image=imagen,
                dark_image=imagen,
                size=(180, 180)
            )

            label = ctk.CTkLabel(
                parent,
                image=foto,
                text="",
                width=200,
                height=200
            )

            label.image = foto

        else:
            label = ctk.CTkLabel(
                parent,
                text="📷",
                font=("Arial", 80),
                width=200,
                height=200,
                fg_color="#333333",
                corner_radius=20
            )

        return label

    def convertir_marcas(self, marcas):
        texto = "-"

        if marcas == 1:
            texto = "/"

        elif marcas == 2:
            texto = "X"

        elif marcas >= 3:
            texto = "✅"

        return texto