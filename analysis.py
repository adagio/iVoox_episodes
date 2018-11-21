import pandas as pd

program_url_id = '1454279'

df = pd.read_csv(f'storage/episodes-{program_url_id}.csv')
df = df[['title','time','likes','comments']]
df = df.dropna() # remove rows with NaN values

df_sorted_by_likes = df[['title', 'likes']].sort_values(by='likes', ascending=False)

print(df_sorted_by_likes.head(10))

df_sorted_by_likes = df[['title', 'likes']].sort_values(by='likes')

print(df_sorted_by_likes.head(10))

likes_values = df_sorted_by_likes[['likes']]

print(likes_values.describe())

df_sorted_by_comments = df[['title', 'comments']].sort_values(by='comments', ascending=False)

print(df_sorted_by_comments.head(10))

df_sorted_by_comments = df[['title', 'comments']].sort_values(by='comments')

print(df_sorted_by_comments.head(10))

comments_values = df_sorted_by_comments[['comments']]

print(comments_values.describe())


