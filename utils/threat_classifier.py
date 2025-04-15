def classify_threat(animal, disaster, gunshot):
    if disaster.lower() != "normal" or gunshot.lower() == "gunshot":
        return "Threat Detected"
    if animal.lower() in ["human", "poacher", "hunter"]:
        return "Threat Detected"
    return "Normal"
