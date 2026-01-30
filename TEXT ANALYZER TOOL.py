import string
from collections import Counter

STOPWORDS = {
    "the", "is", "in", "and", "to", "of", "a", "an", "on", "for",
    "with", "that", "this", "it", "as", "are", "was", "were", "be"
}

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    cleaned_words = [word for word in words if word not in STOPWORDS]
    
    return cleaned_words

def sentence_stats(text):
    sentences = text.replace("!", ".").replace("?", ".").split(".")
    sentences = [s.strip() for s in sentences if s.strip()]
    lengths = [len(sentence.split()) for sentence in sentences]
    
    return {
        "total_sentences": len(sentences),
        "average_length": sum(lengths) / len(lengths) if lengths else 0,
        "max_length": max(lengths) if lengths else 0,
        "min_length": min(lengths) if lengths else 0
    }

def analyze_text(text):
    cleaned_words = clean_text(text)
    total_words = len(cleaned_words)
    word_freq = Counter(cleaned_words)
    top_words = word_freq.most_common(5)
    stats = sentence_stats(text)
    
    return total_words, top_words, stats

def export_results(total_words, top_words, stats):
    with open("text_analysis_results.txt", "w") as file:
        file.write("TEXT ANALYSIS REPORT\n")
        file.write("-------------------\n\n")
        
        file.write(f"Total Words: {total_words}\n\n")
        
        file.write("Top 5 Frequent Words:\n")
        for word, count in top_words:
            file.write(f"{word}: {count}\n")
        
        file.write("\nSentence Statistics:\n")
        file.write(f"Total Sentences: {stats['total_sentences']}\n")
        file.write(f"Average Sentence Length: {stats['average_length']:.2f}\n")
        file.write(f"Longest Sentence Length: {stats['max_length']}\n")
        file.write(f"Shortest Sentence Length: {stats['min_length']}\n")
        
if __name__ == "__main__":
    paragraph = input("Enter a paragraph:\n")
    
    total_words, top_words, stats = analyze_text(paragraph)
    export_results(total_words, top_words, stats)
    
    print("Text analysis complete!")
    print("Results saved to 'text_analysis_results.txt'")
