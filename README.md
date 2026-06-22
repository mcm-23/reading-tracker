# 📚 Reading Tracker

A Python tool that analyses my reading history from a [StoryGraph](https://www.thestorygraph.com/) export — and, crucially, **cleans up the mess that comes with it.**

---

## The problems I needed solved.

When you import a Goodreads library into StoryGraph, the export can come out tangled: **duplicate rows**, where the same book appears twice — one copy with your rating, one blank ghost. On my own library, ~232 of 977 rows were part of a duplicate set, inflating my book count and hiding ratings I'd actually given.

This tool detects those duplicates and collapses them **safely** — sorting so the *rated* copy always wins, never the blank one — turning a messy 977-row export into 861 real, distinct books.

---

## So far, what it does is

- **Loads** a StoryGraph CSV export into a pandas DataFrame
- **Cleans duplicates** from Goodreads → StoryGraph migration, preserving ratings
- **Counts books by reading status** (read / to-read / DNF / paused / currently-reading like most Tracker apps)
- **Calculates average rating** across finished books (also a known and more or less expected feature)
- **Breaks down the full ratings distribution**, including hidden blanks (`NaN`)
- **Finds finished-but-unrated books** — a real to-do list of ratings I forgot to log
- **Exports** filtered results back to CSV

## What's coming (planned)

See [`ROADMAP.md`](ROADMAP.md) for the full plan. Highlights:

- Stats to match StoryGraph's paywalled features (Custom Charts, extra stats filters, and compare stats even further)
- Proper genre analysis from messy multi-tag cells
- Charts (matplotlib) for the data worth *seeing*
- Adding more Next Up from the TBR — behavioural analysis of planned vs actual reading order
- A TBR reality check (how many years to clear the backlog at my current pace) 
- First-class **fanfiction tracking** — the thing no mainstream app does
- Eventually: a small interactive app (likely Streamlit)

---

## Built with

- **Python**
- **pandas**

## Notes

The reading data itself (`*.csv`) is deliberately **not** committed — it's personal. The code is public though. 🔒

---

*This project started as a way to learn Python and pandas hands-on, using data I actually care about. It's a work in progress, and the commit history is the learning log.*