# metrics/generate_metrics.py
import os
import sys
import json
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    if len(sys.argv) < 2:
        print("Uso: python metrics/generate_metrics.py backlog.json")
        sys.exit(1)

    backlog_file = sys.argv[1]
    data = load_data(backlog_file)

    os.makedirs("metrics_output", exist_ok=True)

    df_sprints = pd.DataFrame(data.get("sprints", []))
    df_priority = pd.DataFrame(data.get("priorities", []))
    df_epics = pd.DataFrame(data.get("epics", []))

    df_sprints.to_csv("metrics_output/sprints_metrics.csv", index=False)
    df_priority.to_csv("metrics_output/priority_metrics.csv", index=False)
    df_epics.to_csv("metrics_output/epic_metrics.csv", index=False)

    plt.figure(figsize=(6,4))
    x = df_sprints["name"]
    y = df_sprints["userstories"]
    plt.bar(x, y)
    plt.title("User Stories por Sprint")
    plt.xlabel("Sprint")
    plt.ylabel("Quantidade de User Stories")
    plt.tight_layout()
    plt.savefig("metrics_output/userstories_per_sprint.png")
    plt.close()

    plt.figure(figsize=(6,6))
    labels = df_priority["priority"]
    sizes = df_priority["count"]
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Distribuição de Prioridade (MoSCoW)")
    plt.tight_layout()
    plt.savefig("metrics_output/priority_distribution.png")
    plt.close()

    plt.figure(figsize=(8,4))
    x = df_epics["epic"]
    y = df_epics["count"]
    plt.bar(x, y)
    plt.title("User Stories por Épico")
    plt.xlabel("Épico")
    plt.ylabel("Quantidade de User Stories")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig("metrics_output/userstories_per_epic.png")
    plt.close()

    print("✅ Métricas geradas em metrics_output/")

if __name__ == "__main__":
    main()
