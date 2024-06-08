# Use a pipeline as a high-level helper
from transformers import pipeline
import torch
import json
import gradio as gr

# text_translator = pipeline("translation", model="facebook/nllb-200-distilled-600M")

model_path  = "./Model/models--facebook--nllb-200-distilled-600M/snapshots/f8d333a098d19b4fd9a8b18f94170487ad3f821d"

text_translator = pipeline("translation", model=model_path, torch_dtype=torch.bfloat16)

# text = "Hello friends how are you?"
# translation = text_translator(text,
#                              src_lang="eng_Latn",
#                              tgt_lang="hin_Deva")

# print(translation)

# Load the JSON table
with open('language.json') as f:
    language_data = json.load(f)

def get_flores_200_code(language):
    for code in language_data:
        if code['Language'] == language:
            return code['FLORES-200 code']
    return None

def translate_text(text, destination_language):
    
    # text = "Hello friends how are you?"
    dest_code = get_flores_200_code(destination_language)

    translation = text_translator(text,
                              src_lang="eng_Latn",
                              tgt_lang=dest_code)
    return translation[0]["translation_text"]

gr.close_all()

demo = gr.Interface(fn=translate_text,
                    inputs=[gr.Textbox(label="Input text to translate",lines=6), gr.Dropdown(["English", "German", "Eastern Panjabi", "Sanskrit", "Urdu", "Tamil", "Telugu",  "Yue Chinese", "Chinese (Simplified)", "Chinese (Traditional)", "Hindi", "French", "Spanish"],label="Select destination language")],
                    outputs=[gr.Textbox(label="Translated text", lines=4)],
                    title="@IT AI Enthusiast (https://www.youtube.com/@itaienthusiast/) - Project 4: Multi Language translator",
                    description="THIS APPLICATION WILL BE USED TO TRANSLATE ANY ENGLISH TO MULTIPLE LANGUAGES",
                    concurrency_limit=16)
demo.launch()

# Hello Friends, Welcome to my channel. I hope this video helps you understand AI.
# "Hello friends how are you?"