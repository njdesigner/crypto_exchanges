
import pandas as pd
from datetime import datetime as dt
from coinbase.wallet.client import Client

from . import exchg_lens
# import exchg_lens

class CoinbaseWrapper(exchg_lens.Exchange):
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)

    def crypto_bals_all(self) -> pd.DataFrame:
        df_hldgs = self.all_quotes_usd()
        return df_hldgs[df_hldgs['usd_amt'] > 0]

    def all_quotes_usd(self) -> pd.DataFrame:
        lst_all_raw = self.client.get_accounts(limit=100).data
        lst_curr_bals = [(l.currency, l.native_balance.amount) for l in lst_all_raw]
        lst_curr, lst_amt = map(list, zip(*lst_curr_bals))
        lst_amt = [float(x) for x in lst_amt]
        df = pd.DataFrame({'coin_symb': lst_curr, 'usd_amt': lst_amt})
        df['date_time'] = dt.now()
        df['exchange'] = 'Coinbase'
        return df[['date_time', 'exchange', 'coin_symb', 'usd_amt']]
