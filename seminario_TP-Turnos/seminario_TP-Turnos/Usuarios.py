# Clase base Usuario
class Usuario:
    def __init__(self, nombre, email):
        self._nombre = nombre  # Guarda el nombre
        self._email = email    # Guarda el email

    def get_nombre(self):
        return self._nombre  # Devuelve el nombre

    def get_email(self):
        return self._email  # Devuelve el email
