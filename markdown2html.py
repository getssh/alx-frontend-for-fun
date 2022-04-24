#!/usr/bin/python3
'''markdownhtml'''


if __name__ == "__main__":
  import sys

  if len(sys.argv) < 2:
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)
  elif len(sys.argv) == 3:
    try:
        with open(sys.argv[1]) as f:
            pass
    except: 
        print("Missing " + sys.argv[1])
        sys.exit(1)
  else:
    sys.exit(0)
