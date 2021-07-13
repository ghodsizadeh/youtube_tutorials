import pandas as pd
import requests 
from io import StringIO


class HandleStock:
    def __init__(self,id:int) -> None:
        self.id = id
        df = self.get_stock()
        self.df = df


    def get_stock(self):

        base_url = f'http://www.tsetmc.com/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i={self.id}'
        r = requests.get(base_url)
        csv_buffer = StringIO(r.text)
        df = pd.read_csv(csv_buffer)
        df.columns = [c[1:-1].lower() for c in df.columns]

        return df
    
    def get_analysis(self):
        df = self.df
        start_date = df.iloc[-1].dtyyyymmdd
        max_price = df.close.max()
        min_price = df.close.min()
        tmp_df = df.set_index('dtyyyymmdd')
        last_10_days_price = tmp_df.iloc[:10].close
        last_10_days_price =  last_10_days_price.to_list()
        response = {'max_price ': float(max_price), 'min_price': float(min_price), "last_10_day":last_10_days_price, 'start_date': float(start_date)}
        return response




if __name__ == "__main__":
    stock_id = 35700344742885862
    hs = HandleStock(id =stock_id)
    print(hs.get_analysis())