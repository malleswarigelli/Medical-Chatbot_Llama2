# End to End Medical-Chatbot using Llama2


## How to run?

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```



## Download the Llama 2 Model:
- llama-2-7b-chat.ggmlv3.q4_0.bin

- Download the quantize model from the link below to model folder & keep the model in the model directory:
- https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main

## create `.env` file to store Pinecone credentials
```
PINECONE_API_KEY= "YOUR_PINECONE_API_KEY"
PINECONE_API_ENV= "YOUR PINECONE CLOUD ENV"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

pass them as environment variables
```
### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```



# run the following command
python store_index.py

# Techstack used
- programming language: python
- Generative AI framework: Langchain
- Front end/ Web app: flask
- LLM: meta llama2
- Vector DB: Pinecone
