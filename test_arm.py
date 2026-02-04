import time
import logging
from src.robot_arm import RobotArm

# Configure logging to see our "Simulation" output clearly
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def main():
    print("=======================================")
    print("   CHOZO ARM: FLIGHT SOFTWARE v0.1     ")
    print("=======================================")
    
    # 1. Boot the Robot
    chozo = RobotArm()
    
    # 2. Run Homing (Simulation)
    chozo.home()
    
    # 3. Print Initial State
    print("\nInitial Pose:")
    print(chozo.get_pose())
    
    # 4. Perform a "Wave" Motion
    print("\n--- Initiating Wave Sequence ---")
    
    # Lift Shoulder
    print(">> Raising Shoulder...")
    chozo.set_joint_angle('shoulder', 45, speed=30)
    
    # Wave Elbow
    print(">> Waving Elbow...")
    chozo.set_joint_angle('elbow', 20, speed=100)
    chozo.set_joint_angle('elbow', -20, speed=100)
    chozo.set_joint_angle('elbow', 0, speed=50)
    
    # 5. Final Report
    print("\n--- Sequence Complete ---")
    print("Final Telemetry:")
    print(chozo.get_pose())

if __name__ == "__main__":
    main()