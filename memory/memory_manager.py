'''

记忆按照种类不同进行如下划分。
短时记忆：仅保存3-5分钟，并有容量上限。短时记忆的内容没有格式化。
如果短期记忆的内容是有意义的，我应该延长记忆的时间。
这里是一次reflect。目的是让有用的信息进入大脑，没有用的信息忘掉。
reflect:一些短时记忆的结合。

长时记忆：能够维持很长时间的记忆。包括以下几种。
event：对一段行为的抽象为一个动作。
fact：对一段事实的记忆。
action_list：完成一件事的流程。
'''
from pydantic import BaseModel


class MemoryManager:
    '''
    导入记忆，导出记忆，检索记忆，总结记忆。
    要不要把记忆分开存储？答案：是。

    '''

    def __init__(self, memory_path=None):
        pass

    def load(self):
        pass

    def save(self):
        pass

    def search(self):
        pass

    def reflect(self):
        pass
