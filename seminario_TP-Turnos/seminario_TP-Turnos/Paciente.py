from Usuarios import Usuario

class Paciente(Usuario):  # Hereda de Usuario
    def __init__(self, nombre, email):
        super().__init__(nombre, email)  # Llama al constructor de Usuario

