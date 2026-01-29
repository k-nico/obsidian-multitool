from datetime import datetime
import os.path
import shutil

from plexapi.server import PlexServer

from config import staging_path, obsidian_path, file_server_base_url, plex_base_url, plex_token


md_src_path = f'{staging_path}/Movies'
md_dest_path = f'{obsidian_path}/Movies/db'

plex = PlexServer(plex_base_url, plex_token)
movies = plex.library.section('Movies')


for video in movies.search():
    title = video.title
    sort_title = video.titleSort
    release_date = video.originallyAvailableAt
    downloaded = True
    release_year = video.originallyAvailableAt.year
    title_and_year = f'{title} ({release_year})'.replace(': ', '- ')
    md_file = f'{title_and_year}.md'
    is_movie = True
    poster_path = f'{file_server_base_url}/Posters/Movies/{title_and_year}.jpeg'
    textless_poster = True

    new_file = f'{staging_path}/{md_file}'

    fileContent = f'''---
Title: {title}
ReleaseDate: {release_date}
Downloaded: {downloaded}
isMovie: {is_movie}
Poster: {poster_path}
TextlessPoster: {textless_poster}
sortTitle: {sort_title}
---'''
    
    with open(new_file, 'x') as file:
        file.write(fileContent)
    
    shutil.move(new_file, md_dest_path)