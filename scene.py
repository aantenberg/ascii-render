import math
from vec3 import vec3

def empty(width: int, height: int):
  return [[None for _ in range(width)] for _ in range(height)]

def clamp(v, low, high):
  return max(low, min(v, high))

class light:
  def __init__(self, pos: vec3, intensity: float, visible_point: bool = True):
    self.pos = pos
    self.intensity = intensity
    self.visible_point = visible_point

  def __repr__(self):
    return f'{self.pos=}, {self.intensity=}'
  

class scene:
  def clear_objs(self):
    self.zs = empty(self.width, self.height)
    self.normals = empty(self.width, self.height)
  
  def clear_light(self):
    self.light = light(vec3(0), 0)

  @staticmethod
  def empty(width: int, height: int):
    return scene(width, height)
  
  def __init__(self, width: int, height: int):
    self.width = width
    self.height = height
    self.clear_objs()
    self.clear_light()

  
  # TODO: Add vec2 to use here?
  def add_sphere(self, center: vec3, radius: int):
    cx, cy  = center.x, center.y
    top_left_x, top_left_y = max(cx - radius, 0), max(cy - radius, 0)
    bottom_right_x, bottom_right_y = min(cx + radius + 1, self.width), min(cy + radius + 1, self.height)
    for x in range(top_left_x, bottom_right_x):
      for y in range(top_left_y, bottom_right_y):
        pixel_center_x, pixel_center_y = x + 0.5, y + 0.5
        sqr_dist = (pixel_center_x - cx) ** 2 + (pixel_center_y - cy) ** 2
        if (sqr_dist < radius ** 2):
          z = math.sqrt((radius ** 2) - sqr_dist)
          self.zs[y][x] = z
          self.normals[y][x] = vec3(pixel_center_x - cx, pixel_center_y - cy, z).normalized()


  def set_light_info(self, pos: vec3, intensity: float):
    self.light = light(pos, intensity)

  def add_light(self, light: light):
    self.light = light

  def set_light_pos(self, p: vec3):
    self.light.pos = p

  def set_light_intensity(self, i: float):
    self.light.intensity = i

  def render(self):
    lightnesses = '.,-:;<!*0@'
    for y in range(len(self.zs)):
      for x in range(len(self.zs[y])):
        if self.light.visible_point and self.light.pos.x == x and self.light.pos.y == y:
          print('💡', end='')
        else:
          z = self.zs[y][x]
          if z is not None:
            pos = vec3(x, y, z)
            l = (self.light.pos - pos).normalized()
            
            normal = self.normals[y][x]
            brightness = clamp(normal.dot(l) * self.light.intensity, 0, 0.99)
            
            idx = math.floor(brightness * len(lightnesses))
            print(lightnesses[idx], end=' ')
          else:
            print('  ', end='')
      print()
