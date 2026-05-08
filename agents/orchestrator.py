from agents.classify_agent import classify_material
from agents.duplicate_agent import check_duplicate
from agents.coding_agent import generate_material_code
from agents.audit_agent import audit_material

def run_workflow(material):
    print("开始处理物料")

    category = classify_material(material)

    duplicate_result = check_duplicate(material)

    code = generate_material_code(material, category)

    audit = audit_material(material, category, code)

    result = {
        "material_name": material,
        "category": category,
        "duplicate": duplicate_result,
        "material_code": code,
        "audit_result": audit,
    }

    return result
