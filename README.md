
# News Summary AI

This project is a takehome assignment by akaike.ai
The consist of model which scraps news from Times Of India and generate summary and sentiment and comparative sentiment analysis. The system provides api support for developers.

## Table of Contents

- [Project Setup](#project-setup)
- [Model Details](#model-details)
- [API Development](#api-development)
- [Assumptions & Limitations](#assumptions--limitations)

## Project Setup

### Prerequisites

- python3
- required packages will be downloaded directly from requirements.txt

### Installation

Step-by-step instructions for setting up the project locally.

```bash
# Create virtual environment
py -m venv [whatever name you want]

# Chage directory to environment
cd [environment directory which you created]

# Start the environment
# Below example is with respect to windows
.\Script\activate

# Clone the repository
git clone https://github.com/KaustubhVaidya404/news-summary-ai.git

# Navigate to the project directory
cd news-summary-ai

# Install the dependencies
pip install -r requirements.txt
```

### Running the Application

Below are the instructions for running the Application

```bash
# To run the stremlit locally
streamlit run \app.py

# To run the fast api server
fastapi run .\api.py
```

Stremlit runs on post 8501 and fast api server runs on port 8000

## Model Details

### Summarization Model
The summarization model used in this project is based on frequency-based sentence scoring, which is a statistical approach for text summarization. This method does not involve a neural network architecture like transformers; instead, it relies on the following steps:
- Tokenization: The entire content from the articles is tokenized into sentences and words using NLTK's sent_tokenize and word_tokenize functions.
- Word Frequency Calculation: For each word in the content, its frequency is computed. Words are converted to lowercase to ensure case insensitivity, and non-alphabetical words are excluded from the frequency count.
- Normalization of Word Frequencies: The word frequencies are normalized by dividing each word's frequency by the maximum frequency observed in the text. This helps scale the frequency values between 0 and 1.
- Sentence Scoring: Each sentence is scored based on the sum of normalized frequencies of the words it contains. Sentences with higher total scores are considered more important.
- Summary Generation: The top-scoring sentences are selected to form the overall summary. By default, the top 2 sentences with the highest scores are chosen as the summary.
> Libraries Used:
- NLTK: Tokenization of sentences and words is handled using the NLTK (Natural Language Toolkit) library.

### Sentiment Analysis Model
The sentiment analysis model is powered by VADER (Valence Aware Dictionary and sEntiment Reasoner), which is a lexicon and rule-based sentiment analysis tool specifically tuned for social media texts but also effective on other types of text.
- VADER Sentiment Intensity Analyzer: This model is provided by NLTK and calculates a sentiment score for each sentence based on lexical features. It returns a dictionary containing the following values:
    - positive: Probability that the sentence expresses a positive sentiment.
    - neutral: Probability that the sentence is neutral.
    - negative: Probability that the sentence conveys a negative sentiment.
    - compound: A normalized compound score summarizing the overall sentiment of the text, ranging from -1 (extremely negative) to +1 (extremely positive).
- Tokenization: The text from the articles is concatenated (title + summary), and the VADER model analyzes the sentiment of the combined text for each article.
- Training Data: The VADER model is trained on a combination of datasets including general-purpose lexicons as well as human-annotated datasets. It does not require specific training on a custom dataset for this use case and can be applied out-of-the-box.
> Libraries Used:
- NLTK: NLTK's VADER module is used to compute the sentiment scores.

### Text-to-Speech (TTS)
- The Text-to-Speech (TTS) model used in this project leverages Google Text-to-Speech (gTTS) and a translation service to convert English text into Hindi speech. This model works in the following steps:
- Translation: The input text (in English) is first translated into Hindi using the Translator class from the translate library. The translated text serves as the input for generating the speech.
- Text-to-Speech Conversion: The translated Hindi text is passed to Google Text-to-Speech (gTTS), which generates the audio data in Hindi. The gTTS library uses Google’s TTS engine to synthesize speech from the translated text.
- Audio Buffering: The synthesized speech is written to a buffer (BytesIO) to facilitate easy manipulation and transmission of the generated audio file. This allows for in-memory storage of the audio data.
- Supported Language: The TTS model currently supports Hindi (lang='hi') as the target language for speech generation. However, it can be adapted to other languages supported by the gTTS library by changing the language code.
> Libraries Used:
- gTTS: Used for text-to-speech conversion, supports multiple languages.
- translate: Used for translating the input text from English to Hindi.
- BytesIO: Used to store the audio data in-memory before returning it as a binary stream.

## API Development

#### Accessing API

To access get the data from api

```bash
# To get response
curl -X GET "http://localhost:8000/v1/company?q=YourCompanyName" -H "accept: application/json"
```
```bash
# To get only the desired response i.e only positive or negative or neutral
curl -X GET "http://localhost:8000/v1/company?q=YourCompanyName&sentiment_type=positive" -H "accept: application/json"
```
```bash
# Replace the filename with file name you received to download the audio file
curl -X GET "http://localhost:8000/v1/company/audio/filename" -H "accept: application/json"
```

To access the api docs

```bash
curl -X GET "http://localhost:8000/docs" -H "accept: application/json"
```

## Assumptions & Limitations

### Assumptions

- User will enter company name.
- Language used for input is english only.


### Limitations

- It also scraps information if input is other than company name.
- Cannot generate speech only on summary due to gtts token limitations.
