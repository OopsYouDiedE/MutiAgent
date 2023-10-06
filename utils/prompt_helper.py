'''
辅助完成构建prompt
一个prompt
'''


def base_prompt(prompt, system_prompt="You are a helpful assistant."):
    return [
        {'role': "system", 'content': system_prompt},
        {"role": "user", "content": prompt},
    ]


def base_kwargs(prompt, system_prompt="You are a helpful assistant.", model="gpt-3.5-turbo"):
    return dict(model=model,
                messages=base_prompt(prompt, system_prompt=system_prompt))
