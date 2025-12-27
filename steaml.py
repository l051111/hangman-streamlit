import random
import streamlit as st

# ----------------- DATA FROM YOUR GAME -----------------
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["singam", "puli", "anil", "paampu", "muyal", "nari", "mayil"]

singam_clue = "You have one life left,So i will give you one clue:Kattuke Raja"
puli_clue   = "You have one life left,So i will give you one clue:India oda national Animal"
anil_clue   = "You have one life left,So i will give you one clue:Muthugula Moonu lines irukum"
paampu_clue = "You have one life left,So i will give you one clue:paatha padaye natungum"
muyal_clue  = "You have one life left,So i will give you one clue:kutty ah irukum,vegama oodum ana maan ila"
nari_clue   = "You have one life left,So i will give you one clue:Thanthiramana animal"
mayil_clue  = "You have one life left,So i will give you one clue:muruganin vaganam"

clues = {
    "singam": singam_clue,
    "puli": puli_clue,
    "anil": anil_clue,
    "paampu": paampu_clue,
    "muyal": muyal_clue,
    "nari": nari_clue,
    "mayil": mayil_clue,
}

# ----------------- SESSION STATE INIT -----------------
default_state = {
    "chosen_word": "",
    "display": "",
    "crc_word": "",
    "lives": 6,
    "game_over": False,
    "message": "",
    "clue_given": False,
    "started": False,
}

for k, v in default_state.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ----------------- GAME FUNCTIONS -----------------
def start_game():
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.display = "_" * len(st.session_state.chosen_word)
    st.session_state.crc_word = ""
    st.session_state.lives = 6
    st.session_state.game_over = False
    st.session_state.message = ""
    st.session_state.clue_given = False
    st.session_state.started = True

def process_guess(guess: str):
    if st.session_state.game_over or not guess:
        return

    guess = guess.lower()[0]

    new_display = ""
    for letter in st.session_state.chosen_word:
        if letter == guess:
            new_display += letter
            if letter not in st.session_state.crc_word:
                st.session_state.crc_word += letter
        elif letter in st.session_state.crc_word:
            new_display += letter
        else:
            new_display += "_"

    st.session_state.display = new_display

    if st.session_state.display == st.session_state.chosen_word:
        st.session_state.game_over = True
        st.session_state.message = "You Won!"
        return

    if guess not in st.session_state.chosen_word:
        st.session_state.lives -= 1
        st.session_state.message = (
            f"Oh no!,Your letter not there in word,So you loss one life."
            f" Remaining lives {st.session_state.lives}"
        )
        if st.session_state.lives == 0:
            st.session_state.game_over = True
            st.session_state.message = (
                "You lost all your lives and hanged:)\n"
                f"Game over. The word was: {st.session_state.chosen_word}"
            )

# ----------------- UI -----------------
st.title("Hangman game – Thanglish animals")

st.write(
    "Animals name are in **Thanglish** (ex: singam).\n\n"
    "You should guess the animal name based on letters count.\n\n"
    "You have **6 lives**. Each time when you guess wrong you lose life.\n\n"
    "At 1 life you can get a **clue**. If you lose all lives you will be hanged."
)

col1, col2 = st.columns(2)
with col1:
    if st.button("🎮 New Game"):
        start_game()
with col2:
    if st.button("🔁 Restart"):
        start_game()

if not st.session_state.started:
    st.info("Click **New Game** to start.")
    st.stop()

st.subheader("Game status")

st.text(f"Word: {st.session_state.display}")
st.text(f"Lives remaining: {st.session_state.lives}/6")
st.text(stages[st.session_state.lives])

if st.session_state.message:
    st.write(st.session_state.message)

if (
    st.session_state.lives == 1
    and not st.session_state.clue_given
    and not st.session_state.game_over
):
    if st.button("💡 Need clue?"):
        clue = clues.get(st.session_state.chosen_word, "")
        if clue:
            st.info(clue)
        st.session_state.clue_given = True

if not st.session_state.game_over:
    guess = st.text_input("Please enter one letter that there in your guessing word:", max_chars=1)
    if st.button("Submit guess"):
        process_guess(guess)
        st.rerun()
else:
    st.success("Game finished. Click **New Game** to play again.")
