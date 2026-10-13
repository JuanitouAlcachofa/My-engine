import basicRender
from geom import size, box, collision

def sRect(w, h, color):
    return [[color] * w for _ in range(h)]

X, N = "#FFD700", None
BOLA = [
    [N,X,X,X,N],
    [X,X,X,X,X],
    [X,X,X,X,X],
    [X,X,X,X,X],
    [N,X,X,X,N]
]

PIPE = sRect(w=10, h=25, color="#87D893")

class Escena:
    def __init__(self, fb):
        self.fb = fb
        self.scale = 1                                  # <- aqui decides que tan grande es
        self.w, self.h = size(BOLA, self.scale)         # tamano ya escalado
        self.x = -50                         # x, y = CENTRO de la bola
        self.y = 0
        self.xvel = 0
        self.yvel = 0
 
    def update(self, dt, teclas, pulsadas):
        fb = self.fb
        self.x += self.xvel * dt
        self.y += self.yvel * dt
 
        # bordes de la bola, calculados desde su centro
        left, top, right, bottom = box(self.x, self.y, self.w, self.h)
        if "w" in pulsadas:
            self.yvel += 8
            
        self.yvel -= 1
        self.y += self.yvel  
        
        if self.yvel <= -5:
            self.yvel = -5
        elif self.yvel >= 8: 
            self.yvel = 8
         
        self.x = max(fb.xmin  + self.w/2, min(self.x, fb.xmax - self.w/2))
        self.y = max(fb.ymin  + self.h/2, min(self.y, fb.ymax - self.h/2))
        
        
        
        
 
    def draw(self, fb):
        fb.blit(BOLA, self.x, self.y, self.scale, center=True)
        fb.blit(PIPE, 0,self.y, 1, center=True)
        