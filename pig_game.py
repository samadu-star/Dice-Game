import random

def roll_dice():
    """Roll a 6-sided die and return the result."""
    return random.randint(1, 6)

def play_pig_game():
    print("=" * 40)
    print("      WELCOME TO THE PIG DICE GAME!      ")
    print("=" * 40)
    print("Rules:")
    print("- On your turn, you can roll as many times as you want.")
    print("- Each number (2-6) is added to your turn total.")
    print("- If you roll a 1, you score 0 for the turn and your turn ends.")
    print("- You can 'Hold' to add your turn total to your overall score.")
    print("- First player to reach 50 points wins!")
    print("-" * 40)

    player_score = 0
    computer_score = 0
    winning_score = 50

    while player_score < winning_score and computer_score < winning_score:
        # --- PLAYER TURN ---
        print(f"\n--- YOUR TURN ---")
        print(f"Scores -> You: {player_score} | Computer: {computer_score}")
        turn_total = 0

        while True:
            choice = input("Roll (r) or Hold (h)? ").strip().lower()
            
            if choice == 'r':
                roll = roll_dice()
                print(f"🎲 You rolled a: {roll}")
                
                if roll == 1:
                    print("🐷 Oink! You rolled a 1! Turn over, 0 points added.")
                    turn_total = 0
                    break
                else:
                    turn_total += roll
                    print(f"   Turn total so far: {turn_total} (Potential total score: {player_score + turn_total})")
                    
                    if player_score + turn_total >= winning_score:
                        break
            elif choice == 'h':
                print(f"🔒 You held. {turn_total} points added to your score.")
                break
            else:
                print("Invalid choice. Please enter 'r' to roll or 'h' to hold.")

        player_score += turn_total
        print(f"Your total score is now: {player_score}")

        if player_score >= winning_score:
            print("\n🎉 CONGRATULATIONS! YOU WON THE GAME! 🎉")
            break

        # --- COMPUTER TURN ---
        print(f"\n--- COMPUTER'S TURN ---")
        comp_turn_total = 0
        
        while comp_turn_total < 15 and (computer_score + comp_turn_total) < winning_score:
            roll = roll_dice()
            print(f"🎲 Computer rolled a: {roll}")
            
            if roll == 1:
                print("🐷 Computer rolled a 1! Turn over, 0 points added.")
                comp_turn_total = 0
                break
            else:
                comp_turn_total += roll
                print(f"   Computer's turn total: {comp_turn_total}")

        computer_score += comp_turn_total
        print(f"Computer's total score is now: {computer_score}")

        if computer_score >= winning_score:
            print("\n🤖 THE COMPUTER WON! Better luck next time! 🤖")
            break

if __name__ == "__main__":
    play_pig_game()