import streamlit as st
import random

# Your exact data (unchanged)
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
clues = {
    "singam": "Kattuke Raja",
    "puli": "India oda national Animal",
    "anil": "Muthugula Moonu lines irukum",
    "paampu": "paatha padaye natungum",
    "muyal": "kutty ah irukum,vegama oodum ana maan ila",
    "nari": "Thanthiramana animal",
    "mayil": "muruganin vaganam"
}

# Initialize game state
if 'lives' not in st.session_state:
    st.session_state.lives = 6
if 'chosen_word' not in st.session_state:
    st.session_state.chosen_word = ""
if 'display' not in st.session_state:
    st.session_state.display = ""
if 'crc_word' not in st.session_state:
    st.session_state.crc_word = ""
if 'game_over' not in st.session_state:
    st.session_state.game_over = True

st.title("🎮 Hangman - Thanglish Animals")

# Instructions (your exact text)
st.write("""
Animals name are in **thanglish** (ex: singam). Think the letters in that way.
You should guess the animal name based on below letters count.
You have **6 lives**. Each time when you guess wrong you lose life.
If you lose all lives you will be hanged :)
""")

# New Game button
if st.button("🔄 New Game"):
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.display = "_" * len(st.session_state.chosen_word)
    st.session_state.crc_word = ""
    st.session_state.lives = 6
    st.session_state.game_over = False
    st.rerun()

if st.session_state.game_over and st.session_state.chosen_word:
    st.success("🎉 You Won!" if "_" not in st.session_state.display else "💀 Game Over!")
    st.info(f"Word was: **{st.session_state.chosen_word}**")

if not st.session_state.game_over:
    # Show current game state
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Word")
        st.code(st.session_state.display)
        st.subheader("Lives")
        st.text(f"{st.session_state.lives}/6")
    
    with col2:
        st.text(stages[st.session_state.lives])
    
    # Guess input
    guess = st.text_input("Enter one letter:", max_chars=1).lower()
    
    if st.button("Guess") and guess:
        # Process guess (your exact logic)
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
        
        if guess not in st.session_state.chosen_word:
            st.session_state.lives -= 1
        
        # Check win
        if st.session_state.display == st.session_state.chosen_word:
            st.session_state.game_over = True
        
        # Check lose
        if st.session_state.lives <= 0:
            st.session_state.game_over = True
        
        st.rerun()
    
    # Clue at 1 life (your exact logic)
    if st.session_state.lives == 1:
        if st.button("💡 Clue"):
            st.info(clues[st.session_state.chosen_word])

