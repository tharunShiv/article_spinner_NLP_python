# Article Spinner NLP in Python

An article spinner

## What does Article Spinning mean?

Taking an existing Article and replacing words in it with similar words and coming up with a new Article.

## How do we Automate this?

In this repository, this process has been demonstrated

## So what's the approach?

1. Use the **Trigrams** approach. Consider triplets of words. For each and every word except the extreme words, form a triplet of (previous word, current word, next word)
2. We will now create a dictionary which will be of the form `trigram: ('prev word', 'next word'): ['current word']`
3. Now we have to find the **trigram probability**, i.e., the probability of the current word actually appearing in between the two words.
4. Now set a variable threshold of a 20% chance of a word being replaced.
5. Spin the article

## How do I run this code?

1. Clone the repo
2. Run the main.py by using the command `python main.py`

## Wanna contribute?

Go on
