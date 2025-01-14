import math

from PyQt6.QtCharts import QChartView, QChart, QValueAxis, QLineSeries, QSplineSeries
from PyQt6.QtCore import Qt


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        delta_x = 0.1
        x_min = -2.5
        x_max = 3.0

        start = int(x_min / delta_x)
        end = int(x_max / delta_x)
        values_x = [i * delta_x for i in range(start, end)]

        values_sine = []
        for x in values_x:
            values_sine.append(x ** 3 - 2 * x ** 2 + 4 * x - 3)

        series_sinus = QLineSeries()
        series_sinus.setName("Polynom")

        for i in range(len(values_x)):
            series_sinus.append(values_x[i], values_sine[i])

        axis_x = QValueAxis()
        axis_x.setRange(x_min, x_max)
        axis_x.setTitleText("x-Achse")

        axis_y = QValueAxis()
        axis_y.setTitleText("y-Achse")

        q_chart = QChart()

        q_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        q_chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        q_chart.addSeries(series_sinus)

        series_sinus.attachAxis(axis_x)
        series_sinus.attachAxis(axis_y)

        self.setChart(q_chart)
