#JSON Config: Create a settings.json file, write a function to load settings, and another to update 
#a specific key.


import json
import os
CONFIG_FILE = 'settings.json'
def load_settings():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)
def update_setting(key, value):
    settings = load_settings()
    settings[key] = value
    with open(CONFIG_FILE, 'w') as f:        json.dump(settings, f, indent=4)
# Example usage:
if __name__ == "__main__":
    # Load settings
    settings = load_settings()
    print("Current Settings:", settings)
    # Update a setting
    update_setting('theme', 'dark')
    print("Updated Settings:", load_settings())

    