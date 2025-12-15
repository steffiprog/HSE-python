import re
import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# ================================================
# Путь к шрифту 
ROBOTO_FONT_PATH = r"/Users/stefanieschwarz/Downloads/Roboto-Light.ttf"

# Папка для сохранения результатов
OUTPUT_FOLDER = r"./wordcloud_output"

# Пути к файлам 
PATH_REGIONAL = r"/Users/stefanieschwarz/Downloads/метафоры_рег.txt"
PATH_CAPITAL  = r"/Users/stefanieschwarz/Downloads/метафоры_стол.txt"
# ================================================

# Доменные стоп-слова
DOMAIN_STOPWORDS = {
    "университет","миссия","образование","деятельность",
    "школа","организация","россия","российский","подготовка",
    "поддержание","обеспечение","создание","содействие",
    "и","в","об","о","от","обеспечить", "страна"
}

# Регулярка (очистка от всего, кроме букв и пробелов)
CLEAN_RE = re.compile(r'[^А-Яа-яЁёA-Za-z\s]', flags=re.UNICODE)

# Функции 
def load_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def clean_text(text):
    text = text.lower()
    text = CLEAN_RE.sub(" ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def lemmatize_list(texts, stopwords_extra):
    nlp = spacy.load("ru_core_news_sm")
    results = []
    for doc in nlp.pipe(texts):
        lemmas = []
        for t in doc:
            lemma = t.lemma_.lower().strip()
            if not lemma:
                continue
            if t.is_stop:
                continue
            if lemma in stopwords_extra:
                continue
            if len(lemma) < 2:
                continue
            if not re.match(r'^[а-яё]+$', lemma):
                continue
            lemmas.append(lemma)
        results.append(lemmas)
    return results

def join_lemmas(lemma_list):
    return " ".join(lemma_list)

def make_wordcloud(text, filename):
    wc = WordCloud(
        background_color="white",
        width=2048,
        height=1152,
        font_path=ROBOTO_FONT_PATH,
        collocations=True,
        max_words=80
    ).generate(text)
    
    plt.figure(figsize=(12, 6))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    plt.savefig(filepath, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"✔ Облако сохранено: {filepath}")


# Запуск обработки 
regional_raw = load_lines(PATH_REGIONAL)
capital_raw  = load_lines(PATH_CAPITAL)

regional_clean = [clean_text(t) for t in regional_raw]
capital_clean  = [clean_text(t) for t in capital_raw]

regional_lemmas = lemmatize_list(regional_clean, DOMAIN_STOPWORDS)
capital_lemmas  = lemmatize_list(capital_clean, DOMAIN_STOPWORDS)

regional_text = " ".join(join_lemmas(x) for x in regional_lemmas)
capital_text  = " ".join(join_lemmas(x) for x in capital_lemmas)

make_wordcloud(regional_text, "regional_wordcloud.png")
make_wordcloud(capital_text, "capital_wordcloud.png")

print("\nОблака сохранены в:", OUTPUT_FOLDER)
