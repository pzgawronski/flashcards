import pandas as pd

raw_words = pd.read_csv("data/french_words.csv")
words = [(raw_words.French[index], raw_words.English[index]) for index in range(len(raw_words))]

if __name__ == "__main__":
    print(words)
