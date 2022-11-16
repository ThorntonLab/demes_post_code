import matplotlib.pyplot as plt

import demes
import demesdraw

graph = demes.load("demes_post_model.yaml")

tubes = demesdraw.tubes(graph)

plt.savefig("demes_post_model.png")
