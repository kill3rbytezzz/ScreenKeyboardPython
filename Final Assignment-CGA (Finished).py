import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton #import library application, widget, pushbutton dari pyqt5
from PyQt5.QtGui import QIcon #import library icon dari pyqt5
from PyQt5.QtCore import pyqtSlot #import pyqtSlot dari pyqt5
from OpenGL.GL import * #import * dari OpenGL.GL
from OpenGL.GLUT import* #import * dari OpeGL.GLUT
from OpenGL.GLU import * #import * dari OpenGL.GLU


def window(): #function windows
   app = QApplication(sys.argv)
   widget = QWidget()
   
   buttonQ = QPushButton(widget)  #Deklarasi pemanggilan Button Q
   buttonQ.setText('Q') #Memberi huruf di button dengan huruf Q
   buttonQ.setGeometry(0, 0, 50, 50) #Mengatur posisi dan ukuran button (posisi x = 0, posisi y = 0, width = 50, length = 50)
   buttonQ.clicked.connect(buttonQ_clicked) #pemanggilan fungsi ketika tombol ditekan

   buttonW = QPushButton(widget) #Deklarasi pemanggilan Button W 
   buttonW.setText("W") #Memberi huruf di button dengan huruf @
   buttonW.setGeometry(50, 0, 50, 50) #Mengatur posisi dan ukuran button (posisi x = 0, posisi y = 0, width = 50, length = 50)
   buttonW.clicked.connect(buttonW_clicked) #pemanggilan fungsi ketika tombol ditekan

   buttonE = QPushButton(widget) #Dan Seterusnya
   buttonE.setText('E') #Dan Seterusnya
   buttonE.setGeometry(100, 0, 50, 50) #Dan Seterusnya
   buttonE.clicked.connect(buttonE_clicked) #Dan Seterusnya

   buttonR = QPushButton(widget)
   buttonR.setText("R")
   buttonR.setGeometry(150, 0, 50, 50)
   buttonR.clicked.connect(buttonR_clicked)

   buttonT = QPushButton(widget)
   buttonT.setText('T')
   buttonT.setGeometry(200, 0, 50, 50)
   buttonT.clicked.connect(buttonT_clicked)

   buttonY = QPushButton(widget)
   buttonY.setText("Y")
   buttonY.setGeometry(250, 0, 50, 50)
   buttonY.clicked.connect(buttonY_clicked)

   buttonU = QPushButton(widget)
   buttonU.setText('U')
   buttonU.setGeometry(300, 0, 50, 50)
   buttonU.clicked.connect(buttonU_clicked)

   buttonI = QPushButton(widget)
   buttonI.setText("I")
   buttonI.setGeometry(350, 0, 50, 50)
   buttonI.clicked.connect(buttonI_clicked)

   buttonO = QPushButton(widget)
   buttonO.setText('O')
   buttonO.setGeometry(400, 0, 50, 50)
   buttonO.clicked.connect(buttonO_clicked)

   buttonP = QPushButton(widget)
   buttonP.setText("P")
   buttonP.setGeometry(450, 0, 50, 50)
   buttonP.clicked.connect(buttonP_clicked)

   buttonA = QPushButton(widget)
   buttonA.setText('A')
   buttonA.setGeometry(25, 50, 50, 50)
   buttonA.clicked.connect(buttonA_clicked)

   buttonS = QPushButton(widget)
   buttonS.setText("S")
   buttonS.setGeometry(75, 50, 50, 50)
   buttonS.clicked.connect(buttonS_clicked)

   buttonD = QPushButton(widget)
   buttonD.setText('D')
   buttonD.setGeometry(125, 50, 50, 50)
   buttonD.clicked.connect(buttonD_clicked)

   buttonF = QPushButton(widget)
   buttonF.setText("F")
   buttonF.setGeometry(175, 50, 50, 50)
   buttonF.clicked.connect(buttonF_clicked)

   buttonG = QPushButton(widget)
   buttonG.setText('G')
   buttonG.setGeometry(225, 50, 50, 50)
   buttonG.clicked.connect(buttonG_clicked)

   buttonH = QPushButton(widget)
   buttonH.setText("H")
   buttonH.setGeometry(275, 50, 50, 50)
   buttonH.clicked.connect(buttonH_clicked)

   buttonJ = QPushButton(widget)
   buttonJ.setText('J')
   buttonJ.setGeometry(325, 50, 50, 50)
   buttonJ.clicked.connect(buttonJ_clicked)

   buttonK = QPushButton(widget)
   buttonK.setText("K")
   buttonK.setGeometry(375, 50, 50, 50)
   buttonK.clicked.connect(buttonK_clicked)

   buttonL = QPushButton(widget)
   buttonL.setText('L')
   buttonL.setGeometry(425, 50, 50, 50)
   buttonL.clicked.connect(buttonL_clicked)

   buttonZ = QPushButton(widget)
   buttonZ.setText("Z")
   buttonZ.setGeometry(75, 100, 50, 50)
   buttonZ.clicked.connect(buttonZ_clicked)

   buttonX = QPushButton(widget)
   buttonX.setText('X')
   buttonX.setGeometry(125, 100, 50, 50)
   buttonX.clicked.connect(buttonX_clicked)

   buttonC = QPushButton(widget)
   buttonC.setText("C")
   buttonC.setGeometry(175, 100, 50, 50)
   buttonC.clicked.connect(buttonC_clicked)

   buttonV = QPushButton(widget)
   buttonV.setText('V')
   buttonV.setGeometry(225, 100, 50, 50)
   buttonV.clicked.connect(buttonV_clicked)

   buttonB = QPushButton(widget)
   buttonB.setText("B")
   buttonB.setGeometry(275, 100, 50, 50)
   buttonB.clicked.connect(buttonB_clicked)

   buttonN = QPushButton(widget)
   buttonN.setText('N')
   buttonN.setGeometry(325, 100, 50, 50)
   buttonN.clicked.connect(buttonN_clicked)

   buttonM = QPushButton(widget)
   buttonM.setText("M")
   buttonM.setGeometry(375, 100, 50, 50)
   buttonM.clicked.connect(buttonM_clicked)

   buttonSpace = QPushButton(widget)
   buttonSpace.setText("Space")
   buttonSpace.setGeometry(0, 150, 400, 50)
   buttonSpace.clicked.connect(buttonSpace_clicked)

   buttonBackSpace = QPushButton(widget)
   buttonBackSpace.setText("BackSpace")
   buttonBackSpace.setGeometry(425, 100, 75, 50)
   buttonBackSpace.clicked.connect(buttonBackSpace_clicked)

   buttonEnter = QPushButton(widget)
   buttonEnter.setText("Enter")
   buttonEnter.setGeometry(400, 150, 100, 50)
   buttonEnter.clicked.connect(buttonEnter_clicked)

   window.p=-150 #akan dijadikan acuan untuk posisi windows Y
   window.enter=0 #akan dijadikan acuan untuk posisi windows X

   widget.setGeometry(0,600,500,200) #ukuran windows PyQT yang dipanggil
   widget.setWindowTitle("Virtual Keyboard OpenGL") #nama program
   widget.show()
   sys.exit(app.exec_())

