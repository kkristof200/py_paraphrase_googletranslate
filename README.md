# paraphrase_googletranslate

![python_version](https://img.shields.io/static/v1?label=Python&message=3.5%20|%203.6%20|%203.7&color=blue) [![PyPI downloads/month](https://img.shields.io/pypi/dm/paraphrase_googletranslate?logo=pypi&logoColor=white)](https://pypi.python.org/pypi/paraphrase_googletranslate)

## Description

Paraphrasing via google translate

## Install

````bash
pip install paraphrase_googletranslate
# or
pip3 install paraphrase_googletranslate
````

## Usage

```python
from paraphrase_googletranslate import Paraphraser

original = '"The quick brown fox jumps over the lazy dog" is an English-language pangram—a sentence that contains all of the letters of the English alphabet. Owing to its brevity and coherence, it has become widely known. The phrase is commonly used for touch-typing practice, testing typewriters and computer keyboards, displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.'

phraser = Paraphraser(random_ua=True)

rephrased = phraser.paraphrase(original)

print(original)
print(rephrased)

#This will print:

#"The quick brown fox jumps over the lazy dog" is an English-language pangram—a sentence that contains all of the letters of the English alphabet. Owing to its brevity and coherence, it has become widely known. The phrase is commonly used for touch-typing practice, testing typewriters and computer keyboards, displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.

#"The quick brown fox jumps over the lazy dog" is an English-language pangram a phrase that contains all the letters of the English alphabet. Because of its brevity and consistency, it has become widely known. The phrase is commonly used to practice typing to touch, trying typewriters and computer keyboards, showing examples of sources, and other applications involving the use of text where all the letters of the alphabet is desired.
```
