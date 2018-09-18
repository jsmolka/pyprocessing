from pyprocessing import *


# Draw a cylinder centered on the y-axis, going down from y=0 to y=height.
# The radius at the top can be different from the radius at the bottom,
# and the number of sides drawn is variable.

def setup():
    size(400, 400)


def draw():
    background(0)
    lights()
    translate(width / 2, height / 2)
    rotateY(mouse.x * PI / width)
    rotateZ(mouse.y * -PI / height)
    noStroke()
    fill(255, 255, 255)
    translate(0, -40, 0)
    draw_cylinder(10, 180, 200, 16)  # Draw a mix between a cylinder and a cone
    # draw_cylinder(70, 70, 120, 16) # Draw a cylinder
    # draw_cylinder(0, 180, 200, 4) # Draw a pyramid


def draw_cylinder(top_radius, bottom_radius, tall, sides):
    angle = 0
    angle_increment = TWO_PI / sides
    beginShape(QUAD_STRIP)
    for i in range(sides + 1):
        # normal(cos(angle), sin(angle), 0)
        vertex(top_radius * cos(angle), 0, top_radius * sin(angle))
        vertex(bottom_radius * cos(angle), tall, bottom_radius * sin(angle))
        angle += angle_increment
    endShape()

    # If it is not a cone, draw the circular top cap
    if top_radius != 0:
        angle = 0
        beginShape(TRIANGLE_FAN)

        # Center point
        vertex(0, 0, 0)
        for i in range(sides + 1):
            vertex(top_radius * cos(angle), 0, top_radius * sin(angle))
            angle += angle_increment
        endShape()

    # If it is not a cone, draw the circular bottom cap
    if bottom_radius != 0:
        angle = 0
        beginShape(TRIANGLE_FAN)

        # Center point
        vertex(0, tall, 0)
        for i in range(sides + 1):
            vertex(bottom_radius * cos(angle), tall, bottom_radius * sin(angle))
            angle += angle_increment

        endShape()


run()
