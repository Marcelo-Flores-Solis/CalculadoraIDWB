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

# expresiones regulares
# parentesis opcionales: \(? ... \)?
# operadores permitidos: ([\+\-\*/])
# operandos (\d+\.?\d*)
# espacios opcionales: \s*
# primer y tercer bloque : \s* \(? \s* (\d+\.?\d*) \s* \)? \s*
# segundo bloque: ([\+\-\*/])

pattern = r"^\s*\(?\s*(\d+\.?\d*)\s*\)?\s*([\+\-\*/])\s*\(?\s*(\d+\.?\d*)\s*\)?\s*$"

match = re.match(pattern, operacion_raw)

resultado_html = ""

if match:
    op1 = float(match.group(1))
    operador = match.group(2)
    op2 = float(match.group(3))
    
    try:
        if operador == '+':
            res = op1 + op2
        elif operador == '-':
            res = op1 - op2
        elif operador == '*':
            res = op1 * op2
        elif operador == '/':
            if op2 != 0:
                res = op1 / op2
            else:
                res = "Error: División por cero"

        resultado_html = f"<h2>Resultado: {res}</h2>"
    
    except Exception as e:
        resultado_html = f"<h2>Error en el cálculo: {str(e)}</h2>"
else:
    resultado_html = "<h2 style='color:red;'>Formato de operación no válido</h2>"

# Generar respuesta HTML

# Generar respuesta
print(f"""
<!DOCTYPE html>
<html>
<head>
      <title>Resultado</title>
      <link rel="stylesheet" href="../css/styles.css">
</head>
      
<body>
    <div style="text-align:center; margin-top:50px;">
        <h1>Procesamiento de Operación</h1>
        <p>Entrada recibida: <strong>{operacion_raw}</strong></p>
        {resultado_html}
        <br>
        <a href="../html/index.html">Volver a calcular</a>
    </div>
</body>
</html>
""")



