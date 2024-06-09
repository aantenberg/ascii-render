import math

class vec3:
  def __init__(self, x: float, y: float = None, z: float = None):
    if z is None:
      z = x
    if y is None:
      y = x
    
    self.x = x
    self.y = y
    self.z = z

  def __repr__(self):
    return f'({self.x}, {self.y}, {self.z})'

  def length(self):
    return math.sqrt(self.sqrlen())
  
  def sqrlen(self):
    return self.x ** 2 + self.y ** 2 + self.z ** 2
  
  def __add__(self, other):
    return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
  
  def __sub__(self, other):
    return self + (other * -1)
  
  def __truediv__(self, num : float):
    return vec3(self.x / num, self.y / num, self.z / num)
  
  def __mul__(self, num: float):
    return vec3(self.x * num, self.y * num, self.z * num)
  
  def __iadd__(self, other):
    self.x += other.x
    self.y += other.y
    self.z += other.z
    return self
  
  def __isub__(self, other):
    self.x -= other.x
    self.y -= other.y
    self.z -= other.z
    return self

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y and self.z == other.z
  
  def __neq__(self, other):
    return not self == other
  
  def normalized(self):
    return self / self.length()
  
  def dot(self, other):
    return self.x * other.x + self.y * other.y + self.z * other.z
  
  def clone(self):
    return vec3(self.x, self.y, self.z)
  
  def dist(self, other):
    return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)