from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(-100.0,100.0,-100.0,100.0)

def glutFunc():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Sierpenski Triangle")
    init()

def setAxes():
    glColor3f(0.0,1.0,0.0) 
    glPointSize(5.0)
    glBegin(GL_LINES)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0,-100)
    glVertex2f(0,100)
    glEnd()
    glLineWidth(1.0)

def triangle(a, b,c):
    glVertex2fv(a)
    glVertex2fv(b)
    glVertex2fv(c)


def divide_triangle(a,b,c,m):
    v0=[]
    v1=[]
    v2=[]
    if(m>0):
        for j in range (0,2): 
            v0.append((a[j]+b[j])/2)
        for j in range(0,2):
            v1.append((a[j]+c[j])/2)
        for j in range(0,2): 
            v2.append((b[j]+c[j])/2)
        divide_triangle(a, v0, v1, m-1)
        divide_triangle(c, v1, v2, m-1)
        divide_triangle(b, v2, v0, m-1)
    else:
        triangle(a,b,c)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    setAxes()
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    divide_triangle(coord[0], coord[1], coord[2], 6)
    glEnd()
    glFlush()

def main():
    print("**GENERATION OF FRACTAL IMAGE**")
    print("    **Sierpinski Triangle**    ")
    global coord
    coord=[]
    print("Enter coordinates of triangle: ")
    for i in range(0,3):
        x=int(input(f"Enter x{i+1}: "))
        y=int(input(f"Enter y{i+1}: "))
        coord.append([x,y])
    glutFunc()
    glutDisplayFunc(display)
    glutMainLoop()

main()