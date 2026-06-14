class JugadorPartida:
    def __init__(self, perfil, puntuacion_inicial=0):
        self.nombre = perfil["nombre"]
        self.foto = perfil["foto"]
        self.puntuacion = puntuacion_inicial
        self.historial = []

    def registrar_tirada(self, tirada):
        self.historial.append(tirada)