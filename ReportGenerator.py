from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import datetime

class ReportGenerator(object):
    def generate(self, month):
        self.canvas = canvas.Canvas(str(month.year)+str(month.month)+".pdf")

        self._make_fk_page(month)

        self.canvas.save()

    def _make_fk_page(self, month):
        self.canvas.drawImage("img/fktimmar.png", 0, 0, 595.27, 841.89)
        self._draw_string(10.70, 3.12, "  ".join(str(month.year)))
        self._draw_string(13.16, 3.12, "  ".join(str(month.month)))
        self._draw_string(1.60, 8.58, "Edvin Waldh")
        self._draw_string(15.24, 8.58, "200701122814")
        self._draw_string(1.60, 27.0, "Susanne Waldh")
        self._draw_string(15.24, 27.0, "198104215945")
        datum = datetime.datetime.now().strftime("%Y-%m-%d")
        self._draw_string(1.80, 28.1, datum)
        self._draw_string(15.24, 28.0, "0705 - 16 90 69")

        for i in xrange(1, 32):
            day = month.get_day(i)
            if day != None:
                x, y = self._get_offset_for_position(i)
                self._draw_string(x, y, str(i))
                self._draw_string(x + 1.0, y, str(day.get_start()))
                self._draw_string(x + 2.35, y, str(day.get_end()))
                self._draw_string(x + 4, y, str(self._format_hours(day.get_length())))

        self._draw_string(14.6, 24.7, self._format_hours(month.get_total_time()))

        self.canvas.showPage()

    def _draw_string(self, x, y, s):
        self.canvas.drawString(x * cm, (29.7 - y) * cm, s)

    def _get_offset_for_position(self, position):
        if position < 17:
            return 1.62, 14.40 + (position - 1) * 0.674
        else:
            return 10.66, 14.40 + (position - 17) * 0.674

    def _format_hours(self, hours):
        lookup = {0: "0", 5: "08", 10: "17", 15: "25", 20: "33", 25: "42",
                  30: "5", 35: "58", 40: "66", 45: "75", 50: "83", 55: "92"}
        return str(hours.get_hours()) + "." + lookup[hours.get_minutes()]
