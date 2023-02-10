# Pdf-Proofing

## The Pdf-Proofing includes two functions:
1. examined incorrect language within pdf document.
2. examine different number of images within a pdf document (not really useful)

## Libraries used for both files include 
- re
- fasttext
- pdfminer

## Supported languages for fasttext library
Fasttext supports a wide range of languages for language recognition.
```
af als am an ar arz as ast av az azb ba bar bcl be bg bh bn bo bpy br bs bxr ca cbk ce cebckb co cs cv cy da de diq dsb dty dv el eml en eo es et eu fa fi fr frr fy ga gd gl gn gom gu gv he hi hif hr hsb ht hu hy ia id ie ilo io is it ja jbo jv ka kk km kn ko krc ku kv kw ky la lb lez li lmo lo lrc lt lv mai mg mhr min mk ml mn mr mrj ms mt mwl my myv mzn nah nap nds ne new nl nn no oc or os pa pam pfl pl pms pnb ps pt qu rm ro ru rue sa sah sc scn sco sd sh si sk sl so sq sr su sv sw ta te tg th tk tl tr tt tyv ug uk ur uz vec vep vi vls vo wa war wuu xal xmf yi yo yue zh
```
## Languages that are needed
Trimble uses the following
```
da = danish, de = german, en = english, es = Spanish, fr = french, it = italian, ja = japanese, ko = korean, no = norwegian, nl = dutch, pl = polish, pt = portuguese,  ru = russian, sv = swedish zh, = chinese
```
## Usage languageDetector
Open terminal in your current path by using cmd. type the following:
```
python languageDetector.py
```
Simply **shift + right-click** on the pdf file, and the **copy as path** option will appear, allowing you to obtain the pdf file path.
```text
enter path : "C:\Users\sqadir\Documents\file.pdf"
```
Language option will appear 
```text
LANGUAGES:

da = danish, de = german, en = english, es = Spanish, fr = french, it = italian, ja = japanese, ko = korean, no = norwegian, nl = dutch, pl = polish, pt = portuguese,  ru = russian, sv = swedish zh, = chinese

Enter language : en
```

you will then obtain results which are fairly accurate. 

## Contributing

Pull requests are welcome within Trimble. Please make sure to update tests as appropriate.

## License

Any person within **Trimble** who obtains a copy of this software and related documentation files (the "Software") is hereby authorized to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, as well as to authorize others within Trimble to do so without deleting previous work/commits.
