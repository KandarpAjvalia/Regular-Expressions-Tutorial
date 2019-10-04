import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

bat cat mat pat
'''

sentence = 'Start a sentence and then bring it to an end'

# difference between string and raw string
print("\tTab")
print(r"\tTab")

# pattern = re.compile(r'abc')

# pattern = re.compile(r'cba')

# matches all the characters
# pattern = re.compile(r'.')


# matches all the periods
# pattern = re.compile(r'\.')

# matches coreyms.com
# pattern = re.compile(r'coreyms\.com')

# mathces at the beginning
# pattern = re.compilr(r'$Start')

# mathces at the end
# pattern = re.compile(r'end$')

# pattern to match phone number
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# character set to only match - or .
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

# omly match 800 and 900 numbers
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

# match range of numbers
# pattern = re.compile(r'[1-5]')

# IF INSIDE A SET, CARAT NEGATES THE SET, not letters
# pattern = re.compile(r'[^a-zA-Z]')

# matches letters that are not b
# pattern = re.compile(r'[^b]at')

# Better way, use quantifiers match exact numbers
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# match Mr name
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

# match Mr, Mrs and Ms
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

test = re.findall(r'M(?:r|s|rs)\.?\s[A-Z]\w*', text_to_search)
print(test)
#
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)
#
# with open('data.txt', 'r') as f:
#     contents = f.read()
#
#     matches = pattern.finditer(contents)
#
#     for match in matches:
#         print(match)