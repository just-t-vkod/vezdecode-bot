import json

def get_but(text, color):
    return ({
        "action": {
            "type": "text",
            "label": f"{text}"
        },
        "color": f"{color}"
    })

def get_but_c(text, color, payload):
    return ({
        "action": {
            "type": "callback",
            "label": f"{text}",
            'payload': f"{payload}"
        },
        "color": f"{color}"
    })


clean = {
    "inline": False,
    "buttons": []
}

clean = json.dumps(clean, ensure_ascii=False).encode('utf-8')
clean = str(clean.decode('utf-8'))

first = {
    'one_time': True,
    "inline": False,
    "buttons": [
        [
            {"action":
                {
                    "type": "text",
                    "label": "Нравится",
            },
                "color": 'positive'
            },
            {
                "action": {
                    "type": "text",
                    "label": "Не нравится",
            },
                "color": 'negative'
            }
        ]
    ]
}

first = json.dumps(first, ensure_ascii=False).encode('utf-8')
first = str(first.decode('utf-8'))

k1 = {
    "inline": True,
    "buttons": [
        [
            {"action": {
                "type": "callback",
                "label": "Да)",
                'payload': {"type": "1", 'answer': 'Да)'}
            },
                'color': 'positive'
            },
            {"action": {
                "type": "callback",
                "label": "Нет(",
                'payload': {"type": "1", 'answer': 'Нет('}
            },
                'color': 'negative'
            }
        ]
    ]
}

k1 = json.dumps(k1, ensure_ascii=False).encode('utf-8')
k1 = str(k1.decode('utf-8'))

k2 = {
    "one_time": True,
    "buttons": [
        [
            {"action": {
                "type": "callback",
                "label": "300кк/сек",
                'payload': {"type": "2", 'answer': '300кк/сек'}
            },
                'color': 'primary'
            },
            {"action": {
                "type": "callback",
                "label": "100 руб/год",
                'payload': {"type": "2", 'answer': '100 руб/год'}
            },
                'color': 'negative'
            },
        ],
        [
            {"action": {
                "type": "vkpay",
                'hash': 'action=transfer-to-group&group_id=1&aid=10',
                'payload': {"type": "2", 'answer': 'vk_pay'}
            },
            }
        ]
    ]
}

k2 = json.dumps(k2, ensure_ascii=False).encode('utf-8')
k2 = str(k2.decode('utf-8'))

k3 = {
    "inline": True,
    'buttons': [
        [
            {
                "action": {
                    "type": "callback",
                    "label": "ДА",
                    'payload': {"type": "3", 'answer': "ДА"}
                },
                'color': 'default'
            },
        ],
        [
            {
                "action": {
                    "type": "callback",
                    "label": "НЕТ",
                    'payload': {"type": "3", 'answer': "НЕТ"}
                },
                'color': 'primary'
            },
        ],
        [
            {
                "action": {
                    "type": "open_link",
                    'link': 'https://vk.com/olejii',
                    'label': 'Олег',
                    'payload': {"type": "3", 'answer': 'open_link'}
                },
            }
        ]
    ]
}

k3 = json.dumps(k3, ensure_ascii=False).encode('utf-8')
k3 = str(k3.decode('utf-8'))

k4 = {
    "inline": True,
    'buttons': [
        [
            {
                "action": {
                    "type": "callback",
                    "label": "НЕТ",
                    'payload': {"type": "4", 'answer': "НЕТ"}
                },
                'color': 'default'
            },
        ],
        [
            {
                "action": {
                    "type": "callback",
                    "label": "ТОЧНО НЕТ",
                    'payload': {"type": "4", 'answer': "ТОЧНО НЕТ"}
                },
                'color': 'negative'
            },
        ],
        [
            {
                "action": {
                    "type": "open_link",
                    'link': 'https://vk.com/dez.code',
                    'label': 'Матвей?',
                    'payload': {"type": "4", 'answer': 'open_link'}
                },
            }
        ]
    ]
}

k4 = json.dumps(k4, ensure_ascii=False).encode('utf-8')
k4 = str(k4.decode('utf-8'))

k5 = {
    "one_time": True,
    'buttons': [
        [
            {
                "action": {
                    "type": "callback",
                    "label": "Тортик",
                    'payload': {"type": "5", 'answer': "Тортик"}
                },
                'color': 'positive'
            },
            {
                "action": {
                    "type": "callback",
                    "label": "Сникерсни",
                    'payload': {"type": "5", 'answer': "Сникерс"}
                },
                'color': 'positive'
            }
        ],
        [
            {
                "action": {
                    "type": "callback",
                    "label": "Шоколад",
                    'payload': {"type": "5", 'answer': "Шоколад"}
                },
                'color': 'positive'
            },
            {
                "action": {
                    "type": "callback",
                    "label": "Макбук 👍👍👍",
                    'payload': {"type": "5", 'answer': "Макбук"}
                },
                'color': 'primary'
            },
        ],
    ]
}

k5 = json.dumps(k5, ensure_ascii=False).encode('utf-8')
k5 = str(k5.decode('utf-8'))

k6 = {
    "inline": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "callback",
                    "label": "Дома",
                    'payload': {"type": "6", 'answer': "Дома"}
                },
                'color': 'secondary'
            },
        ],
        [
            {
                "action": {
                    "type": "location",
                    'payload': {"type": "6", 'answer': "Я запомнил где ты живешь."}
                },
            },
        ]
    ]
}

k6 = json.dumps(k6, ensure_ascii=False).encode('utf-8')
k6 = str(k6.decode('utf-8'))

k7 = {
    "one_time": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "callback",
                    "label": "Python",
                    'payload': {"type": "7", 'answer': "Python"}
                },
                'color': 'secondary'
            },
        ],
        [
            {
                "action": {
                    "type": "callback",
                    "label": 'JS',
                    'payload': {"type": "7", 'answer': "JS"}
                },
                'color': 'negative'
            },
            {
                "action": {
                    "type": "callback",
                    "label": 'C++',
                    'payload': {"type": "7", 'answer': "C++"}
                },
                'color': 'negative'
                }
        ]
    ]
}

k7 = json.dumps(k7, ensure_ascii=False).encode('utf-8')
k7 = str(k7.decode('utf-8'))

k8 ={
    "inline": True,
    "buttons": [
        [
            {
                "action": {
                    "type": "callback",
                    "label": "Тык",
                    'payload': {"type": '8'}
                },
            },
        ]
    ]
}

k8 = json.dumps(k8, ensure_ascii=False).encode('utf-8')
k8 = str(k8.decode('utf-8'))
