import pickle
import pandas as pd

class Storage:

    def save_csv(filename, data):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding='utf-8')

    def save_pickle(filename, data):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    def load_pickle(filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data
