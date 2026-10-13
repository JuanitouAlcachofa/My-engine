"""Sistema del motor: ventana, framebuffer, bucle, tiempo y teclado.

No sabe nada de lo que se dibuja. La escena solo tiene que ofrecer dos metodos:
    update(dt, teclas, pulsadas)   -> actualiza el estado
    draw(fb)                       -> dibuja en el framebuffer
"""
import time
from tkinter import Tk, Label, PhotoImage
from fb import FrameBuffer


class Engine:
    def __init__(self, ancho=600, alto=400, pixelSize=4, fps=30, titulo="Motor", bg="black", centered=True, y_up=True):
        self.fps = fps
        self.titulo = titulo
        self.escena = None
        self.teclas = set()        # mantenidas en este momento
        self.pulsadas = set()      # recien pulsadas en este frame

        # --- ventana y lienzos (la ventana se crea ANTES de usar bind) ---
        self.window = Tk()
        self.window.title(titulo)
        self.window.config(bg="black")
        self.lienzo = PhotoImage(width=ancho, height=alto)        # la que se ve
        Label(self.window, image=self.lienzo, bg="black", bd=0).pack()

        # --- framebuffer (tamano logico) y su imagen intermedia ---
        self.fb = FrameBuffer(ancho, alto, pixelSize, centered=centered, y_up=y_up)
        self.pequena = PhotoImage(width=self.fb.width, height=self.fb.height)

        # --- teclado (un solo bind por evento: un segundo bind lo reemplazaria) ---
        self.window.bind("<KeyPress>", self._tecla_abajo)
        self.window.bind("<KeyRelease>", self._tecla_arriba)
        self.window.bind("<FocusOut>", lambda e: self.teclas.clear())
        self.window.focus_force()

        # --- medicion de tiempo / FPS ---
        self._t_anterior = time.perf_counter()
        self._frames = 0
        self._t_fps = self._t_anterior

    # ---------------------------------------------------------- teclado
    def _tecla_abajo(self, e):
        k = e.keysym.lower()
        if k not in self.teclas:         # ignora la repeticion automatica al mantener
            self.pulsadas.add(k)
        self.teclas.add(k)

    def _tecla_arriba(self, e):
        self.teclas.discard(e.keysym.lower())

    # ---------------------------------------------------------- bucle
    def run(self, escena):
        """Arranca el bucle con la escena dada. Bloquea hasta cerrar la ventana."""
        self.escena = escena
        self._t_anterior = time.perf_counter()
        self._t_fps = self._t_anterior
        self._frame()
        self.window.mainloop()

    def _frame(self):
        t = time.perf_counter()
        dt = min(t - self._t_anterior, 0.1)      # tope: evita saltos enormes tras una pausa
        self._t_anterior = t

        self.escena.update(dt, self.teclas, self.pulsadas)
        self.pulsadas.clear()                    # "pulsadas" solo vale durante un frame

        self.fb.clear()
        self.escena.draw(self.fb)
        self.fb.render(self.pequena, self.lienzo)

        # FPS promediados cada medio segundo
        self._frames += 1
        if t - self._t_fps >= 0.5:
            fps = self._frames / (t - self._t_fps)
            self.window.title(f"{self.titulo} - {fps:.0f} fps")
            self._frames = 0
            self._t_fps = t

        gastado = time.perf_counter() - t
        espera = max(1, int((1 / self.fps - gastado) * 1000))
        self.window.after(espera, self._frame)