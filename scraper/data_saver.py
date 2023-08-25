import pandas as pd
import os

def fill_table(docORparagraph:str, main_topic:str, title:str, related_topics:str, data:str):
    if docORparagraph == "paragraph":
        data_path = os.path.join(os.getcwd(), "data", "rest_paragraph_data.csv")
    else:
        data_path = os.path.join(os.getcwd(), "data", "rest_doc_data.csv")

    if not os.path.exists(data_path):
        df = pd.DataFrame(columns=["main_topic", "title", "related_topics" ,"data"])

        df.to_csv(data_path, index=False)
    else:
        df = pd.read_csv(data_path)

    data_dict = {
        "main_topic": main_topic,
        "title": title,
        "related_topics": related_topics,
        "data": data
    }

    new_row = pd.DataFrame([data_dict])
    df = pd.concat([df, new_row], ignore_index=True)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df.to_csv(data_path)