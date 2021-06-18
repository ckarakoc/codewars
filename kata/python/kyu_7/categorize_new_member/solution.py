def open_or_senior(data):
    return ['Senior' if age > 54 and handicap > 7 else 'Open' for age, handicap in data]