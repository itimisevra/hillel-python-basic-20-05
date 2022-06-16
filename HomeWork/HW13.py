translations = {
'apple': ['malum', 'pomum', 'popula'],
'fruit': ['baca', 'bacca', 'popum'],
'punishment': ['malum', 'multa']
}

def invert (translations):
    return {tuple(v):k for k, v in translations.items()}
print(invert(translations))