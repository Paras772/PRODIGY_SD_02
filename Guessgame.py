import random

def get_random_number(min_range, max_range):
    """
    Generates a random number within the specified range.

    :param min_range: The minimum value of the range.
    :param max_range: The maximum value of the range.
    :return: A random number between min_range and max_range (inclusive).
    """
    return random.randint(min_range, max_range)

def calculate_round_score(attempts):
    """
    Calculates the score for the round based on the number of attempts.
    More points are awarded for fewer attempts.

    :param attempts: The number of attempts taken to guess the correct number.
    :return: The score for the round.
    """
    if attempts <= 3:
        return 10
    elif attempts <= 6:
        return 5
    else:
        return 1

def main():
    # Define the range for the random number
    min_range = 1
    max_range = 100

    # Define the total number of rounds and initialize the current round and score
    total_rounds = 3
    current_round = 1
    score = 0

    # Display introductory messages
    print("TASK 02")
    print("Welcome to Guess the Number Game!")
    print("You have to guess a number between 1 and 100.")

    # Loop through each round of the game
    while current_round <= total_rounds:
        # Generate a random number for the current round
        target_number = get_random_number(min_range, max_range)
        attempts = 0
        max_attempts = 10  # Maximum attempts allowed per round

        print(f"\nRound {current_round} of {total_rounds}")
        print(f"Current Score: {score}")

        # Loop for the player to make guesses
        while True:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess == target_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                round_score = calculate_round_score(attempts)
                score += round_score
                print(f"Round Score: {round_score}")
                break
            elif guess < target_number:
                # Feedback if the guess is lower than the target number
                print("Your guess is lower than the target number.")
            else:
                # Feedback if the guess is higher than the target number
                print("Your guess is higher than the target number.")

            # Check if the player has reached the maximum number of attempts
            if attempts >= max_attempts:
                print(f"Sorry, you have reached the maximum number of attempts. The correct number was: {target_number}")
                break

        # Move to the next round
        current_round += 1

    # Display the final score and end the game
    print("\nGame Over!")
    print(f"Total Score: {score}")

if __name__ == "__main__":
    main()
