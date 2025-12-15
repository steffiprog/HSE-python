import re
from collections import Counter

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    return text

def tokenize_text(text):
    text = text.lower()
    text = re.sub(r'[^а-яёa-z0-9.,!?;: -]', ' ', text)  
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def create_frequency_dict(text):  
    words = text.split()
    freq_dict = Counter(words)
    return freq_dict

# Исполняемый скрипт 
if __name__ == "__main__":
    text = load_data("data.txt")
    print(f"Длина файла: {len(text)}")
    print("Первые 200 символов:", text[:200])
    
    cleaned_text = clean_text(text)
    tokens = tokenize_text(cleaned_text)  
    print("После токенизации:", tokens[:200])
    
    freq_dict = create_frequency_dict(tokens)  
    print("Самые частые слова:", freq_dict.most_common(5))