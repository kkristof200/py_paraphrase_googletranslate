# paraphrase_googletranslate



## Description

Paraphrasing via google translate

## Install

~~~~bash
pip install paraphrase_googletranslate
# or
pip3 install paraphrase_googletranslate
~~~~

## Usage

~~~~python
from paraphrase_googletranslate import Paraphraser

original = 'Canvas Print Art size:12inchx12inch(30cmx30cm)x2panels Framed Ready to Hang. Brand: Amoy Art. Canvas print is already perfectly stretched over wooden frame and also hooks have been mounted on each panel,which easily to hang out of box.A perfect wall decorations paintings for living room, bedroom, kitchen, office, Hotel, dining room, office, bathroom, bar etc. HD pictures photo printed on canvas with vivid color on high quality canvas,A perfect gift for your relatives and friends. Packed in Carton Box.100% satisfied guarantee. Shop with confidence!'

phraser = Paraphraser()

rephrased = phraser.paraphrase(original, secondary_language='es')
print(rephrased)
rephrased = phraser.paraphrase(rephrased, secondary_language='de')
print(rephrased)
rephrased = phraser.paraphrase(rephrased, secondary_language='fr')

print('\n\n\n')

print(original)
print(rephrased)
~~~~

## Dependencies

[google-trans-new](https://pypi.org/project/google-trans-new)