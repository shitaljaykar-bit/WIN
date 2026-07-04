import time
import random
import json
from datetime import datetime

class WinMachineIntelligence:
    def __init__(self, machine_id="CNC-ROBOT-01"):
        self.machine_id = machine_id
        self.base_temperature = 42.0  # Celsius
        self.base_vibration = 1.2      # mm/s (RMS)
        self.base_current = 15.0       # Amperes (NILM)
        print(f"📡 [WIN AI INITIALIZED] Monitoring Machine: {self.machine_id}")
        print("Senses Activated: NILM Power Sensing + Acoustic Audio Streams\n" + "="*60)

    def read_sensors(self, structural_wear_factor=1.0):
        """Simulates data incoming from WIN's multi-sensor fusion layer."""
        vibration = (self.base_vibration * structural_wear_factor) + random.uniform(-0.1, 0.2)
        temperature = (self.base_temperature * (structural_wear_factor ** 0.5)) + random.uniform(-0.5, 0.8)
        current = self.base_current + random.uniform(-0.5, 0.5)
        
        # Simulate an acoustic frequency anomaly if wear factor is high
        acoustic_anomaly = "NORMAL_HUM" if structural_wear_factor < 1.4 else "HIGH_FREQUENCY_GRINDING"
        
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "machine_id": self.machine_id,
            "metrics": {
                "vibration_rms_mms": round(vibration, 2),
                "temperature_celsius": round(temperature, 2),
                "nilm_current_amps": round(current, 2)
            },
            "acoustic_signature": acoustic_anomaly
        }

    def brain_anomaly_detector(self, telemetry):
        """WIN Brain Layer: Evaluates telemetry for root-cause anomalies."""
        metrics = telemetry["metrics"]
        score = 0
        reasons = []

        if metrics["vibration_rms_mms"] > 1.8:
            score += 40
            reasons.append("Critical bearing misalignments detected via Vibration Analysis.")
        if metrics["temperature_celsius"] > 50.0:
            score += 30
            reasons.append("Thermal dissipation failure / friction spike.")
        if telemetry["acoustic_signature"] == "HIGH_FREQUENCY_GRINDING":
            score += 30
            reasons.append("Acoustic AI signature matches Gear Teeth Spalling.")

        return {"anomaly_probability_pct": score, "detected_root_causes": reasons}

    def action_agentic_rag(self, root_causes):
        """WIN Action Layer: Orchestrates autonomous repair tasks based on root causes."""
        print("\n🤖 [WIN AGENTIC ACTION LAYER] Anomaly confirmed! Compiling prescriptive guides...")
        time.sleep(1)
        print("🔧 Generating Step-by-Step Autonomous Repair Workflow Guide:")
        
        for idx, cause in enumerate(root_causes, 1):
            print(f"   {idx}. {cause}")
            if "bearing" in cause.lower():
                print("      👉 [ACTION] Dispatching automated grease purge tool to bearing block unit.")
                print("      👉 [ERP] Logging replacement request for SKU-BRG-9923 in parts inventory.")
            elif "gear" in cause.lower():
                print("      👉 [ACTION] Sending autonomous shutdown command to prevent total mechanical catastrophic lock.")
                print("      👉 [WORK ORDER] Scheduled high-priority maintenance ticket assigned to Team B.")
        print("="*60)

# Run the live Industrial Simulator Loop
if __name__ == "__main__":
    win_system = WinMachineIntelligence()
    
    # Simulate a time progression where mechanical degradation happens
    time_steps = [1.0, 1.0, 1.1, 1.4, 1.6]  
    
    for i, wear in enumerate(time_steps):
        print(f"\n⏱️ [TIME INDEX: T+{i*10} Mins] Scanning Factory Floor Assets...")
        telemetry = win_system.read_sensors(structural_wear_factor=wear)
        
        print(f"📊 Telemetry Packet: {json.dumps(telemetry['metrics'])} | Sound: {telemetry['acoustic_signature']}")
        
        # Pass telemetry into the Brain Anomaly Model
        diagnosis = win_system.brain_anomaly_detector(telemetry)
        prob = diagnosis["anomaly_probability_pct"]
        
        if prob > 0:
            print(f"⚠️  [BRAIN WARNING] Anomaly Probability evaluated at {prob}%")
            if prob >= 60:
                print("🚨 CRITICAL STATE INDICATED: Triggering Agentic RAG Pipeline...")
                win_system.action_agentic_rag(diagnosis["detected_root_causes"])
                break
        else:
            print("✅ Status: Optimal Machine Health. Zero-Downtime Pipeline Stable.")
            
        time.sleep(1.5)