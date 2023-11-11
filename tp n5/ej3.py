from datetime import datetime

def obtener_fecha_y_hora_actuales():
    ahora = datetime.now()

    formato = "%Y-%m-%d %H:%M:%S"

    fecha_y_hora_formateadas = ahora.strftime(formato)

    return fecha_y_hora_formateadas


fecha_y_hora_actuales = obtener_fecha_y_hora_actuales()

print("Fecha y hora actuales:", fecha_y_hora_actuales)
