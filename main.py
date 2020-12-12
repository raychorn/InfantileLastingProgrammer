import re

def autocorrect(something):
  regex = r"^[Yy][Oo][Uu]([a-qA-Zs-z]?)\1{0,}([\.\!\?\-\,\@\#\$\%\^\&\*\(\)\+\=]?)$"
  no_punctuation = lambda s:''.join([ch for ch in s if (ch.isalpha())])
  punctuation = lambda s:''.join([ch for ch in s if (not ch.isalpha())])
  add_punctuation = lambda s:punctuation(s) if (s.endswith(punctuation(s))) else ''
  something_new = []
  for word in something.split():
    #print('!!! {}'.format(word))
    if (word == punctuation(word)):
      #print('@@@ {} {}'.format(word, punctuation(word)))
      something_new.append(word)
    else:
      if (word.lower() == 'u') or (re.search(regex, word)):
        #print('*** {} {}'.format(word, add_punctuation(word)))
        something_new.append('your client' + add_punctuation(word))
      else:
        #print('### {} {}'.format(word, add_punctuation(word)))
        something_new.append(no_punctuation(word) + add_punctuation(word) if (len(add_punctuation(word)) > 0) else word + add_punctuation(word))
  something_new = ' '.join(something_new)
  return something_new

t = autocorrect("Let's market you on youtube")
print(t)
assert t == "Let's market your client on youtube"
print('='*30)

t = autocorrect("Our friend Alabinyou is conveniently named, and he wants to build a website called youwin with youuu")
print(t)
assert t == "your client your client youville utube your client youyouyou uuu raiyou united your client your client your client"
print('='*30)

t = autocorrect('You = so close')
print(t)
assert t == 'your client = so close', 'Fails'
print('='*30)

t = autocorrect('We have sent the deliverables to you.')
print(t)
assert t == 'We have sent the deliverables to your client.', 'Fails'
print('='*30)

t = autocorrect('Look forward to meeting youuuuu')
print(t)
assert t == 'Look forward to meeting your client', 'Fails'
print('='*30)

t = autocorrect('We want to film the commercial with you and syndicate it to youtube')
print(t)
assert t == 'We want to film the commercial with your client and syndicate it to youtube', 'Fails'
print('='*30)

t = autocorrect('You should begin on Monday')
print(t)
assert t == 'your client should begin on Monday', 'Fails'
print('='*30)

t = autocorrect('You u youville utube you youyouyou uuu raiyou united youuuu u you')
print(t)
assert t == 'your client should begin on Monday', 'Fails'
print('='*30)

