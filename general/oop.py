# Programacion orientada a objetos
class Libro:
  def __init__(self, titulo, autor, anio_publicacion, isbn):
    self.titulo = titulo
    self.autor = autor
    self.anio_publicacion = anio_publicacion
    self.isbn = isbn

class Biblioteca:
  def __init__(self):
    self.libros = []
    
  def agregar_libro(self, libro):
    self.libros.append(libro)
  
  def buscar_libro(self, titulo):
    for libro in self.libros:
      if libro.titulo == titulo:
        return libro
    return None


if __name__ == '__main__':
  # Crear instancias de libros
  libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605, "1234567890")
  libro2 = Libro("1984", "George Orwell", 1949, "0987654321")

  # Crear la biblioteca y agregar libros
  biblioteca = Biblioteca()
  biblioteca.agregar_libro(libro1)
  biblioteca.agregar_libro(libro2)

  # Buscar un libro por título
  resultado = biblioteca.buscar_libro("1984")
  if resultado:
      print(f"Libro encontrado: {resultado.titulo}, por {resultado.autor}")
  else:
      print("Libro no encontrado")

  # Listar todos los libros
  for libro in biblioteca.libros:
      print(f"{libro.titulo} - {libro.autor}")
