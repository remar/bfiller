from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def draw_string(c, x, y, s):
    c.drawString(x * cm, (29.7 - y) * cm, s)

c = canvas.Canvas("hello.pdf")
c.drawImage("img/fktimmar.png", 0, 0, 595.27, 841.89)
draw_string(c, 1.60, 8.58, "Edvin Waldh")
c.showPage()
c.save()
