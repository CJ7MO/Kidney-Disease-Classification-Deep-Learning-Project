# Kidney-Disease-Classification-using-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/CJ7MO/Kidney-Disease-Classification-using-MLflow-DVC
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/CJ7MO/Kidney-Disease-Classification-using-MLflow-DVC.mlflow \
MLFLOW_TRACKING_USERNAME=CJ7MO \
MLFLOW_TRACKING_PASSWORD=0269ca637d03cf03e28c6dc2d7760fd4ec659d15 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/CJ7MO/Kidney-Disease-Classification-using-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=CJ7MO 

export MLFLOW_TRACKING_PASSWORD=0269ca637d03cf03e28c6dc2d7760fd4ec659d15

```