import json


def load_users():
    '''
    function to load user data from json file
    '''
    try:
        with open('data/users_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_users(users):
    '''
    functions to save data to json file
    '''
    with open('users_data.json', 'w') as file:
        json.dump(users, file, indent=4)