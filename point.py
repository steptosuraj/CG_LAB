#Program to plot origin
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
x,y=input("Input x and y Coordinate space sapareted: ").split()
def init():
    glClearColor(0.0,0.0,0.0,1.0) #set background color
    gluOrtho2D(-100.0,100.0,-100.0,100.0) #set the range of cordinate system

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT) #clear the entire window to the background color
    glColor3f(1.0,0.0,0.0) #set color of drawing
    glPointSize(10.0) #set pixelsize
    glBegin(GL_POINTS)
    glVertex2f(float(x),float(y))     #plot the vertex
    glEnd()
    glFlush()     # push the pixels to dispaly

def main():
    glutInit(sys.argv)  #initialize toolkit
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB) #set display mode
    glutInitWindowSize(500,500)  #set window size
    glutInitWindowPosition(50,50)  #set window posiion
    glutCreateWindow("Plot Origin")#create a window with given name
    glutDisplayFunc(plotpoints) #register redraw function
    init()            #additionalinitilizations
    glutMainLoop()#call back loop 

main()