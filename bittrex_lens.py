
import pandas as pd
from datetime import datetime as dt

import bittrex

from . import exchg_lens
# import exchg_lens


class BittrexWrapper(exchg_lens.Exchange):
    def __init__(self, api_key: str, api_secret: str):
        self.client = bittrex.Bittrex(api_key, api_secret)

    def crypto_bals_all(self) -> pd.DataFrame:
        df_bals_raw = self.df_get_bittrex_balances_raw()
        df_all_coins = self.all_quotes_usd()
        dfm = df_bals_raw.merge(df_all_coins, left_on = 'Currency', right_on = 'coin_symb', how = 'inner')
        dfm['usd_amt'] = dfm['Balance'] * dfm['usd_val']
        dfm['exchange'] = 'Bittrex'
        return dfm[['date_time', 'exchange', 'coin_symb', 'usd_amt']]

    def all_quotes_usd(self) -> pd.DataFrame:
        df_all_quotes = self.df_get_bittrex_market_summaries_raw()
        lst_bool_btc = ['BTC-' in mkt for mkt in df_all_quotes['MarketName']]
        df_btc_base = df_all_quotes[lst_bool_btc]
        usd_btc = df_all_quotes[df_all_quotes['MarketName']=='USD-BTC']['Last'].values[0]
        usd_val = [quote * usd_btc for quote in df_btc_base['Last']]
        df_btc_base['usd_val'] = usd_val
        df_btc_base['Created'] = dt.now()
        df_btc_base['coin_symb'] = [symb.split('-')[1] for symb in df_btc_base['MarketName']]
        df_btc_base.rename(columns = {'Created':'date_time'}, inplace=True)
        return df_btc_base[['date_time', 'coin_symb', 'usd_val']]

    # region GET RAW BITTREX DATA INTO DATA FRAMES

    # helper func, convert 'result' from api call to df, return it
    def df_bittrex_result_raw(self, dct_bittrex_response):
        dct_btrx_result = dct_bittrex_response['result']
        return pd.DataFrame(dct_btrx_result)


    def df_get_bittrex_balances_raw(self):
        return self.df_bittrex_result_raw(self.client.get_balances())


    def df_get_bittrex_currencies_raw(self):
        return self.df_bittrex_result_raw(self.client.get_currencies())


    def df_get_bittrex_market_summaries_raw(self):    
        return self.df_bittrex_result_raw(self.client.get_market_summaries())


    def df_get_bittrex_deposit_history_raw(self):
        return self.df_bittrex_result_raw(self.client.get_deposit_history())


    def df_get_bittrex_withdrawal_history_raw(self):
        return self.df_bittrex_result_raw(self.client.get_withdrawal_history())


    def df_get_bittrex_order_history_raw(self):
        return self.df_bittrex_result_raw(self.client.get_order_history())

    # endregion GET RAW BITTREX DATA INTO DATA FRAMES


