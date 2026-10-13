# Motor Gráfico con TkinterE
Es un proyecto que estoy desarrollando porque se me dió la gana y pues hice mi propio motor gráfico desde 0 (maso menos). 

## Características
- Está hecho a base de la librería Tkinter
- **Framebuffer** integrado: matriz de colores la cual puedes controlar como quieras con `clear` y `render`.
- **Resolución lógica** (`pixelSize`): Con una resolución deseada pero con capacidad de ampliar los pixeles.
- **Primitivas**: funciones como `save_pixel` y `get_pixel` y lineas mediante Bresenham.
- **Sistema de coordenadas** configurable: origen desde el centro o esquina, `y` hacia arriba o hacia abajo y límites en las coordenadas (`xmax`,`xmin`,`ymax`,`ymin`)
- **Sprites con** `blit`: Matrices de colores con transparencia (`None`), escala, anclaje y recorte automático en los bordes de la pantalla. 

- Un bucle principal con limite de FPS y **delta time**
- **Teclado** con dos niveles: teclas mantenidas (`teclas`) y teclas recién pulsadas (`pulsadas`)

- Una separación entre sistema (`engine.py`,`fb.py`), y **escenas** (carpeta `scenes/`, estructurado con `init`, `update` y `draw`) y el un `main.py` decide cual ejecutar.
- Utilidades de geometría (`geom.py`) *(aun falta pulir)*: tamaño de un sprite, caja de colisión y detección de choque de rectángulos.

