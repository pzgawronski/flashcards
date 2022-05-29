import pandas as pd

raw_words = pd.read_csv("data/french_words.csv")
words = raw_words.to_dict(orient="records")

if __name__ == "__main__":
    for pair in words:
        print(pair)
