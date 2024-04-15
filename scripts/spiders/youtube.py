# -*- coding: utf-8 -*-
# @shiweitong 2024/4/12


import pandas as pd
from googleapiclient.discovery import build

DEVELOPER_KEY = 'YOUR_API_KEY_HERE'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def _get_video_comments(service, **kwargs):
    comments, dates, likes, video_titles = [], [], [], []
    results = service.commentThreads().list(**kwargs).execute()

    while results:
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            date = item['snippet']['topLevelComment']['snippet']['publishedAt']
            like = item['snippet']['topLevelComment']['snippet']['likeCount']
            video_title = service.videos().list(part='snippet', id=kwargs['videoId']).execute()['items'][0]['snippet'][
                'title']

            comments.append(comment)
            dates.append(date)
            likes.append(like)
            video_titles.append(video_title)

        # check if there are more comments
        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']
            results = service.commentThreads().list(**kwargs).execute()
        else:
            break

    return pd.DataFrame({'Video Title': video_titles, 'Comments': comments, 'Date': dates, 'Likes': likes})


def get_video_comments(video_id, only_comments=False):
    if 'http' in video_id:
        video_id = video_id.split('=')[-1].strip()
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    comments_df = _get_video_comments(youtube, part='snippet', videoId=video_id, textFormat='plainText')
    if only_comments:
        return comments_df["Comments"].tolist()
    else:
        return comments_df
