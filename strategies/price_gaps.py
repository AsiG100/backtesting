from backtesting import Strategy


class PriceGaps(Strategy):
    decrease = 1.08
    increase = 1.02
    limit = 1.01
    highs = []

    def init(self):
        super().init()

    def next(self):
        # yesterday's price is 5% higher, buy and add tp for 3% higher
        today_price = self.data.Open[-1]

        if not self.highs or today_price > self.highs[-1]:
            self.highs.append(today_price)

        if self.highs[-1] >= today_price * self.decrease:
            self.buy(limit=today_price * self.limit, tp=today_price * self.increase)

    @staticmethod
    def get_optimize_params():
        percentage_range = [x / 100 for x in range(102, 110)]

        return {
            'constraint': lambda p: p.decrease > p.increase,
            'decrease': percentage_range,
            'increase': percentage_range,
            'return_heatmap': True
        }