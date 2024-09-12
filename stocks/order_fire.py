import requests
import json

def create_payload(transaction_type, strategy_name, symbol, strike, selected_series, order_type, price,  qty):
    if transaction_type == 'BUY':
        payload = {
            "trans_type": "BUY",
            "st": strategy_name,
            "symbol": symbol,
            "buy_strikes": strike,
            "expiry_date": selected_series,
            "order_t": order_type,
            "price": price,
            # "sl":trigger_price,
            # "tgt":target_price,
            "multix":str(qty)
        }
    # elif transaction_type == 'BUYTRADE':
    #     payload = {
    #         "trans_type": "TRADE",
    #         "st": strategy_name,
    #         "symbol": symbol,
    #         "buy_strikes": strike,
    #         "expiry_date": selected_series,
    #         "order_t": 'm',
    #         "price": '0',
    #         "multix": str(qty)
    #     }
    elif transaction_type == 'SELL':
        payload = {
            "trans_type": "TRADE",
            "st": strategy_name,
            "symbol": symbol,
            "sell_strikes": strike,
            "expiry_date": selected_series,
            "order_t": 'm',
            "price": '0',
            "multix":str(qty)
        }
    # elif transaction_type == 'EXIT':
    #     payload = {
    #         "trans_type": "EXIT",
    #         "st": strategy_name,
    #         "symbol": symbol,
    #         # "expiry_date": selected_series,
    #         # "order_t": order_type
    #     }
    # elif transaction_type == 'CANCELALL':
    #     payload = {
    #         "trans_type": "CANCELALL",
    #         "st": strategy_name,
    #         "symbol": symbol,
    #         # "expiry_date": selected_series,
    #         # "order_t": order_type
    #     }
    else:
        raise ValueError("Invalid transaction type: "+transaction_type)



    return json.dumps(payload)


def send_payload(payload, timeout=None):
    print(payload)
    try:
        x = requests.get(payload, verify=False, timeout=timeout)
        print(x.text)
    except requests.exceptions.Timeout:
        print.error("Request timed out!")
    except Exception as e:
        print.error("Fatal error occurred: " + str(e))


def send_transaction(transaction_type, strategy_name, symbol, strike, selected_series, order_type, price, qty):

    payload = create_payload(transaction_type, strategy_name, symbol, strike, selected_series, order_type, price, qty)
    url = 'http://gltrades.me/tvTestGeneral?content='
    send_payload(url + payload, timeout=10)


def create_payload(transaction_type, strategy_name, symbol, strike, selected_series, order_type, price,  qty):
    if transaction_type == 'BUY':
        payload = {
            "trans_type": "BUY",
            "st": strategy_name,
            "symbol": symbol,
            "buy_strikes": strike,
            "expiry_date": selected_series,
            "order_t": order_type,
            "price": price,
            # "sl":trigger_price,
            # "tgt":target_price,
            "multix":str(qty)
        }
    elif transaction_type == 'BUY':
        payload = {
            "trans_type": "TRADE",
            "st": strategy_name,
            "symbol": symbol,
            "buy_strikes": strike,
            "expiry_date": selected_series,
            "order_t": 'm',
            "price": '0',
            "multix": str(qty)
        }
    elif transaction_type == 'SELL':
        payload = {
            "trans_type": "TRADE",
            "st": strategy_name,
            "symbol": symbol,
            "sell_strikes": strike,
            "expiry_date": selected_series,
            "order_t": 'm',
            "price": '0',
            "multix":str(qty)
        }
    elif transaction_type == 'EXIT':
        payload = {
            "trans_type": "EXIT",
            "st": strategy_name,
            "symbol": symbol,
            # "expiry_date": selected_series,
            # "order_t": order_type
        }
    elif transaction_type == 'CANCELALL':
        payload = {
            "trans_type": "CANCELALL",
            "st": strategy_name,
            "symbol": symbol,
            # "expiry_date": selected_series,
            # "order_t": order_type
        }
    else:
        raise ValueError("Invalid transaction type: "+transaction_type)



    return json.dumps(payload)


def send_payload(payload, timeout=None):
    print(payload)
    try:
        x = requests.get(payload, verify=False, timeout=timeout)
        print(x.text)
    except requests.exceptions.Timeout:
        print.error("Request timed out!")
    except Exception as e:
        print.error("Fatal error occurred: " + str(e))


def send_transaction(transaction_type, strategy_name, symbol, strike, selected_series, order_type, price, qty):

    payload = create_payload(transaction_type, strategy_name, symbol, strike, selected_series, order_type, price, qty)
    url = 'http://gltrades.me/tvTestGeneral?content='
    send_payload(url + payload, timeout=10)    