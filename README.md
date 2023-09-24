# Higher Lower 👀

— The Ultimate Celebrity Showdown

Get ready for a thrilling celebrity showdown in the "Higher or Lower?" game! Challenge your knowledge of the social media world by comparing the follower counts of your favorite celebrities. It's time to prove that you have your finger on the pulse of popular culture.

Gameplay:

    Start the Game: The excitement kicks off with the game's stylish logo. You're about to dive into the world of celebrity follower counts.

    Celebrity Faceoff: At the core of the game is the challenge of deciding who has more followers: Celebrity A or Celebrity B. You'll be provided with brief descriptions of the celebrities and their respective countries.

    Make Your Guess: It's decision time! Type 'A' or 'B' to select your answer. Are you a social media guru, or will you rely on pure luck?

    Keep Scoring: With every correct guess, your score climbs. Compete with yourself or challenge friends to see who can achieve the highest score.

    Test Your Knowledge: The game features a diverse selection of celebrities, making every round a unique experience.

    Game Over: Make a wrong guess, and it's game over. Your final score will be displayed, showing just how in tune you are with the world of celebrity followers.

Are You Up for the Challenge?

Step into the world of celebrity followers and put your knowledge to the test. With each round, you'll become more attuned to the world of social media. Are you ready to reach for the top score and prove your celebrity expertise?

Give it a try! Challenge yourself or compete with friends to see who's the ultimate celebrity follower count master. Remember, it's not just about luck; it's about knowing who's truly making waves in the social media universe.

## Developer: https://github.com/emiliomorles

## Year: 2023

🔸 I learned:

    - How to check for an answer with multiple values  ✔️


    #guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    guess = "A"
    person_a = 67
    person_b = 102
    def check_answer(guess, person_a, person_b):
      """Checks followers against user's guess 
      and returns True if they got it right.
      Or False if they got it wrong.""" 
      if person_a > person_b:
        return guess == "a"
      else:
        return guess == "b"
    
    print(check_answer(guess, person_a, person_b))
