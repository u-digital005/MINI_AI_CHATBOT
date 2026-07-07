import datetime
import time

class RuleBasedChatbot:
    """A simple rule-based chatbot for basic conversational interactions."""

    def __init__(self):
        # Chatbot Memory Creation [dictionary of responses]
        self.responses = {
            "hello": "Hi! Welcome. How can I help you today?",
            "how are you": "I am doing well. Thank you for asking!",
            "who are you": "I am an AI rule-based chatbot.",
            "motivate me": "Keep going! Every bug in your project gives you better experience.",
            "happy": "That is great to hear!",
            "function kya hota hai": "A function is a reusable block of code. Yeh rahe further results...",
            "bye": "Goodbye! Have a great day ahead."
        }

    def get_greeting(self, user_name):
        """Returns a time-appropriate greeting."""
        present_hr = datetime.datetime.now().hour
        
        # Using if/elif ensures only one condition executes
        if 5 <= present_hr < 12:
            return f"Good Morning, {user_name}!"
        elif 12 <= present_hr < 17:
            return f"Good Afternoon, {user_name}!"
        elif 17 <= present_hr < 22:
            return f"Good Evening, {user_name}!"
        else:
            return f"Good Night, {user_name}!"

    def get_response(self, user_question):
        """Scans the user's input for keywords and returns the matching response."""
        user_question = user_question.lower()
        
        for key in self.responses:
            if key in user_question:
                return self.responses[key]
                
        return "I am not able to tell you that yet. Still learning!"

    def run(self):
        """The main loop to start and maintain the chat session."""
        print("=" * 50)
        name = input("Welcome! Enter your Name: ")
        print(f"\n{self.get_greeting(name)}")
        print("Namaste! Welcome to the Rule-Based ChatBot.")
        print("You can ask me basic questions. Type 'bye' to exit.")
        print("=" * 50)

        # Take User Input Loop
        while True:
            user_input = input(f"\n{name}: ")

            # Check for exit condition first
            if "bye" in user_input.lower():
                print(f"Bot: {self.responses['bye']}")
                break
            
            # Simulate bot processing time
            time.sleep(0.5)
            
            reply = self.get_response(user_input)
            print(f"Bot: {reply}")

# Standard Python idiom to execute the script
if __name__ == "__main__":
    bot = RuleBasedChatbot()
    bot.run()