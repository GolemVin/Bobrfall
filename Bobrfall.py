from tkinter import *
import time
import random
import threading

window = Tk()
window.geometry("600x750")
window.title("Bobrfall")
window.resizable(False,False)
color = "black"
window["bg"] = color

c = Canvas(window, height = 750, width = 600, bg = "white")
c.place(x = 0, y = 0)

png1 = PhotoImage(file = "png/rock.png")
png2 = PhotoImage(file = "png/bobrg.png")
png3 = PhotoImage(file = "png/bgrock.png")
png4 = PhotoImage(file = "png/rocktrav.png")
png5 = PhotoImage(file = "png/bobrgg.png")
png6 = PhotoImage(file = "png/sc50.png")
png7 = PhotoImage(file = "png/freez.png")
png8 = PhotoImage(file = "png/bobrbomb.png")
png9 = PhotoImage(file = "png/bobrgf.png")
png10 = PhotoImage(file = "png/bobrggf.png")

c.create_image(300,375, image = png3)
c.create_image(300,725, image = png4)
c.create_text(538,18, text = "Record", fill = "red",  font = ("Courier 25"))
c.create_text(52,18, text = "Score", fill = "blue",  font = ("Courier 25"))

rocks = []
sc = []
fr = []
bm = []

def gog():
    respawn()
    but.destroy()

def timer():
    global ti
    global score
    ti = ti + 1
    c.delete(score)
    score = c.create_text(92,58, text = ti, fill = "blue",  font = ("Courier 40"))
    
def plus():
    global ti
    global score
    ti = ti + 50
    c.delete(score)
    score = c.create_text(92,58, text = ti, fill = "blue",  font = ("Courier 40"))

def stopfr():
    global tispeed
    tispeed = 0.01

ti = 0
tim = 0

tispeed = 0.01

score = c.create_text(92,58, text = " ")

but = Button(window, text = "PLAY", bg = "orange", fg = "black", font = ("Courier",24,"bold"), command = gog)
but.place(x = 250, y = 370, width = 100)

x = True

def update_x():
    global x
    x = False

window.protocol("WM_DELETE_WINDOW", update_x)

def respawn():
    global chel
    chel = c.create_image(300,675, image = png2)
    for i in range(5):
        r1 = c.create_image(random.randint(37,562),i*(-5000), image = png1)
        rocks.append(r1)
    for i in range(1,6):
        sc50 = c.create_image(random.randint(35,565),i*(-(random.randint(10000,15000))), image = png6)
        sc.append(sc50)
    for i in range(1,6):
        freez = c.create_image(random.randint(35,565),i*(-(random.randint(5000,10000))), image = png7)
        fr.append(freez)
    for i in range(1,6):
        bomb = c.create_image(random.randint(35,565),i*(-(random.randint(15000,25000))), image = png8)
        bm.append(bomb)

def respawn2():
    global chel
    chel = c.create_image(korc[0],korc[1], image = png2)
    for i in range(5):
        r1 = c.create_image(random.randint(37,562),i*(-5000), image = png1)
        rocks.append(r1)
    for i in range(1,6):
        sc50 = c.create_image(random.randint(35,565),i*(-(random.randint(10000,15000))), image = png6)
        sc.append(sc50)
    for i in range(1,6):
        freez = c.create_image(random.randint(35,565),i*(-(random.randint(5000,10000))), image = png7)
        fr.append(freez)
    for i in range(1,6):
        bomb = c.create_image(random.randint(35,565),i*(-(random.randint(15000,25000))), image = png8)
        bm.append(bomb)

def go(event):
    global chel
    global bx
    global by
    bx = c.coords(chel)[0]
    by = c.coords(chel)[1]
    if (event.keysym == "d" or event.keysym == "D") and c.coords(chel)[0] < 570:
        c.delete(chel)
        chel = c.create_image(bx,by, image = png2)
        c.move(chel,30,0)
    if (event.keysym == "a" or event.keysym == "A") and c.coords(chel)[0] > 30:
        c.delete(chel)
        chel = c.create_image(bx,by, image = png5)
        c.move(chel,-30,0)
    if (event.keysym == "Right") and c.coords(chel)[0] < 570:
        c.delete(chel)
        chel = c.create_image(bx,by, image = png2)
        c.move(chel,30,0)
    if (event.keysym == "Left") and c.coords(chel)[0] > 30:
        c.delete(chel)
        chel = c.create_image(bx,by, image = png5)
        c.move(chel,-30,0)

