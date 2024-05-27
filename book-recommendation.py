import streamlit as st
import random
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GENAI_API_KEY = os.getenv('GENAI_API_KEY')

# Initialize Google Generative AI client
genai.init(api_key='AIzaSyBH9Ah7EmduExfkbKCFMNHy9oDJncdMJJs')

# Dictionary of book recommendations categorized by genre
books_with_descriptions = {
    "fiction": [
        {"title": "To Kill a Mockingbird", "description": "A novel about the serious issues of rape and racial inequality."},
        {"title": "1984", "description": "A dystopian novel set in a totalitarian society ruled by Big Brother."},
        {"title": "The Great Gatsby", "description": "A novel about the American dream and the roaring twenties."},
        {"title": "The Catcher in the Rye", "description": "A story about adolescent alienation and loss."}
    ],
    "mystery": [
        {"title": "Gone Girl", "description": "A thriller that explores the complexities of marriage."},
        {"title": "Big Little Lies", "description": "A story about three women whose lives unravel to the point of murder."},
        {"title": "The Girl with the Dragon Tattoo", "description": "A mystery about a journalist and a hacker investigating a disappearance."},
        {"title": "In the Woods", "description": "A psychological mystery about a detective's past coming back to haunt him."}
    ],
    "fantasy": [
        {"title": "Harry Potter and the Sorcerer's Stone", "description": "A young boy discovers he is a wizard and attends a magical school."},
        {"title": "The Hobbit", "description": "A fantasy novel about a hobbit's adventure to reclaim a lost kingdom."},
        {"title": "Game of Thrones", "description": "A story of political intrigue and power struggles in a fantasy world."},
        {"title": "The Name of the Wind", "description": "A tale of a magically gifted young man's rise to legend."}
    ],
    "science fiction": [
        {"title": "Dune", "description": "A story about the struggle for control of a desert planet and its valuable spice."},
        {"title": "Ender's Game", "description": "A young boy is trained to fight in a war against alien invaders."},
        {"title": "The Martian", "description": "An astronaut is stranded on Mars and must survive until rescue."},
        {"title": "Neuromancer", "description": "A cyberpunk novel about a washed-up computer hacker hired for one last job."}
    ],
    "romance": [
        {"title": "Pride and Prejudice", "description": "A classic love story about the manners and matrimonial machinations among the British gentry of the early 19th century."},
        {"title": "Outlander", "description": "A story about a woman who travels back in time and finds romance in 18th century Scotland."},
        {"title": "The Notebook", "description": "A romance that spans decades, recounting a lifelong love story."},
        {"title": "Me Before You", "description": "A love story about a woman caring for a paralyzed man and their unlikely bond."}
    ],
    "horror": [
        {"title": "It", "description": "A group of children face an evil entity that takes the form of a clown."},
        {"title": "The Shining", "description": "A family stays in a haunted hotel where the father slowly goes mad."},
        {"title": "Dracula", "description": "The classic vampire tale of Count Dracula's attempt to move from Transylvania to England."},
        {"title": "Frankenstein", "description": "A scientist creates a monstrous creature in a scientific experiment gone wrong."}
    ],
    "non-fiction": [
        {"title": "Sapiens", "description": "A brief history of humankind."},
        {"title": "Educated", "description": "A memoir about growing up in a strict and abusive household in rural Idaho but eventually escaping to learn about the wider world through education."},
        {"title": "The Immortal Life of Henrietta Lacks", "description": "The story of a woman whose cells were used for scientific research without her knowledge."},
        {"title": "The Wright Brothers", "description": "The story of the brothers who invented the first successful airplane."}
    ],
    "biography": [
        {"title": "The Diary of a Young Girl", "description": "The diary of Anne Frank, a Jewish girl hiding from the Nazis during World War II."},
        {"title": "Steve Jobs", "description": "The biography of Steve Jobs, co-founder of Apple Inc."},
        {"title": "Becoming", "description": "The memoir of former First Lady Michelle Obama."},
        {"title": "Long Walk to Freedom", "description": "The autobiography of Nelson Mandela."}
    ]
}

# Function to recommend a book based on genre
def recommend_book(genre):
    if genre.lower() in books_with_descriptions:
        return random.choice(books_with_descriptions[genre.lower()])
    else:
        return None

# Function to generate a detailed book description using Google Generative AI
def generate_book_description(title, description):
    prompt = f"Provide a detailed summary for the book titled '{title}' which is described as '{description}'. Include information about the main plot, characters, and any significant themes or messages."
    response = genai.generate(prompt)
    return response.result

# Main function to run the Streamlit app
def main():
    st.title("BookBuddy")
    st.subheader("Welcome to BookBuddy: Your Personal Book Recommendation Companion! Get personalized book recommendations based on your mood and preferred genre.")

    # Initial conversation to determine mood
    mood = st.selectbox("How are you feeling today?", ["Happy", "Sad", "Adventurous", "Relaxed", "Curious", "Scared"])

    # First level of prompting: Ask user for their preferred genre
    genre = st.selectbox("Select your preferred book genre:", ["Fiction", "Mystery", "Fantasy", "Science Fiction", "Romance", "Horror", "Non-fiction", "Biography"])

    # Second level of prompting: Get the book recommendation
    if st.button("Recommend"):
        recommendation = recommend_book(genre)
        if recommendation:
            detailed_description = generate_book_description(recommendation['title'], recommendation['description'])
            st.success(f"Based on your mood ({mood}), we recommend you read: {recommendation['title']}\n\n{detailed_description}")
        else:
            st.error("Sorry, we don't have recommendations for that genre.")

if __name__ == "__main__":
    main()
