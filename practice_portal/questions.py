# ============================================================
# questions.py
# Static practice-question bank for the Pupil Practice Portal,
# organized by subject and difficulty.
# ============================================================

QUESTION_BANK = {
    "maths": {
        "easy": [
            {"text": "What is 4 + 5?", "choices": ["9", "8", "10", "7"], "answer": "9"},
            {"text": "What is 10 - 3?", "choices": ["6", "7", "8", "5"], "answer": "7"},
            {"text": "What is 2 x 3?", "choices": ["5", "6", "7", "8"], "answer": "6"},
        ],
        "hard": [
            {"text": "What is 15 + 28?", "choices": ["41", "43", "53", "33"], "answer": "43"},
            {"text": "What is 9 x 8?", "choices": ["63", "72", "81", "64"], "answer": "72"},
            {"text": "What is 100 - 47?", "choices": ["53", "63", "57", "43"], "answer": "53"},
        ],
    },
    "english": {
        "easy": [
            {"text": "Which word is a noun?", "choices": ["Run", "Teacher", "Quickly", "Blue"], "answer": "Teacher"},
            {"text": "Which word means the opposite of 'big'?", "choices": ["Large", "Small", "Tall", "Wide"], "answer": "Small"},
            {"text": "Which word is spelled correctly?", "choices": ["Freind", "Friend", "Frend", "Freend"], "answer": "Friend"},
        ],
        "hard": [
            {"text": "Which word is spelled correctly?", "choices": ["Recieve", "Receive", "Receeve", "Receve"], "answer": "Receive"},
            {"text": "What is the plural of 'child'?", "choices": ["Childs", "Childes", "Children", "Childrens"], "answer": "Children"},
            {"text": "What is the opposite of 'ancient'?", "choices": ["Old", "Modern", "Historic", "Aged"], "answer": "Modern"},
        ],
    },
}


def get_questions(subject, difficulty):
    """
    Returns the list of question dictionaries for the given subject
    and difficulty. Falls back to an empty list if either is unknown.
    """
    subject_bank = QUESTION_BANK.get(subject, {})
    return subject_bank.get(difficulty, [])
