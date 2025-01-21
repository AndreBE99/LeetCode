# Tablas hash
# Ejemplo 1
# Uso de un diccionario para implementar una tabla hash simple:
hash_table = {}

# Insert
hash_table["key1"] = "value1"
hash_table["key2"] = "value2"

# Access
print(hash_table["key1"])  # Output: value1

# Delete
del hash_table["key2"]

# Ejemplo 2
# Crear un diccionario
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Acceder a un valor
print(persona["nombre"])  # 'Ana'

# Agregar o actualizar un par clave-valor
persona["edad"] = 26
print(persona)  # {'nombre': 'Ana', 'edad': 26, 'ciudad': 'Madrid'}

# Eliminar un par clave-valor
del persona["ciudad"]
print(persona)  # {'nombre': 'Ana', 'edad': 26}
