
import openai
openai.api_key = "sk-i3Ud6k6eGJ5ORUYazIJviKCmAlmRXd6bCHKcdrGXzi4RbtOo"
openai.api_base = "https://api.chatanywhere.com.cn"
#GPT回答
def gpt_35_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
        api_key (str): OpenAI API 密钥

    Returns:
        tuple: (results, error_desc)
    """
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            stream=True,
        )
        completion = {'role': '', 'content': ''}
        for event in response:
            if event['choices'][0]['finish_reason'] == 'stop':
                print(f'收到的完成数据: {completion}')
                break
            for delta_k, delta_v in event['choices'][0]['delta'].items():
                print(f'流响应数据: {delta_k} = {delta_v}')
                completion[delta_k] += delta_v
        messages.append(completion)  # 直接在传入参数 messages 中追加消息
        return (True, completion)
    except Exception as err:
        return (False, f'OpenAI API 异常: {err}')
if __name__ == '__main__':
    pass