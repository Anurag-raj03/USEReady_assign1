import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Use an environment variable for security
# Replace 'your-key-here' with your actual API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCCvIpV_tc1DwrVZCmaFeIqdGqo83xRrJU"

def test_connection():
    try:
        # Initialize Gemini 1.5 Flash (cheaper/faster for testing)
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2
        )

        print("--- Testing Gemini Connection ---")
        response = llm.invoke("Hello! Are you working?")
        
        print(f"Status: SUCCESS")
        print(f"Model Response: {response.content}")
        
    except Exception as e:
        print(f"Status: FAILED")
        print(f"Error Message: {e}")

if __name__ == "__main__":
    test_connection()