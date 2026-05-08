from agents.orchestrator import run_workflow

if __name__ == "__main__":
    material = "铝合金山地自行车车架"
    result = run_workflow(material)
    print(result)
