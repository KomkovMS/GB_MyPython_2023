import note_util

NOTES_FILE = "notes.json"


def generate_id(notes):
    if len(notes) == 0:
        return 1
    else:
        last_note = notes[-1]
        return last_note["id"] + 1


def add_note(title, body):
    notes = note_util.load_notes(NOTES_FILE)
    note_id = generate_id(notes)
    timestamp = note_util.get_current_timestamp()

    note = {
        "id": note_id,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }

    notes.append(note)
    note_util.save_notes(notes, NOTES_FILE)


def read_note(note_id):
    notes = note_util.load_notes(NOTES_FILE)
    note = note_util.find_note_by_id(notes, note_id)

    if note:
        print("Заголовок: ", note["title"])
        print("Тело: ", note["body"])
        print("Дата/Время: ", note["timestamp"])
    else:
        print("Заметка не найдена.")


def edit_note(note_id, new_title, new_body):
    notes = note_util.load_notes(NOTES_FILE)
    note = note_util.find_note_by_id(notes, note_id)

    if note:
        note["title"] = new_title
        note["body"] = new_body
        note["timestamp"] = note_util.get_current_timestamp()
        note_util.save_notes(notes, NOTES_FILE)
        print("Заметка успешно отредактирована.")
    else:
        print("Заметка не найдена.")


def delete_note(note_id):
    notes = note_util.load_notes(NOTES_FILE)
    note = note_util.find_note_by_id(notes, note_id)

    if note:
        notes.remove(note)
        note_util.save_notes(notes, NOTES_FILE)
        print("Заметка успешно удалена.")
    else:
        print("Заметка не найдена.")


def list_notes():
    notes = note_util.load_notes(NOTES_FILE)
    print("Список заметок:")

    for note in notes:
        print("ID: ", note["id"])
        print("Заголовок: ", note["title"])
        print("Тело: ", note["body"])
        print("Дата/Время: ", note["timestamp"])
        print("------------------------")
