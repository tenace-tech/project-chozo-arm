import time
import logging

# Configure logging to look like system messages
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# 1. THE DEPENDENCY INJECTION
# We try to import the real hardware library. If it fails, we flag it.
try:
    from buildhat import Motor
    HARDWARE_PRESENT = True
except ImportError:
    HARDWARE_PRESENT = False
    logger.warning("BuildHAT library not found. Running in SIMULATION MODE.")

class ChozoMotor:
    """
    A wrapper class that handles both physical LEGO motors and 
    simulated motors for development on PC.
    """
    def __init__(self, port):
        self.port = port
        self.target_position = 0
        self.current_position = 0
        
        if HARDWARE_PRESENT:
            # Initialize the real hardware
            try:
                self.driver = Motor(port)
                # Reset position to 0 on startup (Homing will come later)
                self.driver.plimit(1.0) # Set power limit to avoid burnout
                self.driver.run_to_position(0)
            except Exception as e:
                logger.error(f"Failed to connect to motor on port {port}: {e}")
                self.driver = None
        else:
            self.driver = None

    def run_to_position(self, degrees, speed=50, blocking=True):
        """
        Moves the motor to an absolute position (degrees).
        """
        self.target_position = degrees
        
        if HARDWARE_PRESENT and self.driver:
            # REAL HARDWARE EXECUTION
            self.driver.run_to_position(degrees, speed, blocking=blocking)
            self.current_position = self.driver.get_aposition()
        else:
            # SIMULATION EXECUTION
            logger.info(f"MOTOR {self.port}: Moving to {degrees}° at {speed}% speed...")
            
            if blocking:
                # Simulate the time it takes to move (crude approximation)
                # Let's assume 100 degrees takes 0.5 seconds at speed 50
                distance = abs(self.target_position - self.current_position)
                delay = (distance / 100) * (100 / speed) * 0.5
                time.sleep(delay)
                
            self.current_position = degrees
            logger.info(f"MOTOR {self.port}: Arrived at {self.current_position}°")

    def get_position(self):
        """Returns the current position in degrees."""
        if HARDWARE_PRESENT and self.driver:
            return self.driver.get_aposition()
        return self.current_position