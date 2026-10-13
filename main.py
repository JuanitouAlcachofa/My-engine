from engine import Engine
from scenes.leap import Escena      # <- para cambiar de escena, cambia solo esta línea

motor = Engine(ancho=600, alto=400, pixelSize=4, fps=30, titulo="Holaaa", bg="#010B1E",centered=True, y_up=True)
motor.run(Escena(motor.fb))