import random

def read_dictionary_file(filename):
    input_file = open(filename, 'r', encoding='utf-8')
    contents = input_file.read()
    contents_list = contents.split("\n")
    input_file.close()
    return contents_list

#print(read_dictionary_file("SampleDictionary1.txt"))

def get_maori_english_dictionary(contents):
    contents_dict = {}
    for pair in contents:
        local_list = pair.split(" - ")
        contents_dict[local_list[0]] = local_list[1]
    return contents_dict

#contents = ['Waipuke - Flood', 'Whakahukapapa - Freeze', 'Mākūkū - Damp',
#           'Whakanui - Celebrate', 'Hākari - Feast', 'Mane - Monday',
#           'Tūrei - Tuesday', 'Wenerei - Wednesday', 'Taite - Thursday',
#           'Paraire - Friday','Rāhoroi - Saturday', 'Rātapu - Sunday',
#            'Kohitātea - January']
#print(get_maori_english_dictionary(contents))

def main():
    filename = "SampleDictionary1.txt"
    contents = read_dictionary_file(filename)
    contents_dict = get_maori_english_dictionary(contents)
    for key, value in sorted(contents_dict.items()):
        print(f"{key}: \n   {value}")

#main()
        
def print_quiz_info(name):
    welcome = f"*Welcome {name} to the Reo Māori Quiz!*"
    print("*" * len(welcome))
    print(welcome)
    print("*" * len(welcome))
    print()
    print("""The quiz has 5 rounds.
In each round you have to work out the English meaning of a Māori word.
You are given 5 options to select from and 3 attempts to select the right one.
Get the right answer and you score 1 point for the round.
Otherwise you score 0 points for the round.
Good luck!\n""")
    
#print_quiz_info("Ann")

def get_user_selection():
    selection = input("Enter your selection (1 to 5): ")
    selection_range = check_selection_range(selection)
    while selection.isdigit() != True or selection_range != True:
        if selection.isdigit() != True or selection_range != True:
            print("Please enter a number from 1 to 5")
            selection = input("Enter your selection (1 to 5): ")
            selection_range = check_selection_range(selection)
    return int(selection)
    

def check_selection_range(selection):
    if selection.isdigit():
        if int(selection) <= 5 and int(selection) >= 1:
            return True
        else:
            return False
    else:
        return False
        
#print(get_user_selection())

def play_round(question_items, question_index):
    print(f"Select the definition for the word {question_items[question_index][0]}")
    print()
    print("Choose from one of the following options:")
    print()

    for tupl in question_items:
        print(f"{question_items.index(tupl)+1}) {tupl[1]}")
    print()
    round_score = 0
    attempt = 2
    selection = get_user_selection()
    while selection != (question_index+1) and attempt >= 1:
        if selection != (question_index+1):
            if attempt >= 1:
                print("Your answer is incorrect. ")
                print(f"You have {attempt} attempt(s) left. Please try again.\n")
                selection = get_user_selection()
                attempt -= 1
    if selection == question_index+1:
        
        if attempt == 2:
            round_score += 7
        elif attempt == 1:
            round_score += 5
        else:
            round_score += 3
        print(f"\nCongratulations! {question_items[question_index][0]} does mean '{question_items[question_index][1]}'!\n")
        return round_score
    if attempt == 0:
        print("Your answer is incorrect.\n")
        print(f"You have not identified the meaning of {question_items[question_index][0]}")
        print(f"{question_items[question_index][0]} means '{question_items[question_index][1]}'")
        print("Better luck next time!\n")
        return round_score
    else:
        if attempt == 2:
            round_score += 7
        elif attempt == 1:
            round_score += 5
        else:
            round_score += 3
        round_score += 1
        print(f"\nCongratulations! {question_items[question_index][0]} does mean '{question_items[question_index][1]}'!\n")
        return round_score

        
	
#question_items = [('Motuka', 'Car'), ('Whanga', 'Harbour'), ('Hakihea', 'December'), ('Pahiketepōro', 'Basketball'),
                  #('Kirihimete', 'Christmas')]
