# class student:
#     def _init_(self, name, house):
#         self.name = name
#         self.house = house
        
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
    
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = student(name, house)
#     return student

# main()

#Importing textblob to help the chatbot to understand human language nuance 

from textblob import TextBlob

#Defining a chatbot class for interaction

class Chatbot:
    def __init__(self):
        
        # defining intents based on keywords
        
        self.intents= {
            "hours":{
                "keywords": ["hours", "open", "closed"],
                "response": "Our working hours are from 9 AM to 5 PM, Monday to Friday."
            },
            "return":{
                "keywords": ["refund", "return", "exchange"],
                "response": "I'd be happy to help you with returns. Please provide your order number."
            }
        }
        
        # Annalyzing the sentiment of the user's message
        
    def get_response(self, message):
        message = message.lower()
        
        for intent_data in self.intents.values():
            if any(keyword in message for keyword in intent_data["keywords"]):
                return intent_data['response']

            # Generating the chatbot's response based on sentiment
            
            sentiment = TextBlob(message).sentiment.polarity
            
            return ("That's great to hear!" if sentiment > 0 else
                    "I'm sorry to hear that." if sentiment < 0 else
                    "I see. Can you tell me about that?")
            
    def chat(self):
                print("Chatbot:Hi, how can i help you today?")
                user_message = input("you: ").strip().lower()
                while user_message not in ["exit", "quit", "bye"]:
                    print(f"\nChatbot: {self.get_response(user_message)}")
                    user_message = input("you: ").strip().lower()
                print("Chatbot: Thankyou for chatting. Have a great day!")


chatbot = Chatbot()
chatbot.chat()