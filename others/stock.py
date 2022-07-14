import datetime
import numpy as np
import pandas as pd

link = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data'
data = pd.read_csv(link)
# ['證券代號', '證券名稱', '成交股數', '成交金額', '開盤價',
#  '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']
print(data)
data.columns = ['STOCK_SYMBOL', 'NAME', 'TRADE_VOLUME', 'TRADE_VALUE', 
                'OPEN', 'HIGH' ,'LOW', 'CLOSE', 'PRICE_CHANGE', 'TRANSACTION']   

def date_get_today(with_time=False):
    '''
    取得今日日期，並指定為台北時區
    '''
    import pytz
    central = pytz.timezone('Asia/Taipei')
    
    if with_time == True:
        now = datetime.datetime.now(central)
    else:
        now = datetime.datetime.now(central).date()
    return now

def conv_to_list(obj):
    '''
    將物件轉換為list
    '''
    if not isinstance(obj, list) :
        results = [obj]
    else:
        results = obj
    return results

def df_conv_col_type(df, cols, to, ignore=False):
    '''
    一次轉換多個欄位的dtype
    '''
    cols = conv_to_list(cols)
    for i in range(len(cols)):
        if ignore :
            try:
                df[cols[i]] = df[cols[i]].astype(to)
            except:
                print('df_conv_col_type - ' + cols[i] + '轉換錯誤')
                continue
        else:
            df[cols[i]] = df[cols[i]].astype(to)
    return df

data['WORK_DATE'] = date_get_today()
cols = data.columns.tolist()
cols = cols[-1:] + cols[:-1]
data = data[cols]
data = data.replace('', np.nan, regex=True)
data = df_conv_col_type(df=data, 
                        cols=[
                            'TRADE_VOLUME', 'TRADE_VALUE', 'OPEN', 'HIGH',
                            'LOW', 'CLOSE', 'PRICE_CHANGE', 'TRANSACTION'],
                        to='float')

prices = {}
stocks = ["3033", "3057", "2504"]
# "6842"
# "6122"
for stock in stocks:
    price = data.loc[data["STOCK_SYMBOL"] == stock]
    close = list(price["CLOSE"].values)[0]
    name = list(price["NAME"].values)[0]
    prices[name] = close


stocks = {
    "喬鼎": [13.05, 2],
    "一元素": [66.4, 1],
    "威健": [30.95, 1],
    "國產": [27.25, 3],
    "擎邦": [19, 4],
}

print("Time", data.iloc[0]["WORK_DATE"])
principal = 0
total = 0
for name, (bid_price, share) in stocks.items():
    if name in prices:
        principal += bid_price * share * 1000
        ask_price = prices[name]
        earn = round((ask_price - bid_price) * share * 1000, 2)
        print(name, earn)
        total += earn

print("盈餘", total)
print("本金", principal)
