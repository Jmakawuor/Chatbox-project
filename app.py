import streamlit as st
import string

# Basic stopword list
basic_stopwords = {
    'a', 'an', 'the', 'and', 'or', 'but', 'if', 'while', 'to', 'of', 'in', 'on',
    'for', 'with', 'as', 'by', 'at', 'from', 'is', 'are', 'was', 'were', 'be', 'been',
    'being', 'have', 'has', 'had', 'do', 'does', 'did', 'so', 'that', 'this', 'these', 'those',
    'i', 'you', 'he', 'she', 'it', 'we', 'they', 'them', 'me', 'my', 'your', 'his', 'her',
    'its', 'our', 'their', 'not', 'no', 'yes'
}

# Preprocessing function (no nltk)
def preprocess(text):
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    cleaned_sentences = []

    for sentence in sentences:
        words = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split()
        words = [word for word in words if word not in basic_stopwords]
        cleaned_sentences.append(" ".join(words))

    return sentences, cleaned_sentences

# Streamlit app
def main():
    st.title("Basic Text Preprocessing App (No NLTK)")

    sample_text = """“There are some peaches worth eating,” said Lon Trustleton to his two
companions, as they passed an orchard of this delicious fruit on the
river road, as it was called.

“Them’s tip-top,” added Matthew Swikes: “I go for havin’ some on ’em.”

“So I say,” replied Lon; and he leaped over the fence, followed by
Matt. “Come along, Wade.”

“No: I’m not going to steal anybody’s peaches,” answered Wade Brooks.

“Oh, come along!” called Lon, the son of the rich Captain Trustleton,
who lived on the hill near the village of Midhampton.

“No: I won’t have any thing to do with the scrape. Besides, I have to
go on an errand to the village,” said Wade.

“See here, Wade Brooks, if you don’t come over here, I’ll break your
skull,” continued Lon Trustleton, shaking his head to emphasize his
words.

“What for? for not stealing peaches?” added Wade, with a smile at the
absurdity of the idea.

“You want to set up for a goody; and when any thing is said about
hooking peaches, you blow on Matt and me, that’s the way of it; and if
you don’t come over here I’ll go over there--that’s all.”
"""

    text_input = st.text_area("Enter text to preprocess:", sample_text, height=300)

    if st.button("Preprocess"):
        original, cleaned = preprocess(text_input)

        st.subheader("Original Sentences:")
        for i, sent in enumerate(original, 1):
            st.write(f"{i}. {sent}")

        st.subheader("Cleaned Sentences:")
        for i, sent in enumerate(cleaned, 1):
            st.write(f"{i}. {sent}")

if __name__ == "__main__":
    main()

# NOTE:
# This is a temporary preprocessing method used due to NLTK resource loading issues.
# Replaces nltk.sent_tokenize and nltk.stopwords with simple Python-based logic.
# Intended original functions:
#   from nltk.tokenize import sent_tokenize, word_tokenize
#   from nltk.corpus import stopwords
