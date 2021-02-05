from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init():
 glClearColor(0.0, 0.0, 0.0, 0.0)
 gluOrtho2D(-100.0,100.0, -100.0,100.0)

def glutFunct():
 glutInit(sys.argv)
 glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
 glutInitWindowSize(500, 500)
 glutInitWindowPosition(0, 0)
 glutCreateWindow("Bezier Curve Algorithm")
 init()

def plotPoint(x, y):
 glBegin(GL_POINTS)
 glVertex3f(x, y, 0)
 glEnd()

def binCoeff(n):
 coeff = []
 for k in range(n+1):
    coeff += [1]
    for j in range(k+1, n+1):
        coeff[k] *= j
    for j in range(1, n-k+1):
        coeff[k] /= j
 return coeff

def getBezierPoints(u, n, coeff, cntrlPts):
 x, y = 0.0, 0.0
 for k in range(n):
    bezBlendFn = coeff[k] * math.pow(u, k) * math.pow(1-u, n-1-k)
    x += cntrlPts[k][0] * bezBlendFn
    y += cntrlPts[k][1] * bezBlendFn
 return x, y

def bezier(n, cntrlPts, nBezier):
 coeff = binCoeff(n-1)
 for k in range(nBezier):
    u = float(k/nBezier)
    x, y = getBezierPoints(u, n, coeff, cntrlPts)
    plotPoint(x, y)

def display(n, cntrlPts, nBezier):
 glClear(GL_COLOR_BUFFER_BIT)
 glColor3f(1.0, 0.0, 0.0)
 glPointSize(2.0)
 bezier(n, cntrlPts, nBezier)
 glFlush()

def main():
 n = int(input("\nEnter the no. of control points : "))
 nBezier = int(input("Enter the no. of Bezier curve points : "))
 cntrlPts = list(list())
 for i in range(n):
    x = float(input("Enter x-coordinate for control point " + str(i+1) +": "))
    y = float(input("Enter y-coordinate for control point " + str(i+1) +": "))
    cntrlPts += [[x, y]]
 glutFunct()
 glutDisplayFunc(lambda: display(n, cntrlPts, nBezier))
 glutMainLoop()
 
main()