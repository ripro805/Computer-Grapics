import turtle
import math
import time


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System Simulation")
screen.setup(width=1200, height=900)
screen.tracer(0)  


sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(5, 5)
sun.penup()

class CelestialBody(turtle.Turtle):
    def __init__(self, name, size, color, distance, speed, parent=None):
        super().__init__()
        self.name = name
        self.size = size
        self.color(color)
        self.shape("circle")
        self.shapesize(size, size)
        self.penup()
        self.distance = distance
        self.angle = 0
        self.speed_val = speed
        self.parent = parent
        self.update_position()
        self.pendown()
        
    def update_position(self):
        if self.parent:
            x = self.parent.xcor() + self.distance * math.cos(math.radians(self.angle))
            y = self.parent.ycor() + self.distance * math.sin(math.radians(self.angle))
        else:
            x = self.distance * math.cos(math.radians(self.angle))
            y = self.distance * math.sin(math.radians(self.angle))
        self.goto(x, y)
        
    def move(self):
        self.angle += self.speed_val
        self.update_position()

mercury = CelestialBody("Mercury", 1.2, "darkgray", 60, 8)
venus = CelestialBody("Venus", 1.5, "goldenrod", 90, 3)
earth = CelestialBody("Earth", 1.7, "dodgerblue", 130, 2)
mars = CelestialBody("Mars", 1.3, "firebrick", 170, 1)
jupiter = CelestialBody("Jupiter", 3.5, "peru", 230, 0.5)
saturn = CelestialBody("Saturn", 3.0, "navajowhite", 300, 0.2)
uranus = CelestialBody("Uranus", 2.2, "lightseagreen", 370, 0.1)
neptune = CelestialBody("Neptune", 2.2, "royalblue", 430, 0.05)

saturn_ring = turtle.Turtle()
saturn_ring.shape("circle")
saturn_ring.shapesize(0.2, 4.5, 1)
saturn_ring.color("wheat")
saturn_ring.penup()

def draw_dashed_orbit(turtle, radius):
    turtle.penup()
    turtle.goto(0, -radius)
    for _ in range(72): 
        turtle.pendown()
        turtle.circle(radius, extent=2.5)  
        turtle.penup()
        turtle.circle(radius, extent=2.5)  

orbit_drawer = turtle.Turtle()
orbit_drawer.color("white")
orbit_drawer.penup()
orbit_drawer.hideturtle()
orbit_drawer.speed(0)
for planet in [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]:
    draw_dashed_orbit(orbit_drawer, planet.distance)

label = turtle.Turtle()
label.color("white")
label.penup()
label.hideturtle()
label.speed(0)

running = True
def stop_simulation():
    global running
    running = False

screen.listen()
screen.onkeypress(stop_simulation, "space")

while running:
    for planet in [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]:
        planet.move()
    
    saturn_ring.goto(saturn.pos())
    
    label.clear()
    for planet in [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]:
        x, y = planet.pos()
        label.goto(x, y - (planet.size * 10 + 5))
        font_size = max(8, int(planet.size * 4))
        label.write(planet.name, align="center", font=("Arial", font_size, "normal"))
    
    screen.update()
    time.sleep(0.01)

screen.bye()