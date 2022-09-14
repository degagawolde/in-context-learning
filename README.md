# in-context-learning
The complexity, cost, and skills required to produce LLMs is immense. Only larger companies and other international groups are able to train LLMs at the size of hundreds of billions of parameters. Given the benefit of LLMs to drive business and society, it is important to learn to use these monster AI models for multiple use in business and social problems. The need for specialized skills in prompt engineering will grow fast as more and and more companies start building their business around LLMs and similar products such as DALL-E 2, MidJourney, Bloom, etc.

## Named entity recognition using the LLMS API

[Entity Extraction with Cohere API](https://github.com/degagawolde/in-context-learning/notebooks/CohereEntityExtract.ipynb)

***Connect to Cohere API**
```
import cohere
co = cohere.Client(api_key)
```


## News scoring using the LLMS API

[News Artifact scoring Cohere API](https://github.com/degagawolde/in-context-learning/notebooks/CohereNewsScoring.ipynb)

## Text Analysis using DeepAI API

[Text Analysis with DeepAI API](https://github.com/degagawolde/in-context-learning/notebooks/DeepAITextAnlaysis.ipynb)

***Connect to the DeepAI API and do sentimental analysis on the given text***

```
requests.post(
    "https://api.deepai.org/api/sentiment-analysis",
    data={
        'text': 'Africa is a land of origin for human kind',
    },
    headers={'api-key': api_key}
)
```

***Connect to the DeepAI API and do summerize the given text***
```
# Example posting a local text file:
requests.post(
    "https://api.deepai.org/api/summarization",
    files={
        'text': open('../data/experimental/interim.txt', 'rb'),
    },
    headers={'api-key': api_key}
)
```
