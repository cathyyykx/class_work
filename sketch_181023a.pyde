x = 0
y = 250

def setup():
    size(640, 480)


def draw():
    global x, y
    
    while x == width:
        x = 0
        
    while y == width:
        y = 0
        
    x += 2.5
    y += 2
    
    background(12, 0, 109)  # sky blue
    
    # land
    fill(0, 153, 0)
    rect(0, 380, 640, 640)
    
    # moon
    fill(255, 255, 153)
    ellipse(540, 80, 95, 90)
    
    # tree
    fill(102, 51, 0)
    rect(480, 260, 50, 120)
    
    fill(0, 132, 39)
    triangle(450, 260, 560, 260, 505, 200)
    
    # house
    fill(163, 65, 0)
    rect(width / 2 - 150, 280, 150, 110)
    
    fill(249, 0, 0)
    triangle(130, 280, 360, 280, 245, 180)
    
    # clouds
    fill(255)
    noStroke()
    ellipse(x, height/2 - 100, 60, 60)
    ellipse(x+30, height/2 - 100, 60, 60)
    ellipse(x+15, height/2 - 120, 60, 60)
    ellipse(x + 45, height/2 - 120, 60, 60)
    
    ellipse(y, height/2 - 30, 50, 50)
    ellipse(y + 35, height / 2 - 30, 50, 50)
    ellipse(y + 15, height / 2 - 50, 50, 50)
    ellipse(y + 45, height / 2 - 50, 50, 50)
    
    ellipse(y + 50, height/2 - 150, 50, 50)
    ellipse(y + 85, height / 2 - 150, 50, 50)
    ellipse(y + 60, height / 2 - 175, 50, 50)
    ellipse(y + 75, height / 2 - 175, 50, 50)
    ellipse(y + 105, height / 2 - 170, 50, 50)
    
    
