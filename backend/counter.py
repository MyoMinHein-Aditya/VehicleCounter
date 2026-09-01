def count_vehicles(detections):
    counts = {
        "cars": 0,
        "motorcycles": 0,
        "heavy_vehicles": 0,
        "total": 0
    }
    
    for det in detections:
        if det["class"] == "car":
            counts["cars"] += 1
        elif det["class"] == "motorcycle":
            counts["motorcycles"] += 1
        elif det["class"] == "heavy vehicle":
            counts["heavy_vehicles"] += 1
            
    counts["total"] = counts["cars"] + counts["motorcycles"] + counts["heavy_vehicles"]
    return counts