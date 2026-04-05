import random
import time
import math

def random_list(quantity, minimum, maximum):
    generated_list = []
    for _ in range(quantity):
        # Generate a random integer between the min and max (inclusive)
        random_num = random.randint(minimum, maximum)
        generated_list.append(random_num)
    
    return generated_list

def ask_question(question_text, answer):
    print(f"{question_text}")
    
    # REPEAT until the user provides a valid integer
    while True:
        user_input = input("> ").strip()
        
        # Check if the input is a valid whole number
        try:
            val = int(user_input)
            break # Exit loop if conversion to int is successful
        except ValueError:
            print("Invalid choice! Please enter a whole number.")
            
    # Check if user input matches the calculated answer
    if val == answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! Correct answer was {answer}.")
        return False

def main():
    # DISPLAY Welcome Message
    print("Welcome to Hirusha Divisekara'S (10741877) Number List Test!")
    print("-" * 50)

    # REPEAT Difficulty Selection until a valid option is chosen
    while True:
        print("Select a difficulty: [E]asy, [M]edium, [H]ard")
        difficulty_input = input("> ").strip().lower()
        
        if difficulty_input in ['e', 'm', 'h']:
            break # Valid input received
        else:
            print("Invalid choice! Enter E, M or H.")

    # SET Variables based on the selected difficulty
    if difficulty_input == 'e':
        questions_total = 3
        list_quantity = 3
        min_val = 1
        max_val = 10
    elif difficulty_input == 'm':
        questions_total = 5
        list_quantity = 4
        min_val = 5
        max_val = 15
    else:
        questions_total = 7
        list_quantity = 6
        min_val = 10
        max_val = 50

    # Display settings summary to the user
    print(f"\nYour test will have {questions_total} questions.")
    print(f"Lists will contain {list_quantity} numbers between {min_val} and {max_val}.")
    print("The last question is a challenge question with twice as many numbers!")
    
    input("\nPress Enter to begin!")

    # Initialize score and start the timer
    current_score = 0
    start_timestamp = time.time()

    # FOR Loop to iterate through the questions
    for current_num in range(1, questions_total + 1):
        
        # Calculate current elapsed time for the display requirement
        current_elapsed = round(time.time() - start_timestamp, 2)
        
        # Display Header with Live Score and Elapsed Time
        print("\n" + "=" * 40)
        print(f"QUESTION {current_num} of {questions_total}")
        print(f"CURRENT SCORE: {current_score} | TIME ELAPSED: {current_elapsed}s")
        print("=" * 40)

        # Logic for the final 'Challenge' question
        if current_num == questions_total:
            # Challenge question uses double the quantity of numbers
            active_list = random_list(list_quantity * 2, min_val, max_val)
            print("[!!!] Challenge Question [!!!]")
        else:
            active_list = random_list(list_quantity, min_val, max_val)
        
        # Output the generated list for the user to analyze
        print(f"LIST: {active_list}")
        
        # SET question_type randomly (1 to 4)
        q_type = random.randint(1, 4)
        
        # Logic for Question Type 1: Summation
        if q_type == 1:
            q_text = "What is the sum of the numbers in this list?"
            correct_ans = sum(active_list)
            
        # Logic for Question Type 2: Range (Difference)
        elif q_type == 2:
            q_text = "What is the difference between the minimum and maximum numbers in this list?"
            correct_ans = max(active_list) - min(active_list)
            
        # Logic for Question Type 3: Average comparison
        elif q_type == 3:
            # Calculate floor of the average as per pseudocode
            calc_avg = math.floor(sum(active_list) / len(active_list))
            q_text = f"How many numbers in this list are higher than the average ({calc_avg})?"
            
            # Count numbers greater than the average
            count_higher = 0
            for item in active_list:
                if item > calc_avg:
                    count_higher += 1
            correct_ans = count_higher
            
        # Logic for Question Type 4: Product of positions
        else:
            # Select two unique positions within the list length
            p1 = random.randint(1, len(active_list))
            p2 = random.randint(1, len(active_list))
            while p1 == p2:
                p2 = random.randint(1, len(active_list))
            
            q_text = f"What is the product of the numbers at positions {p1} and {p2} in this list?"
            # Correct for 0-based indexing (Position 1 is index 0)
            correct_ans = active_list[p1 - 1] * active_list[p2 - 1]

        # CALL the ask_question function and update score based on result
        user_is_correct = ask_question(q_text, correct_ans)
        
        if user_is_correct == True:
            current_score = current_score + 1
        else:
            current_score = current_score - 1
            # Maintain floor of 0 for the score
            if current_score < 0:
                current_score = 0
                
    # END Loop - Calculate Final Results
    end_timestamp = time.time()
    total_duration = end_timestamp - start_timestamp
    
    # Format the final metrics
    final_percent = round((current_score / questions_total) * 100)
    final_time_rounded = round(total_duration, 2)
    avg_per_q = round(total_duration / questions_total, 2)

    # FINAL Results Display
    print("\n" + "#" * 40)
    print("TEST COMPLETE!")
    print(f"Total Time: {final_time_rounded} seconds")
    print(f"Final Score: {current_score} out of {questions_total}")
    print(f"Percentage: {final_percent}%")
    print(f"Average Speed: {avg_per_q} seconds per question")
    print("#" * 40)

    # Perfect Score Achievement
    if current_score == questions_total:
        print("Perfect score! Well done!")

# Run the program
if __name__ == "__main__":
    main()