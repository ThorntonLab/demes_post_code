import matplotlib.pyplot as plt

plt.style.use("rose-pine-moon")
import demes
import demesdraw


graph = demes.load("demes_post_model.yaml")

tubes = demesdraw.tubes(
    graph, colours={"ancestor": "#3e8fb0", "derived1": "#ea9a97", "derived2": "#c4a7e7"}
)

plt.savefig("demes_post_model.png")
