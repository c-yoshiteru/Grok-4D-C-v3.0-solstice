def lerp(min_val, max_val, t):
    """0.0〜1.0 を使った線形補間"""
    return min_val + (max_val - min_val) * t


def determine_sme_params(c_value, mari_stage):
    if mari_stage == "UNITY":
        bpm = 78
        return {
            "BPM": bpm,
            "Pitch_Base_Hz": 432.0,
            "Mood": "Full_Spectrum_Rainbow_Drone",
            "Microtone": "Just_Intonation",
            "Pan_Direction": "360_Static_Field",
            "AudioCue_Trigger": None
        }

    elif mari_stage == "SYNC":
        bpm = lerp(78, 120, c_value)
        return {
            "BPM": round(bpm, 2),
            "Pitch_Base_Hz": 432.0,
            "Mood": "Cosmic_Resonance",
            "Microtone": "Micro_Shift",
            "Pan_Direction": "Gentle_Spiral",
            "AudioCue_Trigger": None
        }

    elif mari_stage == "INVERT":
        return {
            "BPM": 78,
            "Pitch_Base_Hz": 432.0,
            "Mood": "Chladni_Inversion",
            "Microtone": "Dissonant_Insert",
            "Pan_Direction": "Sudden_Flip",
            "AudioCue_Trigger": "CHLADNI_INVERSION.wav"
        }

    else:  # CHAOS
        bpm = lerp(120, 180, 1 - c_value)
        return {
            "BPM": round(bpm, 2),
            "Pitch_Base_Hz": "RANDOM",
            "Mood": "Distorted_Noise",
            "Microtone": "Extreme_Detune",
            "Pan_Direction": "Random_Flash",
            "AudioCue_Trigger": "WHITE_NOISE_ALERT.wav"
        }


def determine_visualizer_params(c_value, mari_stage):
    if mari_stage == "UNITY":
        return {
            "Color_Mode": "Rainbow_Chladni",
            "Primary_Color_Hex": "#FFFFFF",
            "Shape_Density": "HIGH_COMPLEXITY",
            "Movement_Speed": "LOW",
            "Focus_Target": "C_DENSITY_MAP"
        }

    elif mari_stage == "SYNC":
        return {
            "Color_Mode": "Warm_Gradient",
            "Primary_Color_Hex": "#FFA500",
            "Shape_Density": "MEDIUM_COMPLEXITY",
            "Movement_Speed": "MEDIUM",
            "Focus_Target": "WAVE_INTERFERENCE"
        }

    elif mari_stage == "INVERT":
        return {
            "Color_Mode": "Negative_Color",
            "Primary_Color_Hex": "#800080",
            "Shape_Density": "INSTABILITY",
            "Movement_Speed": "HIGH",
            "Focus_Target": "PATTERN_BREAK"
        }

    else:  # CHAOS
        return {
            "Color_Mode": "Random_Noise",
            "Primary_Color_Hex": "#FF0000",
            "Shape_Density": "LOW_COMPLEXITY",
            "Movement_Speed": "EXTREME",
            "Focus_Target": "NOISE_FIELD"
        }


SPDX-License-Identifier: MIT