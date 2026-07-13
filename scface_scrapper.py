import os
import zipfile
import shutil

# --- CONFIGURATION ---
os.environ['KAGGLE_USERNAME'] = "your_kagle_username" ## please enter kaggle username here
os.environ['KAGGLE_KEY'] = "your_kaggle_api_key" ## please enter kaggle api key here

DATASET_ID = "yazkarajih/scface"
BASE_DIR = "face_dataset_ingestion"
TEMP_DIR = os.path.join(BASE_DIR, "temp_extraction")
FINAL_DIR = os.path.join(BASE_DIR, "scface_identities")

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(FINAL_DIR, exist_ok=True)

def ingest_and_restructure_scface():
    print("Connecting to public Kaggle Surveillance Mirror...")
    
    try:
        import kaggle
        # Step 1: Download zip array directly via API
        kaggle.api.dataset_download_files(DATASET_ID, path=TEMP_DIR, unzip=True)
        print("\n[DOWNLOAD COMPLETE] Re-architecting data layout into distinct identity directories...")
        
        file_count = 0
        # Step 2: Traverse the temporary folders to locate the surveillance images
        for root, dirs, files in os.walk(TEMP_DIR):
            for file in files:
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    # SCface files are systematically prefixed by ID (e.g., '001_cam1.jpg')
                    parts = file.split('_')
                    prefix = parts[0]
                    
                    if prefix.isdigit() and len(prefix) == 3:
                        identity_folder = os.path.join(FINAL_DIR, f"identity_{prefix}")
                        os.makedirs(identity_folder, exist_ok=True)
                        
                        # Move the multi-angle image straight into its unique identity folder
                        src_path = os.path.join(root, file)
                        dest_path = os.path.join(identity_folder, file)
                        
                        shutil.move(src_path, dest_path)
                        file_count += 1
                        
                        if file_count % 100 == 0:
                            print(f" -> Sorted {file_count} true CCTV angle frames...", end="\r")

        print(f"\n\n[SUCCESS] Custom Structural Layout Built!")
        print(f"Total files safely stored: {file_count} frames")
        print(f"Identities directory count: {len(os.listdir(FINAL_DIR))} separate individuals")
        print(f"Final Data Target Path: {os.path.abspath(FINAL_DIR)}")
        
        # Step 3: Clean up the messy temporary zip dump files
        shutil.rmtree(TEMP_DIR)
        print("[INFO] Temporary zip build files purged cleanly.")

    except Exception as e:
        print(f"\n[FATAL ERROR] Ingestion engine hit a wall: {e}")

if __name__ == "__main__":
    ingest_and_restructure_scface()