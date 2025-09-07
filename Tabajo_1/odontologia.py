from datetime import datetime

# Valores de la odontogia

VALORES_CITA = {
    "Particular": 80000,
    "EPS": 5000,
    "Prepagada": 30000
}

PRECIOS_ATENCION = {
    "Particular": {
        "Limpieza": 60000,
        "Calzas": 80000,
        "Extracción": 100000,
        "Diagnóstico": 50000
    },
    "EPS": {
        "Limpieza": 0,
        "Calzas": 40000,
        "Extracción": 40000,
        "Diagnóstico": 0
    },
    "Prepagada": {
        "Limpieza": 0,
        "Calzas": 10000,
        "Extracción": 10000,
        "Diagnóstico": 0
    }
}

FORMATO_FECHA = "%Y-%m-%d"

# Clase principal donde se almacena datos de la cita
class Cita:
    def __init__(self, cedula, nombre, telefono, tipo_cliente,
                 tipo_atencion, cantidad, prioridad, fecha_cita):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.cantidad = cantidad
        self.prioridad = prioridad
        self.fecha_cita = fecha_cita

        self.valor_cita = VALORES_CITA[tipo_cliente]
        self.valor_unitario = PRECIOS_ATENCION[tipo_cliente][tipo_atencion]
        self.subtotal = self.valor_unitario * self.cantidad
        self.total_pagar = self.valor_cita + self.subtotal

# Funcion que ayudara a recolectar los datos

def capturar_cita():
    print("\n--- Registrar nueva cita ---")
    cedula = input("Cédula: ")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")

    print("Tipo de cliente (Particular, EPS, Prepagada)")
    tipo_cliente = input("=> ")

    print("Tipo de atención (Limpieza, Calzas, Extracción, Diagnóstico)")
    tipo_atencion = input("=> ")

    if tipo_atencion in ("Limpieza", "Diagnóstico"):
        cantidad = 1
    else:
        cantidad = int(input("Cantidad: "))

    print("Prioridad (Normal, Urgente)")
    prioridad = input("=> ")

    fecha_cita = input("Fecha de la cita (YYYY-MM-DD): ")
    fecha_cita = datetime.strptime(fecha_cita, FORMATO_FECHA)

    cita = Cita(cedula, nombre, telefono, tipo_cliente,
                tipo_atencion, cantidad, prioridad, fecha_cita)
    return cita

# funcion que lista las citas

def listar_citas(citas):
    for c in citas:
        print(f"\nCliente: {c.nombre} - Cédula: {c.cedula}")
        print(f"Atención: {c.tipo_atencion} x{c.cantidad} | Cliente: {c.tipo_cliente}")
        print(f"Valor cita: {c.valor_cita} | Subtotal atención: {c.subtotal}")
        print(f"TOTAL a pagar: {c.total_pagar}")
        print("-" * 40)

# funcion que recolecta total clientes, ingresos y total de extracciones

def calcular_resumen(citas):
    total_clientes = len(citas)
    ingresos = sum(c.total_pagar for c in citas)
    extracciones = sum(1 for c in citas if c.tipo_atencion == "Extracción")
    print("\n--- Resumen ---")
    print("Total clientes:", total_clientes)
    print("Ingresos totales:", ingresos)
    print("Clientes para extracción:", extracciones)

# funcio que ordena las citas por precio de mayor a menor
def ordenar_por_valor(citas):
    return sorted(citas, key=lambda c: c.total_pagar, reverse=True)

# funcion para buscar citas por cedula

def buscar_cedula(citas, cedula):
    for c in citas:
        if c.cedula == cedula:
            return c
    return None

# --------------- menú principal -----------------------------

def menu():
    citas = []
    while True:
        print("\n=== MENU ===")
        print("1. Registrar nueva cita")
        print("2. Listar citas")
        print("3. Ver totales")
        print("4. Ordenar por valor")
        print("5. Buscar por cédula")
        print("0. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            cita = capturar_cita()
            citas.append(cita)
        elif opcion == "2":
            listar_citas(citas)
        elif opcion == "3":
            calcular_resumen(citas)
        elif opcion == "4":
            citas = ordenar_por_valor(citas)
            print("Se ordenaron las citas de mayor a menor valor.")
        elif opcion == "5":
            ced = input("Ingrese la cédula a buscar: ")
            encontrado = buscar_cedula(citas, ced)
            if encontrado:
                print("Cliente encontrado:", encontrado.nombre, "-", encontrado.total_pagar)
            else:
                print("No se encontró esa cédula.")
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()