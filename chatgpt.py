from openai import OpenAI


class ChatGPT:
    """A class to interact with OpenAI GPT-3.5 API using OpenAI API Key."""
    __MODEL = "gpt-3.5-turbo"

    
    def __init__(self, apiKey: str, sytemMsg: str = "You are a study assistant"):
        """Initializes the ChatGPT instance with given API key and an optional system message.
        
        Args:
            apiKey (str): The OpenAI API key.
            systemMsg (str): Optional system message to set the assistant behaviour.
        """
        self.__client = OpenAI(api_key=apiKey)
        self.__messages = [{"role": "system", "content": sytemMsg}]

    
    def response(self, prompt: str) -> str:
        """Returns the response for given prompt.
        
        Args:
            prompt (str): The user's input prompt.
        
        Returns:
            str: The assistant's response.
        """
        self.__addMemory("user", prompt)
        chat = self.__client.chat.completions.create(
            model=ChatGPT.__MODEL,
            messages=self.__messages
        )
        content = chat.choices[0].message.content
        self.__addMemory("system", content)
        return content

    
    def __addMemory(self, role: str, content: str) -> None:
        """Adds the chat memory.
        
        Args:
            role (str): The role of the sender (e.g., "user" or "system").
            content (str): The content of the message.
        """
        self.__messages.append({"role": role, "content": content})