# DesktopGPT with Langchain

## Overview

This is a simple desktop chat application built using PyQt5 and the Langchain library. The application provides a graphical user interface (GUI) for interacting with a chatbot powered by OpenAI's GPT-4 model. Users can type messages, send them, and receive responses from the AI.

## Features

- **Simple and Intuitive UI**: The application features a clean and straightforward interface, making it easy for users to interact with the chatbot.
- **Real-time Interaction**: Messages are processed and displayed in real-time, providing a seamless chat experience.
- **Role-based Coloring**: Messages from the user and the AI have different background colors for easy differentiation.
- **Error Handling**: The application includes basic error handling for overly long AI responses.

## Requirements

- Python 3.x
- PyQt5
- Langchain library
- OpenAI API key

## Installation

1. **Clone the Repository**:  
   ```
   git clone https://github.com/stevielbaby/DesktopGPT.git
   ```

2. **Navigate to the Directory**:  
   ```
   cd yourrepository
   ```

3. **Install Dependencies**:  
   ```
   pip install PyQt5 langchain
   ```

4. **Set OpenAI API Key**:  
   Update the `config.py` file with your OpenAI API key.
   ```python
   OPENAI_API_KEY = "your-api-key-here"
   ```

## Usage

1. **Run the Script**:  
   ```
   python chatbot.py
   ```

2. **Interact with the Chatbot**:  
   Type your message in the text input field and either press Enter or click the "Send" button to send the message.

## Usage

1. **Run the Script**:  
   ```
   python chatbot.py
   ```

2. **Interact with the Chatbot**:  
   Type your message in the text input field and either press Enter or click the "Send" button to send the message.

## Contributing

Feel free to fork the project, make changes, and submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to modify this README to better suit your project's specific needs.