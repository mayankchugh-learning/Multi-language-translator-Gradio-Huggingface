# Multi-language-translator-Gradio-Huggingface

### STEPS:
## How to run? 
### STEP 01- Create a conda environment after opening the repository
```bash
conda create -p multilangTranslatorVenv python -y
```

```bash
source activate ./multilangTranslatorVenv
```
```bash
conda activate /Users/mayankchugh/gitRepos/mayankchugh.learning/Multi-language-translator-Gradio-Huggingface/multilangTranslatorVenv
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- run application
```bash
Python app.py
```

##### after download move the model to code folder
```
cd /Users/mayankchugh/.cache/huggingface/hub/

ls /Users/mayankchugh/.cache/huggingface/hub/
```
###### copy your downloaded model name and path and paste it below (it already pasted for my workspace)
```bash 
sudo mv /Users/mayankchugh/.cache/huggingface/hub/models--facebook--nllb-200-distilled-600M /Users/mayankchugh/gitRepos/mayankchugh.learning/Multi-language-translator-Gradio-Huggingface/Model/models--facebook--nllb-200-distilled-600M
```

#### github Facebook link
[GitHub Facebook documentation link](https://github.com/facebookresearch/flores/blob/main/flores200/README.md)


[Gradio documentation link](https://www.gradio.app/docs/gradio/file)