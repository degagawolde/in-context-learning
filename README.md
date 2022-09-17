# in-context-learning
The complexity, cost, and skills required to produce LLMs is immense. Only larger companies and other international groups are able to train LLMs at the size of hundreds of billions of parameters. Given the benefit of LLMs to drive business and society, it is important to learn to use these monster AI models for multiple use in business and social problems. The need for specialized skills in prompt engineering will grow fast as more and and more companies start building their business around LLMs and similar products such as DALL-E 2, MidJourney, Bloom, etc.

# Objective
Large Language Model(LLMS) can be used for multiple use in business and social problem.
The objective of this challenge is to generate prompts for LLMs to ***extract*** relevant entities from
job descriptions and also to ***classify*** news artifacts given only a few examples of human scores

## Named entity recognition using the LLMS API
![entity](https://camo.githubusercontent.com/bee6479e52d74c33a02b87a01106be06b1e823d579587eeafe5154ec4222b98b/68747470733a2f2f6769746875622e636f6d2f636f686572652d61692f6e6f7465626f6f6b732f7261772f6d61696e2f6e6f7465626f6f6b732f696d616765732f6b6579776f72642d65787472616374696f6e2d6770742d6d6f64656c732e706e67)
Entity Extraction with Cohere API --[notebooks/CohereEntityExtract.ipynb](https://github.com/degagawolde/in-context-learning/notebooks/CohereEntityExtract.ipynb)

***Connect to Cohere API***
```
import cohere
co = cohere.Client(api_key)

```

## News scoring using the LLMS API
![scoring](https://camo.githubusercontent.com/c97c4f86bd22a530acc71bd1d8395f91fc048e12424454b9f0d42745596038ee/68747470733a2f2f6769746875622e636f6d2f636f686572652d61692f6e6f7465626f6f6b732f7261772f6d61696e2f6e6f7465626f6f6b732f696d616765732f73696d706c652d636c61737369666965722d656d62656464696e67732e706e67)

News Artifact scoring Cohere API -- [notebooks/CohereNewsScoring.ipynb](https://github.com/degagawolde/in-context-learning/notebooks/CohereNewsScoring.ipynb)

```
co.classify(
      model='medium',  
      inputs=[text], # the string to be classified
      examples=examples # a couple of examples - training set
  )
```
## Text Analysis using DeepAI API

Text Analysis with DeepAI API -- [notebooks/DeepAITextAnlaysis.ipynb](https://github.com/degagawolde/in-context-learning/notebooks/DeepAITextAnlaysis.ipynb)

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

***Connect to the DeepAI API and summarize the given text***
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
# Streamlit Dashboard frontend and Fast API backend
***streamlit dashboard*** [streamlitapp/main.py](https://github.com/degagawolde/in-context-learning/streamlitapp/main.py)

***Fast API*** [backend/backend_main.py](https://github.com/degagawolde/in-context-learning/backend/backend_main.py)
# What next?
- News Artifact Scoring
- Entity Extraction from job description.
