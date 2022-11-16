import demes

graph = demes.load("demes_post_model.yaml")

print(demes.to_ms(graph, N0=1000, samples=[0, 10, 100]))
