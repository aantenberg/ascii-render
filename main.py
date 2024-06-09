import math
from animation import animation
from scene import scene
from vec3 import vec3

def physics_scene_generator(fps):
  WIDTH = 64
  HEIGHT = 64
  epsilon = 3

  gravity = vec3(0, 100, 0)

  sphere_velocity = vec3(5, 0, 0)
  sphere_pos = vec3(WIDTH // 2, HEIGHT // 2, 0)
  sphere_rad = 10

  prev_sphere_pos = sphere_pos.clone()
  equal_count = 0

  s = scene(WIDTH, HEIGHT)
  s.set_light_pos(vec3(WIDTH // 2 + 5, HEIGHT // 2 - 5, sphere_rad + 5))
  s.set_light_intensity(10)
  s.set_light_visible(False)

  while equal_count < fps:
    if prev_sphere_pos == sphere_pos:
      equal_count += 1
    else:
      equal_count = 0
    prev_sphere_pos = sphere_pos.clone()
    s.clear_objs()
    s.add_sphere(sphere_pos, sphere_rad)
    yield s

    sphere_velocity += (gravity / fps)
    sphere_pos += (sphere_velocity / fps)
    if (sphere_pos.y > HEIGHT - sphere_rad):
      sphere_velocity.y *= -0.9
      sphere_pos.y = HEIGHT - sphere_rad

    if (sphere_pos.x > WIDTH - sphere_rad):
      sphere_velocity.x *= -0.8
      sphere_pos.x = WIDTH - sphere_rad
      if abs(sphere_velocity.x) < epsilon:
        sphere_velocity.x = 0

    if (sphere_pos.x < sphere_rad):
      sphere_velocity.x *= -0.8
      sphere_pos.x = sphere_rad
      if abs(sphere_velocity.x) < epsilon:
        sphere_velocity.x = 0


def moving_light_scene_generator():
  num_frames = 24 * 5
  s = scene(64, 64)
  s.add_sphere(vec3(32, 32, 0), 10)
  s.set_light_info(vec3(0, 32, 0), 1.5)


  theta = 0
  angle_per_frame = math.pi / num_frames
  x = 0
  y = 0
  z = 12
  for _ in range(num_frames):
    yield s
    theta += angle_per_frame
    x += 64 / num_frames
    y += 16 / num_frames
    s.set_light_pos(vec3(x, y, z))


if __name__ == '__main__':
  fps = 24
  # generator = physics_scene_generator(fps)
  generator = moving_light_scene_generator()
  anim = animation(generator, fps)
  anim.play()