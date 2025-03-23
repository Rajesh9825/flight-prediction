from huggingface_hub import HfApi

# Replace with your Hugging Face username and repository name
repo_id = "CV-Raju/flight-price-prediction-model"

api = HfApi()
api.upload_file(
    path_or_fileobj="artifacts/model.pkl",  # Local file
    path_in_repo="model.pkl",  # Name in HF repo
    repo_id=repo_id,
    repo_type="model"  # Make sure it's a "model" repo
)

print(f"Model uploaded to https://huggingface.co/{repo_id}")
