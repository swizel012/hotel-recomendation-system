from flask import Flask, request, render_template
import pandas as pd
from textblob import TextBlob

app = Flask(__name__)

# Load hotel data
file_path = 'C://Users//91749//Downloads/hotel_data (1).xlsx'
df_hotels = pd.read_excel(file_path)

# Clean column names
df_hotels.columns = df_hotels.columns.str.strip()

# Format 'Amenities' column as a list
df_hotels['Amenities'] = df_hotels['Amenities'].apply(lambda x: [amenity.strip() for amenity in x.split(',')])

# Extract distinct amenities
def get_distinct_amenities(df):
    all_amenities = set([amenity for sublist in df['Amenities'] for amenity in sublist])
    return sorted(all_amenities)

# Calculate sentiment scores
def calculate_service_sentiments(df):
    if 'review' in df.columns:
        df['SentimentScore'] = df['review'].apply(lambda review: TextBlob(str(review)).sentiment.polarity)
    return df

# Recommend hotels based on sentiment scores and selected amenities
def recommend_hotels_based_on_services(df, selected_amenities):
    df = df[df['Amenities'].apply(lambda amenities: all(amenity in amenities for amenity in selected_amenities))]
    if 'SentimentScore' in df.columns:
        df = df.sort_values(by='SentimentScore', ascending=False)
    return df

@app.route('/')
def index():
    distinct_amenities = get_distinct_amenities(df_hotels)
    return render_template('index.html', amenities=distinct_amenities, recommendations=None)

@app.route('/recommend', methods=['POST'])
def recommend():
    selected_amenities = request.form.getlist('amenities')

    # Calculate sentiment scores
    df_hotels_with_sentiments = calculate_service_sentiments(df_hotels.copy())

    # Filter hotels based on selected amenities
    recommendations = recommend_hotels_based_on_services(df_hotels_with_sentiments, selected_amenities)

    # Drop duplicates based on hotel name
    recommendations = recommendations.drop_duplicates(subset=['Hotel name'])

    # Limit to top 6 recommendations
    recommendations = recommendations.head(6)

    return render_template('index.html', amenities=get_distinct_amenities(df_hotels), recommendations=recommendations.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
