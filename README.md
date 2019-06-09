# TTS Thai

Open source thai text to speech engine.

Google Colab : https://colab.research.google.com/drive/1e16gG3zpz3Y-fKT4Tw8bAbZWuwVTWEoh

## Install

$ pip install https://github.com/PyThaiNLP/pythainlp/archive/dev.zip

$ pip install https://github.com/wannaphongcom/thaitts/archive/master.zip

and install espeak-ng

## Using

```python
from thaitts import TTS
t=TTS()
t.speak("แมวกินปลาทู")
```

