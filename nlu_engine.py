import io
import json

from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

nlu_engine = SnipsNLUEngine(config=CONFIG_EN)

with io.open("dataset.json", 'r') as f:
    dataset = json.load(f)

nlu_engine.fit(dataset)


