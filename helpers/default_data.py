from helpers.date_and_time import get_date, get_time

user_accounts = [
    {"username": "james", "password": "James"},
    {"username": "claudia", "password": "Claudia"},
    {"username": "david", "password": "David"}
]

default_words = [
    {"timestamp": f'{get_time()} - {get_date()}', "word": "new", "user_id": 1, "part_of_speech": "adjective", "translation": "nuevo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "horse", "user_id": 1, "part_of_speech": "adjective", "translation": "nuevo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "but", "user_id": 1, "part_of_speech": "adjective", "translation": "nuevo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "fantastic", "user_id": 1, "part_of_speech": "adjective", "translation": "nuevo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "whole", "user_id": 1, "part_of_speech": "adjective", "translation": "nuevo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "so", "user_id": 1, "part_of_speech": "adjective", "translation": "nuevo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "school", "user_id": 1, "part_of_speech": "adjective", "translation": "nuevo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "book", "user_id": 3, "part_of_speech": "noun", "translation": "libro", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "book", "user_id": 3, "part_of_speech": "noun", "translation": "libro", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "book", "user_id": 3, "part_of_speech": "noun", "translation": "libro", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "book", "user_id": 3, "part_of_speech": "noun", "translation": "libro", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "book", "user_id": 3, "part_of_speech": "noun", "translation": "libro", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "book", "user_id": 3, "part_of_speech": "noun", "translation": "libro", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": f'{get_time()} - {get_date()}', "word": "book", "user_id": 3, "part_of_speech": "noun", "translation": "libro", "sentence": "This is an example of a sentence using this word"}
]