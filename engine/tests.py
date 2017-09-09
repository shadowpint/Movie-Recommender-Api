import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds
import os

from recommend.settings import BASE_DIR, MEDIA_ROOT

DATA_ROOT = os.path.join(BASE_DIR, 'engine')
data_dir =os.path.join(DATA_ROOT, 'dataset','ml-20m')
# ratings_list = [i.strip().split("::") for i in open('ml-1m/ratings.dat', 'r').readlines()]
# users_list = [i.strip().split("::") for i in open('ml-1m/users.dat', 'r').readlines()]
# movies_list = [i.strip().split("::") for i in open('ml-1m/movies.dat', 'r').readlines()]
#
# ratings = np.array(ratings_list)
#
# movies = np.array(movies_list)

# ratings_df = pd.DataFrame(ratings_list, columns = ['UserID', 'MovieID', 'Rating', 'Timestamp'], dtype = int)
# movies_df = pd.DataFrame(movies_list, columns = ['MovieID', 'Title', 'Genres'])
# movies_df['MovieID'] = movies_df['MovieID'].apply(pd.to_numeric)
# movies_df.to_csv('ml-1m/movies.csv')
# ratings_df.to_csv('ml-1m/ratings.csv')
#print movies_df.head()
#print ratings_df.head()

def compi(df2):
    ratings_df=pd.read_csv(os.path.join(MEDIA_ROOT, 'ratings.csv'))
    ratings_df = ratings_df.append(df2, ignore_index=True)

    # print ratings_df.tail()
    movies_df = pd.read_csv(os.path.join(MEDIA_ROOT, 'movies.csv'))

    R_df = ratings_df.pivot(index='UserID', columns='MovieID', values='Rating').fillna(0)
    # print R_df.head()

    R = R_df.as_matrix()
    user_ratings_mean = np.mean(R, axis=1)
    R_demeaned = R - user_ratings_mean.reshape(-1, 1)

    U, sigma, Vt = svds(R_demeaned, k=50)
    sigma = np.diag(sigma)

    all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)

    preds_df = pd.DataFrame(all_user_predicted_ratings, columns=R_df.columns)
    predictions = recommend_movies(preds_df, 2, movies_df, ratings_df, 5)
    predictions.to_csv('result.csv')
    return predictions

def recommend_movies(preds_df, userID, movies_df, original_ratings_df, num_recommendations=5):
    # Get and sort the user's predictions
    user_row_number = userID - 1  # UserID starts at 1, not 0
    sorted_user_predictions = preds_df.iloc[user_row_number].sort_values(ascending=False)  # UserID starts at 1
    r=pd.DataFrame(sorted_user_predictions)
    print r[r.columns[0]]
    # Get the user's data and merge in the movie information.
    user_data = original_ratings_df[original_ratings_df.UserID == (userID)]
    user_full = (user_data.merge(movies_df, how='left', left_on='MovieID', right_on='MovieID').
                 sort_values(['Rating'], ascending=False)
                 )

    print 'User {0} has already rated {1} movies.'.format(userID, user_full.shape[0])
    print 'Recommending highest {0} predicted ratings movies not already rated.'.format(num_recommendations)

    # Recommend the highest predicted rating movies that the user hasn't seen yet.
    recommendations = (movies_df[~movies_df['MovieID'].isin(user_full['MovieID'])].
                       merge(pd.DataFrame(sorted_user_predictions).reset_index(), how='left',
                             left_on='MovieID',
                             right_on='MovieID').
                       rename(columns={user_row_number: 'Predictions'}).
                       sort_values('Predictions', ascending=False).
                       iloc[:num_recommendations, :-1]
                       )

    # recommendations = (recommendations.merge(pd.DataFrame(sorted_user_predictions)).reset_index()
    #
    #              )
    print type(recommendations)
    return  recommendations




