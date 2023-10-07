from dotenv import load_dotenv
import  os

class config:
    def __init__(self) -> None:
        load_dotenv()
        self.OPENAI_API_KEY = "YOUR-API-KEY"
