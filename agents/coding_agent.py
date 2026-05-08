from datetime import datetime

def generate_material_code(material_name, category):
    prefix_map = {
        "原材料": "RAW",
        "半成品": "SEMI",
        "成品": "FG",
        "包装材料": "PKG",
        "辅助材料": "AUX"
    }

    prefix = prefix_map.get(category, "OTH")

    timestamp = datetime.now().strftime("%H%M%S")

    return f"{prefix}-{timestamp}"
