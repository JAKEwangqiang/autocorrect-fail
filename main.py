#!/usr/bin/env python3
"""Funniest Autocorrect Fail — entry.

The line is the entry's title on make.fun (one line, under 200 characters).
Running this prints it.
"""
LINE = "I texted my date 'I had a great thyme tonight' — autocorrect fixed it to 'great time' and ruined my only good herb joke."

def fail():
    """Return the autocorrect fail."""
    return LINE

def main():
    print(fail())

if __name__ == "__main__":
    main()
