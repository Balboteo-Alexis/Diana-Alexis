import customtkinter as ctk

from views.confirmacion_partida_view import ConfirmacionPartidaView
from views.seleccion_perfiles_view import SeleccionPerfilesView
from views.intro_view import IntroView
from views.menu_juegos_view import MenuJuegosView
from views.numero_jugadores_view import NumeroJugadoresView


class DardosApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.jugadores = []



        self.title("Diana Alexis")
        self.geometry("1200x700")

        self.modo_juego = None
        self.numero_jugadores = None

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.mostrar_intro()

    def limpiar_pantalla(self):
        for widget in self.winfo_children():
            widget.destroy()

    def mostrar_intro(self):
        self.limpiar_pantalla()
        IntroView(self, self.mostrar_menu_juegos).pack(fill="both", expand=True)

    def mostrar_menu_juegos(self):
        self.limpiar_pantalla()
        MenuJuegosView(
        self,
        self.seleccionar_modo,
        self.mostrar_intro
        ).pack(fill="both", expand=True)

    def seleccionar_modo(self, modo):
        self.modo_juego = modo
        self.mostrar_numero_jugadores()

    def mostrar_numero_jugadores(self):
        self.limpiar_pantalla()
        NumeroJugadoresView(
            self,
            self.modo_juego,
            self.seleccionar_numero_jugadores,
            self.mostrar_menu_juegos
        ).pack(fill="both", expand=True)

    def seleccionar_numero_jugadores(self, numero):
        self.numero_jugadores = numero
        self.mostrar_seleccion_perfiles()
    
    def mostrar_seleccion_perfiles(self):
        self.limpiar_pantalla()
        SeleccionPerfilesView(
            self,
            self.numero_jugadores,
            self.confirmar_perfiles,
            self.mostrar_numero_jugadores
        ).pack(fill="both", expand=True)

    def confirmar_perfiles(self, perfiles):
        self.jugadores = perfiles
        self.mostrar_confirmacion_partida()
        
        
    def mostrar_confirmacion_partida(self):
        self.limpiar_pantalla()

        ConfirmacionPartidaView(
        self,
        self.modo_juego,
        self.jugadores,
        self.comenzar_partida,
        self.mostrar_seleccion_perfiles
        ).pack(fill="both", expand=True)


    def comenzar_partida(self):
        print("===== PARTIDA INICIADA =====")
        print("Modo:", self.modo_juego)

        for jugador in self.jugadores:
            print(jugador["nombre"])