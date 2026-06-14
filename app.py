import customtkinter as ctk

from views.confirmacion_partida_view import ConfirmacionPartidaView
from views.seleccion_perfiles_view import SeleccionPerfilesView
from views.intro_view import IntroView
from views.menu_juegos_view import MenuJuegosView
from views.numero_jugadores_view import NumeroJugadoresView
from views.partida_view import PartidaView
from views.resultados_view import ResultadosView
from views.cricket_view import CricketView

from models.partida import Partida

from game_modes.x01 import ModoX01
from game_modes.cricket import ModoCricket
from game_modes.around_the_clock import ModoAroundTheClock


class DardosApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🎯 Dardos Manager")
        self.geometry("1600x900")
        self.state("zoomed")

        self.modo_juego = None
        self.numero_jugadores = None
        self.jugadores = []
        self.partida = None

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
        if self.modo_juego == "301":
            modo = ModoX01(301)
        elif self.modo_juego == "501":
            modo = ModoX01(501)
        elif self.modo_juego == "Cricket":
            modo = ModoCricket()
        elif self.modo_juego == "Around the Clock":
            modo = ModoAroundTheClock()
        else:
            modo = ModoX01(501)

        self.partida = Partida(
            self.modo_juego,
            self.jugadores,
            modo
        )

        self.mostrar_partida()

    def mostrar_partida(self):
        self.limpiar_pantalla()

        if self.modo_juego == "Cricket":
            CricketView(
                self,
                self.partida,
                self.mostrar_menu_juegos,
                self.mostrar_resultados
            ).pack(fill="both", expand=True)

        else:
            PartidaView(
                self,
                self.partida,
                self.mostrar_menu_juegos,
                self.mostrar_resultados
            ).pack(fill="both", expand=True)    
        
    def mostrar_resultados(self):
        self.limpiar_pantalla()

        ResultadosView(
            self,
            self.partida,
            self.mostrar_menu_juegos
        ).pack(fill="both", expand=True)