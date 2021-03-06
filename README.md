# OC_IA_Projet1

This project uses Microsoft Azure Cognitives Services to detect the language of a text.<br/>
This text may be choosen by you or you can use a database to test the detector.

## Installation

### Configure your access to Microsoft Azure :

Create a file `.env` and set the parameters with the values provided by Azure.<br/>
The three necessary environment variables are :<br/>
TRANSLATOR_TEXT_SUBSCRIPTION_KEY=""<br/>
TRANSLATOR_TEXT_ENDPOINT=""<br/>
TRANSLATOR_TEXT_LOCATION=""<br/>

### Option 1 : Installation and execution with pipenv

For this method, it is necessary to have pipenv already installed on your python installation. If pipenv is not already installed on your computer, refer to [this page](docs/pipenv/installation-en.md).

1. Clone this repository using `$ git clone https://github.com/S0Imyr/OC_IA_Projet1.git`
2. Move to root folder with `$ cd OC_IA_Projet1`
3. Install project dependencies with `pipenv install` 
4. Launch the detector: <br/>
    a. without text input : `pipenv run python detector.py` <br/>
    b. with text input : `pipenv run python detector.py --text "<the text whose language you want to detect>"`

## Utilisation

### With a custom text

Run `python detector.py --text <your text>` to detect the language of the text passed as an argument.

```bash
$ pipenv run python detector.py --text "Three can keep a secret, if two of them are dead."
> 
>  You choose to translate the text : 
> Three can keep a secret, if two of them are dead.
> The detected language is English with a confidence of 100.0%.
> 
> The language source is unknown.
```

### Random text

Run `python detector.py` to detect the language of a random text in one of the most spoken languages from the dataset (`data/x_test.txt`).

```bash
$ pipenv run python detector-cli.py
>
> The random text is :
> आठवीं और नवीं शताब्दियों में वेस्ट फ्रैंकों ने सैक्सनों और फ्रीज़नों का पूरी तौर से दमन कर दिया। साथ ही फ्रांकिश भ
ाषा भी जर्मैनिकों पर छा गईं। किंतु नवीं शताब्दी में ही अनेक स्थानीय प्रभाव के व्यक्तियों ने उभर कर राज्य को छिन्न 
भिन्न कर दिया। १३वीं शताब्दी में कांउट फ्लोरिस पंचम के शासन में हालैंड बहुत शक्तिशाली हो गया, और उसकी सीमाएँ भी दू
र दूर तक फैल गईं। १५वीं शताब्दी में बर्गडी के ड्यूक शक्तिशाली हो गए। १५४७ में स्पेन के राजा चार्ल्स पंचम ने नीदरलै
ंड और आस्ट्रिया के संघ का आदेश जारी किया और १५४९ में स्पेन में नीदरलैंड भी सम्मिलित कर लिया गया।
>
> The detected language is Hindi with a confidence of 99.0%.
>
> The language of the source text is Hindi
> Success
```
