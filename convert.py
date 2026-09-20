import json

# 1. Load your original Excel-generated JSON
with open('input.json', 'r') as file:
    excel_data = json.load(file)

firebase_ready_data = {}

# 2. Loop through and create the "walk_X" keys
for item in excel_data:
    node_key = f"walk_{item['walkId']}" 
    firebase_ready_data[node_key] = item

final_output = {"walks": firebase_ready_data}

# 3. Save the new file
with open('firebase_ready.json', 'w') as file:
    json.dump(final_output, file, indent=2)

print("🎉 Success! 'firebase_ready.json' has been created.")
