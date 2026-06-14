from game_modes.modo_base import ModoBase


class ModoCricket(ModoBase):
    nombre = "Cricket"
    puntuacion_inicial = 0
    limite_rondas = 20

    objetivos = [20, 19, 18, 17, 16, 15, "BULL"]

    def preparar_jugador(self, jugador):
        if not hasattr(jugador, "cricket_marcas"):
            jugador.cricket_marcas = {}

            for objetivo in self.objetivos:
                jugador.cricket_marcas[objetivo] = 0

    def aplicar_tirada(self, jugador, numero, multiplicador, jugadores=None):
        resultado = {
            "valida": True,
            "mensaje": "",
            "ganador": False,
            "ganador_objeto": None
        }

        if jugadores is None:
            jugadores = [jugador]

        for jugador_partida in jugadores:
            self.preparar_jugador(jugador_partida)

        objetivo = None
        impactos = 0
        valor_puntos = 0

        if numero in [20, 19, 18, 17, 16, 15]:
            objetivo = numero
            impactos = multiplicador
            valor_puntos = numero

        elif numero == 25:
            objetivo = "BULL"
            impactos = 1
            valor_puntos = 25

        elif numero == 50:
            objetivo = "BULL"
            impactos = 2
            valor_puntos = 25

        else:
            resultado["mensaje"] = f"{jugador.nombre} ha fallado. No cuenta."

        if objetivo is not None:
            if self.segmento_cerrado_por_todos(objetivo, jugadores):
                resultado["mensaje"] = (
                    f"{objetivo} está cerrado por todos. No suma."
                )

            else:
                marcas_actuales = jugador.cricket_marcas[objetivo]

                if marcas_actuales >= 3:
                    puntos = impactos * valor_puntos
                    jugador.puntuacion += puntos

                    resultado["mensaje"] = (
                        f"{jugador.nombre} ya tenía cerrado {objetivo} "
                        f"y suma {puntos} puntos."
                    )

                else:
                    marcas_necesarias = 3 - marcas_actuales

                    if impactos < marcas_necesarias:
                        jugador.cricket_marcas[objetivo] += impactos

                        resultado["mensaje"] = (
                            f"{jugador.nombre} marca {objetivo} "
                            f"({jugador.cricket_marcas[objetivo]}/3)."
                        )

                    elif impactos == marcas_necesarias:
                        jugador.cricket_marcas[objetivo] = 3

                        resultado["mensaje"] = (
                            f"{jugador.nombre} cierra el {objetivo}."
                        )

                    else:
                        jugador.cricket_marcas[objetivo] = 3

                        impactos_sobrantes = impactos - marcas_necesarias
                        puntos = impactos_sobrantes * valor_puntos
                        jugador.puntuacion += puntos

                        resultado["mensaje"] = (
                            f"{jugador.nombre} cierra el {objetivo} "
                            f"y suma {puntos} puntos."
                        )

            if self.jugador_ha_cerrado_todo(jugador):
                ganador = self.obtener_ganador_por_puntos(jugadores)

                resultado["ganador"] = True
                resultado["ganador_objeto"] = ganador
                resultado["mensaje"] = (
                    f"{jugador.nombre} ha cerrado todos los números. "
                    f"Gana {ganador.nombre} por puntos."
                )

        return resultado

    def segmento_cerrado_por_todos(self, objetivo, jugadores):
        cerrado = True

        for jugador in jugadores:
            self.preparar_jugador(jugador)

            if jugador.cricket_marcas[objetivo] < 3:
                cerrado = False

        return cerrado

    def jugador_ha_cerrado_todo(self, jugador):
        cerrado = True

        self.preparar_jugador(jugador)

        for objetivo in self.objetivos:
            if jugador.cricket_marcas[objetivo] < 3:
                cerrado = False

        return cerrado

    def obtener_ganador_por_puntos(self, jugadores):
        ganador = jugadores[0]

        for jugador in jugadores:
            if jugador.puntuacion > ganador.puntuacion:
                ganador = jugador

        return ganador