import time

class animation:
  def __init__(self, scene_generator, fps=24):
    self.scene_generator = scene_generator
    self.fps = fps

  def play(self):
    delta_t = 1 / self.fps
    for scene in self.scene_generator:
      scene.render()
      time.sleep(delta_t)
      # Reset the cursor to the left (each char is space-separated, so we move width * 2 - 1 spaces left)
      print(f'\x1b[{scene.width * 2 - 1}D')
      # Reset the cursor to the top
      print(f'\x1b[{scene.height}A')
