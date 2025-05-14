#!/usr/bin/env python

import stats


def main():
    try:
      # Prints the entirety of the book text to console
      # printedTextOut = stats.get_book_text("books/frankenstein.txt")
      # print(printedTextOut)

      # Prints the total number of words in the book
      totalWordCount = stats.get_book_wordCount("books/frankenstein.txt")
      print(f"{totalWordCount} words found in the document")

      # Prints the total number of characters in the book, per character count
      totalCharCount = stats.get_book_charCounts("books/frankenstein.txt")
      print(f"{totalCharCount}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
