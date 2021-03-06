from datetime import datetime

today = datetime.today()
date = datetime.strftime(today, '%Y-%m-%d')

asset_data = [
    # 以上是固定的
    {"amount": 33994, "asset_type": "美金", "date": date},
    {"amount": 7774.79, "asset_type": "公积金", "date": date},
    {"amount": 5607, "asset_type": "工行", "date": date},
    {"amount": 5399.14, "asset_type": "湾仔学堂", "date": date},
    {"amount": 10000, "asset_type": "亿霆实", "date": date},
    # 以下是变动的
    {"amount": 115261.57, "asset_type": "招行", "date": date},
    {"amount": 254.94, "asset_type": "微信", "date": date},
]


income_data = [
    {"income": 270, "source": "知行优学", "date": date},
]

outcome_data = [
    {"amount": 3.96, "source": "相互宝", "date": date, 'category': "健康"},
]
