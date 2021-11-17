import wget as wget
# wget 'https://datasets.towardsai.net/combined_data_4.txt'
# wget 'https://raw.githubusercontent.com/towardsai/tutorials/master/recommendation_system_tutorial/movie_titles.csv'
# wget 'https://raw.githubusercontent.com/towardsai/tutorials/master/recommendation_system_tutorial/new_features.csv'

from datetime import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import os
import random
import matplotlib
import matplotlib.pyplot as plt
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

# import xgboost as xgb
from surprise import Reader, Dataset
from surprise import BaselineOnly
from surprise import KNNBaseline
from surprise import SVD
from surprise import SVDpp
from surprise.model_selection import GridSearchCV

def load_data():
    netflix_csv_file = open("netflix_rating.csv", mode = "w")
    rating_files = ['combined_data_4.txt']
    for file in rating_files:
        with open(file) as f:
            for line in f:
                line.strip()
                if line.endswith(":"):
                    movie_id = line.replace(":", "")
                else:
                    row_data = []
                    row_data = [item for item in line.split(",")]
                    row_data.insert(0, movie_id)
                    netflix_csv_file.write(",".join(row_data))
                    netflix_csv_file.write("\n")

    netflix_csv_file.close()
    df = pd.read_csv('netflix_rating.csv', sep=",", names = ["movie_id","customer_id", "rating", "date"])
    return df

# netflix_rating_df = load_data()
# netflix_rating_df
# netflix_rating_df.head()
#
# netflix_rating_df.duplicated(["movie_id","customer_id", "rating", "date"]).sum()
#
# split_value = int(len(netflix_rating_df) * 0.80)
# train_data = netflix_rating_df[:split_value]
# test_data = netflix_rating_df[split_value:]



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
