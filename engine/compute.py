# from os import path
# import graphlab as gl
# import graphlab
# gl.product_key.set_product_key('D7F2-866A-9982-60F0-CE29-2C19-F1FA-B376')
# gl.product_key.get_product_key()
# from datetime import datetime
#
# # Path to the dataset directory
# data_dir = 'engine/dataset/ml-20m'
#
# def comp(sf,user_id):
#     items = gl.SFrame.read_csv(path.join(data_dir, 'movies.csv'))
#
#     # Table of interactions between users and items: userId, movieId, rating, timestamp
#     actions = gl.SFrame.read_csv(path.join(data_dir, 'ratings.csv'))
#
#     ### Prepare Data ###
#
#     # Prepare the data by removing items that are rare
#     rare_items = actions.groupby('movieId', gl.aggregate.COUNT).sort('Count')
#     rare_items = rare_items[rare_items['Count'] <= 5]
#     items = items.filter_by(rare_items['movieId'], 'movieId', exclude=True)
#
#     actions = actions[actions['rating'].astype(float) >= 3]
#     actions = actions.filter_by(rare_items['movieId'], 'movieId', exclude=True)
#     print actions
#
#     # Extract year, title, and genre
#     items['year'] = items['title'].apply(lambda x: x[-5:-1])
#     items['title'] = items['title'].apply(lambda x: x[:-7])
#     items['genres'] = items['genres'].apply(lambda x: x.split('|'))
#
#     # Get the metadata ready
#     urls = gl.SFrame.read_csv(path.join(data_dir, 'movie_urls.csv'))
#     items = items.join(urls, on='movieId')
#     users = gl.SFrame.read_csv(path.join(data_dir, 'user_names.csv'))
#
#     training_data, validation_data = gl.recommender.util.random_split_by_user(actions, 'userId', 'movieId')
#
#     ### Train Recommender Model ###
#     model = gl.recommender.create(training_data,'userId', 'movieId',target='rating')
#     # model=gl.load_model('my_model_file')
#
#
#
#     # model.predict(sf)
#     # print(model.predict(sf))
#     # print (model.recommend(user_id, new_observation_data=sf, k=10))
#     # print type(model.recommend(['1'], new_observation_data=sf, k=10))
#     data = model.recommend(user_id, new_user_data=sf, k=10)
#
#     # print(data.to_dataframe())
#     # g.export('output.json', orient='records')
#     #model.save('my_model_file')
#     return data.to_dataframe()
#     # Interactively evaluate and explore recommendations
#     # view = model.views.overview(observation_data=training_data,
#     #                             validation_set=validation_data,
#     #                             user_data=users,
#     #                             user_name_column='name',
#     #                             item_data=items,
#     #                             item_name_column='title',
#     #                             item_url_column='url')
#     # view.show()