def initiate(): #funct initiate 
    glViewport(0 , 0, 500, 500) #mendeskripsikan koordinat yang akan dipakai di opengl
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    #glClearColor(1.0,1.0,1.0,1.0)

def garis(x1,y1,x2,y2): #func garis
    glBegin(GL_LINES) #mendeskripsikan penggunaan GL_LINES (Garis)
    glVertex2f(x1,y1) #Posisi x1, y1 (titik garis pertama)
    glVertex2f(x2,y2) #Posisi x2, y2 (titik garis kedua)
    glEnd()


def buttonA_clicked(): #func buttonA_clicked (function yang dipanggil ketika tombol A di click)
    window.p=window.p+150 #deklarasi variabel window.p yang akan menjadi acuan munculnya window dari huruf A
    def draw(): #nested function dari buttonA yaitu draw, menggambarkan huruf yang akan menjadi output huruf
        garis(20,20,75,125)
        garis(75,125,130,20)
        garis(130,20,120,20)
        garis(120,20,95,70)
        garis(95,70,55,70)
        garis(55,70,30,20)
        garis(30,20,20,20)
        garis(60,80,75,110)
        garis(75,110,90,80)
        garis(90,80,60,80)

    def display(): #funct display, memanggil func draw untuk memberikan output huruf
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()

    def main(): #funct main untuk menampilkan window huruf (opengl)
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150) #ukuran window opengl (width 150, length 150)
        glutInitWindowPosition(window.p, window.enter) #posisi munculnya window, window akan muncul sesuai dengan posisis y adalah nilai variabel window.p dan posisi x adalaha window.enter
        wind = glutCreateWindow(b"Huruf A") #nama window pyopengl
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main() #pemanggilan fungsi main

