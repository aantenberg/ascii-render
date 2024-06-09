import math
import time
from vec3 import vec3

WIDTH = 64
HEIGHT = 64

def empty():
  return [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

def clamp(v, low, high):
  return max(low, min(v, high))

def normalize(x, y, z):
  l = math.sqrt(x ** 2 + y ** 2 + z ** 2)
  return x / l, y / l, z / l


def sphere(depths, normals, center, radius):
  cx, cy  = center.x, center.y
  top_left_x, top_left_y = cx - radius, cy - radius
  bottom_right_x, bottom_right_y = cx + radius, cy + radius
  for x in range(max(int(top_left_x), 0), min(int(bottom_right_x) + 1, WIDTH)):
    for y in range(max(int(top_left_y), 0), min(int(bottom_right_y) + 1, HEIGHT)):
      pixel_center_x, pixel_center_y = x + 0.5, y + 0.5
      sqr_dist = (pixel_center_x - cx) ** 2 + (pixel_center_y - cy) ** 2
      if (sqr_dist < radius ** 2):
        z = math.sqrt((radius ** 2) - sqr_dist)
        depths[y][x] = z
        normals[y][x] = vec3(pixel_center_x - cx, pixel_center_y - cy, z).normalized()

def render(depths, normals):

  intensity = 1

  LIGHT_POS = vec3(WIDTH // 2 + 5, HEIGHT // 2 - 7, 7)

  lightnesses = '.,-:;<!*0@'
  for y in range(len(depths)):
    for x in range(len(depths[y])):
      z = depths[y][x]
      if z is not None:
        pos = vec3(x, y, z)
        l = (LIGHT_POS - pos).normalized()
        
        normal = normals[y][x]
        brightness = clamp(normal.dot(l) * intensity, 0, 0.99)
        
        idx = math.floor(brightness * len(lightnesses))
        print(lightnesses[idx], end=' ')
      else:
        print('  ', end='')
    print()

def main():
  fps = 24
  delta_t = 1 / fps

  epsilon = 3

  gravity = vec3(0, 100, 0)

  v = vec3(5, 0, 0)

  sphere_rad = 6
  sphere_pos = vec3(WIDTH // 2, HEIGHT // 2, 0)

  prev = sphere_pos.clone()
  equal_count = 0

  while equal_count < fps:
    if prev == sphere_pos:
      equal_count += 1
    else:
      equal_count = 0
    prev = sphere_pos.clone()
    depths = empty()
    normals = empty()
    sphere(depths, normals, sphere_pos, sphere_rad)
    render(depths, normals)
    time.sleep(delta_t)
    print(f'\x1b[{WIDTH * 2}D')
    print(f'\x1b[{HEIGHT + 2}A')
    v += (gravity * delta_t)
    sphere_pos += (v * delta_t)
    if (sphere_pos.y > HEIGHT - sphere_rad):
      v.y *= -0.9
      sphere_pos.y = HEIGHT - sphere_rad

    if (sphere_pos.x > WIDTH - sphere_rad):
      v.x *= -0.8
      sphere_pos.x = WIDTH - sphere_rad
      if abs(v.x) < epsilon:
        v.x = 0

    if (sphere_pos.x < sphere_rad):
      v.x *= -0.8
      sphere_pos.x = sphere_rad
      if abs(v.x) < epsilon:
        v.x = 0


if __name__ == '__main__':
  main()