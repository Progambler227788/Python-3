# Function to print question and options
def login_info(authenticateDictioary,username,password):
    if username == authenticateDictioary["username"] and password == authenticateDictioary["password"]:
        print('Valid Credentials.')
        return True # Username and Password are correct
    if username != authenticateDictioary["username"] :
        print('Invalid username')
    if  password != authenticateDictioary["password"]:
        print('Invalid password')
    return False


wrongQuestionsDictionary = dict() # Dictionary to store question, correct answer and user answer

def printQuestions(dictionaryQuestions):
  question_number = 1 # 1 to 10 questions
  
  # Iterate over dictioary to print question then options and then ask user option.
  for question, details in dictionaryQuestions.items(): 
    print(f"Q{question_number}: {question}")
    character=97 # 97 is ascii value of character small a
    for option in (details["options"]):
        print(f"{chr(character)}. {option}")
        character+=1 # increment like 98,99,100 for b,c,d as there are 4 options
    while True:
        input_option = input('Enter Option for correct answer (a, b, c, d): ').lower()
        if input_option in ['a', 'b', 'c', 'd']:
            break
        else:
            print("Invalid input. Please enter a valid option.")
    user_answer = details["options"][ord(input_option.lower()) - 97] # like a has ascii of 97, so 97-97 is 0 giving first option
    if input_option.lower() != details["answer"].lower():
        wrongQuestionsDictionary[question] = {
            "correct_answer":  details["options"][ord(details["answer"])-97], # concert a to correct value
            "user_answer": user_answer
        }
        
 
    
    print()  # Separate question numbers by adding new line
    question_number += 1
  

# driver code with main function
def main():
# User Input to ask username and password
  username = input('Enter username:')
  password = input('Enter password:')
  # Dictionary to hold username and password
  authenticateDictioary = { "username": "PGR107", "password": "Python"}
  
  # Ask till not correct credentials
  while not login_info(authenticateDictioary,username,password):
       username = input('Enter username:')
       password = input('Enter password:')
  
  # Dictioary to hold questions and options and question answer. Question name is key and others are values
  # options is of list type for options like Bergen, Oslo etc
  # answer will keep number using a,b,c,d for correct answer
  questions_dict = {
      "What is the capital of Norway?": {
          "options": ["Bergen", "Oslo", "Stavanger", "Trondheim"],
          "answer": "b"  # Oslo
      },
      "What is the currency of Norway?": {
          "options": ["Euro", "Pound", "Krone", "Deutsche Mark"],
          "answer": "c"  # Krone
      },
      "What is the largest city in Norway?": {
          "options": ["Oslo", "Stavanger", "Bergen", "Trondheim"],
          "answer": "a"  # Oslo
      },
      "When is constitution day (the national day) of Norway?": {
          "options": ["27th May", "17th May", "17th April", "27th April"],
          "answer": "b"  # 17th May
      },
      "What color is the background of the Norwegian flag?": {
          "options": ["Red", "White", "Blue", "Yellow"],
          "answer": "a"  # Red
      },
      "How many countries does Norway border?": {
          "options": ["1", "2", "3", "4"],
          "answer": "c"  # 3
      },
      "What is the name of the university in Trondheim?": {
          "options": ["UiS", "UiO", "NMBU", "NTNU"],
          "answer": "d"  # NTNU
      },
      "How long is the border between Norway and Russia?": {
          "options": ["96 km", "196 km", "296 km", "396 km"],
          "answer": "b"  # 196 km
      },
      "Where in Norway is Stavanger?": {
          "options": ["North", "South", "South-west", "South-east"],
          "answer": "c"  # South-west
      },
      "From which Norwegian city did the world’s famous composer Edvard Grieg come?": {
          "options": ["Oslo", "Bergen", "Stavanger", "Troms"],
          "answer": "b"  # Bergen
      }
  }
  # Call Quiz method to run quiz
  printQuestions(questions_dict)
  # Results for quiz
  print("Quiz Results:")
  # Calculate length to get correct and wrong answers of quiz
  length =len(wrongQuestionsDictionary)
  print(f"Correct Answers: { 10 - length}")
  print(f"Wrong Answers: { length}")
  # Print wrong questions and user answers along with question
  for question, details in wrongQuestionsDictionary.items(): 
    print(f"Question: {question}")
    print(f"Correct Answer: {details['correct_answer']}")
    print(f"User Answer: {details['user_answer']}")
    print()
  
    
# Call main functon to execute program
if __name__ == "__main__":
    main()