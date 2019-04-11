import time

path_to_file = 'corpus.txt'

with open(path_to_file, 'r') as f:
    text = f.readlines()

start = int(round(time.time() * 1000))
longest = ''
lines = text
for line in lines:
    for word in line.split(' '):
        if len(word) > len(longest):
            longest = word

end = int(round(time.time() * 1000)) - start
print('Longest word is \'{}\' length {}'.format(longest, len(longest)))
print('Processing time: {}ms'.format(end))




with open(path_to_file, 'r') as f:
    text = f.read()


start = int(round(time.time() * 1000))
longest = ''
lines = text.split('\n')
for line in lines:
    for word in line.split(' '):
        if len(word) > len(longest):
            longest = word

end = int(round(time.time() * 1000)) - start
print('Longest word is \'{}\' length {}'.format(longest, len(longest)))
print('Processing time: {}ms'.format(end))
