f = open('inp.txt').read().split('\n\n')

coolString = f[0]
coolImg = f[1].split('\n')


def expand(img, s):  # Add 4 to each dimension axis
    height = len(img)
    width = len(img[0])
    outp = []
    for i in range(-2, height+2):
        row = ''
        for j in range(-2, width+2):
            if i < 0 or j < 0 or i >= height or j >= width:
                row += s
            else:
                row += img[i][j]
        outp.append(row)
    return outp


def faltning(img, coolString, x, y):
    res = ''
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            p = img[i][j]
            if p == '.':
                res += '0'
            elif p == '#':
                res += '1'
    num = int(res, 2)
    return coolString[num]


def do(img, string, s):
    height = len(img)
    width = len(img[0])
    outp = []
    for i in range(height):
        row = ''
        if i in [0, height-1]:
            row = s*width
        else:
            for j in range(width):
                if j in [0, width-1]:
                    row += s
                else:
                    r = faltning(img, string, j, i)
                    row += r
        outp.append(row)
    return outp


def countLit(img):
    height = len(img)
    width = len(img[0])
    s = 0
    for i in range(height):
        for j in range(width):
            if img[i][j] == '#':
                s += 1
    return s


for i in range(50):
    print(i)  # For user to know it's running ;)
    s1 = ''
    s2 = ''
    # Because the first index of the coolString is a #, the infinite extended region of the image will be alternating between '#' and '.'
    # We know when this happens, so we simulate this by extending with alternating characters and do the Faltning with alternating characters
    if i % 2 == 0:
        s1 = '.'
        s2 = '#'
    else:
        s1 = '#'
        s2 = '.'
    coolImg = expand(coolImg, s1)
    coolImg = do(coolImg, coolString, s2)

print(countLit(coolImg))
