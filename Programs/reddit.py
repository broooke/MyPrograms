import os
import praw


reddit = praw.Reddit(client_id='NnlD1vekCdzMcQ',
                     client_secret='mMhYa1ldBWOfkDUmt-YT05XUSSR9fw',
                     user_agent='<console:HAPPY:1.0>')

subreddit = reddit.subreddit("television")
for post in subreddit.hot(limit=3):
    i=  0
    print("**************")
    print(post.title)
    for comment in post.comments:
        print("Comment:" + str((i+1)))
        if hasattr(comment, "body"):
            print("-----")
            print(comment.body)
