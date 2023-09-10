import datetime
from backtesting import Backtest

from strategies.dca import DCA
from strategies.price_gaps import PriceGaps
from utils import get_dataframe

start = datetime.date(2013, 1, 1)
end = datetime.date(2023, 1, 1)
GOOG = get_dataframe('BTC-USD', start, end)


bt = Backtest(GOOG, DCA, commission=.002)
# print(bt.optimize(
#     **PriceGaps.get_optimize_params()
# ))
print(bt.run())