def buttonB_clicked(): #sama kayak yang diatas
    window.p=window.p+150
    def draw():
        garis(30,10,30,140)
        garis(30,140,120,103)
        garis(120,103,80,75)
        garis(80,75,120,44)
        garis(120,44,30,10)
        garis(50,120,50,85)
        garis(50,85,100,103)
        garis(100,103,50,120)
        garis(50,65,50,30)
        garis(50,30,100,44)
        garis(100,44,50,65)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf B")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()

    main()
def buttonC_clicked():
    window.p=window.p+150
    def draw():
        garis(110,20,20,75)
        garis(20,75,110,140)
        garis(110,140,110,130)
        garis(110,130,30,75)
        garis(30,75,110,30)
        garis(110,30,110,20)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()

    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf C")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonD_clicked():
    window.p=window.p+150
    def draw():
        garis(30,140,30,20)
        garis(30,20,70,20)
        garis(70,20,120,50)
        garis(120,50,120,110)
        garis(120,110,70,140)
        garis(70,140,30,140)
        garis(50,120,50,40)
        garis(50,40,70,40)
        garis(70,40,100,60)
        garis(100,60,100,100)
        garis(100,100,70,120)
        garis(70,120,50,120)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf D")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()

    main()
def buttonE_clicked():
    window.p=window.p+150
    def draw():
        garis(130,20,30,20)
        garis(30,20,30,140)
        garis(30,140,130,140)
        garis(130,140,130,130)
        garis(130,130,40,130)
        garis(40,130,40,80)
        garis(40,80,130,80)
        garis(130,80,130,70)
        garis(130,70,40,70)
        garis(40,70,40,30)
        garis(40,30,130,30)
        garis(130,30,130,20)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()

    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf E")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonF_clicked():
    window.p=window.p+150
    def draw():
        garis(30,20,30,140)
        garis(30,140,130,140)
        garis(130,140,130,130)
        garis(130,130,40,130)
        garis(40,130,40,100)
        garis(40,100,110,100)
        garis(110,100,110,90)
        garis(110,90,40,90)
        garis(40,90,40,20)
        garis(40,20,30,20)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf F")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()

    main()

def buttonG_clicked():
    window.p=window.p+150
    def draw():
        garis(130,140,30,140)
        garis(30,140,30,20)
        garis(30,20,130,20)
        garis(130,20,130,80)
        garis(130,80,80,80)
        garis(80,80,80,70)
        garis(80,70,120,70)
        garis(120,70,120,30)
        garis(120,30,40,30)
        garis(40,30,40,130)
        garis(40,130,130,130)
        garis(130,130,130,140)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf F")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()

    main()

def buttonH_clicked():
    window.p=window.p+150
    def draw():
        garis(30,140,30,20)
        garis(30,20,40,20)
        garis(40,20,40,70)
        garis(40,70,120,70)
        garis(120,70,120,20)
        garis(120,20,130,20)
        garis(130,20,130,140)
        garis(130,140,120,140)
        garis(120,140,120,80)
        garis(120,80,40,80)
        garis(40,80,40,140)
        garis(40,140,30,140)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf H")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonI_clicked():
    window.p=window.p+150   
    def draw():
        garis(70,140,70,20)
        garis(70,20,80,20)
        garis(80,20,80,140)
        garis(80,140,70,140)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()

    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf I")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonJ_clicked():
    window.p=window.p+150
    def draw():
        garis(130,140,130,20)
        garis(130,20,30,20)
        garis(30,20,30,70)
        garis(30,70,50,70)
        garis(50,70,50,60)
        garis(50,60,40,60)
        garis(40,60,40,30)
        garis(40,30,120,30)
        garis(120,30,120,140)
        garis(120,140,130,140)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf J")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()

    main()
