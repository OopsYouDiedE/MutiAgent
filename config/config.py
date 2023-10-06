class Config:
    OPENAI_API_BASE = 'https://api.openai.com/v1'
    OPENAI_PROXY = 'http://127.0.0.1:7000'
    OPENAI_API_KEY = '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'
    DEFAULT_OPENAI_MODEL = 'gpt-3.5-turbo-0613'


class ConfigForChatgptKwangs:
    BASE_MESSAGE=[
        {'role': "system", 'content': "You are a helpful assistant."}
        ]
    TEST_KWANGS = dict(model="gpt-3.5-turbo", messages=[
        {'role': "system", 'content': "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ])
