# Define a rule-based expert system

# Rule 1
def rule1(symptoms):
    if "fever" in symptoms and "cough" in symptoms:
        return "You may have a flu."
    return None

# Rule 2
def rule2(symptoms):
    if "headache" in symptoms and "sore throat" in symptoms:
        return "You may have a common cold."
    return None

# Rule 3
def rule3(symptoms):
    if "rash" in symptoms and "itching" in symptoms:
        return "You may have an allergic reaction."
    return None

# Function to run the expert system
def run_expert_system():
    symptoms = []
    while True:
        user_input = input("Enter a symptom (or 'done' to finish): ")
        if user_input == "done":
            break
        symptoms.append(user_input)

    # Apply rules sequentially
    rules = [rule1, rule2, rule3]
    for rule in rules:
        result = rule(symptoms)
        if result is not None:
            print("Expert System:", result)
            return

    print("Expert System: No diagnosis could be made.")

# Run the expert system
run_expert_system()

