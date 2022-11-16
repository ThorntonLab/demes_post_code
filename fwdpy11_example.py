import fwdpy11

# Read the model in from the YAML.
# The 1 tells fwdpy11 to generate
# a model where the ancestral population is
# evolved for N generations, where N is its initial size
model = fwdpy11.discrete_demography.from_demes("demes_post_model.yaml", 1)

print(model.asblack())
