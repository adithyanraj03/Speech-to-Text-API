
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

def text_summarizer(text, max_length=150):
    # Load pre-trained GPT-2 model and tokenizer
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Tokenize and generate a summary
    input_ids = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(input_ids, max_length=max_length, min_length=50, num_beams=4, length_penalty=2.0, early_stopping=True)

    # Decode and return the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

if __name__ == "__main__":
    input_text = "Hello, my name is John. I am a software engineer at XYZ company. I have been working in this field for over 5 years. I am passionate about coding and love to learn new things. I am excited to try out this new AI text summarization model."

    summary = text_summarizer(input_text)
    print("Original Text:")
    print(input_text)
    print("\nSummary:")
    print(summary)