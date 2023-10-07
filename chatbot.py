# Import required libraries from PyQt5, config, and langchain
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit, QMessageBox, QSplitter
from PyQt5.QtGui import QColor, QTextCharFormat, QTextCursor
from PyQt5.QtCore import Qt
from config import config  # Not used in the original code
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage

# Define the ChatWindow class, inheriting from QWidget
class ChatWindow(QWidget):
    # Class-level constants for roles and maximum token length
    ROLE_ME = "Me"
    ROLE_AI = "@Stvlmusic Threads AI"
    MAX_TOKEN_LENGTH = 8192  # Not used correctly in the original code

    # Initialize the ChatWindow object
    def __init__(self):
        super().__init__()  # Call the parent class's constructor
        
        self.config = config()   

        self.api_key = self.config.OPENAI_API_KEY

        # Initialize the ChatOpenAI object with a temperature setting
        self.chat = ChatOpenAI(temperature=1)
        
        # Initialize an empty conversation dictionary
        self.conversation = {"messages": []}

        # Initialize the UI components
        self.init_ui()

    # Initialize the UI components
    def init_ui(self):
        # Create a vertical layout
        self.layout = QVBoxLayout()
        
        # Create a splitter for text area and text input
        self.splitter = QSplitter(Qt.Vertical)

        # Create a read-only text area for displaying messages
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.splitter.addWidget(self.text_area)

        # Create a text input field for typing messages
        self.text_input = QLineEdit()
        self.text_input.returnPressed.connect(self.send_message)
        self.splitter.addWidget(self.text_input)

        # Add the splitter to the layout
        self.layout.addWidget(self.splitter)

        # Create a 'Send' button and connect its click event to send_message function
        self.button = QPushButton('Send')
        self.button.clicked.connect(self.send_message)
        self.layout.addWidget(self.button)

        # Set the layout for the QWidget
        self.setLayout(self.layout)

    # Function to handle sending messages
    def send_message(self):
        # Get the user input and strip any leading/trailing white spaces
        user_input = self.text_input.text().strip()

        # If user input is not empty
        if user_input:
            # Simulate a button click animation
            self.button.animateClick()

            # Process the user's message and the AI's response
            self.process_user_message(user_input)
            self.process_ai_response(user_input)

            # Clear the text input field
            self.text_input.clear()

    # Function to process and display the user's message
    def process_user_message(self, user_input):
        self.append_message(self.ROLE_ME, user_input)  # Append the message to the text area
        self.add_message_to_conversation(self.ROLE_ME, user_input)  # Add the message to the conversation dictionary

    # Function to process and display the AI's response
    def process_ai_response(self, user_input):
        # Get the AI's response based on the conversation history
        response = self.chat.predict_messages(self.conversation["messages"])
        
        # Add the AI's response to the conversation dictionary
        self.add_message_to_conversation(self.ROLE_AI, response.content)
        
        # Check if the response is too long to display (Note: This check is incorrect in the original code)
        if len(response.content.split()) > self.MAX_TOKEN_LENGTH:
            QMessageBox.critical(self, "Response Too Long", "The response is too long to display.")
        else:
            # Append the AI's response to the text area
            self.append_message(self.ROLE_AI, response.content)

    # Function to add a message to the conversation dictionary
    def add_message_to_conversation(self, role, content):
        # Create a message object based on the role
        message = HumanMessage(content=content) if role == self.ROLE_ME else AIMessage(content=content)
        
        # Append the message object to the conversation dictionary
        self.conversation["messages"].append(message)

    # Function to append a message to the text area
    def append_message(self, author, text):
        # Define background colors for different roles
        color_dict = {
            self.ROLE_ME: QColor(204, 229, 255),
            self.ROLE_AI: QColor(255, 204, 229)
        }

        # Get the background color based on the author's role
        color = color_dict.get(author, QColor(255, 255, 255))

        # Create a QTextCharFormat object with the background color
        fmt = QTextCharFormat()
        fmt.setBackground(color)

        # Get the text cursor from the text area
        cursor = self.text_area.textCursor()
        
        # Move the cursor to the end of the text
        cursor.movePosition(QTextCursor.End)
        
        # Insert the message text with the background color
        cursor.insertText(f'{author}: {text}\n', fmt)
        
        # Update the text cursor in the text area
        self.text_area.setTextCursor(cursor)

# Create a QApplication object
app = QApplication([])

# Create a ChatWindow object and display it
window = ChatWindow()
window.show()

# Start the application event loop
app.exec_()
