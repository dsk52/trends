from pytrends.request import TrendReq
import matplotlib.pyplot as plt


class PytrendsSearch(object):
    def __init__(self):
        self.pytrends = TrendReq(hl='ja-JP', tz=360)
        self.geo = 'JP'

    def search_result(self, keywords):
        pytrends = TrendReq(hl='ja-JP', tz=360)
        pytrends.build_payload(
            keywords,
            timeframe='2014-01-01 2018-09-30',
            geo='JP')
        df = pytrends.interest_over_time()
        df.plot(figsize=(15, 3), lw=.7)
        plt.show()


if __name__ == '__main__':
    keyword_list = ["Python"]

    print('============= Start Search ===================')
    df = PytrendsSearch().search_result(keyword_list)
