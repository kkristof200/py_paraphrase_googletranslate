# paraphrase_googletranslate

![PyPI - package version](https://img.shields.io/pypi/v/paraphrase_googletranslate?logo=pypi&style=flat-square)
![PyPI - license](https://img.shields.io/pypi/l/paraphrase_googletranslate?label=package%20license&style=flat-square)
![PyPI - python version](https://img.shields.io/pypi/pyversions/paraphrase_googletranslate?logo=pypi&style=flat-square)
![PyPI - downloads](https://img.shields.io/pypi/dm/paraphrase_googletranslate?logo=pypi&style=flat-square)

![GitHub - last commit](https://img.shields.io/github/last-commit/kkristof200/py_paraphrase_googletranslate?style=flat-square)
![GitHub - commit activity](https://img.shields.io/github/commit-activity/m/kkristof200/py_paraphrase_googletranslate?style=flat-square)

![GitHub - code size in bytes](https://img.shields.io/github/languages/code-size/kkristof200/py_paraphrase_googletranslate?style=flat-square)
![GitHub - repo size](https://img.shields.io/github/repo-size/kkristof200/py_paraphrase_googletranslate?style=flat-square)
![GitHub - lines of code](https://img.shields.io/tokei/lines/github/kkristof200/py_paraphrase_googletranslate?style=flat-square)

![GitHub - license](https://img.shields.io/github/license/kkristof200/py_paraphrase_googletranslate?label=repo%20license&style=flat-square)

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