from textblob import TextBlob

class Chatbot:
    def __init__(self):
        
        self.intents = {
            "hours": {
                "keywords": ["hours", "open", "closed"],
                "response": "Our working hours are from 9 AM to 5 PM, Monday to Friday."
            },
            "return": {
                "keywords": ["refund", "return", "exchange"],
                "response": "I'd be happy to help you with returns. Please provide your order number."
            }
        }

    
    def get_response(self, message):
        message = message.lower()

        for intent_data in self.intents.values():
            if any(keyword in message for keyword in intent_data["keywords"]):
                return intent_data["response"]

        sentiment = TextBlob(message).sentiment.polarity

        if sentiment > 0:
            return "That's great to hear!"
        elif sentiment < 0:
            return "I'm sorry to hear that."
        else:
            return "I see. Can you tell me more about that?"

    def chat(self):
        print("Chatbot: Hi, how can I help you today?")
        while True:
            user_message = input("You: ").strip().lower()
            if user_message in ["exit", "quit", "bye"]:
                break
            print(f"Chatbot: {self.get_response(user_message)}")

        print("Chatbot: Thank you for chatting. Have a great day!")



chatbot = Chatbot()
chatbot.chat()
