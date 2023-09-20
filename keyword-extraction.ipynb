from collections import Counter
import re
import string

def preprocess_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    return text

def tokenize(text):
    return text.split()

def remove_stopwords(tokens):
    stopwords = set(["a", "an", "the", "in", "to", "for", "of", "and", "is", "our", "we", "with", "should", "have", "be", "are", "using", "include", "strong", "on", "by"])
    return [t for t in tokens if t not in stopwords]

def extract_keywords(tokens, num_keywords=20):
    frequency = Counter(tokens)
    return [word for word, freq in frequency.most_common(num_keywords)]

def expertise_blend(keywords):
    common_terms = set(["software", "engineer", "python", "java", "c++", "web", "development", "html", "css", "javascript", "coding", "debugging", "communication", "skills", "team", "candidate", "experience", "responsibilities", "knowledge"])
    return [k for k in keywords if k in common_terms]

if __name__ == "__main__":
    job_description = input("Enter the job description: ")
    preprocessed_text = preprocess_text(job_description)
    tokens = tokenize(preprocessed_text)
    filtered_tokens = remove_stopwords(tokens)
    keywords = extract_keywords(filtered_tokens)
    final_keywords = expertise_blend(keywords)
    print("Extracted Keywords:", final_keywords)
