import csv
from datetime import datetime
import shutil

from config import stagingPath, obsidianPath, fileServerBaseUrl

csvName = 'MovieExport.csv'
csvSrcPath = f'{stagingPath}/{csvName}'
mdSrcPath = f'{stagingPath}/Movies'
mdDestPath = f'{obsidianPath}/Movies/db'
movieList = []


with open(csvSrcPath, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)

    for row in csvReader:
        movieList.append(row)

for movie in movieList:
    title = movie.get('title')
    releaseDate = movie.get('releaseDate')
    downloaded = movie.get('downloaded')
    releaseYear = datetime.strptime(releaseDate, '%m/%d/%Y').date().year
    movieYear = f'{title} ({releaseYear})'
    mdFile = f'{movieYear}.md'
    poster = f'{fileServerBaseUrl}/Posters/Movies/{movieYear}.jpeg'
    textlessPoster = movie.get('textlessPoster')
    isMovie = movie.get('isMovie')

    newFile = f'{stagingPath}/{mdFile}'

    fileContent = f'''---
Title: {title}
ReleaseDate: {releaseDate}
Downloaded: {downloaded}
isMovie: {isMovie}
Poster: {poster}
TextlessPoster: {textlessPoster}
sortTitle: {title}
---'''
    
    with open(newFile, 'x') as file:
        file.write(fileContent)
    
    shutil.move(newFile,mdDestPath)