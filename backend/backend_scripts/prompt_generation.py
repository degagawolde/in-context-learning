
from doctest import Example


class cohereExtractor():
    def __init__(self, examples,co):
        self.examples = examples
        self.co = co

    def make_prompt(self, example):
        prompt = self.examples + example

        return prompt#("".join([str(exam) for exam in prompt]))

    def extract(self, example):
        extraction = self.co.generate(
            model='large',
            prompt=self.make_prompt(example),
            max_tokens=100,
            temperature=0.5,
            stop_sequences=["----"])

        return(extraction.generations[0].text[:-1])


class CohereClassifier:
    def __init__(self,examples,co) -> None:
        self.examples = examples
        self.co = co
        
    def classify_text(self, text):
        classifications = self.co.classify(
            model='xlarge',  # model version - medium-22020720
            inputs=[text],
            examples=self.examples
        )
        return classifications.classifications
