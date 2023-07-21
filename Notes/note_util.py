import json
from datetime import datetime

def load_notes(file_path):
    try:
        with open(file_path, "r") as file:
            notes = json.load(file)
            return notes
    except FileNotFoundError:
        return []

def save_notes(notes, file_path):
    with open(file_path, "w") as file:
        json.dump(notes, file, indent=4)

def generate_id():
    return str(datetime.now())

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def find_note_by_id(notes, note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None
