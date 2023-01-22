import turtle
delay = 0.1

#alustaa turtlen
piirto = turtle.Screen()
piirto.title("Pirkka-Paint®")
piirto.bgcolor("white")
piirto.setup(width=1100, height=600)
piirto.tracer(0)

#asettaa default-parametrejä sekä piirtää tervetulotekstin
pen = turtle.Turtle()
pen.pensize(10)
pen.shape("square")
pen.shapesize(0.5,0.5,2)
pen.penup()
pen.goto(0,260)
pen.write("Tervetuloa Pirkka-Paint® -käyttäjäksi!" , align="center", font=("Helvetica", 15, "bold"))
pen.home()
pen.pendown()

#määritellään liikkumiskomennot
def go_up():
    y = pen.ycor()
    pen.sety(y + 10)
def go_down():
    y = pen.ycor()
    pen.sety(y - 10)
def go_left():
    x = pen.xcor()
    pen.setx(x - 10)
def go_right():
    x = pen.xcor()
    pen.setx(x + 10)

#määritellään värivaihtoehdot
color_input = "9"
bgcolor_input = "10"
colors={"Punainen":"red","Oranssi":"orange","Keltainen":"yellow","Vihreä":"green","Sininen":"blue","Pinkki":"pink","Liila":"purple","Ruskea":"brown","Musta":"black","Valkoinen":"white"}
colorslist=["red","orange","yellow","green","blue","pink","purple","brown","black","white"]

#kynän värin vaihto
def colorlist():
    global color_input
    global colors
    global colorslist
    color_input=""
    input_msg="Valitse väri!\n"
    for index, item in enumerate(list(colors)):
        input_msg += f"{index+1}) {item}\n"
    input_msg += "Valintasi: "
    while color_input not in map(str, range(1, len(colorslist)+1)):
        color_input = input(input_msg)
    print("Valitsit: " + list(colors)[int(color_input)-1])
    pen.pencolor(colorslist[int(color_input)-1])
    pen.goto(pen.xcor(),pen.ycor())

#taustan värin vaihto
def bg_colorlist():
    global colors
    global colorslist
    global bgcolor_input
    bgcolor_input = ""
    input_msg="Valitse taustan väri!\n"
    for index, item in enumerate(list(colors)):
        input_msg += f"{index+1}) {item}\n"
    input_msg += "Valintasi: "
    while bgcolor_input not in map(str, range(1, len(colorslist)+1)):
        bgcolor_input = input(input_msg)
    print("Valitsit: " + list(colors)[int(bgcolor_input)-1])
    turtle.bgcolor(colorslist[int(bgcolor_input)-1])

#kynän vaihto kumiksi, eli samaan väriin taustan kanssa
pentoggle=0
def pen_toggle():
    global color_input
    global pentoggle
    if pentoggle == 1:
        pen.pencolor(colorslist[int(color_input)-1])
        pen.goto(pen.xcor(),pen.ycor())
        pentoggle = 0
    else:
        pen.pencolor(colorslist[int(bgcolor_input)-1])
        pen.goto(pen.xcor(),pen.ycor())
        pentoggle = 1

#kynän koon säätäminen
pensize=10
def size_inc():
    global pensize
    pensize +=2
    pen.pensize(pensize)
    pen.goto(pen.xcor(),pen.ycor())
def size_dec():
    global pensize
    if pensize-2 <= 0:
        pensize = 1
    else:
        pensize -=2
    pen.pensize(pensize)
    pen.goto(pen.xcor(),pen.ycor())

def screenshot():
    print("Millä nimellä halua tallentaa kuvan? ")
    filename = input()
    screen = pen.getscreen().getcanvas().postscript(file= filename + ".ps")
    print("Kuva tallennettu!")

def tekstin_kirjoitus():
    print("Minkä nimisen tekstitiedoston haluat avata?")
    filename = input() + ".txt"
    file = open(filename, "a")
    file.write("\n")
    file.close()
    with open(filename) as teksti:
        for rivi in teksti:
            pen.write(rivi , align="center", font=("Helvetica", 15, "bold"))
            pen.penup()
            go_down()
            go_down()
            pen.pendown()
    

piirto.listen()
piirto.onkeypress(go_up, "w")
piirto.onkeypress(go_down, "s")
piirto.onkeypress(go_left, "a")
piirto.onkeypress(go_right, "d")
piirto.onkeypress(pen_toggle, "space")
piirto.onkeypress(size_inc, ".")
piirto.onkeypress(size_dec, ",")
piirto.onkeypress(pen.clear, "r")
piirto.onkeypress(colorlist, "v")
piirto.onkeypress(bg_colorlist, "b")
piirto.onkeypress(screenshot, "p")
piirto.onkeypress(tekstin_kirjoitus, "t")

while True:
    piirto.update()