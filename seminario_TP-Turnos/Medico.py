from Usuarios import Usuario

class Medico(Usuario):  # Hereda de Usuario
    def __init__(self, nombre, email, especialidad):
        super().__init__(nombre, email)  # Llama al constructor de Usuario
        self._especialidad = especialidad  # Guarda la especialidad

    def get_especialidad(self):
        return self._especialidad  # Devuelve la especialidad
