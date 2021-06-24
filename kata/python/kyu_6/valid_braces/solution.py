def validBraces(string):
    braces = ["{}", "[]", "()"]
    for _ in range(int(len(string) / 2)):
        for brace in braces:
            string = string.replace(brace, '')
        if not string:
            return True
    return False