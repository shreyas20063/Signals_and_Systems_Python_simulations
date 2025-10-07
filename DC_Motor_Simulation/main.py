"""
DC Motor Feedback Control Simulation
=====================================

Course: Signals and Systems (EE204T)
Professor: Ameer Mulla
Students: Prathamesh Nerpagar, Duggimpudi Shreyas Reddy

About This Simulation:
---------------------
This interactive simulation demonstrates feedback control principles for DC motors.
It allows users to explore how different parameters affect system behavior:

- Amplifier gain (α): Controls the input signal amplification
- Feedback gain (β): Determines the feedback strength (0 to 1)
- Motor constant (γ): Represents motor torque-to-current ratio
- Lag pole (p): Adds second-order dynamics to the system

Features:
- Real-time visualization of pole-zero maps in the s-plane
- Step response analysis showing system transient behavior
- Toggle between First-Order and Second-Order system models
- Interactive sliders for parameter adjustment
- System stability analysis and steady-state value calculations

The simulation helps understand concepts like:
- Feedback control systems
- System stability and pole locations
- Transient response characteristics
- Steady-state behavior
"""

import matplotlib.pyplot as plt
from simulator import MotorFeedbackSimulator

def main():
    """Main entry point for the DC Motor Feedback Control Simulation"""
    simulator = MotorFeedbackSimulator()
    simulator.update_model(simulator.model_type)
    plt.show()

if __name__ == '__main__':
    main()
