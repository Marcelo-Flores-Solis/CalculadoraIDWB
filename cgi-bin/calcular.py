# import
import cgi
import re
import cgitb

# habilitar el modo de depuración
cgitb.enable()
print("Content-Type: text/html\n") 

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



