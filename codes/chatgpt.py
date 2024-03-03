from openai import OpenAI 

class ChatGPT:
    """A class for interacting with the OpenAI GPT-3.5 API for chat-
    based completions."""
    
    def __init__(self, api_key): 
        """Initialize the ChatGPT instance with the provided
        API key."""
        self.__client = OpenAI(api_key=api_key) 
        self.__messages = [
                {"role": "system", "content": "You are a study assistant."},
                {"role": "user", "content": None}
        ] 
 
               
    def response(self, prompt):
        """Generate a response from the GPT-3.5 model based on 
        the provided prompt.
        Args:
            prompt (str): The prompt to generate a response for.
        Returns:
            str: The generated response."""
        self.__messages[1]["content"] = prompt
        chat = self.__client.chat.completions.create( 
                    model="gpt-3.5-turbo", 
                    messages=self.__messages) 
        return chat.choices[0].message.content 
        