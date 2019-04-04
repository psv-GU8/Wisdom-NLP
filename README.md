# A Chatbot based on RASA Stack (NLU + Core)

The current repo is a module developed for my WISDOM chatbot project. This module is termed as the "NLP Module" in the architecture design of my WISDOM Project. The NLP module is the core module that interacts with several other modules such as the "Scrapping Module" , "ML Module", "DB Module" and the Flask Server. The NLP Module is built using the RASA Stack (RASA NLU + RASA Core ).

## The RASA Stack

The Rasa stack is a set of open source machine learning tools for us developers to create contextual chat/voice based assistants..... [Know more](https://rasa.com/)

* NLU = a library for natural language understanding with intent classification and entity extraction
* Core = a chatbot framework with machine learning-based dialogue management

### Directory Structure
```
|-(+)-config
|  |-config.yml
|  
|-(+)-data
|  |-nlu_train.md
|  |-stories.md
|
|-(+)-helper
|-(+)-models
|  |-(+)-dialouge
|  |-(+)-nlu
|
|-(+)-test
|  |-test_core_model.py
|  |-test_nlu_model.py
|
|-(+)-train
|  |-train_core_model.py
|  |-train_nlu_model.py
|
|-actions.py
|-domain.yml
|-README.md
```

### Dependencies

- python==3.6
- spacy en model
- jsonpickle==1.0.0
- six==1.11.0
- redis==2.10.6
- fakeredis==0.10.3
- future==0.17.1
- numpy~=1.16.0
- typing==3.6.6
- ruamel.yaml==0.15.85
- requests~=2.2
- tensorflow==1.12.0
- h5py==2.7.1
- apscheduler==3.5.1
- tqdm==4.29.1
- ConfigArgParse==0.13.0
- networkx==2.2
- pykwalify==1.7.0
- coloredlogs==10.0
- flask==1.0.2
- flask_cors==3.0.7
- scikit-learn==0.20.2
- rasa_nlu~=0.14.6
- colorhash==1.0.2
- pika==0.12.0
- jsonschema==2.6.0
- packaging~=18.0
- gevent==1.4
- pytz==2018.9
- rasa-core-sdk~=0.12.2
- rasa_core~=0.13.2
- pymongo==3.7.2
- python-dateutil==2.7.5
- spacy~=2.0.18
- sklearn_crfsuite==0.3.6
- keras-applications==1.0.6
- keras-preprocessing==1.0.5

### Installation 

```
**NOTE**: I highly recommend that you first create a virtual environment and then install the dependencies. I'd suggest you to create venv using conda, set python version to 3.6 and then pip install the dependencies.

```

1. clone the repo and cd into the cloned directory.
2. install all the dependencies in requirement.
``` pip install -r requirements.txt ```
3. test the installation using the ./helper/inspect_rasa_version.py
4. use files in ./train to train the nlu model and the dialouge management model accordingly.
5. use the files in ./test to test trained models accordingly.
