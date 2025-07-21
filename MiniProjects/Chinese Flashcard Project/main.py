BACKGROUND_COLOR = "#B1DDC6"
import pandas

with open("data/chinese_words.csv", "r", encoding="utf-8") as file:
    data = pandas.read_csv(file)