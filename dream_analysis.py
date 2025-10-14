print("Welcome to Dream Analysis!")

dream = input("Enter your dream: ")

keywords = dream.lower().split()
print("Keywords in your dream:", keywords)

if "fly" in keywords or "sky" in keywords:
    category = "Adventure dream"
elif "fall" in keywords or "scary" in keywords:
    category = "Nightmare"
else:
    category = "Normal dream"

print("Dream category:",category)
