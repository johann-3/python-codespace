#capturar excepsiones y manejar errores en codigo
#suceptible a fallas/errores
"""
try:
    nombre = input("¿cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "el nombre es " + nombre

    print(nombre_usuario)
except:
    print("ha ocurrido un error ingresa bien el nombre")
else:
    print("todo ha funcionado correctamente")
finally:
    print("fin de la iteracion")
"""


#multiples excepcionse 
"""
try:
    numero = int(input("ingresa un numero para elevarlo al cuadrado: "))
    print("el cuadrado del numero es: " + str(numero * numero))
except TypeError:
    print("debes convertir los str a int en tu codigo")
#except ValueError:
   # print("introduce un numero correcto")
except Exception as e:
    print(type(e))
    print("ha ocurrido un error: ", type(e).__name__)
"""

#excepciones personalizadaas
try:
    nombre = input("introduce un nombre: ")
    edad = int(input("introduce tu edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("la edad igresada no es real")
    elif len(nombre) <= 1:
        raise ValueError("el nombre no es correcto no esta completo")
    else:
        print(f"bienvenido al master en python {nombre}")
except ValueError:
    print("introduce los datos correctamente")
except Exception as e:
    print("exise un error")

