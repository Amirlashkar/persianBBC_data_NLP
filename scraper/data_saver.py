import pandas as pd
import os

def fill_table(paragraph:str, topic:str):
    data_path = os.path.join(os.getcwd(), "data.csv")
    if not os.path.exists(data_path):
        df = pd.DataFrame(columns=["paragraph", "topic"])
        df.to_csv(data_path)
    else:
        df = pd.read_csv(data_path)

    data_dict = {
        "paragraph": paragraph,
        "topic": topic
    }

    new_row = pd.DataFrame([data_dict])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(data_path)