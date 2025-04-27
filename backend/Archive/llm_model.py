from langchain_community.llms import LlamaCpp

MODEL_PATH = "C:/Users/gaierr/gpt4all/resources/phi-2.Q4_K_M.gguf"

llm = LlamaCpp(
    model_path=MODEL_PATH,
    temperature=0.1,
    n_ctx=2048,         # Match model training
    n_batch=64,         # Avoid GGUF warning
    max_tokens=512,
    verbose=False,
)