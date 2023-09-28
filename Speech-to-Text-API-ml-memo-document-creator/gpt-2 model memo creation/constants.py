
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
    input_text = "Office Assistant Resume Summary  Experienced office assistant seeking to leverage advanced office skills for improved efficiency at Media XYZ. 5+ years of industry experience includes decreasing data entry mistakes by 23%, decreasing negative feedback by 11%, and giving insights into creating paperless office environments Click here for the full office assistant resume example.Executive Assistant Resume Summary Accomplished executive assistant with experience in providing support to a high-level CEO and other executives for 4 years. Helped with everything from customer support, to data entry and preparing well-researched documents. Skilled at time management, proficient in MS Office and Adobe Photoshop."

    summary = text_summarizer(input_text)
    print("Original Text:")
    print(input_text)
    print("\nSummary:")
    print(summary)