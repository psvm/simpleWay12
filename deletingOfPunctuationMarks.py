#Delete all punctuation marks into the given text
import re
text = "This!, is- a? strange: ;text .with a lo!t number of,,, punctuation... mistakes?"
print(re.sub('[.,!?:;-]', '', text))