from src.motor_driver import ChozoMotor

def main():
    print("--- CHOZO ARM SYSTEM DIAGNOSTIC ---")
    
    # Initialize a "Virtual" Motor on Port A
    shoulder = ChozoMotor('A')
    
    print(f"Initial Position: {shoulder.get_position()}")
    
    # Command a movement
    print("Commanding move to 90 degrees...")
    shoulder.run_to_position(90, speed=50)
    
    print(f"Final Position: {shoulder.get_position()}")
    print("--- TEST COMPLETE ---")

if __name__ == "__main__":
    main()