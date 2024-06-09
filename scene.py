import math
from vec3 import vec3

def empty(width, height):
  return [[None for _ in range(width)] for _ in range(height)]


def clamp(v, low, high):
  return max(low, min(v, high))

class light:
  def __init__(self, pos, intensity, visible_point=True):
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
  
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.clear_objs()
    self.clear_light()
  
  def add_sphere(self, center, radius):
    cx, cy  = center.x, center.y
    top_left_x, top_left_y = cx - radius, cy - radius
    bottom_right_x, bottom_right_y = cx + radius, cy + radius
    for x in range(max(int(top_left_x), 0), min(int(bottom_right_x) + 1, self.width)):
      for y in range(max(int(top_left_y), 0), min(int(bottom_right_y) + 1, self.height)):
        pixel_center_x, pixel_center_y = x + 0.5, y + 0.5
        sqr_dist = (pixel_center_x - cx) ** 2 + (pixel_center_y - cy) ** 2
        if (sqr_dist < radius ** 2):
          z = math.sqrt((radius ** 2) - sqr_dist)
          self.zs[y][x] = z
          self.normals[y][x] = vec3(pixel_center_x - cx, pixel_center_y - cy, z).normalized()

  def set_light_info(self, pos, intensity):
    self.light = light(pos, intensity)

  def add_light(self, light):
    self.light = light

  def set_light_pos(self, p):
    self.light.pos = p

  def set_light_intensity(self, i):
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
