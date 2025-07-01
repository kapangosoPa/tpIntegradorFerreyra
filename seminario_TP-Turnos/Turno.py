class Turno:
    def __init__(self, paciente, medico, fecha):
        self._paciente = paciente  # Guarda el objeto Paciente
        self._medico = medico      # Guarda el objeto Medico
        self._fecha = fecha        # Guarda la fecha del turno

    def mostrar_turno(self):
        # Devuelve una cadena con los datos del turno
        return f"Turno: {self._fecha} - Paciente: {self._paciente.get_nombre()} - Médico: {self._medico.get_nombre()} ({self._medico.get_especialidad()})"
