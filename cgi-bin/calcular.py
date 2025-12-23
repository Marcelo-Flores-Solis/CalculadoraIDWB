# import
import cgi
import re
import cgitb

# habilitar el modo de depuración
cgitb.enable()
print("Content-Type: text/html\n") 

# expresiones regulares
# parentesis opcionales: \(? ... \)?
# operadores permitidos: [\+\-\*\/]
# operandos (\d+\.?\d*)

