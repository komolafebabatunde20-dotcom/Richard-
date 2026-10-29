def greet_user():
    # Greet the user
    print("Hello! Welcome.")
    
    # Take user details
    name = input("What is your name? ")
    age = input("How old are you? ")
    nationality = input("What is your nationality? ")
    
    # Display a personalized greeting
    print(f"\nNice to meet you, {name}!")
    print(f"It's great to connect with someone who is {age} years old and from {nationality}.")
    print("Have a wonderful day ahead!")

if __name__ == "__main__":
    greet_user()