# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import config

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = config.GOOGLE_OAUTH_CLIENT_ID

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_console()

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)


def getStats(id):
    request = youtube.videos().list(
        part="statistics",
        id=id
    )
    response = request.execute()

    '''
            {
          'kind': 'youtube#videoListResponse',
          'etag': 'pb0L2LNjZp0HpYItz4E3xWhrQbY',
          'items': [
            {
              'kind': 'youtube#video',
              'etag': 'gIVtTPCVAZridQQnCz2DSPuHsPA',
              'id': 'hwtrw64xQmQ',
              'statistics': {
                'viewCount': '4887',
                'likeCount': '1',
                'dislikeCount': '0',
                'favoriteCount': '0',
                'commentCount': '0'
              }
            }
          ],
          'pageInfo': {
            'totalResults': 1,
            'resultsPerPage': 1
          }
        }
    '''
    # print(response)

    return (response['items'][0]['statistics']['viewCount'], None)



# getStats('hwtrw64xQmQ')
