
class Point:
    # Static counter to track getter calls
    _getter_count = 0
    
    def __init__(self, x, y):
      # Alusta piste x- ja y-koordinaateilla
        self._x = float(x)  # We use _x and _y as private attributes
        self._y = float(y)
    
    @property
    def x(self):
      # Ominaisuus x:lle: lisää laskuria luettaessa
        Point._getter_count += 1
        return self._x
    
    @x.setter
    def x(self, value):
       # Setteri x:lle: sallii kirjoittamisen
        self._x = float(value)
    
    @property
    def y(self):
    # Ominaisuus y:lle: lisää laskuria luettaessa
        Point._getter_count += 1
        return self._y
    
    @y.setter
    def y(self, value):
        # Setter for y: sallii kirjoittamisen
        self._y = float(value)
    
    def get_x(self):
      # Palauttaa x-koordinaatin (lisää myös laskuria ominaisuuden kautta)
        return self.x
    
    def get_y(self):
        # Palauttaa y-koordinaatin (lisää myös laskuria ominaisuuden kautta)
        return self.y
    
    @classmethod
    def getter_count(cls):
       # Palauttaa kuinka monta kertaa getteriä on kutsuttu
        return cls._getter_count
    
    def __str__(self):
     # Pisteen merkkijonoesitys
        return f"Point({self._x}, {self._y})"

# Test program
if __name__ == "__main__":
    # Counter initial test
    print(f"Initial value of Point.getter_count()=={Point.getter_count()}")
    assert Point.getter_count() == 0

    # Create the points that the test expects
    points = []
    coords = [(-1, 2), (3, 4), (-3, -4), (0.122, 0.2112), (0.111, -277272.272)]
    for coord in coords:
        points.append(Point(coord[0], coord[1]))
        print(f"Point{coord[0], coord[1]} created")

    # Run the tests that the test expects
    earlier_getter_count = Point.getter_count()
    for p, c in zip(points, coords):
        print(32 * '-')
        pstr = f"Point({c[0]}, {c[1]})"
        print(f"Test {pstr}")
        
        # Access to x
        a = p.x  # This should increment the counter
        assert Point.getter_count() >= (earlier_getter_count + 1)
        print(f"{pstr}: Accessing x increases Point.getter_count()")
        
        # Access to y
        b = p.y  # Tämän pitäisi kasvattaa laskuria
        assert Point.getter_count() >= (earlier_getter_count + 2)
        print(f"{pstr}: Accessing y increases Point.getter_count()")
        
        # Writing x and y
        p.x = -p.x
        p.y = -p.y
        assert p.x == (-c[0])
        assert p.y == (-c[1])
        print(f"{pstr}: Writing x and y values seems to work")
        
        # Verify that the counter does not increase without access
        earlier_getter_count = Point.getter_count()
        for _ in range(10):
            assert earlier_getter_count == Point.getter_count()
        print(f"{pstr}: Point.getter_count() not increasing when not read x or y.")
        
        print(f"Test {pstr} completed")
