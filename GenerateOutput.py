import json

# Example data to be written to the JSON file
data = {
    "output": {
        "grade1": 0,1,2,3,4,5
    }
}

# Writing JSON data
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("JSON data has been written to 'output.json'")
