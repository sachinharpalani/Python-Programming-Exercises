import re


def extract_questions(exercises_filepath, questions_filepath):
    with open(exercises_filepath,'r') as f_handler:
        all_lines = f_handler.read()
        only_questions = ''.join(re.findall(r'Question:(.*?)Hints', all_lines, re.S))

        with open(questions_filepath,'w') as questions_handler:
            questions_handler.truncate()
            questions_handler.write(only_questions)
