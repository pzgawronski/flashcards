import pandas as pd

raw_words = {}

try:
    raw_words = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    raw_words = pd.read_csv("data/french_words.csv")
finally:
    words = raw_words.to_dict(orient="records")


def save():
    wordlist = pd.DataFrame(words)
    wordlist.to_csv("data/to_learn.csv", index=False)


if __name__ == "__main__":
    for pair in words:
        print(pair)