def buttonK_clicked():
    window.p=window.p+150
    def draw():
        garis(30,140,30,20)
        garis(30,20,40,20)
        garis(40,20,40,70)
        garis(40,70,130,20)
        garis(130,20,130,30)
        garis(130,30,40,80)
        garis(40,80,130,130)
        garis(130,130,130,140)
        garis(130,140,40,90)
        garis(40,90,40,140)
        garis(40,140,30,140 )

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()

    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf K")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonL_clicked():
    window.p=window.p+150
    def draw():
        garis(30,140,30,20)
        garis(30,20,100,20)
        garis(100,20,100,30)
        garis(100,30,40,30)
        garis(40,30,40,140)
        garis(40,140,30,140)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf L")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()

    main()
def buttonM_clicked():
    window.p=window.p+150    
    def draw():
        garis(30,30,30,140)
        garis(30,140,40,140)
        garis(40,140,75,90)
        garis(75,90,120,140)
        garis(120,140,130,140)
        garis(130,140,130,30)
        garis(130,30,120,30)
        garis(120,30,120,130)
        garis(120,130,75,80)
        garis(75,80,40,130)
        garis(40,130,40,30)
        garis(40,30,30,30)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()

    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf M")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonN_clicked():
    window.p=window.p+150
    def draw():
        garis(25,25, 25,125)
        garis (25, 125, 40,125)
        garis (40,125, 110,40)
        garis(110,40, 110,125)
        garis (110,125,125,125)
        garis (125,125, 125,25)
        garis (125,25, 110,25)
        garis (110,25,40,110)
        garis (40,110,40,25)
        garis (40,25,25,25)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf N")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()

    main()

def buttonO_clicked():
    window.p=window.p+150    
    def draw():
        garis(30,130,30,30)
        garis (30,30, 120,30)
        garis (120,30,120,130)
        garis (120,130,30,130)
        garis (50,110,50,50)
        garis (50,50,100,50)
        garis (100,50,100,110)
        garis (100, 110,50,110)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()

    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf O")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonP_clicked():
    window.p=window.p+150
    def draw():
        garis(25,25, 25,135)
        garis (25, 135, 125,135)
        garis (125,135,125,75)
        garis(125,75,45,75)
        garis (45,75,45,25)
        garis (45,25,25,25)
        garis (45,115,45,95)
        garis (45,95,105,95)
        garis (105,95,105,115)
        garis (105,115 , 45,115)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf P")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonQ_clicked():
    window.p=window.p+150    
    def draw():
        garis(25,125,25,25)
        garis (25, 25,110,25)
        garis (110,25,125,15)
        garis(125,15,135,30)
        garis (135,30,120,40)
        garis (120,40,120,125)
        garis (120,125,25,125)
        garis (45,110,45,45)
        garis (45,45,85,45)
        garis(85,45,75,55)
        garis(75,55, 90,65)
        garis(90,65,100,55)
        garis (100,55,100,110)
        garis(100,110,45,110)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()

    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf Q")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonR_clicked():
    window.p=window.p+150
    def draw():
        garis(25,25, 25,135)
        garis (25, 135, 125,135)
        garis(125,135, 125,85)
        garis(125,85, 60,85)
        garis (60,85,125,25)
        garis (125,25, 100,25)
        garis (100,25, 45,75)
        garis (45,75,45,25)
        garis (45,25, 25,25)
        garis (45,120,45,100)
        garis (45,100,110,100)
        garis (110,100,110,120)
        garis (110,120,45,120)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf R")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()

    main()
