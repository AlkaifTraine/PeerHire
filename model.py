import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_freelancers(job_desc, max_rate, freelancers_path="freelancers.csv"):
    df = pd.read_csv(freelancers_path)

    # Remove freelancers who charge more than budget
    df = df[df['hourly_rate'] <= int(max_rate)]

    # Combine skills + experience
    df['profile'] = df['skills'] + " " + df['experience'].astype(str) + " years"

    # Add job description
    job = job_desc + f" {max_rate} budget"

    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform(df['profile'].tolist() + [job])

    # Last one is the job
    cosine_sim = cosine_similarity(vectors[-1], vectors[:-1])

    top_indices = cosine_sim[0].argsort()[-5:][::-1]
    return df.iloc[top_indices][['name', 'skills', 'experience', 'hourly_rate']].to_dict(orient='records')
