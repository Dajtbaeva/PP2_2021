from re import sub

print(sub('([a-z0-9])([A-Z])', r'\1_\2', input()).lower())

# JavaScript -> java_script
# FooBAR -> foo_bar
# WordPerfect -> word_perfect 