#  Import
try:
   from urllib.request import urlopen as uReq
except ImportError:
   from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup
def generateInputs():
    toReturn = []
    #  URL - get HTTP Request later on...
    my_url = 'https://www.nytimes.com/2020/01/12/us/politics/trump-suleimani-explanations.html'
    #  opening up connection, grabbing the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    #  html parsing
    page_soup = soup(page_html, "html.parser")
    print("\n")
    print("\n")
    #  headline
    headline = page_soup.findAll("div", {"class":"css-1vkm6nb ehdk2mb0"})
    headlineText = headline[0].text
    print(headlineText)
    toReturn.append(headlineText)
    print("\n")
    print("\n")
    #  body
    body = page_soup.findAll("section", {"name": "articleBody"})
    bodyText = body[0].text
    print(bodyText)
    with open('body.txt', 'w') as bodydoc:
        bodydoc.write(bodyText)
        bodydoc.close()
    toReturn.append("body.txt")
    print("\n")
    print("\n")

    # news outlet - HARDCODED for now!
    newsOutlet = "New York Times"
    print(newsOutlet + "\n\n")
    toReturn.append(newsOutlet)
    return toReturn
# ============================================== Headline categorization ================================
import sentiment_analysis
import sent2vec
from scipy.spatial import distance
def getCategory(headline):
        model = sent2vec.Sent2vecModel()
        model.load_model('sent2vec/wiki_unigrams.bin')
        # headline = "You should protect your pets from disease."
        headline = headline.lower()
        categoryList = []

        with open('sent2vec/categories.txt', 'r') as categories:
                for line in categories:
                        if not line[0] == '\n':
                                categoryList.append(line.split("\n")[0])
        # print(str(categoryList))
        # embed headline
        emb = model.embed_sentence(headline)
        minDistCategory = None
        minDist = 1000000
        # embed categories and compare
        for i in range(len(categoryList)):
            times3category = (categoryList[i] + " ") * 3
            # print(times3category)
            # category embedding
            categoryEmb = model.embed_sentence(times3category)
            dist = distance.cosine(categoryEmb, emb)
            # print("Found cosine distance to category: " + categoryList[i] + " distance: " + str(dist))
            if dist < minDist:
                minDist = dist
                minDistCategory = categoryList[i]
        print("Category of headline: " + headline + " : " + minDistCategory)
        return minDistCategory
# ======================================== Sentiment analysis on article body =============================
# Copyright 2016, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
        # distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# [START language_sentiment_tutorial]
"""Demonstrates how to make a simple call to the Natural Language API."""
# [START language_sentiment_tutorial_imports]
import argparse
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# [END language_sentiment_tutorial_imports]
# [START language_sentiment_tutorial_print_result]
def print_result(annotations):
        score = annotations.document_sentiment.score
        magnitude = annotations.document_sentiment.magnitude
        for index, sentence in enumerate(annotations.sentences):
                sentence_sentiment = sentence.sentiment.score
                print('Sentence {} has a sentiment score of {}'.format(index, sentence_sentiment))

        print('Overall Sentiment: score of {} with magnitude of {}'.format(
            score, magnitude))
        return 0

# [END language_sentiment_tutorial_print_result]
# [START language_sentiment_tutorial_analyze_sentiment]
def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(movie_review_filename, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

        document = types.Document(content=content,
                                  type=enums.Document.Type.PLAIN_TEXT)
        annotations = client.analyze_sentiment(document=document)
        # Print the results
    return annotations
# [END language_sentiment_tutorial_analyze_sentiment]
# [START language_sentiment_tutorial_run_application]
if __name__ == '__main__':
        # parser = argparse.ArgumentParser(
        #       description=__doc__,
        #       formatter_class=argparse.RawDescriptionHelpFormatter)
        # parser.add_argument(
        #       'movie_review_filename',
        #       help='The filename of the movie review you\'d like to analyze.')
        # args = parser.parse_args()
        # annotations = analyze(args.movie_review_filename)
        inputs = generateInputs()
        annotations = analyze("body.txt")
        FINAL_CATEGORY = getCategory(inputs[0])
        FINAL_SENTIMENT_SCORE = annotations.document_sentiment.score
        FINAL_SENTIMENT_MAGNITUDE = annotations.document_sentiment.magnitude
        print(
            "Ready for neural net output generation!!!! \nGot category of headline: " + FINAL_CATEGORY + "\nGot sentiment score of article body: "
            + str(FINAL_SENTIMENT_SCORE) + "\nGot sentiment magnitude of article body: " + str(
                FINAL_SENTIMENT_MAGNITUDE))

        # Now populate training data csv with URL, Sentiment, sentiment magnitude, category, and bias.

# [END language_sentiment_tutorial_run_application]



