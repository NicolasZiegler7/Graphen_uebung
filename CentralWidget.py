from PyQt6.QtCharts import QChartView, QChart, QValueAxis, QLineSeries, QSplineSeries
from PyQt6.QtCore import Qt


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        delta_x = 0.01
        x_min = -10
        x_max = 5

        start = int(x_min / delta_x)
        end = int(x_max / delta_x)
        values_x = [i * delta_x for i in range(start, end)]

        values_y = []
        for x in values_x:
            if x == 0.0:
                values_y.append(0.0)
            else:
                values_y.append(1 / x)

        series_spline = QLineSeries()
        series_spline.setName("Hyperbel")

        for i in range(len(values_x)):
            series_spline.append(values_x[i], values_y[i])

        axis_x = QValueAxis()
        axis_x.setRange(x_min, x_max)
        axis_x.setTitleText("x-Achse")

        axis_y = QValueAxis()
        axis_y.setTitleText("y-Achse")
        axis_y.setRange(-15, 15)

        q_chart = QChart()

        q_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        q_chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        q_chart.addSeries(series_spline)

        series_spline.attachAxis(axis_x)
        series_spline.attachAxis(axis_y)

        self.setChart(q_chart)
