from paraphrase_googletranslate import Paraphraser

original = '"The quick brown fox jumps over the lazy dog" is an English-language pangram—a sentence that contains all of the letters of the English alphabet. Owing to its brevity and coherence, it has become widely known. The phrase is commonly used for touch-typing practice, testing typewriters and computer keyboards, displaying examples of fonts, and other applications involving text where the use of all letters in the alphabet is desired.'

phraser = Paraphraser(random_ua=True)

rephrased = phraser.paraphrase(original)

print(original)
print(rephrased)