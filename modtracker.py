import praw
import os
import glob

files = glob.glob('./users/*')
for f in files:
    os.remove(f)

r = praw.Reddit(user_agent='modtracker - /u/nannal')
#while loop of subrddit from here bby
for line in open('/home/danielabbott/reddit/redditmods/subreddit','r'):
        sub = str(line.rstrip('\n'))
        print sub
        try:

            mods= r.get_moderators(sub.strip())
            print "OK"
            for Redditor in mods:
                writeloc=str("./users/"+str(Redditor))
                target = open(writeloc, 'a')
                target.write(sub+"\n")
                target.close()
        except:
            target2 = open("errorsubs", 'a')
            target2.write(sub+"\n")
            target2.close()
            print "ERROR"
