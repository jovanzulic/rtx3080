import yaml

filename = './config/stores.yaml'


def get_data():
    with open(filename) as f:
        return yaml.load(f, Loader=yaml.FullLoader)
