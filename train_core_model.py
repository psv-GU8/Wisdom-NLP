from rasa_core.policies import FallbackPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.agent import Agent

fallback = FallbackPolicy(fallback_action_name='utter_unclear', core_threshold=0.2, nlu_threshold=0.6)
agent = Agent('domain.yml', policies=[fallback, MemoizationPolicy(), KerasPolicy()])
training_data = agent.load_data('./data/stories.md')
agent.train(training_data)
agent.persist('./models/dialouge')
