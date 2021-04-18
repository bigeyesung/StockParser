#https://www.ethanideas.url.tw/python-stock/
import requests
import pandas as pd
import numpy as np

def financial_statement(year, season, type='財務分析資料查詢彙總表'):

    if year >= 1000:
        year -= 1911

    if type == '綜合損益彙總表':
        url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb04'
    elif type == '資產負債彙總表':
        url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb05'
    elif type == '營益分析彙總表':
        url = 'https://mops.twse.com.tw/mops/web/ajax_t163sb06'
    elif type == "財務分析資料查詢彙總表":
        url = 'https://mops.twse.com.tw/mops/web/ajax_t51sb02'
    else:
        print('type does not match')

    r = requests.post(url, {
        'encodeURIComponent':1,
        'run':1,
        'step':1,
        'firstin':1,
        'off':1,
        'ifrs':'Y',
        'isnew':'',
        'TYPEK':'sii',
        'year':year
        # 'season':str(season),
    })
    print(r.text)
    r.encoding = 'utf8'
    dfs = pd.read_html(r.text, header=None)
    print(dfs)
    return pd.concat(dfs[1:], axis=0, sort=False)\
             .set_index(['公司代號'])\
             .apply(lambda s: pd.to_numeric(s, errors='ceorce'))


ret=financial_statement(104,4)
print(ret)