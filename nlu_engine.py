import io
import json

from snips_nlu import SnipsNLUEngine, load_resources
from snips_nlu.default_configs import CONFIG_EN

nlu_engine = SnipsNLUEngine(resources=load_resources("snips_nlu_en"))

with io.open("dataset.json", 'r') as f:
    dataset = json.load(f)

nlu_engine.fit(dataset)


