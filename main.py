#!/usr/bin/env python

import stats
import sys


def main():
  try:
    bookFileLocation = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookFileLocation}...")

    # Prints the total number of words in the book
    print("----------- Word Count ----------")
    totalWordCount = stats.get_book_wordCount(bookFileLocation)
    print(f"Found {totalWordCount} total words")

    # Prints the total number of characters in the book, per character count
    print("----------- Character Count ----------")
    totalCharCount = stats.get_book_charCounts(bookFileLocation)
    for char in totalCharCount:
      print(f"{char['char']}: {char['num']}")
  except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  except Exception as e:
    print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
