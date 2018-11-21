

def analyze(df):

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


