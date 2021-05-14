# Speech-Recognition

This report provides a way of speech recognition


### Prerequisites

1. Download the google drive folder **speech**, the google drive will automaticly compress the folder as a zip file and rename the zip file.
2. After downloading, change the zip file name to **speech**.
3. Uncompress the speech.zip file and you will get a **speech** folder.  Assume your mnist folder is under **This PC > Downloads**
4. Open **Anaconda Prompt**. It is recommended to use **Anaconda Prompt** to run this report, because it provides environment to run python files.
5. Please type in the following cammands to change to your folder path. 

```
cd Downloads\speech
```

6. Please type in the following cammand to install the prerequisite package

```
pip install SpeechRecognition
```

### Test
```
python speech.py --audio_dir hello.wav
```

This file will recognitize the audio you have input

## Run on GPU Server
1. Clone the source code 

