from collections import Counter

print("Welcome to Dream Analysis!")

file_path = "dreams_data.txt"
all_keywords = []

stopwords = ["i", "was", "the", "a", "an", "and", "my", "in", "on", "from", "of", "to"]

# Define more dream categories
dream_categories = {
    "Romantic dream": ["love", "romantic", "kiss", "partner", "boyfriend", "girlfriend"],
    "Adventure dream": ["fly", "flying", "sky", "mountain", "adventure", "journey"],
    "Nightmare": ["fall", "falling", "scary", "nightmare", "dark", "monster"],
    "Weird dream": ["weird", "strange", "confused", "bizarre", "odd", "dreamlike"],
    "Happy dream": ["happy", "joy", "smile", "fun", "party", "laugh"],
    "Animal dream": ["dog", "cat", "animal", "lion", "snake", "elephant"],
    "Water dream": ["water", "river", "ocean", "swim", "drown", "rain"],
    "Flying dream": ["fly", "flying", "air", "sky", "helicopter", "plane"],
    "Chase dream": ["chase", "running", "escape", "hunted", "caught"],
    "Career/School dream": ["exam", "work", "job", "school", "boss", "teacher"]
}

while True:
    dream = input("\nEnter your dream (or type 'exit' to quit): ")
    
    if dream.lower() == "exit":
        print("\nThank you for using Dream Analysis!")
        break

    # Extract keywords
    keywords = [word.lower() for word in dream.split() if word.lower() not in stopwords]
    all_keywords.extend(keywords)
    print("Keywords in your dream:", keywords)

    # Determine category
    category_found = "Normal dream"  # default
    for category, words in dream_categories.items():
        if any(word in keywords for word in words):
            category_found = category
            break

    print("Dream category:", category_found)

    # Save dream and category to file
    with open(file_path, "a") as f:
        f.write(f"Dream: {dream}\nCategory: {category_found}\n\n")

# Show top 5 keywords
if all_keywords:
    keyword_counts = Counter(all_keywords)
    most_common = keyword_counts.most_common(5)
    print("\nMost common keywords across all dreams:")
    for word, count in most_common:
        print(f"{word}: {count} times")