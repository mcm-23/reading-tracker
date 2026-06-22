🗺️ Roadmap

The plan for this tracker, roughly in build order. Each phase is sized to be a branch (or a few), so the commit history doubles as a learning log.

Legend: ✅ done · 🔨 next up · 🧭 planned · 🌠 aspirational


✅ Phase 1 — Core stats + data cleaning (done)

The foundation. Load real data, clean it, ask basic questions.

 Load StoryGraph CSV into a pandas DataFrame
 Inspect shape, columns, missing values (NaN)
 Count books by reading status (value_counts)
 Average rating of finished books (.mean() on a filtered set)
 Full ratings distribution including blanks (dropna=False)
 Find finished-but-unrated books (combined filter with & and .isna())
 Detect and safely remove migration duplicates (sort-then-drop_duplicates)
 Export filtered results to CSV (.to_csv)



🔨 Phase 2 — Match StoryGraph's paid stats

Rebuild the things the apps charge for. Mostly remixes of Phase 1 tools.

 Most-read authors (value_counts on Authors)
 Average rating per genre/tag — harshest vs most generous
 Next Up longer list
 TBR reality check: at my current reading pace, how many years to clear the to-read pile? (math + a reckoning)


Teaches: confident reuse of filtering, grouping intuition, simple derived metrics.


🧭 Phase 3 — Time & grouping

The most job-relevant pandas skill set.


 Parse date columns properly (Last Date Read, Dates Read)
 Books read per year
 Pages read per month
 Pages read per week
 Reading pace trends over time


Lessons: groupby(), date handling — the two biggest pandas skills still ahead.


🧭 Phase 4 — Tags done right

The Tags column crams multiple values into one cell ("dark academia, queer, gothic"). Untangling it reveals what I actually read.


 Split multi-value tag cells into individual tags
 True genre/tag frequency counts
 Cross genre with rating ("do I rate dark academia higher than I think?")

Lessons: string operations, .str.split(), explode(), reshaping messy real-world columns.


🧭 Phase 5 — Charts

Where it stops being terminal text and becomes something worth screenshotting.


 Bar chart: books per year
 Ratings distribution as a histogram
 Genre breakdown visual
 Save charts as images for Substack / portfolio


Lessons: matplotlib basics, turning a DataFrame into a figure.


🧭 Phase 6 — Behavioural analysis (the original idea)

The part that's genuinely hard to buy anywhere. Track not just what I read but how my reading deviates from my plans.


 Extend "Next Up" beyond 5 books — a real planned queue through December
 Compare planned reading order vs actual reading order
 Detect when I jumped the queue — and what stole the show
 Surface which genres or moods most often break my plan
 "Reading behaviour change" summary over time


Lessons: joining/comparing datasets, ranking, sequence comparison — real analytical thinking.


🧭 Phase 7 — TBD '(most likely how to track my own fanfiction reading if I get to read some again this year)


Lessons: schema design, handling a heterogeneous dataset.


🌠 Future — Make it an app


 Move analysis into a Jupyter notebook (presentable, charted)
 Build an interactive dashboard (likely Streamlit)
 Persist a cleaned dataset so cleaning isn't re-run every time
 Long shot: a proper import pipeline that fixes export messes automatically



Roadmap is a living document. Phases will shuffle as I learn what's interesting and what's hard.