import math

class Point:
     #Toteuta luokka tässä
    _getter_count = 0
    
    def __init__(self, x, y):
        """Alustaa pisteen x- ja y-koordinaateilla"""
        self._x = float(x)
        self._y = float(y)
    
    @property
    def x(self):
        """Ominaisuus x:lle: kasvattaa laskuria luettaessa"""
        Point._getter_count += 1
        return self._x
    
    @x.setter
    def x(self, value):
        """Asetin x:lle: sallii kirjoittamisen"""
        self._x = float(value)
    
    @property
    def y(self):
        """Ominaisuus y:lle: kasvattaa laskuria luettaessa"""
        Point._getter_count += 1
        return self._y
    
    @y.setter
    def y(self, value):
        """Asetin y:lle: sallii kirjoittamisen"""
        self._y = float(value)
    
    def get_x(self):
        """Palauttaa x-koordinaatin"""
        return self.x
    
    def get_y(self):
        """Palauttaa y-koordinaatin"""
        return self.y
    
    @classmethod
    def getter_count(cls):
        """Palauttaa kuinka monta kertaa gettereitä on kutsuttu"""
        return cls._getter_count
    
    @classmethod
    def closest(cls, points):
        """Palauttaa lähimmän pisteen etäisyyden origoon"""
        if not points:
            return 0.0
        return min(math.sqrt(p.x**2 + p.y**2) for p in points)
    
    def __str__(self):
        """Pisteen merkkijonoesitys"""
        return f"Point({self._x}, {self._y})"

if __name__ == "__main__":

    print(f"Point.getter_count() alkuperäinen arvo=={Point.getter_count()}")
    assert Point.getter_count() == 0

    points = []
    coords = [(-1, 2), (3, 4), (-3, -4), (0.122, 0.2112), (0.111, -277272.272)]
    for coord in coords:
        points.append(Point(coord[0], coord[1]))
        print(f"Point({coord[0]}, {coord[1]}) luotu")

    earlier_getter_count = Point.getter_count()
    for p, c in zip(points, coords):
        print(32 * '-')
        pstr = f"Point({c[0]}, {c[1]})"
        print(f"Testi {pstr}")
        
        a = p.x
        assert Point.getter_count() >= (earlier_getter_count + 1)
        print(f"{pstr}: x:n käyttö kasvattaa Point.getter_count()")
        
        b = p.y
        assert Point.getter_count() >= (earlier_getter_count + 2)
        print(f"{pstr}: y:n käyttö kasvattaa Point.getter_count()")
        
        p.x = -p.x
        p.y = -p.y
        assert p.x == (-c[0])
        assert p.y == (-c[1])
        print(f"{pstr}: x- ja y-arvojen kirjoittaminen toimii")
        

        earlier_getter_count = Point.getter_count()
        for _ in range(10):
            assert earlier_getter_count == Point.getter_count()
        print(f"{pstr}: Point.getter_count() ei kasva kun x tai y ei lueta.")
        
        print(f"Testi {pstr} valmis")

    
    for i in range(len(points)):
        p_closest_dist = Point.closest(points)
        print('Lähimmän pisteen etäisyys O:hon on %0.2f' % (p_closest_dist))
        points.pop(0)