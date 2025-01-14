import math

from PyQt6.QtCharts import QChartView, QChart, QValueAxis, QLineSeries, QSplineSeries
from PyQt6.QtCore import Qt


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        delta_x = 0.02
        x_min = -1.0 * math.pi  # -3.14...
        x_max = 2.0 * math.pi  # 6.28...

        start = int(x_min / delta_x)
        end = int(x_max / delta_x)
        values_x = [i * delta_x for i in range(start, end)]

        values_sine = []
        for x in values_x:
            values_sine.append(math.sin(x))

        values_cosine = []
        for x in values_x:
            values_cosine.append(math.cos(x))

        series_sinus = QLineSeries()
        series_sinus.setName("Sinus")

        series_cosine = QLineSeries()
        series_cosine.setName("Cosinus")

        for i in range(len(values_x)):
            series_sinus.append(values_x[i], values_sine[i])
            series_cosine.append(values_x[i], values_cosine[i])

        axis_x = QValueAxis()
        axis_x.setRange(x_min, x_max)
        axis_x.setTitleText("x-Achse")

        axis_y = QValueAxis()
        axis_y.setTitleText("y-Achse")
        axis_y.setRange(-1, 1)

        q_chart = QChart()

        q_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        q_chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        q_chart.addSeries(series_sinus)
        q_chart.addSeries(series_cosine)

        series_sinus.attachAxis(axis_x)
        series_sinus.attachAxis(axis_y)

        series_cosine.attachAxis(axis_x)
        series_cosine.attachAxis(axis_y)

        self.setChart(q_chart)
