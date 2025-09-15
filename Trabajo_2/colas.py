from collections import deque
from datetime import datetime

FORMATO_FECHA = "%Y-%m-%d"
FORMATO_HORA = "%H:%M"

# normalizar prioridad, fecha y hora para evitar errores

def normaliza(txt):
    if txt is None:
        return ""
    return str(txt).strip()

def es_extraccion(txt):
    t = normaliza(txt).lower()
    # aceptar "extraccion" sin tilde y "extracción" con tilde
    return t == "extraccion" or t == "extracción"

def es_urgente(txt):
    return normaliza(txt).lower() == "urgente"

def fecha_valida(fecha_txt):
    try:
        datetime.strptime(fecha_txt, FORMATO_FECHA)
        return True
    except:
        return False

def hora_valida(hora_txt):
    try:
        datetime.strptime(hora_txt, FORMATO_HORA)
        return True
    except:
        return False
    
class Cita:
    def __init__(self, cedula, nombre, telefono, tipo_cliente,
                 tipo_atencion, prioridad, fecha, hora, cantidad=1):
        self.cedula = normaliza(cedula)
        self.nombre = normaliza(nombre)
        self.telefono = normaliza(telefono)
        self.tipo_cliente = normaliza(tipo_cliente)
        self.tipo_atencion = normaliza(tipo_atencion)
        self.prioridad = normaliza(prioridad)
        self.fecha = normaliza(fecha)  # esperado YYYY-MM-DD
        self.hora = normaliza(hora)    # esperado HH:MM
        try:
            self.cantidad = int(cantidad)
        except:
            self.cantidad = 1

    def es_extraccion_urgente(self):
        return es_extraccion(self.tipo_atencion) and es_urgente(self.prioridad)

class Cita:
    def __init__(self, cedula, nombre, telefono, tipo_cliente,
                 tipo_atencion, prioridad, fecha, hora, cantidad=1):
        self.cedula = normaliza(cedula)
        self.nombre = normaliza(nombre)
        self.telefono = normaliza(telefono)
        self.tipo_cliente = normaliza(tipo_cliente)
        self.tipo_atencion = normaliza(tipo_atencion)
        self.prioridad = normaliza(prioridad)
        self.fecha = normaliza(fecha) 
        self.hora = normaliza(hora)   
        try:
            self.cantidad = int(cantidad)
        except:
            self.cantidad = 1

    def es_extraccion_urgente(self):
        return es_extraccion(self.tipo_atencion) and es_urgente(self.prioridad)

class ColaUrgencias:
    def __init__(self):
        self.q = deque()

    def generar(self, lista_citas):
        # filtra solo extracción + urgente
        filtradas = []
        for c in lista_citas:
            if c.es_extraccion_urgente():
                filtradas.append(c)

        if len(filtradas) == 0:
            self.q = deque()
            print("No hay citas de extracción urgentes.")
            return

        # orden por fecha ascendente 
        try:
            def clave_fecha(c):
                if fecha_valida(c.fecha):
                    return c.fecha
                else:
                    return "9999-12-31"
            ordenadas = sorted(filtradas, key=clave_fecha)
        except:
            ordenadas = filtradas

        self.q = deque()
        for item in ordenadas:
            self.q.append(item)

        print("Cola de URGENCIAS generada con", len(self.q), "paciente(s).")

    def ver(self):
        print("\n--- COLA URGENCIAS ---")
        if len(self.q) == 0:
            print("Cola vacía.")
            return
        idx = 1
        for c in list(self.q):
            print(str(idx) + ".", c.fecha, "-", c.nombre, "-", c.cedula)
            idx = idx + 1

    def llamar_siguiente(self):
        if len(self.q) == 0:
            print("No hay pacientes en la cola de urgencias.")
            return
        c = self.q.popleft()
        print("Llamando URGENCIA:", c.nombre, "-", c.cedula, "|", c.fecha, c.hora)

class ColaAgenda:
    def __init__(self):
        self.q = deque()

    def generar_por_fecha(self, lista_citas, fecha_objetivo):
        if not fecha_valida(fecha_objetivo):
            print("Fecha inválida (use YYYY-MM-DD).")
            return

        candidatos = []
        for c in lista_citas:
            if c.fecha == fecha_objetivo:
                candidatos.append(c)

        if len(candidatos) == 0:
            self.q = deque()
            print("No hay citas para esa fecha.")
            return

        # ordenar por hora ascendente
        try:
            def clave_hora(c):
                if hora_valida(c.hora):
                    return c.hora
                else:
                    return "23:59"
            candidatos = sorted(candidatos, key=clave_hora)
        except:
            pass

        self.q = deque()
        for x in candidatos:
            self.q.append(x)

        print("Cola de AGENDA creada para", fecha_objetivo, "con", len(self.q), "paciente(s).")

    def ver(self):
        print("\n--- COLA AGENDA ---")
        if len(self.q) == 0:
            print("Cola vacía.")
            return
        idx = 1
        for c in list(self.q):
            print(str(idx) + ".", c.hora, "-", c.nombre, "-", c.cedula)
            idx = idx + 1

    def atender_siguiente(self):
        if len(self.q) == 0:
            print("No hay pacientes en la cola de agenda.")
            return
        c = self.q.popleft()
        print("Atendiendo AGENDA:", c.nombre, "-", c.cedula, "|", c.fecha, c.hora)

