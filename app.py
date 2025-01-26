import csv

def getWantToRead(newDict, oldDict):
    for row in oldDict:
        if row[16] == 'to-read':
            newDict.append({'title': row[1], 'author': row[2]})

def readCSVFile():
    filePath = 'csv-file/goodreads.csv'
    wantToRead = []
    with open(filePath) as fileObject:
        header = next(fileObject)
        reader = csv.reader(fileObject)
        getWantToRead(wantToRead, reader)
    return wantToRead            

def configureAuthorName():
    bookList = readCSVFile()
    for book in bookList:
        authorName = book['author']
        removeExtraSpaces = " ".join(authorName.split())
        book['author'] = removeExtraSpaces
    return bookList

def main():
    wantToRead = configureAuthorName()
    print(wantToRead)
      
main()
