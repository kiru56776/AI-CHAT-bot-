import os
import google.generativeai as genai

# --- Configuration ---
# To use this program, you must first get an API key from Google AI Studio.
# Once you have the key, set it as an environment variable on your system.
# On Linux/macOS: export GEMINI_API_KEY='your_api_key'
# On Windows: set GEMINI_API_KEY='your_api_key'
#
# IMPORTANT: Never hardcode your API key directly in your code, especially if
# you are sharing it on platforms like GitHub. Environment variables keep your
# key secure.

try:
    # Use the os.getenv() function to read the environment variable.
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
    genai.configure(api_key=api_key)
except ValueError as e:
    print(f"Error: {e}")
    print("Please set the GEMINI_API_KEY environment variable and try again.")
    exit()

# --- Model Selection ---
# You can choose a different model if you'd like. The 'gemini-1.5-flash'
# model is a good choice for fast conversational responses.
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Chat Function ---
def get_gemini_response(prompt):
    """
    Sends a user prompt to the Gemini API and returns the response text.

    Args:
        prompt (str): The user's input string.

    Returns:
        str: The AI's response as a string, or an error message.
    """
    try:
        # Use a single-turn request for simplicity.
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Handle potential errors from the API call.
        return f"An error occurred: {e}"

# --- Main Chat Loop ---
def main():
    """
    Runs the main chat interface in the console.
    """
    print("Gemini Chatbot (type 'exit' or 'quit' to end the conversation).")
    print("You can start chatting now!")

    while True:
        try:
            user_input = input("\nYou: ")

            # Check for termination commands.
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break

            if not user_input.strip():
                # Don't send empty prompts to the API.
                continue

            # Get the response from the AI.
            response = get_gemini_response(user_input)

            # Print the AI's response.
            print(f"AI: {response}")

        except KeyboardInterrupt:
            # Allows the user to exit the program with Ctrl+C.
            print("\nGoodbye!")
            break
        except Exception as e:
            # Catch any other unexpected errors.
            print(f"An unexpected error occurred: {e}")

# Run the main function when the script is executed.
if __name__ == "__main__":
    main()
