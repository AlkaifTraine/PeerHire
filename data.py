import pandas as pd

freelancers = pd.DataFrame([
    {"id": 1, "name": "Alice", "skills": "Python, Flask, ML", "experience": 3, "past_projects": 10, "hourly_rate": 30},
    {"id": 2, "name": "Bob", "skills": "JavaScript, React, Node", "experience": 5, "past_projects": 20, "hourly_rate": 40},
    {"id": 3, "name": "Charlie", "skills": "Python, Django, Data Science", "experience": 4, "past_projects": 15, "hourly_rate": 35},
    {"id": 4, "name": "David", "skills": "Java, Spring, ML", "experience": 2, "past_projects": 5, "hourly_rate": 25},
    {"id": 5, "name": "Eve", "skills": "Python, FastAPI, NLP", "experience": 6, "past_projects": 30, "hourly_rate": 50},
    {"id": 6, "name": "Frank", "skills": "C++, Embedded Systems", "experience": 4, "past_projects": 12, "hourly_rate": 45},
])

freelancers.to_csv("freelancers.csv", index=False)
