# visualizer.py
# Cham Visualizer v3.0 - Harmony Aware

from dataclasses import dataclass
from enum import Enum

class VisualMode(Enum):
    CHAOTIC = "chaotic"
    FLOW = "flow"
    COHERENT = "coherent"
    STILL = "still"

@dataclass
class VisualizerState:
    mode: str
    motion_speed: float
    noise_level: float
    color_spread: float
    focus_point: float  # 0.0=分散, 1.0=一点集中

def generate_visualizer(stage, c_value: float, harmony: float) -> VisualizerState:
    """
    harmony: Gemini Oracle から注入される調和度 (0.0-1.0)
    """

    if harmony > 0.88:
        mode = VisualMode.STILL
        return VisualizerState(
            mode=mode.value,
            motion_speed=0.05,
            noise_level=0.0,
            color_spread=0.1,
            focus_point=1.0
        )

    elif harmony > 0.6:
        mode = VisualMode.COHERENT
        return VisualizerState(
            mode=mode.value,
            motion_speed=0.2,
            noise_level=0.1,
            color_spread=0.3,
            focus_point=0.8
        )

    elif harmony > 0.3:
        mode = VisualMode.FLOW
        return VisualizerState(
            mode=mode.value,
            motion_speed=0.5,
            noise_level=0.4,
            color_spread=0.6,
            focus_point=0.5
        )

    else:
        mode = VisualMode.CHAOTIC
        return VisualizerState(
            mode=mode.value,
            motion_speed=0.9,
            noise_level=0.9,
            color_spread=1.0,
            focus_point=0.1
        )



SPDX-License-Identifier: MIT
