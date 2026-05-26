test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high',
}
test_tuple = ("My Key", "My Value")

def add_setting(obj, setting):
    
    if not isinstance(obj, dict):
        return(f'Object expected as first parameter, got {type(obj)}')        
    if not isinstance(setting, tuple):
        return(f'Tuple expected as second parameter, got {type(setting)}')

    setting_key, setting_value = setting
    setting_key = setting_key.lower()
    setting_value = setting_value.lower()

    if setting_key in obj:
        return f'Setting \'{setting_key}\' already exists! Cannot add a new setting with this name.'
    else:
        obj[setting_key] = setting_value
        return f'Setting \'{setting_key}\' added with value \'{setting_value}\' successfully!'

def update_setting(obj, setting):

    if not isinstance(obj, dict):
        return(f'Object expected as first parameter, got {type(obj)}')        
    if not isinstance(setting, tuple):
        return(f'Tuple expected as second parameter, got {type(setting)}')        

    setting_key, setting_value = setting
    setting_key = setting_key.lower()
    setting_value = setting_value.lower()

    if setting_key in obj:
        obj[setting_key] = setting_value
        return f'Setting \'{setting_key}\' updated to \'{setting_value}\' successfully!'
    else:
        return f'Setting \'{setting_key}\' does not exist! Cannot update a non-existing setting.'

def delete_setting(obj, setting):

    if not isinstance(obj, dict):
        return(f'Object expected as first parameter, got {type(obj)}')        
    if not isinstance(setting, str):
        return(f'String expected as second parameter, got {type(setting)}')        

    setting_key = setting.lower()

    if setting_key in obj:
        del obj[setting_key]
        return f'Setting \'{setting_key}\' deleted successfully!'
    else:
        return f'Setting not found!'

def view_settings(obj):
    if not isinstance(obj, dict):
        return(f'Object expected as first parameter, got {type(obj)}')        

    if len(obj) == 0:
        return 'No settings available.'
    else:
        settings = "Current User Settings:\n"
        for k, v in obj.items():
            settings += f'{k.capitalize()}: {v}\n'
        return settings

print(add_setting(test_settings, test_tuple))
print(update_setting(test_settings, test_tuple))
print(delete_setting(test_settings, 'theme'))
print(view_settings(test_settings))