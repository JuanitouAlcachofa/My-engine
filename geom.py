"""Ayudas geometricas generales.

Una "caja" es una tupla (izquierda, arriba, derecha, abajo).
"""


def size(sprite, scale=1):
    """(ancho, alto) de un sprite ya escalado, igual que lo calcula blit."""
    return (max(1, round(len(sprite[0]) * scale)),
            max(1, round(len(sprite) * scale)))


def box(cx, cy, w, h):
    """Caja de algo de tamano w x h cuyo CENTRO esta en (cx, cy)."""
    return (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)


def collision(a, b):
    """True si dos cajas se solapan."""
    return a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]