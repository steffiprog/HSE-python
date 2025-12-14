#0 базовый синтаксис

import json 

# Открытие 
with open('data.json', 'r', encoding='utf-8') as f:
 config = json.load(f)

type(config) # dict

for key in config.keys():
  print(f'Ключи верхнего уровня: {key}')

for value in config['departments'].values():
  print(f'Значения словаря: {value}')

for key, value in config['departments'].items():
  print(f"Пара ключ-значение: {key}: {value}")
 
config['departments']['dev'].append("David")
print(f'Сотрудники отдела dev: {config['departments']['dev']}')
 
config['budget'] *= int(config["budget"]) * 1.1
print(f'Новый бюджет: {config['budget']}')

# Запись
with open('data_update.json', 'w', encoding='utf-8') as f:
 json.dump(config, f, ensure_ascii=False, indent=2)


 #1 Анализ конфигурации модели NLP

 config = {
    "model_name": "bert-base-uncased",
    "batch_size": 32,
    "max_length": 128,
    "learning_rate": 2e-5,
    "epochs": 3,
    "labels": ["positive", "negative", "neutral"]
}

way1 = config["learning_rate"]  
way2 = config.get("learning_rate")

config["early_stopping"] = True
config["batch_size"] = 64

for key, value in config.items():
    if type(value) == int:
        print(f"Числовые параметры конфигурации: {key}: {value}")

test_config = config.copy()
test_config["batch_size"] = 8
test_config["epochs"] = 1
for key, value in test_config.items():
    print(f"Версия для тестирования:  {key}: {value}")

#2 Обработка ответа от NLP-сервиса

api_response = {
    "text": "I really enjoyed the movie, the acting was amazing!",
    "sentiment": {
        "label": "positive",
        "score": 0.95,
        "confidence": "high"
    },
    "entities": [
        {"entity": "movie", "type": "ENTERTAINMENT", "confidence": 0.89},
        {"entity": "acting", "type": "SKILL", "confidence": 0.92}
    ],
    "language": "en",
    "processed_in": 0.45
}

score_val = {api_response["sentiment"]["score"]}
print({score_val})

for entity_name in api_response["entities"]:
    print({entity_name["entity"]})

max_confidence = max(api_response["entities"], 
                            key=lambda x: x["confidence"])
print(f"{max_confidence_entity['confidence']}: {max_confidence_entity['entity']}")

api_response["model_version"] = "2.1.0"
api_response["model_version"] = float()

print("Отфильтрованный список: ")
for key, value in api_response.items():
    if type(value) is not str:
        print(f"{key}: {value}")

#3 Конфигурация пайплайна обработки текста

pipeline_config = {
    "steps": {
        "tokenization": {"enabled": True, "method": "word"},
        "stopwords": {"enabled": True, "language": "english", "custom_words": []},
        "stemming": {"enabled": False, "algorithm": "porter"},
        "normalization": {"enabled": True, "lowercase": True, "remove_punct": True}
    },
    "input_encoding": "utf-8",
    "output_format": "tokens"
}

pipeline_config["steps"]["stemming"]["enabled"] = True
pipeline_config["steps"]["stemming"]["custom_words"] = "numbers"

enabled_steps = [step for step, config in pipeline_config["steps"].items() if config["enabled"] == True]
print(f"Включенные шаги: {enabled_steps}")

pipeline_config["output_format"] = "vectors"

enabled_steps = []
for step_name, step_config in pipeline_config["steps"].items():
    if step_config["enabled"]:
        enabled_steps.append(step_name)
print(f"Включенные шаги: {enabled_steps}")

# Создать упрощенную конфигурацию

simplified_config = {
    "steps": {},
    "input_encoding": pipeline_config["input_encoding"],
    "output_format": pipeline_config["output_format"]
}
for step_name, step_config in pipeline_config["steps"].items():
    if step_config["enabled"]:
        simplified_config["steps"][step_name] = step_config

print("Упрощенная конфигурация:")
print(simplified_config)

#4 Агрегация статистики NLP-моделей

models_stats = {
    "bert-base": {
        "accuracy": 0.92,
        "f1_score": 0.91,
        "inference_time": 120,
        "size_mb": 440
    },
    "distilbert": {
        "accuracy": 0.89,
        "f1_score": 0.88,
        "inference_time": 65,
        "size_mb": 250
    },
    "roberta-large": {
        "accuracy": 0.94,
        "f1_score": 0.93,
        "inference_time": 210,
        "size_mb": 1600
    }
}

max_accuracy_model = max(models_stats.items(), key=lambda x: x[1]["accuracy"])
print(f"Максимально точная модель: '{max_accuracy_model[0]}' = {max_accuracy_model[1]['accuracy']}")

inference_time = [model["inference_time"] for model in models_stats.values()]
avg_inference_time = sum(inference_time) / len(inference_time)
print(f"Среднее время inference: {avg_inference_time}")

metrics = {}
for name, data in models_stats.items():
    metrics[model_name] = {
        "accuracy": data["accuracy"],
        "f1_score": data["f1_score"]
    }

models_stats["albert-base"] = {
    "accuracy": 0.87,
    "f1_score": 0.86,
    "inference_time": 55,
    "size_mb": 180
}

filtered_models = {}
for model_name, model_data in models_stats.items():
    if model_data["size_mb"] < 500:
        filtered_models[model_name] = model_data

#5 Работа с JSON-конфигом NLP-сервиса

with open('nlp_service_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

config["models"]["summarization"] = {
    "path": "/models/summarization",
    "max_input_length": 1024,
    "supported_languages": ["en", "es"]
}

config["rate_limit"] += 50
config["models"]["sentiment"]["supported_languages"].append("ru")

server_settings = config["server"]

with open("nlp_service_config_updated.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)
