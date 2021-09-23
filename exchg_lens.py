
import pandas as pd

class Exchange:
    """
        a parent class (interface) for exchange wrappers
    """

    def crypto_bals_all(self) -> pd.DataFrame:
        """
            return a data frame of all current crypto holdings.

            cols: [date_time, exchange, coin, usd_amt]
        """

    def all_quotes_usd(self) -> pd.DataFrame:
        """get latest quotes in usd for all coins on exchange

        Returns:
            pd.DataFrame: columns [date_time, coin_symb, usd_val]
        """