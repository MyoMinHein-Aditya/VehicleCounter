def count_vehicles(detections):
    counts = {
        "cars": 0,
        "motorcycles": 0,
        "total": 0
    }
    
    for det in detections:
        if det["class"] == "car":
            counts["cars"] += 1
        elif det["class"] == "motorcycle":
            counts["motorcycles"] += 1
            
    counts["total"] = counts["cars"] + counts["motorcycles"]
    return counts