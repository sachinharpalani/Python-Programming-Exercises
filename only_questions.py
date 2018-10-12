import re

with open('/home/gblp229/code/Python-programming-exercises/100+ Python challenging programming exercises.txt','r') as f_handler:
    all_lines = f_handler.read()
    only_questions = ''.join(re.findall(r'Question:(.*?)Hints', all_lines, re.S))

    with open('/home/gblp229/code/python_questions.txt','w') as questions_handler:
        questions_handler.write(only_questions)
