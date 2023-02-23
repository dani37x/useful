def open_json(file_path):
    data = []
    with open(file_path) as fp:
        data = json.load(fp)
    return data


def save_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4, separators=(',', ': '))
        
        
# example usage


def user_searched(username, ip, searched):

    objects_list = open_json(file_path=DATA)

    searched = str(searched).lower()

    objects_list.append({
            "username": f"{username}",
            "ip": f"{ip}",
            "searched": f"{searched}",
            "time": f"{str(datetime.now().strftime('%d-%m-%Y  %H:%M:%S'))}"
        })

    save_json(file_path=DATA, data=objects_list)
