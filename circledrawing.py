from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

print("1.Mid point circle drawing algorithm\n2.Polar circle generation algorithm\n3.Non-Polar circle generation algorithm\n")
i=int(input("Choose from above option to draw circle: "))
if i==1:
    x_centre,y_centre,r=map(int,input("Input x coordinate,y coordinate,radius space separated: ").split())
elif i==2:
    x_centre,y_centre,r=map(int,input("Input x coordinate,y coordinate,radius space separated: ").split())
elif i==3:
    x_centre,y_centre,r=map(int,input("Input x coordinate,y coordinate,radius space separated: ").split())
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
	glVertex2i(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

def midPointCircleDraw(x_centre, y_centre, r): 
    glClear(GL_COLOR_BUFFER_BIT)
    x = r 
    y = 0
    setPixel(x+x_centre,y+y_centre) 
    if (r > 0) : 
        setPixel(x+x_centre,-y+y_centre)
        setPixel(y+x_centre,x+y_centre)
        setPixel(y+x_centre,x+y_centre)
        setPixel(-y+x_centre,x+y_centre)
    P = 1 - r
    while x > y:
        y += 1 
        if P <= 0:  
            P = P + 2 * y + 1 
        else:          
            x -= 1
            P = P + 2 * y - 2 * x + 1
          
        if (x < y): 
            break

        setPixel(x+x_centre,y+y_centre)  
        setPixel(-x+x_centre,y+y_centre)  
        setPixel(x+x_centre,-y+y_centre)  
        setPixel(-x+x_centre,-y+y_centre)  
         
        if x != y: 
            setPixel(y+x_centre,x+y_centre)  
            setPixel(-y+x_centre,x+y_centre)  
            setPixel(y+x_centre,-x+y_centre)  
            setPixel(-y+x_centre,-x+y_centre) 

def drawCircle(xc,yc,x,y):
    setPixel(xc+x, yc+y) 
    setPixel(xc-x, yc+y) 
    setPixel(xc+x, yc-y) 
    setPixel(xc-x, yc-y) 
    setPixel(xc+y, yc+x) 
    setPixel(xc-y, yc+x) 
    setPixel(xc+y, yc-x) 
    setPixel(xc-y, yc-x) 

def circlePolar( xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r 
    drawCircle(xc, yc, x, y) 
    while (y >= x):
        x+=1
        if (d > 0):
            y-=1  
            d = d + 4 * (x - y) + 10 
        else:
            d = d + 4 * x + 6 
        drawCircle(xc, yc, x, y)

def nonPolar(xc, yc, radius):
    glColor3f(0.0, 1.0, 1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    x = xc - radius
    target = xc + radius
    glVertex2f(x, yc)
    glVertex2f(target, yc)
    factor = 5000
    incr = 1 / factor
    x += incr
    while x < target:
        y = math.sqrt(radius * radius - (x - xc) * (x - xc))
        glVertex2f(x, yc + y)
        glVertex2f(x, yc - y)
        x += incr
    glEnd()
    glFlush()

def outputDisplay():
    if i==1:
        glClear(GL_COLOR_BUFFER_BIT)
        midPointCircleDraw(x_centre, y_centre, r)
    elif i==2:
        glClear(GL_COLOR_BUFFER_BIT)
        circlePolar(x_centre, y_centre, r)
    elif i==3:
        glClear(GL_COLOR_BUFFER_BIT)
        nonPolar(x_centre,y_centre,r)
    else:
        pass

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(700,700)
    glutCreateWindow("Plot Circles")
    glutDisplayFunc(outputDisplay)
    init()
    glutMainLoop()

main()