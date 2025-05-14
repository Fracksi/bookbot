#!/usr/bin/env python

import stats


def main():
    bookFileLocation = "books/frankenstein.txt"
    try:
      print("============ BOOKBOT ============")
      print(f"Analyzing book found at {bookFileLocation}...")

      # Prints the total number of words in the book
      print("----------- Word Count ----------")
      totalWordCount = stats.get_book_wordCount(bookFileLocation)
      print(f"found {totalWordCount} total words")

      # Prints the total number of characters in the book, per character count
      print("----------- Character Count ----------")
      totalCharCount = stats.get_book_charCounts(bookFileLocation)
      for char in totalCharCount:
        print(f"{char['char']}: {char['num']}")

      # Prints the entirety of the book text to console
      # printedTextOut = stats.get_book_text(bookFileLocation)
      # print(printedTextOut)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
