import openai

# Set your OpenAI API key here
openai.api_key = 'YOUR_API_KEY'

def generate_sentence(object_name):
    prompt = f"Generate two to three sentences about {object_name}."
    
    try:
        # Use OpenAI's completion API to generate sentences
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        
        # Extract the generated text from the API response
        generated_text = response['choices'][0]['text']
        return generated_text
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
object_name = input("Enter an object (e.g., dog, car, camera): ").lower()
result = generate_sentence(object_name)

print(result)
