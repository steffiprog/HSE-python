#1 

customers = {
    "maria28": [28, "female", "Moscow", "frequent purchases"],
    "alex_tech": [35, "male", "Saint Petersburg", "rare purchases"],
    "olga_shopper": [24, "female", "Kazan", "occasional purchases"],
}

customers = dict(
    maria28=[28, "female", "Moscow", "frequent purchases"],
    alex_tech=[35, "male", "Saint Petersburg", "rare purchases"],
    olga_shopper=[24, "female", "Kazan", "occasional purchases"],
)

customers = dict(
    [
        ("maria28", [28, "female", "Moscow", "frequent purchases"]),
        ("alex_tech", [35, "male", "Saint Petersburg", "rare purchases"]),
        ("olga_shopper", [24, "female", "Kazan", "occasional purchases"]),
    ]
)

# 2
value1 = customers[“maria28”]
value2 = customers.get(“alex_tech”)
value3 = customers.get(“real name“, „N/A“)

print(value1, value2, value3)

#3 
customers[„maria28“] = [29, „female“, „Moscow“, „rare purchases“] #изменение 
customers[„alex_tech“] = [35, „male, „Saint Petersburg“, „rare purchases“, „premium customer“] #добавление
                          
#4
removed_customer = customers.pop("maria28")
del customers["maria28"]

#5
import json 

# Открытие 
with open('data.json', 'r', encoding='utf-8') as f:
 config = json.load(f)

type(config) # dict

# Запись
with open('data_update.json', 'w', encoding='utf-8') as f:
 json.dump(config, f, ensure_ascii=False, indent=2)