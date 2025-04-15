from flask import Flask, render_template, jsonify
from threading import Thread
from services.animal_detection import run_animal_detection
from services.disaster_detection import run_disaster_detection
from services.gunshot_detection import run_gunshot_detection
from utils.threat_classifier import classify_threat
from alerts.notifier import send_telegram_alert

app = Flask(__name__)

detection_results = {
    "animal": "",
    "disaster": "",
    "gunshot": "",
    "threat": ""
}

def monitor_system():
    while True:
        animal = run_animal_detection()
        disaster = run_disaster_detection()
        gunshot = run_gunshot_detection()

        threat = classify_threat(animal, disaster, gunshot)

        detection_results.update({
            "animal": animal,
            "disaster": disaster,
            "gunshot": gunshot,
            "threat": threat
        })

        if threat == "Threat Detected":
            send_telegram_alert(f"⚠️ Threat Detected!\nAnimal: {animal}\nDisaster: {disaster}\nGunshot: {gunshot}")

@app.route("/")
def index():
    return render_template("index.html", results=detection_results)

@app.route("/status")
def status():
    return jsonify(detection_results)

if __name__ == "__main__":
    monitoring_thread = Thread(target=monitor_system, daemon=True)
    monitoring_thread.start()
    app.run(debug=True)
