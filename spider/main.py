import re

import requests
import hmac
from hashlib import sha256
from urllib.parse import quote, unquote, urlencode
import time

from tqdm import trange
import execjs

UUID = '84f1905e254ec020a72caec03dfa46cf'
HMAC_KEY = "abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b"
session = requests.Session()
JSTEXT = """window = {}
function get_acw(arg1) {
  while (window["_phantom"] || window["__phantomas"]) {}
  var _0x5e8b26 = "3000176000856006061501533003690027800375";
  String["prototype"]["hexXor"] = function (_0x4e08d8) {
    var _0x5a5d3b = "";
    for (var _0xe89588 = 0; _0xe89588 < this["length"] && _0xe89588 < _0x4e08d8["length"]; _0xe89588 += 2) {
      var _0x401af1 = parseInt(this["slice"](_0xe89588, _0xe89588 + 2), 16);

      var _0x105f59 = parseInt(_0x4e08d8["slice"](_0xe89588, _0xe89588 + 2), 16);

      var _0x189e2c = (_0x401af1 ^ _0x105f59)["toString"](16);

      if (_0x189e2c["length"] == 1) {
        _0x189e2c = "0" + _0x189e2c;
      }

      _0x5a5d3b += _0x189e2c;
    }

    return _0x5a5d3b;
  };

  String["prototype"]["unsbox"] = function () {
    var _0x4b082b = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13, 6, 11, 39, 18, 20, 8, 14, 21, 32, 26, 2, 30, 7, 4, 17, 5, 3, 28, 34, 37, 12, 36];
    var _0x4da0dc = [];
    var _0x12605e = "";

    for (var _0x20a7bf = 0; _0x20a7bf < this["length"]; _0x20a7bf++) {
      var _0x385ee3 = this[_0x20a7bf];

      for (var _0x217721 = 0; _0x217721 < _0x4b082b["length"]; _0x217721++) {
        if (_0x4b082b[_0x217721] == _0x20a7bf + 1) {
          _0x4da0dc[_0x217721] = _0x385ee3;
        }
      }
    }

    _0x12605e = _0x4da0dc["join"]("");
    return _0x12605e;
  };

  arg2 = arg1["unsbox"]()["hexXor"](_0x5e8b26);
  return arg2
}"""
headers = {
    'From-Domain': '51job_web',
    'Referer': 'https://we.51job.com/pc/search',
    'property': "",
    'sign': '',  # 签名
    'uuid': UUID,  # 用户id
}
params = {
    'api_key': '51job',
    'timestamp': str(int(time.time())),
    'keyword': "爬虫",
    'searchType': '2',
    'industry': '',
    'function': '',
    'jobArea': '000000',
    'jobArea2': '',
    'landmark': '',
    'metro': '',
    'salary': '',
    'workYear': '',
    'degree': '',
    'companyType': '',
    'companySize': '',
    'jobType': '',
    'issueDate': '',
    'sortType': '0',
    'pageNum': '3',
    'requestId': '52fe92480e32ce275ade9de5f1271409',
    'pageSize': '20',
    'source': '1',
    'accountId': '',
    'pageCode': 'sou|sou|soulb',
}
cookies = {
    'guid': UUID,
    'acw_sc__v2': '65560157d2b580f5ed023a18ece86f581ecc645a',
}


def get_sign(value):
    return hmac.new(HMAC_KEY.encode('utf-8'), value.encode('utf-8'), digestmod=sha256).hexdigest()


def get_property():
    values = {
        "partner": "",
        "webId": 2,  # 固定是2
        "fromdomain": headers['From-Domain'],
        "frompageUrl": "https://we.51job.com/",
        "pageUrl": headers['Referer'],
        "identityType": "",
        "userType": "",
        "isLogin": "否",
        "accountid": "",
    }

    res = str(values).replace(' ', '').replace('\'', '"')
    res = quote(res).replace('%3A', ':').replace('%2C', ',')
    return res


def update_cookie(arg1):
    ctx = execjs.compile(JSTEXT)
    res = ctx.call('get_acw', arg1)
    session.cookies.set('acw_sc__v2', res)


def get_data(key, page):
    params['keyword'] = key
    params['pageNum'] = str(page)
    headers['sign'] = get_sign('/api/job/search-pc?' + urlencode(params))
    headers['property'] = get_property()

    resp = session.get("https://we.51job.com/api/job/search-pc", params=params, headers=headers)
    if failed := re.findall(r"var arg1='(.*?)';", resp.text):
        print('[failed] retry')
        update_cookie(failed[0])
        return get_data(key, page)  # 回调该函数
    return resp.text


if __name__ == '__main__':
    session.cookies.set('guid', UUID)
    with open('data.json', 'a', encoding='utf-8') as f:
        for i in trange(1, 2):
            data = get_data('爬虫', i)
            f.write(data)
            f.write('\n')
            time.sleep(2)
