import openai
import os
import datetime

from openai import OpenAI
client = OpenAI(api_key = "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")

def process_subtopic(subtopic):
    completions = client.completions.create(
        model='gpt-3.5-turbo-instruct',
        temperature=0.5,
        prompt="Create a linkedin post without and emojis and emoticons based on {} with line break".format(subtopic),
        max_tokens=300,
        n=1,
        stop=None               
    )

    return completions.choices[0].text


def read_subtopics_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        subtopics = [line.strip() for line in file.readlines()]
    return subtopics

def get_current_day():
    # Getting current day as an integer (Monday - 0, Tuesday - 1, ...)
    return datetime.datetime.now().weekday()

def read_used_subtopics(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            used_subtopics = [line.strip() for line in file.readlines()]
        return used_subtopics
    except FileNotFoundError:
        return []
    
    
def write_used_subtopic(file_path, subtopic):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(subtopic + '\n')

def write_content_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    subtopics_file_path = 'subtopics.txt'

    subtopics_list = read_subtopics_from_file(subtopics_file_path)

    current_day = get_current_day()
    print(current_day)

    used_subtopics_file_path = 'used_subtopics.txt'
    used_subtopics = read_used_subtopics(used_subtopics_file_path)

    # Use a new subtopic only if the current day is not in the used_subtopics list
    if current_day < len(subtopics_list) and current_day not in used_subtopics:
        subtopic_to_use = subtopics_list[current_day]
        response = process_subtopic(subtopic_to_use)
        response = "Hello LinkedIn Fam! Today we are going to deep dive in the topic {}".format(subtopic_to_use) + response
        # print(response)
        if subtopic_to_use not in used_subtopics:
            content_file_path = 'content.txt'
            write_content_to_file(content_file_path, response)
            print('Content successfully written to file')

        # Mark the current day as used
            write_used_subtopic(used_subtopics_file_path, subtopic_to_use)
        else:
            print(f'Content for subtopic "{subtopic_to_use}" already generated for today.')

        # Mark the current day as used
        # write_used_subtopic(used_subtopics_file_path, subtopic_to_use)
    
    else:
        print("All subtopics used or not a valid day for a subtopic.")