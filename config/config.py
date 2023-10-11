class Config:
    OPENAI_API_BASE = 'https://api.openai.com/v1'
    OPENAI_PROXY = 'http://127.0.0.1:7000'
    OPENAI_API_KEY = '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'
    DEFAULT_OPENAI_MODEL = 'gpt-3.5-turbo-0613'


class ConfigForChatgptKwangs:
    BASE_MESSAGE = [
        {'role': "system", 'content': "You are a helpful assistant."}
    ]
    TEST_KWANGS = dict(model="gpt-3.5-turbo", messages=[
        {'role': "system", 'content': "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ])


class ConfigForMemory:
    'memory本体，最近访问的时间戳，重要性，'
    BASE_MEMORY = [['酒馆里人声鼎沸，酒杯碰撞声不断', 7, 2],
                   ['唐三坐下后发现酒馆里有各种不同类型的客人', 10, 3],
                   ['一位威风凛凛的中年人坐在唐三对面的桌子上', 15, 4],
                   ['中年人提出和唐三玩一个游戏的挑战', 17, 6],
                   ['唐三接受了挑战', 20, 7],
                   ['唐三和剑魔站在酒馆中央，剑魔举起宝剑，酒滴滴落', 25, 6],
                   ['唐三用酒杯接住了其中一滴酒滴', 30, 8],
                   ['观众们惊叹唐三的技巧，欢呼起来', 32, 9],
                   ['剑魔对唐三的表现感到赞赏', 35, 5],
                   ['剑魔给唐三倒了一杯美酒作为奖励', 38, 8],
                   ['唐三和剑魔举杯庆祝', 40, 7],
                   ['唐三因此结识了许多新朋友', 45, 6]]
    SHORT_MEMORY_MAX_NUM=7
    BASE_IMPORTANCE =[

    ]