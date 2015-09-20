import os

import pyglet
from pyglet import gl

import settings

# should be called get texture!!!
def get_sprite(filename):
    image = pyglet.image.load(os.path.join('sprites', filename))
    texture = image.get_texture()
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
    texture.width = texture.width * settings.scale
    texture.height = texture.height * settings.scale
    return texture

# this is most likely the way to get if one wants to rotate the bird
# this is based on brief exploration of texture and sprit object
# namely sprit object (image object) has rotation that is not limited to full 
# 90 degree rotation like texture object
# should be checked further on
def get_sprite_for_real(filename):
    image = pyglet.image.load(os.path.join('sprites', filename))
    return sprite

class BBox(object):
    def __init__(self, x, y, dx, dy):
        self.xmin = x
        self.xmax = x + dx
        self.ymin = y
        self.ymax = y + dy


def check_collision(a, b):
    for b1 in a.bboxes:
        for b2 in b.bboxes:
            if b1.xmax < b2.xmin or b1.xmin > b2.xmax or b1.ymax < b2.ymin or b1.ymin > b2.ymax:
                continue
            else:
                return True
