from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
# import math

x1,y1,x2,y2=map(int,input("enter x1,y1,x2,y2 space separated: ").split())

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

def lineBres(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    p=2*dy - dx
    if x1 > x2:
        x=x2
        y=y2
        xend=x1
    else:
        x=x1
        y=y1
        xend=x2
    glVertex2f(x,y)
    while x<xend:
        x+=1
        if p < 0 :
            p+=2*dy
        else:
            y=y+1
            p+=2*dy-2*dx
        glVertex2f(x,y)

def plotlines():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    lineBres(x1,y1,x2,y2)
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