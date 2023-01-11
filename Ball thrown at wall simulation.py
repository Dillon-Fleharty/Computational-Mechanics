# This simple Program models a small ball being thrown at a wall
# and falling for one second. The rate is slowed down to show 
# gravitational force as the ball falls in the y-axis before and 
# after hitting the wall. It also generates some simple graphs 
# for position and velocity.

import vpython as vp
import numpy as np


#Initialize the sence (background)
scene = vp.canvas()

# Create ball size, velocity, and gravity
ball = vp.sphere(pos = vp.vector(-4,2,0), 
                 radius = .3, 
                 color = vp.color.green,
                 vel = vp.vector(15,0,0), 
                 gravity = vp.vector(0,9.8,0))

# Create Wall
wall = vp.box(pos = vp.vector(4,0,0), 
              size = vp.vector(0.01,10,10))

# Horizontal Position vs Time Graph
vp.graph(title = "Horizontal Position Vs. Time", 
         xtitle = "Time (s)",
         ytitle = "Position (m)")

xGraph = vp.gcurve(color = vp.color.blue)

# Vertical Position vs Time Graph
vp.graph(title = "Vertical Position Vs. Time", 
         xtitle = "Time (s)",
         ytitle = "Position (m)")

yGraph = vp.gcurve(color = vp.color.black)

# Horizontal Position vs Velocity Graph
vp.graph(title = "Horizontal Velocity Vs. Time", 
         xtitle = "Time (s)",
         ytitle = "Velocity (m/s)")

vxGraph = vp.gcurve(color = vp.color.black)

# Vertical Velocity Vs. Tim
vp.graph(title = "Velocity (m/s) Vs. Time", 
         xtitle = "Time (s)",
         ytitle = "Velocity (m/s)")

vyGraph = vp.gcurve(color = vp.color.black)

# Move the ball
t = 0
dt = .001
tmax = 1

while t < tmax: 
    vp.rate(100)

    # Set the ball in motion
    ball.pos = ball.pos + ball.vel*dt
    ball.vel = ball.vel - ball.gravity*dt
    # Verify position where bouncing occurs
    if ball.pos.x > (wall.pos.x - (ball.radius-.015)):
        ball.vel.x = -ball.vel.x
        
    # Make Plots for Graph
    xGraph.plot(t, ball.pos.x)
    yGraph.plot(t, ball.pos.y)
    vxGraph.plot(t, ball.vel.x)
    vyGraph.plot(t, ball.vel.y)
    
    t = t + dt

# end program



