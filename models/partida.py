from models.jugador_partida import JugadorPartida


class Partida:
    def __init__(self, modo_juego, perfiles, modo):
        self.modo_juego = modo_juego
        self.modo = modo

        self.jugadores = [
            JugadorPartida(perfil, modo.puntuacion_inicial)
            for perfil in perfiles
        ]

        self.turno_actual = 0
        self.dardos_lanzados = 0
        self.tiradas_turno = []
        self.ganador = None

        self.ronda_actual = 1
        self.limite_rondas = getattr(modo, "limite_rondas", None)

    def jugador_actual(self):
        return self.jugadores[self.turno_actual]

    def registrar_tirada(self, numero, multiplicador):
        resultado = {
            "valida": False,
            "mensaje": "",
            "ganador": False
        }

        if self.ganador is not None:
            resultado["mensaje"] = "La partida ya ha terminado"

        else:
            jugador = self.jugador_actual()

            resultado = self.modo.aplicar_tirada(
                jugador,
                numero,
                multiplicador,
                self.jugadores
            )

            if resultado["valida"]:
                puntos = numero * multiplicador

                self.tiradas_turno.append({
                    "numero": numero,
                    "multiplicador": multiplicador,
                    "puntos": puntos
                })

                self.dardos_lanzados += 1

                if resultado["ganador"]:
                    self.ganador = resultado.get("ganador_objeto", jugador)
                    jugador.registrar_tirada(self.tiradas_turno.copy())

                else:
                    if self.dardos_lanzados == 3:
                        jugador.registrar_tirada(self.tiradas_turno.copy())
                        self.siguiente_turno()

                        if self.partida_supera_limite_rondas():
                            self.ganador = self.modo.obtener_ganador_por_puntos(
                                self.jugadores
                            )

                            resultado["ganador"] = True
                            resultado["ganador_objeto"] = self.ganador
                            resultado["mensaje"] = (
                                f"Fin de la ronda 20. "
                                f"Gana {self.ganador.nombre} por puntos."
                            )

        return resultado

    def siguiente_turno(self):
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)
        self.dardos_lanzados = 0
        self.tiradas_turno = []

        if self.turno_actual == 0:
            self.ronda_actual += 1

    def partida_supera_limite_rondas(self):
        supera_limite = False

        if self.limite_rondas is not None:
            if self.ronda_actual > self.limite_rondas:
                supera_limite = True

        return supera_limite