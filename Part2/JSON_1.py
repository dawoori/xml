# 메모리에서 JSON 문자열을 처리하기

import json

# JSON encoding, 직렬화(serialization) : 파이썬 객체를 메모리 / 디스크에 JSON 문자열로 변환.

newDict = {                 # 파이썬 딕셔너리 객체
    'id': 205,
    'name': '정병지',
    'scholarship': True,    # JSON string과 비교
    'handphone': None,      # JSON string과 비교
    'address': {
        'street': "성북구 정릉로 77",
        'city': "서울",
        'zipcode': "02707"
    },
    'hobbies': ['독서', '자전거', '베이킹'],
    'courses': [
        {
            'major' : '컴퓨터공학',
            'classes' : ['자료구조', '화일처리', '데이타베이스']
        },
        {
            'minor': '수학',
            'classes': ['통계학', '회귀분석']
        }
    ]
}

# JSON 스트링에 쓰기
# dump()에 의해 모든 작은 따옴표('')는 큰 따옴표("")로 변환됨
jsonString = json.dumps(newDict, ensure_ascii=False)      # dump into string
print(jsonString)
print()

jsonString = json.dumps(newDict, indent=4, ensure_ascii=False)
print(jsonString)
print()

#########################################
# JSON decoding, 역직렬화(deserialization) : 메모리 / 디스크에 있는 JSON 문자열을 파이썬 객체로 변환.

jsonString = '''{
    "id": 205,
    "name": "정병지",
    "scholarship": true,        
    "handphone": null,          
    "address": {
        "street": "성북구 정릉로 77",
        "city": "서울",
        "zipcode": "02707"
    },
    "hobbies": ["독서", "자전거", "베이킹"],
    "courses": [
        {
            "major" : "컴퓨터공학",
            "classes" : ["자료구조", "화일처리", "데이타베이스"]
        },
        {
            "minor": "수학",
            "classes": ["통계학", "회귀분석"]
        }
    ]
}'''

# JSON 스트링을 읽기
newDict = json.loads(jsonString)              # load into string
print(newDict)