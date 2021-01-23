from binance.client import Client
API_KEY = 'DW63JPveYTDCPg0sjsxsW0zbj76G3BbDSoGVUp1HccCtVzmOn9C1NZjBCBLXPrTt'
API_SECRET = '9QWr2ESkt080VwzLXCUqy9RViG6Nypy91F4wkIYYaFl3ZSDwsibAevq22gokzpjK'
client = Client(API_KEY,API_SECRET)

prices = client.get_all_tickers()
info = client.get_account()
exchange_info = client.get_exchange_info()
symbols = exchange_info['symbols']        

infoo = client.get_symbol_info('BNBBTC')

# print(info)

orders = client.get_all_orders(symbol='BNBBTC', limit=10)
print(exchange_info)
# {'symbol': 'BTCUSDT', 'status': 'TRADING', 'baseAsset': 'BTC', 'baseAssetPrecision': 8, 'quoteAsset': 'USDT', 'quotePrecision': 8, 'quoteAssetPrecision': 8, 'baseCommissionPrecision': 8, 'quoteCommissionPrecision': 8, 'orderTypes': ['LIMIT', 'LIMIT_MAKER', 'MARKET', 'STOP_LOSS_LIMIT', 'TAKE_PROFIT_LIMIT'], 'icebergAllowed': True, 'ocoAllowed': True, 'quoteOrderQtyMarketAllowed': True, 'isSpotTradingAllowed': True, 'isMarginTradingAllowed': True, 'filters': [{'filterType': 'PRICE_FILTER', 'minPrice': '0.01000000', 'maxPrice': '1000000.00000000', 'tickSize': '0.01000000'}, {'filterType': 'PERCENT_PRICE', 'multiplierUp': '5', 'multiplierDown': '0.2', 'avgPriceMins': 5}, {'filterType': 'LOT_SIZE', 'minQty': '0.00000100', 'maxQty': '9000.00000000', 'stepSize': '0.00000100'}, {'filterType': 'MIN_NOTIONAL', 'minNotional': '10.00000000', 'applyToMarket': True, 'avgPriceMins': 5}, {'filterType': 'ICEBERG_PARTS', 'limit': 10}, {'filterType': 'MARKET_LOT_SIZE', 'minQty': '0.00000000', 'maxQty': '136.73172611', 'stepSize': '0.00000000'}, {'filterType': 'MAX_NUM_ORDERS', 'maxNumOrders': 200}, {'filterType': 'MAX_NUM_ALGO_ORDERS', 'maxNumAlgoOrders': 5}], 'permissions': ['SPOT', 'MARGIN']}
