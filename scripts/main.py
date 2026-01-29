from datetime import datetime
from pathlib import Path
import shutil

from plexapi.server import PlexServer

from config import staging_path, obsidian_path, file_server_base_url, plex_base_url, plex_token


md_src_path = f'{staging_path}/Movies'
md_dest_path = f'{obsidian_path}/Movies/db'

plex = PlexServer(plex_base_url, plex_token)
movies = plex.library.section('Movies')
count = 0


for video in movies.search():
    title = video.title.replace(': ', '- ')
    sort_title = video.titleSort.replace(': ','- ')
    release_year = video.originallyAvailableAt.year
    downloaded = True
    textless_poster = True

    title_and_year = f'{title} ({release_year})'
    
    poster_path = f'{file_server_base_url}/Posters/Movies/{title_and_year}.jpeg'
    is_movie = True

    md_file = f'{title_and_year}.md'

    new_file = f'{md_src_path}/{md_file}'

    fileContent = f'''---
Title: {title}
sortTitle: {sort_title}
ReleaseYear: {release_year}
Downloaded: {downloaded}
TextlessPoster: {textless_poster}
Poster: {poster_path}
isMovie: {is_movie}
---'''

    obsidian_file = Path(f'{md_dest_path}/{md_file}')

    if obsidian_file.exists():
        pass
    else:
        with open(new_file, 'x') as file:
            file.write(fileContent)
    
        shutil.move(new_file, md_dest_path)
        print(f'{md_dest_path}/{md_file} created')
        count += 1

print(count)