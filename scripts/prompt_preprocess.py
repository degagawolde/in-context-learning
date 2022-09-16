import pandas as pd

class TestPreprocess:
    def __init__(self) -> None:
        pass
    def entity_extraction(self,test_df:pd.DataFrame):
        test_doc = test_df.document.apply(
            lambda x: x.replace("\n", " ")+'\n\nExtracted Text:').to_list()
        return test_doc