def chek():
    try:
        korc = c.coords(chel)
    except:
        return
    for i in rocks:
        kor1 = c.coords(i)
        if (kor1[0]-37.5 <= korc[0]-30 <= kor1[0]+37.5 or kor1[0]-37.5 <= korc[0]+30 <= kor1[0]+37.5) and (kor1[1]-52.5 <= korc[1]-30 <= kor1[1]+52.5 or kor1[1]-52.5 <= korc[1]+30 <= kor1[1]+52.5):
            c.delete("all")
            c.create_image(300,375, image = png3)
            c.create_image(300,725, image = png4)
            c.create_text(538,18, text = "Record", fill = "red",  font = ("Courier 25"))
            c.create_text(52,18, text = "Score", fill = "blue",  font = ("Courier 25"))
            rocks.clear()
            sc.clear()
            fr.clear()
            bm.clear()
            global ti
            global tim
            global tispeed
            if ti > tim:
                tim = ti
            ti = 0
            tispeed = 0.01
            c.create_text(508,58, text = tim, fill = "red",  font = ("Courier 40"))
            c.create_image(korc[0],korc[1], image = png9)
            time.sleep(0.4)
            respawn()
            return

def bomb():
    try:
        korc = c.coords(chel)
    except:
        return
    for i in bm:
        kor1 = c.coords(i)
        if (kor1[0]-37.5 <= korc[0]-30 <= kor1[0]+37.5 or kor1[0]-37.5 <= korc[0]+30 <= kor1[0]+37.5) and (kor1[1]-52.5 <= korc[1]-30 <= kor1[1]+52.5 or kor1[1]-52.5 <= korc[1]+30 <= kor1[1]+52.5):
            korc = c.coords(chel)
            c.delete("all")
            c.create_image(300,375, image = png3)
            c.create_image(300,725, image = png4)
            c.create_text(538,18, text = "Record", fill = "red",  font = ("Courier 25"))
            c.create_text(52,18, text = "Score", fill = "blue",  font = ("Courier 25"))
            rocks.clear()
            sc.clear()
            fr.clear()
            bm.clear()
            global ti
            global tim
            global score2
            global tispeed
            if ti > tim:
                tim = ti
            tispeed = 0.01
            score2 = c.create_text(92,58, text = ti, fill = "blue",  font = ("Courier 40"))
            c.create_text(508,58, text = tim, fill = "red",  font = ("Courier 40"))
            respawn2()
            return

c.bind_all("<Key>", go)

while x == True:
    for b in bm:
        c.move(b,0,4)
        kor = c.coords(b)
        if kor[1]-52.5 >= 750:
            c.coords(b,0,800)
    for s in sc:
        c.move(s,0,random.randint(3,4))
        kor1 = c.coords(s)
        korc = c.coords(chel)
        if (kor1[0]-37.5 <= korc[0]-30 <= kor1[0]+37.5 or kor1[0]-37.5 <= korc[0]+30 <= kor1[0]+37.5) and (kor1[1]-52.5 <= korc[1]-30 <= kor1[1]+52.5 or kor1[1]-52.5 <= korc[1]+30 <= kor1[1]+52.5):
            c.coords(s,0,800)
            plus()
    for f in fr:
        c.move(f,0,random.randint(3,4))
        kor1 = c.coords(f)
        korc = c.coords(chel)
        if (kor1[0]-37.5 <= korc[0]-30 <= kor1[0]+37.5 or kor1[0]-37.5 <= korc[0]+30 <= kor1[0]+37.5) and (kor1[1]-52.5 <= korc[1]-30 <= kor1[1]+52.5 or kor1[1]-52.5 <= korc[1]+30 <= kor1[1]+52.5):
            c.coords(f,0,800)
            tispeed = 0.1
            threading.Timer(10,stopfr).start()
    for i in rocks:
        c.move(i,0,random.randint(5,6))
        kor = c.coords(i)
        if kor[1]-52.5 >= 600:
            c.coords(i,random.randint(37,562),-40)
            timer()
            try:
                c.delete(score2)
            except:
                break
    chek()
    bomb()
    window.update()
    time.sleep(tispeed)