import cmd
import logging
from .robot_arm import RobotArm

# Configure logging to be less noisy for the CLI user
# We only want to see the "User Facing" info, not every debug flag
logging.basicConfig(level=logging.INFO, format='%(message)s')

class ChozoShell(cmd.Cmd):
    intro = 'Welcome to the CHOZO ARM Command Interface.\nType "help" or "?" to list commands.\n'
    prompt = '(chozo) '
    
    def preloop(self):
        """Initialize the robot before the shell starts."""
        print("Booting Hardware...")
        self.robot = RobotArm()
        print("System Online.")

    def do_move(self, arg):
        """
        Move a joint to a specific angle.
        Usage: move <joint_name> <angle>
        Example: move shoulder 45
        """
        args = arg.split()
        if len(args) != 2:
            print("Error: Usage is 'move <joint> <angle>'")
            return
            
        joint, angle = args[0], args[1]
        
        try:
            angle_val = float(angle)
            print(f"Commanding {joint} to {angle_val} degrees...")
            self.robot.set_joint_angle(joint, angle_val)
        except ValueError:
            print("Error: Angle must be a number.")
        except Exception as e:
            print(f"Error: {e}")

    def do_status(self, arg):
        """Show current telemetry for all joints."""
        pose = self.robot.get_pose()
        print("\n--- TELETMETRY ---")
        for joint, angle in pose.items():
            print(f"{joint.ljust(10)}: {angle:>6.1f}°")
        print("------------------\n")

    def do_home(self, arg):
        """Run the homing sequence."""
        self.robot.home()

    def do_exit(self, arg):
        """Shutdown and exit."""
        print("Shutting down...")
        return True

if __name__ == '__main__':
    ChozoShell().cmdloop()