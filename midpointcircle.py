from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

print("1.Polar ellipse drawing algorithm\n2.Non Polar ellipse drawing algorithm\n")
i=int(input("Choose from above option to draw ellipse: "))
if i==1:
    x_centre,y_centre,rx,ry=map(int,input("Input x centre,y centre,rx,ry space separated: ").split())
elif i==2:
    x_centre,y_centre,rx,ry=map(int,input("Input x centre,y centre,rx,ry space separated: ").split())
else:
    print("invalid input\n\n\n")

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-100.0,100.0,-100.0,100.0)

def setPixel(xcoordinate,ycoordinate):
	glColor3f(1.0,1.0,1.0) 
	glPointSize(5.0)
	glBegin(GL_LINES)
	glVertex2f(-500,0)
	glVertex2f(500,0)
	glEnd()
	glBegin(GL_LINES)
	glVertex2f(0,-500)
	glVertex2f(0,500)
	glEnd() 
	glColor3f(0.0,1.0,1.0)
	glPointSize(5.0)
	glBegin(GL_POINTS)
	glVertex2f(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

def ellipsep(x1,y1,r1,r2):
	xCenter=x1
	yCenter=y1
	rx=r1
	ry=r2
	angle=0
	end=(22/7)/2
	while angle<end:
		x=(rx*math.cos(angle))
		y=(ry*math.sin(angle))
		setPixel(xCenter+x,yCenter+y)
		setPixel(xCenter-x,yCenter+y)
		setPixel(xCenter-x,yCenter-y)
		setPixel(xCenter+x,yCenter-y)
		angle=angle+0.001      
	glFlush()

def ellipsenp(x1,y1,r1,r2):
	x=0
	y=0
	xCenter=x1
	yCenter=y1
	rx=r1
	ry=r2
	while x<=rx :
		y=math.sqrt(math.pow(rx*ry,2)-math.pow(x*ry,2))/rx
		setPixel(xCenter+x,yCenter+y)
		setPixel(xCenter-x,yCenter+y)
		setPixel(xCenter-x,yCenter-y)
		setPixel(xCenter+x,yCenter-y)
		x=x+0.001      
	glFlush()

def outputDisplay():
    if i==1:
        glClear(GL_COLOR_BUFFER_BIT)
        ellipsep(x_centre, y_centre, rx,ry)
    elif i==2:
        glClear(GL_COLOR_BUFFER_BIT)
        ellipsenp(x_centre, y_centre, rx,ry)
    else:
        pass

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(700,700)
    glutCreateWindow("Plot ellipse")
    glutDisplayFunc(outputDisplay)
    init()
    glutMainLoop()

main()