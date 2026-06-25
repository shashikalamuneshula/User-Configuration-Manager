
test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}

def add_setting(settings_dict, setting_tuple):
    key = str(setting_tuple[0]).lower()
    value = str(setting_tuple[1]).lower()
    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict, setting_tuple):
    key = str(setting_tuple[0]).lower()
    value = str(setting_tuple[1]).lower()
    
    if key in settings_dict:
        settings_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict, key):
    key = str(key).lower()
    
    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"
        
    return "Setting not found!"

def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."
        
    output = "Current User Settings:\n"
    for key, value in settings_dict.items():
        output += f"{key.capitalize()}: {value}\n"
        
    return output
print(view_settings(test_settings))
#add setting
print(add_setting(test_settings, ('THEME', 'dark')))
print(add_setting(test_settings, ('language', 'English')))
#update setting
print(update_setting(test_settings, ('theme', 'light')))
print(update_setting(test_settings, ('font_size', 'medium')))
#delete setting
print(delete_setting(test_settings, 'VOLUME'))
print(delete_setting(test_settings, 'brightness'))
#empty dictionary
print(view_settings({}))


