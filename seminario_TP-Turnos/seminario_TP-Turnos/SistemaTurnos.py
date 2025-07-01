from Paciente import Paciente
from Medico import Medico
from Turno import Turno

class SistemaTurnos:
    def __init__(self):
        self._pacientes = []  # Lista de pacientes registrados
        self._medicos = []    # Lista de médicos registrados
        self._turnos = []     # Lista de turnos asignados

    def agregar_paciente(self, paciente):
        self._pacientes.append(paciente)  # Agrega un paciente a la lista

    def agregar_medico(self, medico):
        self._medicos.append(medico)  # Agrega un médico a la lista

    def asignar_turno(self, paciente, medico, fecha):
        turno = Turno(paciente, medico, fecha)  # Crea un nuevo turno
        self._turnos.append(turno)  # Guarda el turno

    def mostrar_turnos(self):
        for turno in self._turnos:
            print(turno.mostrar_turno())  # Imprime los datos del turno
