# Provides the entirety of the book string to console
def get_book_text(filePathToBook):
  returnContentString = ""
  with open(filePathToBook) as f:
    returnContentString = f.read()

  return returnContentString

# Provides the total word count in the book
def get_book_wordCount(filePathToBook):
  returnContentString = ""
  returnContentWordTotal = 0
  with open(filePathToBook) as f:
    returnContentString = f.read()
    returnContentWordTotal = len(returnContentString.split())

  return returnContentWordTotal

# Provides the total character count broken down in the book
def get_book_charCounts(filePathToBook):
  returnContentString = ""
  returnContentCharCounts = {}

  with open(filePathToBook) as f:
    returnContentStringRaw = f.read()
    returnContentString = returnContentStringRaw.lower()

    for char in returnContentString:
      if char in returnContentCharCounts:
        returnContentCharCounts[char] += 1
      else:
        returnContentCharCounts[char] = 1

  return returnContentCharCounts
