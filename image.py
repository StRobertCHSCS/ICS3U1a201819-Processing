# Need to load image file into 
# the sketch's data folder.
# Top menu: Sketch -> Add File

def setup():
    global sat_img
    global back_img

    size(512, 480)
    sat_img = loadImage("laugh_trans.png")
    back_img = loadImage("mario_back.png")


def draw():
    background(back_img)
    image(sat_img, 50, 50, 50, 50)