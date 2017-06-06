from visual import *
import math


scene1 = display(title="1", width=550, height=550, x=10, y=10, range=50)
scene2 = display(title="2", width=550, height=550, x=561, y=10, range=50)


#dla pierwszego okna

l = 10
m = 10

fi = pi - 0.1
teta = pi

fi_v = 0.0
teta_v = 0.0

fi_a = 0.0
teta_a = 0.0

#drugie
fi2 = pi - 0.1
teta2 = pi

fi_v2 = 0.0
teta_v2 = 0.0

fi_a2 = 0.0
teta_a2 = 0.0

#poczatkowe wartosci
cyl1 = cylinder(pos=(0,0,0), length = l, axis=(0,l,0), radius=0.1, display=scene1)
ball1 = sphere(pos=(0,l,0), radius=1, color=color.red, display=scene1)

cyl12 = cylinder(pos=(0,0,0), length = l, axis=(0,l,0), radius=0.1, display=scene2)
ball12 = sphere(pos=(0,l,0), radius=1, color=color.red, display=scene2)

cyl2 = cylinder(pos=(0,l,0), length = l, axis=(l*sin(fi), -l*cos(fi),0), radius=0.1, display=scene1)
ball2 = sphere(pos=(l*sin(fi)+ ball1.pos.x, -l*cos(fi) + ball1.pos.y, 0), radius=1, color=color.green, display=scene1)

cyl22 = cylinder(pos=(0,l,0), length = l, axis=(l*sin(fi), -l*cos(fi),0), radius=0.1, display=scene2)
ball22 = sphere(pos=(l*sin(fi)+ ball1.pos.x, -l*cos(fi) + ball1.pos.y, 0), radius=1, color=color.green, display=scene2)

dt = 0.005
g = 9.8
g2 = 9.8000000001


while 1:
    rate(1000)
    fi_a = (-g/l*(2*sin(fi) - sin(teta) * cos(fi - teta)) - 0.5 * teta_v * teta_v * sin(2*fi - 2*teta) - teta_v*teta_v *sin(fi-teta))/(1 + sin(fi - teta) * sin(fi-teta))
    teta_a = (-g/l*(2*sin(teta) - sin(fi) * cos(fi - teta)) - 0.5 * fi_v * fi_v * sin(2*fi - 2*teta) + 2*fi_v*fi_v*sin(fi-teta))/(1 + sin(fi - teta) * sin(fi-teta))

    fi_v = fi_v + fi_a * dt
    teta_v = teta_v + teta_a * dt

    fi = fi + fi_v * dt
    teta = teta + teta_v * dt

    cyl1.axis = vector(l*sin(fi), -l*cos(fi), 0)
    ball1.pos = vector(l*sin(fi), -l*cos(fi), 0)

    cyl2.pos = vector(l*sin(fi), -l*cos(fi), 0)
    cyl2.axis = vector(l*sin(teta), -l*cos(teta),0)
    ball2.pos = vector(l*sin(teta) + ball1.pos.x, -l*cos(teta) + ball1.pos.y, 0)

    #drugie okno
    fi_a2 = (-g2/l*(2*sin(fi2) - sin(teta2) * cos(fi2 - teta2)) - 0.5 * teta_v2 * teta_v2 * sin(2*fi2 - 2*teta2) - teta_v2*teta_v2 *sin(fi2-teta2))/(1 + sin(fi2 - teta2) * sin(fi2-teta2))
    teta_a2 = (-g2/l*(2*sin(teta2) - sin(fi2) * cos(fi2 - teta2)) - 0.5 * fi_v2 * fi_v2 * sin(2*fi2 - 2*teta2) + 2*fi_v2*fi_v2*sin(fi2-teta2))/(1 + sin(fi2 - teta2) * sin(fi2-teta2))

    fi_v2 = fi_v2 + fi_a2 * dt
    teta_v2 = teta_v2 + teta_a2 * dt

    fi2 = fi2 + fi_v2 * dt
    teta2 = teta2 + teta_v2 * dt

    cyl12.axis = vector(l*sin(fi2), -l*cos(fi2), 0)
    ball12.pos = vector(l*sin(fi2), -l*cos(fi2), 0)

    cyl22.pos = vector(l*sin(fi2), -l*cos(fi2), 0)
    cyl22.axis = vector(l*sin(teta2), -l*cos(teta2),0)
    ball22.pos = vector(l*sin(teta2) + ball12.pos.x, -l*cos(teta2) + ball12.pos.y, 0)
