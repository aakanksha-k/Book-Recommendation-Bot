import json

def lambda_handler(event, context):
    try:
        # Extract the genre slot value
        genre = event['sessionState']['intent']['slots']['Genre']['value']['interpretedValue']
        
        # Define book recommendations based on genre
        recommendations = {
            "science fiction": ["Dune by Frank Herbert", "Neuromancer by William Gibson"],
            "fantasy": ["The Hobbit by J.R.R. Tolkien", "Harry Potter by J.K. Rowling"],
            "mystery": ["Gone Girl by Gillian Flynn", "The Girl with the Dragon Tattoo by Stieg Larsson"],
            "romance": ["Pride and Prejudice by Jane Austen", "The Notebook by Nicholas Sparks"],
            "thriller": ["The Da Vinci Code by Dan Brown", "The Girl on the Train by Paula Hawkins"],
            "non-fiction": ["Sapiens by Yuval Noah Harari", "Educated by Tara Westover"],
            "historical": ["All the Light We Cannot See by Anthony Doerr", "The Nightingale by Kristin Hannah"],
            "biography": ["Steve Jobs by Walter Isaacson", "Becoming by Michelle Obama"],
            "young adult": ["The Fault in Our Stars by John Green", "Divergent by Veronica Roth"],
            "horror": ["It by Stephen King", "The Haunting of Hill House by Shirley Jackson"],
            "adventure": ["The Alchemist by Paulo Coelho", "Life of Pi by Yann Martel"],
            "self-help": ["How to Win Friends and Influence People by Dale Carnegie", "Atomic Habits by James Clear"],
            "classics": ["To Kill a Mockingbird by Harper Lee", "1984 by George Orwell"]
        }
        
        # Check if genre is provided and fetch recommendations
        if genre:
            genre_lower = genre.lower()
            if genre_lower in recommendations:
                recommended_books = recommendations[genre_lower]
                message = f"I recommend reading {', '.join(recommended_books)}."
            else:
                message = "I don't have recommendations for that genre. Please try another genre."
        else:
            message = "I'm sorry, I didn't catch the genre. Could you please repeat it?"
        
        # Return the response in the correct format
        response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": event['sessionState']['intent']['name'],
                    "state": "Fulfilled"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": message
                }
            ]
        }
        return response
    
    except Exception as e:
        print(f"Error: {e}")
        response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": event['sessionState']['intent']['name'],
                    "state": "Failed"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "There was an error processing your request. Please try again later."
                }
            ]
        }
        return response
