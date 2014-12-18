import gizeh
import moviepy.editor as mpy
import numpy as np

width,height = 130, 130 # Width and height in pixels
duration = 2 # duration of the clip in seconds
number_of_circles = 20

def make_frame(t):

    surface = gizeh.Surface(width, height)

    for i in range(number_of_circles):
        angle = 2 * np.pi  * (1.0 *i / number_of_circles + t / duration)
        radius = width * (1.0-1.0 * i / number_of_circles)
        center = width *( 0.5 + gizeh.polar2cart(0.1,angle))
        circle = gizeh.circle(radius, xy = center ,fill=(i%2,i%2,i%2))
        circle.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration = duration)
clip.write_gif("./circle.gif", fps=15, opt = "OptimizePlus", fuzz = 10)