class SistemaConsultorio:
    def __init__(self,base_datos=[]):
        self.bd = base_datos              # lista de Cita
        self.urgencias = ColaUrgencias()
        self.agenda = ColaAgenda()

    def capturar_cita(self):
        print("\n--- Registrar nueva cita ---")
        try:
            cedula = input("Cédula: ").strip()
            nombre = input("Nombre: ").strip()
            telefono = input("Teléfono: ").strip()
            tipo_cliente = input("Tipo de cliente (Particular/EPS/Prepagada): ").strip()
            tipo_atencion = input("Tipo de atención (Limpieza/Calzas/Extracción/Diagnóstico): ").strip()
            prioridad = input("Prioridad (Normal/Urgente): ").strip()

            fecha = input("Fecha (YYYY-MM-DD): ").strip()
            if not fecha_valida(fecha):
                print("Fecha inválida.")
                return

            hora = input("Hora (HH:MM): ").strip()
            if not hora_valida(hora):
                print("Hora inválida.")
                return

            try:
                cantidad = int(input("Cantidad (solo si aplica, ej. calzas): ").strip())
            except:
                cantidad = 1

            cita = Cita(cedula, nombre, telefono, tipo_cliente,
                        tipo_atencion, prioridad, fecha, hora, cantidad)
            self.bd.append(cita)
            print("Cita registrada.")
        except:
            print("No se pudo registrar la cita.")

    def listar_citas(self):
        print("\n--- Listar citas ---")
        if len(self.bd) == 0:
            print("No hay citas.")
            return
        i = 1
        for c in self.bd:
            print(str(i)+".", c.fecha, c.hora, "-", c.nombre, "-", c.tipo_atencion, "-", c.prioridad)
            i = i + 1

    def generar_cola_urgencias(self):
        self.urgencias.generar(self.bd)

    def ver_cola_urgencias(self):
        self.urgencias.ver()

    def llamar_siguiente_urgencia(self):
        self.urgencias.llamar_siguiente()

    def generar_cola_agenda_por_fecha(self):
        fecha_txt = input("Fecha para la agenda (YYYY-MM-DD): ").strip()
        self.agenda.generar_por_fecha(self.bd, fecha_txt)

    def ver_cola_agenda(self):
        self.agenda.ver()

    def atender_siguiente_agenda(self):
        self.agenda.atender_siguiente()

    def menu(self):
        while True:
            print("\n=== MENU ===")
            print("1. Registrar cita")
            print("2. Listar citas")
            print("3. Generar COLA URGENCIAS (Extracción + Urgente)")
            print("4. Ver COLA URGENCIAS")
            print("5. Llamar siguiente URGENCIAS")
            print("6. Generar COLA AGENDA por fecha")
            print("7. Ver COLA AGENDA")
            print("8. Atender siguiente AGENDA")
            print("9. Cargar ejemplos (opcional)")
            print("0. Salir")

            op = input("Opción: ").strip()

            if op == "1":
                self.capturar_cita()
            elif op == "2":
                self.listar_citas()
            elif op == "3":
                self.generar_cola_urgencias()
            elif op == "4":
                self.ver_cola_urgencias()
            elif op == "5":
                self.llamar_siguiente_urgencia()
            elif op == "6":
                self.generar_cola_agenda_por_fecha()
            elif op == "7":
                self.ver_cola_agenda()
            elif op == "8":
                self.atender_siguiente_agenda()
            elif op == "0":
                print("Chao.")
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    pacientes = [
            Cita("111","Marta Díaz","3001111111","Particular","Extracción","Urgente","2025-09-14","08:30",1),
            Cita("222","Juan Pérez","3002222222","EPS","Extracción","Urgente","2025-09-15","09:00",1),
            Cita("333","Ana Gómez","3003333333","Prepagada","Limpieza","Normal","2025-09-14","10:00",1),
            Cita("444","Luis Rojas","3004444444","Particular","Extracción","Normal","2025-09-14","11:00",1),
            Cita("555","Carlos Ruiz","3005555555","Prepagada","Extracción","Urgente","2025-09-16","08:00",1)
    ]

    prueba = SistemaConsultorio(pacientes)
    prueba.menu()