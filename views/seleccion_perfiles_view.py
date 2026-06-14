import customtkinter as ctk
from data.perfiles import PERFILES


class SeleccionPerfilesView(ctk.CTkFrame):
    def __init__(self, master, numero_jugadores, on_confirmar, on_volver):
        super().__init__(master)

        self.numero_jugadores = numero_jugadores
        self.on_confirmar = on_confirmar
        self.on_volver = on_volver
        self.perfiles_seleccionados = []

        titulo = ctk.CTkLabel(
            self,
            text=f"Selecciona {numero_jugadores} perfiles",
            font=("Arial", 34, "bold")
        )
        titulo.pack(pady=25)

        self.info = ctk.CTkLabel(
            self,
            text="0 seleccionados",
            font=("Arial", 20)
        )
        self.info.pack(pady=10)

        self.frame_perfiles = ctk.CTkFrame(self)
        self.frame_perfiles.pack(pady=20)

        self.botones = []

        columnas = 4

        for i, perfil in enumerate(PERFILES):
            boton = ctk.CTkButton(
                self.frame_perfiles,
                text=perfil["nombre"],
                width=180,
                height=70,
                font=("Arial", 18, "bold"),
                command=lambda p=perfil: self.seleccionar_perfil(p)
            )
            boton.grid(row=i // columnas, column=i % columnas, padx=10, pady=10)
            self.botones.append((boton, perfil))

        self.boton_confirmar = ctk.CTkButton(
            self,
            text="Empezar partida",
            width=250,
            height=50,
            state="disabled",
            command=self.confirmar
        )
        self.boton_confirmar.pack(pady=15)

        boton_volver = ctk.CTkButton(
            self,
            text="Volver",
            width=180,
            height=40,
            command=self.on_volver
        )
        boton_volver.pack(pady=10)

    def seleccionar_perfil(self, perfil):
        if perfil in self.perfiles_seleccionados:
            self.perfiles_seleccionados.remove(perfil)
        else:
            if len(self.perfiles_seleccionados) < self.numero_jugadores:
                self.perfiles_seleccionados.append(perfil)

        self.actualizar_vista()

    def actualizar_vista(self):
        self.info.configure(
            text=f"{len(self.perfiles_seleccionados)} seleccionados de {self.numero_jugadores}"
        )

        for boton, perfil in self.botones:
            if perfil in self.perfiles_seleccionados:
                boton.configure(fg_color="green")
            else:
                boton.configure(fg_color="#1f6aa5")

        if len(self.perfiles_seleccionados) == self.numero_jugadores:
            self.boton_confirmar.configure(state="normal")
        else:
            self.boton_confirmar.configure(state="disabled")

    def confirmar(self):
        self.on_confirmar(self.perfiles_seleccionados)