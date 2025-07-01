# Se importan todas las clases a utilizar
from SistemaTurnos import SistemaTurnos
from Paciente import Paciente
from Medico import Medico
from Turno import Turno
# Crea el sistema de turnos
sistema = SistemaTurnos()

# Crea un paciente
nombrePaciente = input("Ingrese nombre de paciente: ")
mailPaciente = input("Ingrese mail de paciente: ")
paciente1 = Paciente(nombrePaciente, mailPaciente)
sistema.agregar_paciente(paciente1)  # Agrega al sistema

fecha = Turno.agregar_fecha(Turno)
# Crea un médico
nombreDoctor = input("Ingrese nombre de Doctor: ")
mailDoctor = input("Ingrese mail del Doctor: ")
especialidad = input("Ingrese especialidad: ")
medico1 = Medico(nombreDoctor, mailDoctor, especialidad)
sistema.agregar_medico(medico1)  # Agrega al sistema

# Asigna un turno entre el paciente y el médico

sistema.asignar_turno(paciente1, medico1, fecha)

# Muestra los turnos asignados
sistema.mostrar_turnos()
