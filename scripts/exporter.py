from datetime import datetime

from plexapi.server import PlexServer

from config import plex_base_url, plex_token

plex = PlexServer(plex_base_url, plex_token)

movies = plex.library.section('Movies')
for video in movies.search():
    if video.originallyAvailableAt:
        print(video.title, video.originallyAvailableAt.year)
