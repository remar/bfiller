from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import datetime
from AnnotatedWeek import AnnotatedWeek

class ReportGenerator(object):
    def generate(self, month):
        self._employer_name = "Edvin Waldh"
        self._employer_number = "200701122814"
        self._employee_name = "Susanne Waldh"
        self._employee_number = "198104215945"
        self._employee_tel = "0705 - 16 90 69"

        self.canvas = canvas.Canvas(str(month.year)+str(month.month)+".pdf")

        self._make_fk_page(month)

        self._make_kommun_pages(month)

        self.canvas.save()

    def _make_fk_page(self, month):
        self._draw_background("img/fktimmar.png")
        self._draw_string(10.70, 3.12, "  ".join(str(month.year)))
        self._draw_string(13.16, 3.12, "  ".join(str(month.month)))
        self._draw_string(1.60, 8.58, self._employer_name)
        self._draw_string(15.24, 8.58, self._employer_number)
        self._draw_string(1.60, 27.0, self._employee_name)
        self._draw_string(15.24, 27.0, self._employee_number)
        datum = datetime.datetime.now().strftime("%Y-%m-%d")
        self._draw_string(1.80, 28.1, datum)
        self._draw_string(15.24, 28.0, self._employee_tel)

        for i in xrange(1, 32):
            day = month.get_day(i)
            if day != None:
                x, y = self._get_offset_for_position(i)
                self._draw_string(x, y, str(i))
                self._draw_string(x + 0.8, y, str(day.get_start()))
                self._draw_string(x + 2.35, y, str(day.get_end()))
                self._draw_string(x + 4, y, str(self._format_hours(day.get_length())))

        self._draw_string(14.6, 24.7, self._format_hours(month.get_total_time()))

        self.canvas.showPage()

    def _make_kommun_pages(self, month):
#        self._draw_background("img/kommuntimmar.png")
#        self.canvas.showPage()
#        self._get_week_numbers_pairwise
        week_numbers = month.get_week_numbers()
        pairwise = zip(week_numbers[::2], week_numbers[1::2])
        if len(week_numbers) % 2 == 1:
            pairwise.append((week_numbers[-1], None))

        for week_pair in pairwise:
            first = month.get_week(week_pair[0])
            second = month.get_week(week_pair[1]) if week_pair[1] != None else None
            self._make_kommun_page(first, second, month)
            

        for week_number in month.get_week_numbers():
            week = month.get_week(week_number)

    def _make_kommun_page(self, first, second, month):
        self._draw_background("img/kommuntimmar.png")

        self._draw_string(1.89, 5.26, self._employee_name)
        self._draw_string(13.30, 5.26, self._employee_number)
        self._draw_string(2.70, 6.26, str(month.year))
        self._draw_string(5.85, 6.26, str(month.month))
        self._draw_string(7.65, 6.26, self._employer_name)

        self._print_week_in_kommun_page(first, 0)
        if second != None:
            self._print_week_in_kommun_page(second, 1)
        self.canvas.showPage()

    def _print_week_in_kommun_page(self, week, offset):
        start = week.get_first_valid_day()
        end = week.get_last_valid_day()
        date = week.get_earliest_day_in_month()
        for day in xrange(start, end + 1):
            week_day = week.get_day(day)
            if week_day == None:
                continue
            x, y = self._get_kommun_offset_for_day(day + offset * 7)
            self._draw_string(x, y, str(date))
            self._draw_string(x + 1.0, y, str(week_day.get_start()))
            self._draw_string(x + 2.26, y, str(week_day.get_end()))
            date += 1

    def _draw_background(self, image):
        self.canvas.drawImage(image, 0, 0, 595.27, 841.89)

    def _draw_string(self, x, y, s):
        self.canvas.drawString(x * cm, (29.7 - y) * cm, s)

    def _get_offset_for_position(self, position):
        if position < 17:
            return 1.62, 14.40 + (position - 1) * 0.674
        else:
            return 10.66, 14.40 + (position - 17) * 0.674

    def _get_kommun_offset_for_day(self, day):
        return (3.06, 8.93 + 1.1*day)

    def _format_hours(self, hours):
        lookup = {0: "0", 5: "08", 10: "17", 15: "25", 20: "33", 25: "42",
                  30: "5", 35: "58", 40: "66", 45: "75", 50: "83", 55: "92"}
        return str(hours.get_hours()) + "." + lookup[hours.get_minutes()]
