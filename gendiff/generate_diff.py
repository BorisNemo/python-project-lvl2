import json


def get_data_file(filepath):
    with open(filepath) as file:
        return json.load(file)


def generate_diff(file_path1, file_path2):
    file1 = get_data_file(file_path1)
    file2 = get_data_file(file_path2)
    diff_data = {}
    keys = list(set(file1.keys()) | set(file2.keys()))
    keys.sort()
    for key in keys:
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                diff_data[f'  {key}'] = file1[key]
            else:
                diff_data[f'- {key}'] = file1[key]
                diff_data[f'+ {key}'] = file2[key]
        if key not in file2:
            diff_data[f'- {key}'] = file1[key]
        if key not in file1:
            diff_data[f'+ {key}'] = file2[key]

    result = json.dumps(diff_data, indent=2, separators=('', ': '))
    return result.replace('"', "")
