strings = ['longest', 'long', 'longer']

print(sorted(strings, key=lambda x: (-len(x), x)))
