# Reading Tracker

A Python tool that analyses my reading history from a StoryGraph export —
and cleans up the mess that comes with it.

## What it does
- Loads ~860 books from a CSV export
- Cleans duplicate rows left behind by a Goodreads → StoryGraph migration
- Answers questions the reading apps lock behind a paywall: average rating,
  ratings breakdown, books per status, finished-but-unrated books

## Built with
- Python
- pandas

## Why
Existing trackers don't fix the duplicate-and-lost-rating problem that
happens when you move your library between apps. This does. It also forces me to learn how to code features instead of accumulating subscriptions because I love this type of data.
