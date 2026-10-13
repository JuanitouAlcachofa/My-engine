import basicRender
from geom import size, box, collision

X, N = "#FFD700", None
BOLA = [
    [N,X,X,X,N],
    [X,X,X,X,X],
    [X,X,X,X,X],
    [X,X,X,X,X],
    [N,X,X,X,N]
]

class Escena:
    def __init__(self, fb):
        self.fb = fb
        self.scale = 1                                  # <- aqui decides que tan grande es
        self.w, self.h = size(BOLA, self.scale)         # tamano ya escalado
        self.x = fb.width / 2                           # x, y = CENTRO de la bola
        self.y = fb.height / 2
        self.xvel = 40
        self.yvel = 30
 
    def update(self, dt, teclas, pulsadas):
        self.x += self.xvel * dt
        self.y += self.yvel * dt
 
        # bordes de la bola, calculados desde su centro
        left, top, right, bottom = box(self.x, self.y, self.w, self.h)
 
        if left < 0:
            self.x = self.w / 2                         # el centro queda a media anchura de la pared
            self.xvel = abs(self.xvel)
        elif right > self.fb.width:
            self.x = self.fb.width - self.w / 2
            self.xvel = -abs(self.xvel)
 
        if top < 0:
            self.y = self.h / 2
            self.yvel = abs(self.yvel)
        elif bottom > self.fb.height:
            self.y = self.fb.height - self.h / 2
            self.yvel = -abs(self.yvel)
 
    def draw(self, fb):
        fb.blit(BOLA, self.x, self.y, self.scale, center=True)