f = open('./inp.txt').read().split('target area: ')[1]

x,y = f.split(', ')
xs,ys = x.split('..'), y.split('..')
x1 = int(xs[0][2:])
x2 = int(xs[1])
y1 = int(ys[0][2:])
y2 = int(ys[1])

xRange = list(range(x1,x2+1))
yRange = list(range(y1,y2+1))

xs = []
ys = []

def checkX(xRange,xVel):
    global xs
    org = xVel
    xPos = 0
    while True:
        xPos += xVel
        if xVel > 0:
            xVel -= 1
        if xPos > xRange[-1]:
            return False
        if xPos in xRange:
            xs.append(org)
            return True

def checkY(yRange,yVel):
    org = yVel
    yPos = 0
    while True:
        yPos += yVel
        yVel -= 1
        if yPos < yRange[0]:
            return False
        if yPos in yRange:
            ys.append(org)
            return True

def maxY(yVel):
    return int(yVel*(yVel+1)/2)

def minX(xRange):
    for x in range(10000):
        if x*(x+1)/2 >= xRange[0]: # Max xPos is the sum from 1 to xVel
            return x

def checkXY(xVel,yVel,xRange,yRange):
    org = yVel
    xPos = 0
    yPos = 0
    while True:
        xPos += xVel
        yPos += yVel
        if xVel > 0:
            xVel -= 1
        yVel -= 1
        if xPos in xRange and yPos in yRange:
            return True
        if xPos > xRange[-1] or yPos < yRange[0]:
            return False

x0 = minX(xRange)

for x in range(x0, 200): # The range maxes for x and y might have to change a bit depending on your input
    checkX(xRange,x)

for y in range(-200, 200): # Now we have to also check the negative y's
    checkY(yRange,y)

s = 0

for x in xs:
    for y in ys:
        if checkXY(x,y,xRange,yRange):
            s += 1

print(s)