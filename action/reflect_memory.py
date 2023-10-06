'''
reflect_memory
'''
from loguru import logger

from config.config import ConfigForChatgptKwangs, ConfigForMemory
from utils.llm_openai import openai_llm
from utils.prompt_helper import base_kwargs

if __name__ == '__main__':
    memories = str([i[0] for i in ConfigForMemory.BASE_MEMORY])
    prompt = f'''
    根据下方的内容提炼出你认为可能有用的结论。并以list[str]形式输出。每条结论只有一句话。
    ###
    {memories}
    ###
    OutPut:
    ["结论1",
    "
    '''
    logger.info(openai_llm(kwargs=base_kwargs(prompt))['choices'][0]['message']['content'])
