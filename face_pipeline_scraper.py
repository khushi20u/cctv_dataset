import os
import zipfile

# --- CONFIGURATION ---
os.environ['KAGGLE_USERNAME'] = "YOUR_KAGGLE_USERNAME_HERE"
os.environ['KAGGLE_KEY'] = "Your kaggle api key"

# Define the new high-resolution datasets to ingest
DATASETS = {
    "choke_point": "danukatheja/choke-point"
}

BASE_DIR = "face_dataset_ingestion"

def ingest_dataset(dataset_name, dataset_id):
    target_dir = os.path.join(BASE_DIR, dataset_name)
    os.makedirs(target_dir, exist_ok=True)
    
    print(f"\n--- Ingesting {dataset_name} ({dataset_id}) ---")
    try:
        import kaggle
        # Download payload
        kaggle.api.dataset_download_files(dataset_id, path=target_dir, unzip=True)
        print(f"[SUCCESS] {dataset_name} extracted safely to: {target_dir}")
    except Exception as e:
        print(f"[ERROR] Failed to pull {dataset_name}: {e}")

if __name__ == "__main__":
    for name, d_id in DATASETS.items():
        ingest_dataset(name, d_id)
