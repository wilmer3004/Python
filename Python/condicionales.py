# Las condicionales son las encargadas de que se ejecute un código dependiendo de si se cumple la condición

# if else

edad = 19
if edad  >= 18:
    print("Podes pasar")
else:
    print("No podes pasar")

print("No forma parte de ninguna condición")
# Esto sucede por que python es un lenguaje identado
contraseña = "Wilmer"
contraseña_usuario ="Wilmer"
if contraseña == contraseña_usuario:
    print("Se inicio sesión")
else:
    print("No se puede iniciar sesión")

# elif

ingreso_mensual = 200

if ingreso_mensual>10000:
    print("Estas bien en cualquier parte del mundo")
    
elif ingreso_mensual>1000:
    print("Estas bien en Latinoamérica")
elif ingreso_mensual>500:
    print("Estas bien en Argentina")
elif ingreso_mensual>200:
    print("Estas bien en Venezuela")
    
else:
    print("Sos pobre")
    
# if 




