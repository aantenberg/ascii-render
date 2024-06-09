import math
from vec3 import vec3


def empty(width: int, height: int):
    return [[None for _ in range(width)] for _ in range(height)]

def clamp(v, low, high):
    return max(low, min(v, high))

class light:
    def __init__(self, pos: vec3, intensity: float, visible_point: bool = False):
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

    def __init__(self, width: int, height: int, darkmode=True, char_aspect_ratio=1/2):
        self.width = width
        self.height = height
        self.darkmode = darkmode
        self.char_aspect_ratio = char_aspect_ratio
        self.clear_objs()
        self.clear_light()

    # TODO: Add vec2 to use here?
    def add_sphere(self, center: vec3, radius: int):
        cx, cy = center.x, center.y
        top_left_x, top_left_y = max(cx - radius, 0), max(cy - radius, 0)
        bottom_right_x, bottom_right_y = min(
            cx + radius + 1, self.width), min(cy + radius + 1, self.height)
        for x in range(int(top_left_x), int(bottom_right_x)):
            for y in range(int(top_left_y), int(bottom_right_y)):
                pixel_center_x, pixel_center_y = x + 0.5, y + 0.5
                sqr_dist = (pixel_center_x - cx) ** 2 + \
                    (pixel_center_y - cy) ** 2
                if (sqr_dist < radius ** 2):
                    z = math.sqrt((radius ** 2) - sqr_dist)
                    self.zs[y][x] = z
                    self.normals[y][x] = vec3(
                        pixel_center_x - cx, pixel_center_y - cy, z).normalized()

    def set_light_info(self, pos: vec3 = vec3(0), intensity: float = 0, visible_point: bool = False):
        self.light = light(pos, intensity, visible_point)

    def add_light(self, light: light):
        self.light = light

    def set_light_pos(self, p: vec3):
        self.light.pos = p

    def set_light_intensity(self, i: float):
        self.light.intensity = i

    def set_light_visible(self, visible: bool):
        self.light.visible_point = visible

    def __text_at_point(self, x, y):
        light_pos = self.light.pos
        if self.light.visible_point and light_pos.x == x and light_pos.y == y:
            return '💡'
        z = self.zs[y][x]
        if z is None:
            return ' '
        lightnesses = '.,-:;<!*0@'[::-1 if not self.darkmode else 1]
        pos = vec3(x, y, z)
        l = (light_pos - pos).normalized()
        normal = self.normals[y][x]
        brightness = clamp(normal.dot(l) * self.light.intensity, 0, 0.99)
        idx = math.floor(brightness * len(lightnesses))
        return lightnesses[idx]

    def render(self):
        inverse_char_ar = 1 / self.char_aspect_ratio
        print(
            "\n".join(
                [(" " * int(inverse_char_ar - 1)).join(
                    [self.__text_at_point(x, y) for x in range(self.width)])
                for y in range(self.height)]
            )
        )
