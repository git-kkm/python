def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    print('The char count is {}'.format(count) )
    return count

file = open("myfile.txt")
text = file.read()
print('len(text)={}'.format(len(text)))

for char in 'abcdefghijklmnopqrstuvwxyz':
    percent = 100 * count_char(text, char) / len(text)
    print('The char {} has percentage {}'.format(char, percent) )
