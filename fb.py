import math

class FrameBuffer:
    def __init__(self, width, heigth, pixelSize, bColor="#000000", centered=True, y_up=True):
        self.pixelSize = pixelSize
        self.bColor = bColor
        self.width = width // pixelSize
        self.height = heigth // pixelSize
        self.y_up = y_up

        self.ox = self.width // 2 if centered else 0
        if centered:
            self.oy = self.height // 2
        else:
            self.oy = self.height if y_up else 0

        self.buffer = [[self.bColor for _ in range(self.width)] for _ in range(self.height)]

    @property
    def xmin(self):
        return -self.ox

    @property
    def xmax(self):
        return self.width - self.ox

    @property
    def ymin(self):
        return self.oy - self.height if self.y_up else -self.oy

    @property
    def ymax(self):
        return self.oy if self.y_up else self.height - self.oy

    def _celda(self, x, y):
        col = math.floor(x) + self.ox
        if self.y_up:
            row = self.oy - 1 - math.floor(y)
        else:
            row = math.floor(y) + self.oy
        if 0 <= col < self.width and 0 <= row < self.height:
            return col, row
        return None
    

    def save_pixel(self, x, y, color):
        c = self._celda(x, y)
        if c is not None:
            self.buffer[c[1]][c[0]] = color
    
    
    def drawRect(self, x, y, w, h, color):
        for j in range(h):
            for i in range(w):
                self.save_pixel(x+i, y+j, color)        
    

    def get_pixel(self, x, y):
        c = self._celda(x, y)
        return None if c is None else self.buffer[c[1]][c[0]]


    def clear(self):
        self.buffer = [[self.bColor for _ in range(self.width)] for _ in range(self.height)]


    def render(self, pequena, grande):
        filas = ["{" + " ".join(fila) + "}" for fila in self.buffer]
        pequena.put(" ".join(filas), to=(0, 0))
        grande.tk.call(grande.name, "copy", pequena.name,
                    "-zoom", self.pixelSize, self.pixelSize)

        
    def dump(self, x0=0, y0=0, w=60, h=30):
        for y in range(y0, min(y0 + h, self.height)):
            fila = ""
            for x in range(x0, min(x0 + w, self.width)):
                fila += "." if self.buffer[y][x] == self.bColor else "#"
            print(fila)
            

    def blit(self, sprite, x, y, scale=1, center=False):
        sh = len(sprite)
        if sh == 0 or scale <= 0:
            return
        sw = len(sprite[0])

        out_w = max(1, round(sw * scale))
        out_h = max(1, round(sh * scale))

        if center:
            x, y = x - out_w / 2, y - out_h / 2
        col = math.floor(x) + self.ox
        if self.y_up:
            row = self.oy - math.floor(y) - out_h
        else:
            row = math.floor(y) + self.oy
        x, y = col, row

        # Rango del sprite escalado que cae dentro del buffer (recorte)
        j0, j1 = max(0, -y), min(out_h, self.height - y)
        i0, i1 = max(0, -x), min(out_w, self.width - x)

        for j in range(j0, j1):
            fila_origen = sprite[min(int(j / scale), sh - 1)]
            py = y + j
            for i in range(i0, i1):
                color = fila_origen[min(int(i / scale), sw - 1)]
                if color is None:
                    continue
                self.buffer[py][x + i] = color