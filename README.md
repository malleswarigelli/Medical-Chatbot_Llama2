# End to End Medical-Chatbot using Llama2


## How to run?

```bash
conda create -n medchat python=3.8 -y
```

```bash
conda activate medchat
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```


# Download the quantize model from the link provided in model folder & keep the model in the model directory:
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
# run the following command
python store_index.py