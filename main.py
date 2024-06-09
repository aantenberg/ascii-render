from scene import scene
import time
from vec3 import vec3

# TODO: Add types to all functions
def main():
  WIDTH = 64
  HEIGHT = 64

  fps = 24
  delta_t = 1 / fps
  epsilon = 3

  gravity = vec3(0, 100, 0)

  v = vec3(5, 0, 0)
  sphere_rad = 10
  sphere_pos = vec3(WIDTH // 2, HEIGHT // 2, 0)

  prev = sphere_pos.clone()
  equal_count = 0

  s = scene(WIDTH, HEIGHT)
  s.set_light_pos(vec3(WIDTH // 2 + 5, HEIGHT // 2 - 5, sphere_rad + 5))
  s.set_light_intensity(10)

  while equal_count < fps:
    if prev == sphere_pos:
      equal_count += 1
    else:
      equal_count = 0
    prev = sphere_pos.clone()
    s.clear_objs()
    s.add_sphere(sphere_pos, sphere_rad)
    s.render()
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