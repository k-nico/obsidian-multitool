import csv
from datetime import datetime
from mdutils import MdUtils
import shutil

from config import moviePath, obsidianPath

fileName = 'MovieExport.csv'
sourcePath = f'{moviePath}/{fileName}'
destPath = f'{obsidianPath}'
movie_list = []

with open(sourcePath, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)

    for row in csvReader:
        movie_list.append(row)

for movie in movie_list:
    title = movie.get('title')
    releaseDate = movie.get('releaseDate')
    releaseYear = datetime.strptime(releaseDate, '%m/%d/%Y').date().year
    downloaded = movie.get('downloaded')
    textlessPoster = movie.get('textlessPoster')
    movieFile = f'{title} ({releaseYear}).md'

    newFile = open(f'{moviePath}/{movieFile}', 'x')

# mdutils or frontmatter
    # with open(fileName, 'w') as mdFile:
    #     pass

    # shutil.move(sourcePath,destPath)

    # print(newFile.read())

    # for movie in movie_list:
    #     print(movie)
        # mdFile = MdUtils(file_name=fileName,title='movie')
        # print(mdFile)
    # mdFile.create_md_file()

    # if movie.endswith('.md'):
    #     shutil.move(sourcePath, destPath)