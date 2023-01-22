#lamiae7
import f
import json
import pandas as pd
from facebook_scraper import get_posts
L=get_posts('ID_publication',cookies = 'www.facebook.com.cookies.json', options={"comments":True,"reactions" : True, "allow_extra_requests": True}) 628

#www.facebook.com.cookies.json étant le fichier json ou j'ai mis mes cookies
post_df_full = pd.DataFrame()
for post in L:# List des commentaires
    post_entry = post
    fb_post_df = pd.DataFrame.from_dict(post_entry, orient='index')
    fb_post_df = fb_post_df.transpose()
    post_df_full = post_df_full.append(fb_post_df)
    i=0
j=0
comments=[]
while j<len(B):
    while i<len(B[0]):
        comments.append(B[j][i]['comment_text'])
        i+=1
    j+=1

post_df_full = pd.DataFrame()
for post in L:
    post_entry = post
    fb_post_df = pd.DataFrame.from_dict(post_entry, orient='index')
    fb_post_df = fb_post_df.transpose()
    post_df_full = post_df_full.append(fb_post_df)

print(post_df_full.info())
print(post_df_full)