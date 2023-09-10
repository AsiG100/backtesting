import datetime

from backtesting import Strategy


class DCA(Strategy):
    time_period = 7
    limit = 1.03
    buy_dates = []

    def init(self):
        super().init()

    def next(self):
        date = self.data.index.date[-1]
        time_gap = datetime.timedelta(days=self.time_period)

        if not self.buy_dates or self.buy_dates[-1] + time_gap <= date:
            self.buy()
            self.buy_dates.append(date)

    @staticmethod
    def get_optimize_params():
        percentage_range = [x / 100 for x in range(102, 110)]

        return {
            'constraint': lambda p: p.decrease > p.increase,
            'decrease': percentage_range,
            'increase': percentage_range,
            'return_heatmap': True
        }