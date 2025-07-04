# Placeholder content for visualizer.py
import matplotlib.pyplot as plt

def generate_sentiment_plot(df):
    df['sentiment'].value_counts().plot(kind='bar')
    plt.title("Sentiment Distribution")
    plt.savefig("outputs/plots/sentiment_distribution.png")
    plt.close()
