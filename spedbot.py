import time
import praw
import datetime
x = 1
r = praw.Reddit('Comment crawler and responder by sped')

print 'Logging in....'
#put your login info here
r.login('USERNAME','PASSWORD')

print 'Replying to posts...'

already_done = set()
while True:
    #put the subreddit you want to scan here or ALL for all
    subreddit = r.get_subreddit('SUBREDDIT')
    subreddit_comments = subreddit.get_comments()
    #this is for the timestamp
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

 
    for comment in subreddit_comments:
            #change hello and reply to what you want to search for and reply with
            if comment.body == 'Hello' and comment.id not in already_done:
               comment.reply('world!')
               already_done.add(comment.id)
               print st, 'Replied to post.'
               time.sleep(15)
               x +=1
                           
                   