#question_index = 3
#print("Round score:", play_round(question_items, question_index)) 
# question_items = [('Repo', 'Swamp'), ('Turi', 'Knee'), ('Kiriata', 'Cinema'), ('Kai', 'Food'), ('Pune', 'Spoon')]
# question_index = 4
# print("Round score:", play_round(question_items, question_index))

def get_high_scores(filename):
    input_file = open(filename, 'r', encoding='utf-8')
    contents = input_file.read()
    contents_list = contents.split("\n")
    high_score_dict = {}
    for set in contents_list:
        dict_list = set.split(": ")        
        high_score_dict[dict_list[0]] = int(dict_list[1])
    input_file.close()
    return high_score_dict

#print(get_high_scores("HighScores1.txt"))

# def main():
#     filename = "SampleDictionary1.txt"
#     contents = read_dictionary_file(filename)
#     contents_dict = get_maori_english_dictionary(contents)
#     for key, value in sorted(contents_dict.items()):
#         print(f"{key}: \n   {value}")

def main(): #Do not alter in any way!
    filename = "TeReoMaori_to_English_Dictionary.txt"
    file_contents = read_dictionary_file(filename)
    maori_english_dict = get_maori_english_dictionary(file_contents)
    name = input("Please enter your name: ")
    play_game(maori_english_dict, name)
    
def get_five_dictionary_items(maori_english_dict): #Do not alter in any way!
    dictionary_items = []
    maori_words = list(maori_english_dict.keys())
    while len(dictionary_items) < 5:
        random_index = random.randrange(0, len(maori_words))
        dictionary_item = maori_words[random_index], maori_english_dict[maori_words[random_index]]
        while dictionary_item in dictionary_items:
            random_index = random.randrange(0, len(maori_words))
            dictionary_item = maori_words[random_index], maori_english_dict[maori_words[random_index]]
        dictionary_items.append(dictionary_item)
    return dictionary_items

def get_question_index(question_items): #Do not alter in any way!
    return random.randrange(len(question_items))

#Q7
def play_game(maori_english_dict, name):
    print_quiz_info(name)
    round_score = 0
    round = 1
    while round <= 5:

        print(f"Round {round}\n")
        question_items = get_five_dictionary_items(maori_english_dict)
        question_index = get_question_index(question_items)
        round_score += play_round(question_items, question_index)
        round += 1
    print(f"Your final quiz score is: {round_score}")

# random.seed(5)  
# main()
def print_contents(filename):
    input_stream = open(filename, 'r')
    content = input_stream.read()
    input_stream.close()
    print(content)

def handle_high_scores(high_scores_dict, name, score, high_score_filename):
    # Print a message to the user based on their score relative to the list of high scores.
    if name in high_scores_dict:
        if score > high_scores_dict[name]:
            print(f"{name}, you've beaten your previous high score! Well done!")
            high_scores_dict[name] = score
        else:
            print(f"{name}, your score of {score} is not enough to beat your high score of {high_scores_dict[name]}. Better luck next time!")
    else:
        print(f"{name}, you have not made the list of high scores! \nBetter luck next time!")

    # Print the list of high scores.
    print("\n   High Scores")
    sorted_scores = sorted(high_scores_dict.items(), key=lambda item: item[1], reverse=True)
    for player, high_score in sorted_scores:
        print(f"{player.ljust(15)}{high_score}")

    # Write the list of high scores to the specified text file.
    with open(high_score_filename, 'w') as file:
        for player, high_score in sorted_scores:
            file.write(f"{player}: {high_score}\n")

high_scores_dict = {'Ann': 35, 'Damir': 32, 'Andrew': 33, 'John': 19, 'Barry':29}
high_score_filename = 'atha534.txt'
handle_high_scores(high_scores_dict, "Robert", 17, high_score_filename)
print("\nFile contents:\n")
print_contents(high_score_filename)

