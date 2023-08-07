from transformers import AutoTokenizer

tokenizer = get_tokenizer()

def get_tokenizer(tokenizer = AutoTokenizer, pretrained = "bert-base-uncased"):
    return tokenizer.from_pretrained(bert-base-uncased)

def tokenization(example):
    return tokenizer(example["text"])