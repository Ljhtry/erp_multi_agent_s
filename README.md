# ERP Multi-Agent 主数据治理系统

## 功能
- 物料分类
- 相似物料检测
- 自动编码
- ERP规则审核
- Multi-Agent协同

## 安装

```bash
pip install -r requirements.txt
```

## 配置

复制 `.env.example` 为 `.env` 并填写 API KEY。

## 运行

```bash
python main.py
```

## 输出示例

```python
{
    'material_name': '铝合金山地自行车车架',
    'category': '原材料',
    'duplicate': {
        'matched_material': '铝合金车架',
        'distance': 0.43,
        'possible_duplicate': True
    },
    'material_code': 'RAW-231522',
    'audit_result': '命名符合规范，建议复用已有物料编码'
}
```
