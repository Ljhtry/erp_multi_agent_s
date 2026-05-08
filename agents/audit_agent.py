from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def audit_material(material, category, code):
    prompt = f"""
    请审核以下ERP物料：

    物料名称：{material}
    分类：{category}
    编码：{code}

    请检查：
    1. 是否符合ERP规范
    2. 是否命名清晰
    3. 是否存在风险

    返回审核意见。
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
