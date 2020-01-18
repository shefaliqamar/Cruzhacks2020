
import numpy as np
from scipy import spatial
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE







def find_closest_embeddings(embedding):
 return sorted(embeddings_dict.keys(),
               key=lambda word: spatial.distance.euclidean(embeddings_dict[word], embedding))


embeddings_dict = {}
with open("glove.6B.50d.txt", 'r') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], "float32")
        embeddings_dict[word] = vector

    # print(find_closest_embeddings(embeddings_dict["king"])[0:5])
    # print(spatial.distance.euclidean(embeddings_dict["king"], embeddings_dict["liberal"]))
    # print(spatial.distance.euclidean(embeddings_dict["president"], embeddings_dict["liberal"]))
    # print(spatial.distance.euclidean(embeddings_dict["queen"], embeddings_dict["liberal"]))
    # print(spatial.distance.euclidean(embeddings_dict["president"], embeddings_dict["republican"]))
    lines = ["Hello this is a tutorial on how to convert the word in an integer format",
             "this is a beautiful day", "Jack is going to office", "war war war"]

    new_lines = []
    for line in lines:
        split_line = line.split(" ")  # new lines has the new format lines=new_lines
        new_lines.append(split_line)

    print(new_lines)
    linenum = 0
    for line in new_lines:
        linenum += 1
        lineLiberalScore = 0
        lineConservativeScore = 0
        for word in line:
            lineLiberalScore += spatial.distance.euclidean(embeddings_dict[word.lower()], embeddings_dict["liberal"])
            print(str(embeddings_dict[word.lower()]))
            lineConservativeScore += spatial.distance.euclidean(embeddings_dict[word.lower()], embeddings_dict["conservative"])
        print("For line: " + str(linenum) + " \nLiberalScore: " + str(lineLiberalScore) + "\n ConservativeScore: " + str(lineConservativeScore))
