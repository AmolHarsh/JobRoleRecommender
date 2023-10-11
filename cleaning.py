#%%
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import rake 
from rake_nltk import Rake

data = pd.read_excel("/Users/sumeetvijaywargiya/Downloads/about_datascience.xlsx")
data.head()

# Initialize the WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# List of stopwords
stop_words = set(stopwords.words('english'))

#%%

def clean_text(text):
    
    if not isinstance(text, str):
        return text
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    print(text)
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove extra white spaces
    text = text.strip()
    text = re.sub(' +', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    # Remove stopwords and lemmatize
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    final = ' '.join(tokens)
    return final

# Apply the cleaning function to the 'about' column
#%%
about_array = data["about"].values
# cleaned = []
# for text in about_array:
#     temp = clean_text(text)
#     cleaned.append(temp)

# %%
temp = clean_text(about_array[1])
print(temp)
r = Rake()

# %%
final = r.extract_keywords_from_text(temp)

# %%
