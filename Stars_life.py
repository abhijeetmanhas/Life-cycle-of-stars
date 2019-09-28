# Life-cycle-of-stars
#Astrohack Project
from vpython import *
win= 500

L=50
animation = canvas( width=win, height=win, align='left')
animation.range= L
animation.title= 'LIFE CYCLE OF STARS'
s='''    EARLY LIFE
    All stars have similar life stages until the star reaches the red-giant stage.
    Eventually the temperature reaches roughly 15 million degrees and fusion starts.
    The star begins to glow brightly and contracts.
    It is now a star, which will shine for millions to billions of years.
    As the star ages, it converts hydrogen to helium in its core by the process of fusion. 
    When the hydrogen supply runs out, the core of the star becomes unstable and contracts as the outer shell expands. 
    As it cools and expands in this way, it starts to glow red.
    At this point, the star has reached the red-giant phase.
'''
animation.caption=s

gray=color.gray(0.7)

Natoms=1000
mass = 4E-3/6E23 # helium mass
Ratom = 0.09 # wildly exaggerated size of helium atom
k = 1.4E-23 # Boltzmann constant
T = 300 # around room temperature
dt = 1E-5
pavg = sqrt(2*mass*1.5*k*T) # average kinetic energy p**2/(2mass) = (3/2)kT
Atoms = []
p = []
apos = []
pavg = sqrt(2*mass*1.5*k*T) # average kinetic energy p**2/(2mass) = (3/2)kT
    
for i in range(Natoms):
    x = L*random()-L/2
    y = L*random()-L/2
    z = L*random()-L/2
    i == 0
    Atoms.append(sphere(pos=vector(x,y,z), radius=Ratom, color=gray))
    apos.append(vec(x,y,z))
    theta = pi*random()
    phi = 2*pi*random()
    px = pavg*sin(theta)*cos(phi)
    py = pavg*sin(theta)*sin(phi)
    pz = pavg*cos(theta)
j=0.2
k=1
nebula=sphere(pos=vector(-1,0,0),radius=10,color=color.yellow, opacity=j)

for j in range(0,10):
    rate(10)
    nebula.opacity= nebula.opacity+ 0.3
    
    while(k<=100):
        rate(150)
        nebula.radius=nebula.radius-0.1
        if nebula.radius<=3:
            break
        else:
            continue
v='''   LOW MASS STARS
    Stars that are approximately 10 times the size of the sun or smaller are called low-mass stars.
    After helium is fused into carbon, the core of the star collapses once more. 
    As it contracts, the outer part of the star is blown outwards.
    This forms a planetary nebula.
    As it cools down, the core of the star that remains forms a white dwarf.
    As it cools further, it may form what is known as a black dwarf.
'''
animation.caption=v

nebula=sphere(pos=vector(-1,0,0),radius=8,color=color.gray(0.7), opacity=0.7)
for j in range(0,10):
    rate(10)
    nebula.opacity= nebula.opacity+ 0.3
    
    while(k<=100):
        rate(150)
        nebula.radius=nebula.radius-0.1
        if nebula.radius<=3:
            break
        else:
            continue

z='''   HIGH MASS STARS
    As larger stars reach the red-giant phase, their temperature increases as helium is fused into carbon.
    Core temperature increases, with fusion forming oxygen, nitrogen and iron. When the star core converts to iron, fusion ceases.
    Iron is too stable and it takes more energy to fuse iron than is liberated.
    After fusion stops, the star collapses. 
    Temperatures exceed 100 billion degrees and the expansive forces overcome the contracting ones.
    The heart of the star explodes outward to form an explosion known as a supernova.
    As this explosion tears through the outer shells of the star, fusion occurs once more. 
    Through this release of energy, the supernova creates heavy elements.
    If the remnant of the explosion is greater than 1.4 to three solar masses, it will become a neutron star.
    If it is about three solar masses, the star will end its life as a black hole.
'''
animation.caption=z

nebula=sphere(pos=vector(-1,0,0),radius=3,color=color.red, opacity=0.7)
for j in range(0,10):
    rate(10)
    nebula.opacity= nebula.opacity+ 0.3
    
    while(k<=100):
        rate(150)
        nebula.radius=nebula.radius+0.1
        if nebula.radius<=12:
            break
        else:
            continue
        
nebula=sphere(pos=vector(-1,0,0),radius=12,color=color.black)

for i in range(Natoms):
    x = L*random()-L/2
    y = L*random()-L/2
    z = L*random()-L/2
    i == 0
    Atoms.append(sphere(pos=vector(x,y,z), radius=Ratom, color=color.red))
    apos.append(vec(x,y,z))
    theta = pi*random()
    phi = 2*pi*random()
    px = pavg*sin(theta)*cos(phi)
    py = pavg*sin(theta)*sin(phi)
    pz = pavg*cos(theta)
