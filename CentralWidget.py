from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtCore import Qt, QDateTime, QPointF
from PyQt6.QtGui import QMouseEvent

import random


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        random.seed(QDateTime.currentMSecsSinceEpoch())

        self.__series_clicked = QLineSeries()
        self.__series_clicked.setName("Current Time - Clicked Value")

        self.__series_random = QLineSeries()
        self.__series_random.setName("Clicked Time - Random Value")

        axis_datetime = QDateTimeAxis()
        axis_datetime.setTitleText("Datum")

        start_date = QDateTime.currentDateTime().addSecs(-1 * 60 * 5)
        end_date = QDateTime.currentDateTime().addSecs(1 * 60 * 5)

        axis_datetime.setRange(start_date, end_date)

        axis_datetime.setFormat("hh:mm:ss")

        axis_dollar = QValueAxis()
        axis_dollar.setTitleText("Wertebereich")
        axis_dollar.setRange(1000, 2000)

        self.__chart = QChart()
        self.__chart.setTitle("Random numbers, dates & mouseEvents")

        self.__chart.addAxis(axis_datetime, Qt.AlignmentFlag.AlignBottom)
        self.__chart.addAxis(axis_dollar, Qt.AlignmentFlag.AlignLeft)

        self.__chart.addSeries(self.__series_clicked)
        self.__chart.addSeries(self.__series_random)

        self.__series_clicked.attachAxis(axis_datetime)
        self.__series_clicked.attachAxis(axis_dollar)

        self.__series_random.attachAxis(axis_datetime)
        self.__series_random.attachAxis(axis_dollar)

        self.setChart(self.__chart)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button().LeftButton:
            event.accept()

            new_value = self.__chart.mapToValue(event.pos().toPointF(), self.__series_clicked)
            new_point_clicked = QPointF(QDateTime.currentMSecsSinceEpoch(), new_value.y())
            self.__series_clicked.append(new_point_clicked)

            new_point_random = QPointF(new_value.x(), random.randrange(1000, 2000))
            for i in range(len(self.__series_random.points())):
                if self.__series_random.at(i).x() > new_point_random.x():
                    self.__series_random.insert(i, new_point_random)

                    return

            self.__series_random.append(new_point_random)
