import time

def stopwatch():
    print("Simple Stopwatch")
    print("Commands: 'start', 'stop', 'reset', 'exit'")
    
    start_time = 0
    elapsed_time = 0
    running = False
    
    while True:
        command = input("Enter command: ").lower()
        
        if command == "start":
            if not running:
                start_time = time.time() - elapsed_time
                running = True
                print("Stopwatch started.")
            else:
                print("Stopwatch is already running.")
        
        elif command == "stop":
            if running:
                elapsed_time = time.time() - start_time
                running = False
                print(f"Stopwatch stopped at {elapsed_time:.2f} seconds.")
            else:
                print("Stopwatch is not running.")
        
        elif command == "reset":
            start_time = 0
            elapsed_time = 0
            running = False
            print("Stopwatch reset.")
        
        elif command == "exit":
            print("Exiting stopwatch.")
            break
        
        else:
            print("Invalid command. Use 'start', 'stop', 'reset', or 'exit'.")

stopwatch()