def buttonS_clicked():
    window.p=window.p+150    
    def draw():
        garis(25,25, 25,45)
        garis (25,45,105,45)
        garis (105,45,105,65)
        garis (105,65,25,65)
        garis (25,65,25,125)
        garis (25,125,125,125)
        garis(125,125,125,105)
        garis(125,105,45,105)
        garis (45,105,45,85)
        garis (45,85,125,85)
        garis(125,85,125,25)
        garis(125,25,25,25)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()

    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf S")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonT_clicked():
    window.p=window.p+150
    def draw():
        garis(25,125,125,125)
        garis (125,125,125,105)
        garis(125,105,85,105)
        garis (85,105,85,25)
        garis (85,25,65,25)
        garis(65,25,65,105)
        garis(65,105,25,105)
        garis (25,105,25,125)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf T")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()

    main()
def buttonU_clicked():
    window.p=window.p+150    
    def draw():
        garis(25,25, 25,125)
        garis (25,125,45,125)
        garis(45,125,45,45)
        garis (45,45,105,45)
        garis(105,45,105,125)
        garis(105,125,125,125)
        garis(125,125,125,25)
        garis(125,25,25,25)


    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()

    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf U")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonV_clicked():
    window.p=window.p+150
    def draw():
        garis(25,125, 60,25)
        garis (60,25,90,25)
        garis (90,25,125,125)
        garis (125,125,105,125)
        garis (105,125,75,40)
        garis (75,40,45,125)
        garis (45,125,25,125)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf V")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()

    main()

def buttonW_clicked():
    window.p=window.p+150    
    def draw():
        garis (25,125,40,25)
        garis (40,25,60,25)
        garis (60,25,75,110)
        garis (75,110, 90,25)
        garis(90,25,110,25)
        garis (110,25,125,125)
        garis(125,125,110,125)
        garis(110,125,100,40)
        garis (100,40,85,125)
        garis(85,125,65,125)
        garis(65,125,50,40)
        garis(50,40,40,125)
        garis(40,125,25,125)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()

    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf W")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonX_clicked():
    window.p=window.p+150
    def draw():
        garis(25,125, 45,125)
        garis (45,125,75,85)
        garis (75,85,105,125)
        garis (105,125,125,125)
        garis (125,125,85,75)
        garis (85,75,125,25)
        garis (125,25,105,25)
        garis (105,25,75,65)
        garis (75,65,45,25)
        garis (45,25,25,25)
        garis (25,25,65,75)
        garis (65,75,25,125)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf X")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonY_clicked():
    window.p=window.p+150    
    def draw():
        garis(25,125, 45,125)
        garis (45,125,75,80)
        garis (75,80,105,125)
        garis (105,125,125,125)
        garis (125,125,85,65)
        garis (85,65,85,25)
        garis (85,25,65,25)
        garis (65,25,65,65)
        garis (65,65,25,125)

    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()

    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p, window.enter)
        wind = glutCreateWindow(b"Huruf Y")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonZ_clicked():
    window.p=window.p+150
    def draw():
        garis(25,125, 25,105)
        garis (25,105,105,105)
        garis (105,105,25,45)
        garis (25,45,25,25)
        garis (25,25,125,25)
        garis (125,25,125,45)
        garis (125,45,55,45)
        garis (55,45,125,95)
        garis (125,95,125,125)
        garis (125,125,25,125)


    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        draw()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p , window.enter)
        wind = glutCreateWindow(b"Huruf Z")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonSpace_clicked(): #button space, ketika ditekan akan menampilkan window kosong tanpa garis/huruf setelah window terakhir
    window.p=window.p+150    
    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p , window.enter)
        wind = glutCreateWindow(b"Spasi")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()

    main()

def buttonBackSpace_clicked(): #button backspace akan menampilkan window kosong diatas huruf sebelumnya (yang akan dihapus)
    window.p=window.p-150
    def display():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        initiate()
        glutSwapBuffers()
    
    def main():
        glutInit()
        glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB )
        glutInitWindowSize(150, 150)
        glutInitWindowPosition(window.p+150 , window.enter)
        wind = glutCreateWindow(b"Huruf Z")
        glutDisplayFunc(display)
        glutIdleFunc(display)
        glutMainLoop()
    main()

def buttonEnter_clicked(): #funct tombol enter, akan menambah nilai variabel window.enter menjadi +175 dan memberikan nilai window.p kembali ke -150
    window.enter=window.enter+175
    window.p=-150

if __name__ == '__main__':
   window()