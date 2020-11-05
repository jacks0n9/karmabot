
#!/usr/bin/python
import praw
import pdb
import re
import os
reddit = praw.Reddit('bot1')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

with open("posts_replied_to.txt", "r") as f:
    posts_replied_to = f.read()
    posts_replied_to = list(filter(None, posts_replied_to))
subreddit = reddit.subreddit("justtestingmybot")

for submission in subreddit.new():
    if submission.id not in posts_replied_to:
                posts_replied_to.append(submission.id)
                submission.reply("Hi there. I am a bot in testing phase.")
                submission.upvote()
                with open("posts_replied_to.txt", "w") as f:
                    f.write(str(posts_replied_to))
                    f.close()