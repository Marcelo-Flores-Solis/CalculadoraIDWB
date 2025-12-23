# import
import sys
import os
import re
import urllib.parse

# Reemplazo del cgitb
def imprimir_error(e):
    print("Content-Type: text/html\n")
    print(f"<h2>Error en el servidor: {e}</h2>")
    sys.exit()

print("Content-Type: text/html\n") 

# Obtener datos 
try:
    # cantidad de datos enviados
    longitud = int(os.environ.get('CONTENT_LENGTH', 0))
    # leer datos crudos
    datos_crudos = sys.stdin.read(longitud)
    # codficar datos para un diccionario
    datos_parseados = urllib.parse.parse_qs(datos_crudos)
    
    operacion_raw = datos_parseados.get("operacion", [""])[0]
except Exception as e:
    imprimir_error(e)

# Este Regex valida que la cadena SOLO contenga:

patron_seguro = r"^[0-9\+\-\*/\.\(\)\s]+$"


resultado_html = ""

if re.match(patron_seguro, operacion_raw):
    try:
        # Usamos eval() de forma segura tras la validación del Regex.
        res = eval(operacion_raw)
        
        if isinstance(res, float):
            res = round(res, 4)
            
        resultado_html = f"<h2>Resultado: {res}</h2>"
    
    except ZeroDivisionError:
        resultado_html = "<h2 style='color:red;'>Error: no existe division por 0</h2>"
    except Exception:
        resultado_html = "<h2 style='color:red;'>Error: Expresion invalida</h2>"
else:
    resultado_html = "<h2 style='color:red;'>Formato no valido</h2>"

# Generar respuesta HTML

print(f"""
<!DOCTYPE html>
<html>
<head>
    <title>Resultado</title>
    <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
    <div class="container result-card">
        <h1>Procesamiento </h1>
        <p>Entrada recibida: <strong>{operacion_raw}</strong></p>
        
        <div class="result-value">
            {resultado_html}
        </div>

        <br>
        <a href="../html/index.html">Volver a calcular</a>
    </div>
</body>
</html>
""")



