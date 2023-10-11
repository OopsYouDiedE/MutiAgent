from loguru import logger
from pydantic import BaseModel

from utils.llm_openai import openai_llm, to_json
from utils.prompt_helper import base_kwargs


# plan我想做什么？
class Event(BaseModel):
    action_name: str
    location: str
    time_left: int
    total_time: int
    importance: int
    effect: str


class Plan(BaseModel):
    # 可能需要一些触发器
    event_list: list[Event] = []
    description: str
    done: bool = False
    # 限制
    start_time: int
    end_time: int
    # 对Plan完成时间预估。
    total_estimate_time: int
    done_event: int
    importance: int
    # 当前事件进行的索引:
    current_event_index: int

    def get_next_event(self):
        self.current_event_index += 1
        if self.current_event_index == len(self.event_list):
            self.done = True
            return None
        else:
            return self.event_list[self.current_event_index]


class Plan_Manager:
    # 每个event包括:动作，剩余时长，全部时长，重要性（不可打断值）
    current_event: Event

    # 每个Plan包括：描述，目标，计划列表，强制性要求，等等。
    # 每个进行中的Plan:每个时刻都检查Plan如果有更重要的Plan或者耗时很短的Plan，可以中断该Plan执行临时插入的plan。
    # 还有一种Plan，是通用型Plan，可以用在很多角色中。
    current_plan: Plan
    wait_plan_list: list[Plan]

    # 生成Planlist
    def generate_plan(self):
        pass


if __name__ == '__main__':
    prompt = '''
    ### The current plans that have been scheduled are: 
    {"plan_content": "Organize personal affairs", 
    "reason": "Complete personal hygiene tasks such as washing up, folding the bed, getting dressed, and grooming.", 
    "importance": 7, "start_time": "2_13 now"} {"plan_content": "Prepare breakfast", "reason": "Prepare toast and 
    warm milk for consumption.", "importance": 6, "start_time": "2_13 7:30"} {"plan_content": "Prepare lunch", 
    "reason": "Prepare a sumptuous meal and eat.", "importance": 6, "start_time": "2_13 11:30"} {"plan_content": 
    "Prepare dinner", "reason": "Prepare a sumptuous meal and eat.", "importance": 6, "start_time": "2_13 17:30"} {
    "plan_content": "Prepare for sleep", "reason": "Complete bedtime routine and sleep.", "importance": 6, 
    "start_time": "2_13 22:30"} The following is a spatial relationship diagram. ### 'Xiao Hong's home': { 'Living 
    room': {'Sofa': 'Idle', 'TV': 'Idle', 'Coffee table': 'Idle'}, 'Kitchen': {'Refrigerator': 'Idle', 
    'Stove': 'Idle', 'Microwave': 'Idle', 'Dining table': 'Idle'}, 'Bedroom': {'Bed': 'Idle', 'Wardrobe': 'Idle', 
    'Dressing table': 'Idle'}, 'Bathroom': {'Bathtub': 'Idle', 'Toilet': 'Idle', 'Sink': 'Idle'}, 'Study room': {
    'Desk': 'Idle', 'Bookshelf': 'Idle', 'Chair': 'Idle'} } Based on the information provided, what plans do you 
    intend to make? How important are these plans? When should they start? Please write down your thought process and 
    then output each plan in the following format: [{"plan_content": {your plan content}, "reason": {reason for 
    proposing this plan}, "importance": {the importance of your plan, from 1 to 10, with 1 being the most important 
    and cannot be interrupted, and 10 being unimportant and can be terminated at any time.}, "start_time": {if it 
    starts immediately, fill in "now"; if it starts at a specific time, fill in "m_d h:m", e.g., "1_1 15:00"}}] ### 
    Your name is Xiao Hong, and you are currently at home. It is February 13th. Today is your day off, and you want 
    to relax and make the most of your vacation. Please use the format below to output your plan for the day.
    <IMPORTANT> The example shown above is for illustrative purposes only. The actual content and number of plans should 
    be determined based on the context.
    ###
    Format: [{"plan_content": "Pack personal belongings", "reason": "Check if you have all the items you need for 
    school.", "importance": 7, "start_time": "now"}, {"plan_content": "Organize personal affairs", "reason": "Complete 
    tasks such as washing up, folding the bed, and getting dressed.", "importance": 5, "start_time": "now"}, 
    {"plan_content": "Have breakfast", "reason": "Prepare toast and warm milk for consumption.", "importance": 6, 
    "start_time": "2_14 7:30"}]
    ###
    [{"plan_content":
    '''
    output = openai_llm(kwargs=base_kwargs(prompt, model='gpt-3.5-turbo-16k-0613'))
    try:
        output = to_json('[{"plan_content":' + output)
    except Exception as e:
        logger.error(e)

    logger.info(output)
    for plan in output:
        prompt = '''
        According to the following plan, please break down the plan into a more detailed sequence of actionable steps. 
        Please output each action in the following format:
        ###
        [{"action_name": {Name of the action, expressed as a verb.},
        "effect": {Effect on the target of the action, e.g., "I: had breakfast."},
        "location": {Location where the action is performed.},
        "total_time": {Time required to complete the action, in minutes.},
        "importance": {Importance of the action, on a scale of 1 to 10, 
        where 1 is the most important and cannot be interrupted, 
        and 10 is unimportant and can be terminated at any time.}]
        ###
        The following is a spatial relationship diagram. 
        'Xiao Hong's home': { 
        'Living room': {'Sofa': 'Idle', 'TV': 'Idle', 'Coffee table': 'Idle'}, 'Kitchen': {'Refrigerator': 'Idle', 
        'Stove': 'Idle', 'Microwave': 'Idle', 'Dining table': 'Idle'}, 'Bedroom': {'Bed': 'Idle', 'Wardrobe': 'Idle', 
        'Dressing table': 'Idle'}, 'Bathroom': {'Bathtub': 'Idle', 'Toilet': 'Idle', 'Sink': 'Idle'}, 'Study room': {
        'Desk': 'Idle', 'Bookshelf': 'Idle', 'Chair': 'Idle'} }
        '''+f'''
        plan_content:{plan['plan_content']}
        reason:{plan['reason']}
        '''+'''
        <IMPORTANT> The example shown above is for illustrative purposes only. The actual content and number of plans should 
        be determined based on the context.
        ###
        Format:
        [{"action_name":"Make the bed","effect":"Bed: tidy","location":"Bed","total_time":3,"importance":7},
        {"action_name":"Brush teeth","effect":"Me: clean","location":"Sink","total_time":5,"importance":7},
        {"action_name":"Get dressed","effect":"Me: wear school uniform","location":"Wardrobe","total_time":3,"importance":6},
        {"action_name":"Eat breakfast","effect":"Me: have eaten breakfast","location":"Table","total_time":15,"importance":7},
        {"action_name":"Check backpack","effect":"Me: have a backpack with class materials","location":"Bedroom","total_time":3,"importance":5},
        {"action_name":"Go","effect":"","location":"School","total_time":5,"importance":7},
        {"action_name":"Daydream","effect":"","location":"","total_time":10,"importance":10}]
        ###
        [{"action_name":
        '''
        output = openai_llm(kwargs=base_kwargs(prompt, model='gpt-3.5-turbo-0613'))
        logger.info(output)