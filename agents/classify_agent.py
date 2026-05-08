from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_material(material_name):
    prompt = f"""
    你是ERP物料分类专家。

    请对以下物料进行分类：

    物料：{material_name}

    分类规则：
    - 原材料
    - 半成品
    - 成品
    - 包装材料
    - 辅助材料

    只返回分类名称。
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
