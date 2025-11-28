# main.py

import os

def run_application():
    """
    The main logic function of the application.
    This function should contain the core business logic.
    """
    # Example: Check an environment variable (standard in GCP/Docker)
    environment = os.getenv('ENV', 'development')
    print(f"Starting application in {environment} mode.")
    
    # --- Your main code goes here ---
    print("Project initialized successfully on M4 Pro!")
    # --- End of main code ---
    
    return True

# --- Standard Python Entry Point ---
if __name__ == "__main__":
    # This block ensures the code only runs when executed directly
    # (i.e., when you run 'python main.py'), not when imported as a module.
    
    if run_application():
        print("Application finished execution.")
    else:
        print("Application failed.")