import time
import logging
from .motor_driver import ChozoMotor

logger = logging.getLogger(__name__)

# CONFIGURATION: Which joint connects to which port?
# (We can move this to a json/yaml file later)
DEFAULT_CONFIG = {
    'base': 'A',
    'shoulder': 'B',
    'elbow': 'C',
    'wrist_1': 'D',
    'wrist_2': 'E',
    'wrist_3': 'F'
}

class RobotArm:
    """
    The Main Controller for the Chozo Arm.
    Orchestrates all 6 motors and maintains the robot's kinematic state.
    """
    def __init__(self, port_config=None):
        self.config = port_config if port_config else DEFAULT_CONFIG
        self.joints = {}
        
        logger.info("Initializing Chozo Arm Subsystems...")
        
        # Initialize all motors based on config
        for joint_name, port in self.config.items():
            logger.info(f"  - Configuring {joint_name} on Port {port}...")
            self.joints[joint_name] = ChozoMotor(port)
            
        logger.info("System Online.")

    def home(self):
        """
        Calibration sequence to find zero points.
        (Placeholder: For now, we assume current position is zero)
        """
        logger.info("Starting Homing Sequence...")
        # TODO: Implement current-sensing homing logic here
        for name, motor in self.joints.items():
            motor.current_position = 0
            motor.target_position = 0
        logger.info("Homing Complete. All joints at 0.0°")

    def set_joint_angle(self, joint_name, angle, speed=50, blocking=True):
        """
        Moves a specific joint to a target angle.
        """
        if joint_name not in self.joints:
            logger.error(f"Invalid joint name: {joint_name}")
            return
            
        motor = self.joints[joint_name]
        motor.run_to_position(angle, speed, blocking)

    def get_pose(self):
        """
        Returns a dictionary of the current angles of all joints.
        Useful for telemetry or saving 'keyframes' for animation.
        """
        return {name: motor.get_position() for name, motor in self.joints.items()}

    def emergency_stop(self):
        """
        Cuts power to all motors immediately.
        """
        # TODO: Add hardware stop command when available
        logger.warning("EMERGENCY STOP TRIGGERED")