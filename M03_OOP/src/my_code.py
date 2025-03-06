"""class Point:
    #Implement the class here
    
#Write test software under this if
if __name__ == "__main__":
    pass
"""
class Point:
    # Contador estático para rastrear las llamadas a los getters
    _getter_count = 0
    
    def __init__(self, x, y):
        """Inicializa un punto con coordenadas x e y"""
        self._x = float(x)  # Usamos _x y _y como atributos privados
        self._y = float(y)
    
    @property
    def x(self):
        """Propiedad para x: incrementa el contador al leer"""
        Point._getter_count += 1
        return self._x
    
    @x.setter
    def x(self, value):
        """Setter para x: permite escritura"""
        self._x = float(value)
    
    @property
    def y(self):
        """Propiedad para y: incrementa el contador al leer"""
        Point._getter_count += 1
        return self._y
    
    @y.setter
    def y(self, value):
        """Setter para y: permite escritura"""
        self._y = float(value)
    
    def get_x(self):
        """Devuelve la coordenada x (también incrementa el contador vía propiedad)"""
        return self.x
    
    def get_y(self):
        """Devuelve la coordenada y (también incrementa el contador vía propiedad)"""
        return self.y
    
    @classmethod
    def getter_count(cls):
        """Devuelve el número de veces que se han llamado los getters"""
        return cls._getter_count
    
    def __str__(self):
        """Representación en string del punto"""
        return f"Point({self._x}, {self._y})"

# Programa de prueba
if __name__ == "__main__":
    # Test inicial del contador
    print(f"Initial value of Point.getter_count()=={Point.getter_count()}")
    assert Point.getter_count() == 0

    # Crear los puntos que el test espera
    points = []
    coords = [(-1, 2), (3, 4), (-3, -4), (0.122, 0.2112), (0.111, -277272.272)]
    for coord in coords:
        points.append(Point(coord[0], coord[1]))
        print(f"Point{coord[0], coord[1]} created")

    # Ejecutar las pruebas que el test espera
    earlier_getter_count = Point.getter_count()
    for p, c in zip(points, coords):
        print(32 * '-')
        pstr = f"Point({c[0]}, {c[1]})"
        print(f"Test {pstr}")
        
        # Acceso a x
        a = p.x  # Esto debería incrementar el contador
        assert Point.getter_count() >= (earlier_getter_count + 1)
        print(f"{pstr}: Accessing x increases Point.getter_count()")
        
        # Acceso a y
        b = p.y  # Esto debería incrementar el contador
        assert Point.getter_count() >= (earlier_getter_count + 2)
        print(f"{pstr}: Accessing y increases Point.getter_count()")
        
        # Escritura de x e y
        p.x = -p.x
        p.y = -p.y
        assert p.x == (-c[0])
        assert p.y == (-c[1])
        print(f"{pstr}: Writing x and y values seems to work")
        
        # Verificar que el contador no aumenta sin acceso
        earlier_getter_count = Point.getter_count()
        for _ in range(10):
            assert earlier_getter_count == Point.getter_count()
        print(f"{pstr}: Point.getter_count() not increasing when not read x or y.")
        
        print(f"Test {pstr} completed")