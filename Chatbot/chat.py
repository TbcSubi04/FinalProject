import tkinter as tk
import random
import json
import time

# List of random agent names
agent_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]

# Predefined list of keywords and responses
responses = {
    "coffee": "Our campus coffee bar is open from 8 AM to 5 PM. Want a cup?",
    "location": "Our campus is located at 123 Poppleton Street.",
    "admission": "You can find the admission details on our website, or I can email them to you.",
    "fees": "The tuition fees depend on the course. Please visit the fees page for more info."
}

# Random responses for unknown questions
default_responses = [
    "Hmm, I'm not sure about that. Can you ask something else?",
    "Sorry, I don't have an answer for that right now.",
    "I don't quite understand. Could you rephrase your question?",
    "That sounds interesting, but I can't answer that at the moment."
]

# Function to get a random agent name
def get_random_agent_name():
    return random.choice(agent_names)

# Function to log chat history to a file
def log_chat(user_input, agent_response):
    with open("chat_log.txt", "a") as log_file:
        log_file.write(f"User: {user_input}\n")
        log_file.write(f"Agent: {agent_response}\n")
        log_file.write("-" * 50 + "\n")

# Function to handle the conversation
def chat():
    # Get the user name from the entry box
    user_name = entry_name.get()
    if not user_name:
        return  # Ensure the user entered a name
    
    # Display greeting message in the chat window
    chat_window.insert(tk.END, f"Hi {user_name}! Welcome to the University of Poppleton chatbot.\n")
    
    # Display random agent name
    agent_name = get_random_agent_name()
    chat_window.insert(tk.END, f"I'll be your agent today. You can call me {agent_name}.\n")
    
    # Start the chat loop
    def process_input():
        user_input = entry_question.get()  # Get user's input
        if user_input.lower() in ["bye", "exit", "quit"]:
            chat_window.insert(tk.END, f"{agent_name}: Goodbye, {user_name}! Have a great day!\n")
            root.quit()  # Exit the chat window

        else:
            # Look for keywords in the question
            response = None
            for keyword, reply in responses.items():
                if keyword in user_input.lower():
                    response = reply
                    break
            
            # If no keyword is found, provide a random response
            if not response:
                response = random.choice(default_responses)
            
            # Display agent's response in the chat window
            chat_window.insert(tk.END, f"{user_name}: {user_input}\n")
            chat_window.insert(tk.END, f"{agent_name}: {response}\n")
            log_chat(user_input, response)  # Log the conversation

        # Clear the entry box after processing
        entry_question.delete(0, tk.END)
        
    # Simulate random disconnections
    def simulate_disconnect():
        if random.random() < 0.1:  # 10% chance of disconnection
            chat_window.insert(tk.END, f"{agent_name}: Oops, looks like I'm having some technical issues. Reconnecting...\n")
            chat_window.update()
            time.sleep(2)
            chat_window.insert(tk.END, f"{agent_name}: I'm back!\n")
            chat_window.update()

    # Button to send the message
    button_send.config(command=lambda: [process_input(), simulate_disconnect()])

# Set up the main Tkinter window
root = tk.Tk()
root.title("University of Poppleton Chatbot")

# Create and place the GUI elements
label_name = tk.Label(root, text="What's your name?")
label_name.pack(pady=5)

entry_name = tk.Entry(root)
entry_name.pack(pady=5)

label_question = tk.Label(root, text="Ask a question:")
label_question.pack(pady=5)

entry_question = tk.Entry(root)
entry_question.pack(pady=5)

button_send = tk.Button(root, text="Send", width=20)
button_send.pack(pady=5)

chat_window = tk.Text(root, height=20, width=50)
chat_window.pack(pady=10)

# Start the conversation when the user enters their name
entry_name.bind("<Return>", lambda event: chat())

# Start the Tkinter main loop
root.mainloop()
