import json


techniques_list = input("Enter a list of techniques: ").split()

data_list = []
for technique in techniques_list:
    score = int(input("Enter a score for " + technique + ": "))
    if score == 5:
        color = '#33691E'
    elif score == 4:
        color = '#689F38'
    elif score == 3:
        color = '#8BC34A'
    elif score == 2:
        color = '#AED581'
    elif score == 1:
        color = '#DCEDC8'
    elif score == 0:
        color = '#9C27B0'
    data = {"techniqueID": technique, "color": color, "comment": "", "enabled": True, 
            "metadata": [], "showSubtechniques": True}
    data_list.append(data)

output_dict = {"name": "Detections Tanium", "versions": {"navigator": "4.9", "layer": "4.5"},
        "domain": "enterprise-attack", "description": "description", "filters": {"platforms": ["Windows", "Linux", "macOS"]},
        "sorting": 0, "layout": {"layout": "flat", "aggregateFunction": "sum", "showAggregateScores": True, "countUnscored": False, "showName": True, "showID": False},
        "hideDisable": True, "selectSubtechniquesWithParent": False, "techniques": data_list,
        "showTacticRowBackground": False, "tacticRowBackground": "#dddddd", "selectTechniquesAcrossTactics": True, "gradient": {"colors": ["#aeb6bf", "#aeb6bf"], "minValue": 0, "maxValue": 10000},
        "legendItems": [
        {"label": "Detection score 0: Forensics/Context", "color": "#9C27B0"},
        {"label": "Detection score 1: Basic", "color": "#DCEDC8"},
        {"label": "Detection score 2: Fair", "color": "#AED581"},
        {"label": "Detection score 3: Good", "color": "#8BC34A"},
        {"label": "Detection score 4: Very good", "color": "#689F38"},
        {"label": "Detection score 5: Excellent", "color": "#33691E"}]}

json_string = json.dumps(output_dict)

with open("output.json", "w") as outfile:
    outfile.write(json_string)

