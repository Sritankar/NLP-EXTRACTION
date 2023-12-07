import spacy
import json

nlp = spacy.load("en_core_web_md")


with open('DATA.JSON', 'r') as file:
    data = json.load(file)


def process_text(text):
    if isinstance(text, str):
        doc = nlp(text)

       
        names = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
        
        if names:
            print(f"Names in text: {text}")
            print(f"Extracted names: {', '.join(names)}")
            print("----")
    else:
        print("Text is not a string.")

if isinstance(data, list):
    for item in data:
        if 'text' in item:
            text = item['text']
            if isinstance(text, list):
                for sub_text in text:
                    process_text(str(sub_text))
            else:
                process_text(str(text))
        else:
            print("Text field is missing.")
else:
    print("Data is not in the expected format (list of dictionaries).")
