from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtCore import Qt, QDateTime, QTimer, pyqtSlot
from PyQt6.QtGui import QMouseEvent


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.changeAxisRange)

        self.__series = QLineSeries()
        self.__series.setName("Goldpreisentwicklung in $")

        self.__axis_x = QDateTimeAxis()
        self.__axis_x.setTitleText("Datum")
        self.__axis_x.setFormat("hh:mm:ss")
        self.__axis_x.setMin(QDateTime.currentDateTime().addSecs(-60 * 10))

        self.changeAxisRange()

        axis_dollar = QValueAxis()
        axis_dollar.setTitleText("Goldpreis in $")
        axis_dollar.setRange(1250, 2750)

        self.__chart = QChart()
        self.__chart.setTitle("Goldpreisentwicklung")

        self.__chart.addAxis(self.__axis_x, Qt.AlignmentFlag.AlignBottom)
        self.__chart.addAxis(axis_dollar, Qt.AlignmentFlag.AlignLeft)

        self.__chart.addSeries(self.__series)

        self.__series.attachAxis(self.__axis_x)
        self.__series.attachAxis(axis_dollar)

        self.setChart(self.__chart)

        self.__timer.start(1000)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button().LeftButton:
            event.accept()

            new_value = self.__chart.mapToValue(event.pos().toPointF(), self.__series)

            for i in range(len(self.__series.points())):
                if self.__series.at(i).x() > new_value.x():
                    self.__series.insert(i, new_value)

                    return

            self.__series.append(new_value)

    @pyqtSlot()
    def changeAxisRange(self):
        end_date = QDateTime.currentDateTime().addSecs(60 * 10)

        self.__axis_x.setMax(end_date)
