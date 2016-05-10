# ptx-transportdata-bus-stops-parser

### intro
This parser can only parse .json file from [公共運輸整合資訊平台](http://ptx.transportdata.tw), you will get explicit information of following data:
 - 台北市公車站牌
 - 新北市公車站牌
 - 桃園市公車站牌
 - 台中市公車站牌
 - 台南市公車站牌
 - 高雄市公車站牌

The ouput file contains stop names in Chinese, English and position datas of longitude, latitue.
### Usage
Put .json file which download from [站牌資料](http://ptx.transportdata.tw/MOTC/v1/Bus/Stop/) in the "input" folder, and simply run:
```sh
$ python parser.py
```
The results will be created in "output" folder with pre suffix 'parsed_'.
### Results
Source json:
```sh
[
  {
    "StopUID": "string",
    "StopID": "string",
    "AuthorityID": "string",
    "StopName": {
      "Zh_tw": "string",
      "En": "string"
    },
    "StopPosition": {
      "PositionLat": 0,
      "PositionLon": 0
    },
    "StopAddress": "string",
    "UpdateTime": "string"
  }
]
```
Output json:
```sh
[
  {
    "StopName": {
      "Zh_tw": "string",
      "En": "string"
    },
    "StopPosition": {
      "PositionLat": 0,
      "PositionLon": 0
    }
  }
]
```
License
----

MIT