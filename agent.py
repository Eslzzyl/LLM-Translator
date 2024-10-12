import os
from prompt import SYSTEM_PROMPT_GENERAL_TRANSLATOR, SYSTEM_PROMPT_ACADEMIC_TRANSLATOR, USER_PROMPT_TRANSLATOR
from openai import OpenAI


class Translator:
    def __init__(self):
        # 从环境变量获取 OPENAI_API_KEY 和 OPENAI_API_BASE
        api_key = os.getenv("OPENAI_API_KEY")
        base_url = os.getenv("OPENAI_API_BASE")
        self.llm = OpenAI(api_key=api_key, base_url=base_url)
    
    def infer(self, text, model, temperature, target_language="中文", agent_type="通用翻译"):
        if agent_type == "通用翻译":
            self.system_prompt = SYSTEM_PROMPT_GENERAL_TRANSLATOR
            self.user_prompt = USER_PROMPT_TRANSLATOR
        elif agent_type == "学术翻译":
            self.system_prompt = SYSTEM_PROMPT_ACADEMIC_TRANSLATOR
            self.user_prompt = USER_PROMPT_TRANSLATOR
        else:
            raise ValueError(f"Invalid agent type: {agent_type}")
        
        response = self.llm.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": self.user_prompt.format(target_language=target_language, text=text)}
            ],
            temperature=temperature,
            stream=True
        )
        full_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                yield full_response


if __name__ == "__main__":
    agent = Translator()
    agent.infer("Hello, world!", "gpt-4o-mini", 1.3, "中文", "通用翻译")
