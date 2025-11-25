import random

def movie_chatbot():
    print("🎬 Welcome to MovieBot!")
    print("Ask me for a recommendation (e.g., 'action', 'comedy', 'romance'). Type 'exit' to quit.\n")

    # Predefined keyword-to-movie mapping
    recommendations = {
        "action": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
        "comedy": ["Superbad", "The Hangover", "Step Brothers"],
        "romance": ["The Notebook", "Pride & Prejudice", "La La Land"],
        "sci-fi": ["Interstellar", "The Matrix", "Blade Runner 2049"],
        "horror": ["Get Out", "The Conjuring", "A Quiet Place"]
    }

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("👋 Goodbye! Enjoy your movies!")
            break

        # Check if keyword exists
        if user_input in recommendations:
            movies = recommendations[user_input]
            choice = random.choice(movies)  # randomize recommendation
            print(f"MovieBot: You might enjoy '{choice}'!")
        else:
            print("MovieBot: Sorry, I don’t have recommendations for that genre. Try 'action', 'comedy', 'romance', 'sci-fi', or 'horror'.")

if __name__ == "__main__":
    movie_chatbot()