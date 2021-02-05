from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
# import math

x1,y1,x2,y2=map(int,input("enter x1,y1,x2,y2 space separated: ").split())

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

def ROUND(n):
	return int(n+0.5)

def dda(x1,y1,x2,y2):
	x,y = x1,y1
	length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
	dx = (x2-x1)/float(length)
	dy = (y2-y1)/float(length)
	glVertex2f(ROUND(x),ROUND(y))

	for i in range(length):
		x+= dx
		y+= dy
		glVertex2f(ROUND(x),ROUND(y))

def plotlines():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    dda(x1,y1,x2,y2)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(700,700)
    glutCreateWindow("Plot Lines")
    glutDisplayFunc(plotlines)
    init()
    glutMainLoop()

main()