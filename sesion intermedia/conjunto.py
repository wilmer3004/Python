# Creamos un conjunto con set para identificar que estos son iterables
conjunto = set(["dato 1","dato2"])

# Mostramos resultados
print(conjunto)

# Un conjunto dentro de otro conjunto al congelar el conjunto1  
conjunto1 = frozenset({"dato 1","dato2"})
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)



# Teoría de conjuntos
# Esta se basa en agarrar datos de un subconjunto de un supercojunto

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# Verificando si es un subconjunto
# resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1
print(resultado)

# Verificando si es un supercojunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1
print(resultado)

# Verificar si hay algún resultado en común

resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)

