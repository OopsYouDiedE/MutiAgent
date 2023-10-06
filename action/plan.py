from loguru import logger

from config.config import ConfigForChatgptKwangs
from utils.llm_openai import openai_llm
from utils.prompt_helper import base_kwargs

if __name__ == '__main__':
    inner_voice = """你很兴奋地计划在2月14日下午5点在Hobbs咖啡馆举办情人节派对，
    你渴望告诉每个人来参加派对；你和Maria Lopez认识了大约一年，自从Maria Lopez去Hobbs咖啡馆后，你们成为了好朋友；
    Maria Lopez对你来说是一个忠实的朋友，也是Hobbs咖啡馆的常客；Klaus Mueller是Hobbs咖啡馆的常客；你喜欢在Hobbs咖啡馆工作。
    """
    prompt = f'''
    请根据以下信息设计一份合适的日程表，以list[[str,str]]形式输出
    ###
    你的名字叫Isabella Rodriguez。你是Hobbs咖啡馆店主
    {inner_voice}
    ###
    以下是一个合适的日程表设计
    '''
    logger.info(openai_llm(kwargs=base_kwargs(prompt))['choices'][0]['message']['content'])