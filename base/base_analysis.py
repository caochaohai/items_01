import yaml
def data_analysis(file_name, code_key):
    with open("./data/" + file_name + ".yaml", 'r', encoding="utf-8") as f:
        data_list = list()
        data = yaml.load(f, Loader=yaml.FullLoader)[code_key]

        data_list.extend(data.values())
        print(data_list)
        return data_list