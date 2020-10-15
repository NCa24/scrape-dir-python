from os import listdir, stat
from os.path import isfile, isdir ,join
import datetime

def getBirthTimeFromStat(fileMetadata: str):
    birthTimeInS = fileMetadata.st_birthtime
    return datetime.datetime.fromtimestamp(birthTimeInS).strftime("%d %b, %Y")

def getByteSize(fileMetadata):
    return fileMetadata.st_size

def scrapeDirectory(path: str):
  acc = []
  for file in listdir(path):
    if isfile(join(path, file)):
      stats = stat(join(path, file))
      dic = {"file": file, "path": join(path, file), "creationDate": getBirthTimeFromStat(stats), "size": getByteSize(stats)}
      acc.append(dic)
    if isdir(join(path, file)):
      acc.extend(scrapeDirectory(join(path, file)))
  return acc

files = scrapeDirectory("./")

uniqueSet = set()
uniqueFiles = []
duplicateFiles = []
for file in files:
  tup = (file.get("file"), file.get("creationDate")) # creating a tuple to add to set
  if tup not in uniqueSet:
    uniqueSet.add(tup)
    uniqueFiles.append(file)
  else:
    duplicateFiles.append(file)

for file in uniqueFiles:
  print(file.get("file"), file.get("path"), file.get("creationDate"))

print("duplicate")

for file in duplicateFiles:
  print(file.get("file"), file.get("path"), file.get("creationDate"))