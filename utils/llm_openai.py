import openai
from config.config import Config, ConfigForChatgptKwangs
from loguru import logger


def openai_llm(messages: str = None,
               kwargs: dict = None

               ):
    """
    请参照openai的教程，message应该在使用时定义，
    其他部分请在config中提前定义，并以dict形式传入，
    message的构造方法应该放在Action中。
    """
    kwargs.setdefault('messages', messages)
    openai.api_key = Config.OPENAI_API_KEY
    openai.proxy = Config.OPENAI_PROXY
    completion = openai.ChatCompletion.create(

        **kwargs
    )
    return completion


if __name__ == '__main__':
    logger.info(openai_llm(kwargs=ConfigForChatgptKwangs.TEST_KWANGS))
