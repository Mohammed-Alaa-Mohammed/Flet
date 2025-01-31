from skyfield.api import load
from datetime import datetime
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# تحميل بيانات الكواكب
planets = load('de421.bsp')
ts = load.timescale()
earth = planets['earth']
mars = planets['mars']

# إعدادات OpenGL
window_width = 800
window_height = 600
rotation_angle = 0

def calculate_planet_position(planet, time):
    position = planet.at(time).position.km
    return position[0] / 1e6, position[1] / 1e6, position[2] / 1e6

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

def draw_sphere(radius, slices, stacks):
    glutSolidSphere(radius, slices, stacks)

def draw_scene():
    global rotation_angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 30, 0, 0, 0, 0, 1, 0)

    # دوران بسيط لإظهار حركة الكواكب
    rotation_angle += 0.2
    glRotatef(rotation_angle, 0, 1, 0)

    # حساب المواقع الكوكبية
    now = ts.now()
    earth_pos = calculate_planet_position(earth, now)
    mars_pos = calculate_planet_position(mars, now)

    # رسم الأرض
    glPushMatrix()
    glColor3f(0.0, 0.0, 1.0)
    glTranslatef(earth_pos[0], earth_pos[1], earth_pos[2])
    draw_sphere(0.5, 20, 20)
    glPopMatrix()

    # رسم المريخ
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(mars_pos[0], mars_pos[1], mars_pos[2])
    draw_sphere(0.3, 20, 20)
    glPopMatrix()

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height, 1, 100)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Space Simulation")
    init()
    glutDisplayFunc(draw_scene)
    glutIdleFunc(draw_scene)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
