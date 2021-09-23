# crypto_exchg_lens

**The initial steps of a Python interface to aggregate cryptocurrency holdings and exchange data in a consistent format from multiple exchange APIs.**

Very early days of the public version; currently, the functionality allows for pulling all holdings from both Bittrex and Coinbase exchanges, for account holders with active API credentials.

**Useage:**

```python
import pandas as pd
import bittrex_lens as btrx
import coinbase_lens as coin

# get instance of Bittrex wrapper
API_KEY_BITTREX = 'xxx'
API_SECRET_BITTREX = 'xxx'
btrx_lens = btrx.BittrexWrapper(STR_API_KEY_BITTREX, STR_API_SECRET_BITTREX)

# get instance of Coinbase wrapper
STR_API_KEY_COINBASE = 'xxx' 
STR_API_SECRET_COINBASE = 'xxx'
coin_lens = coin.CoinbaseWrapper(STR_API_KEY_COINBASE, STR_API_SECRET_COINBASE)

# get current balances from both exchanges, same DataFrame format
df_btrx_bals = btrx_lens.crypto_bals_all()
df_coin_bals = coin_lens.crypto_bals_all()
```

Both the Bittrex and Coinbase classes use the exchg_lens.Exchange class as an interface.