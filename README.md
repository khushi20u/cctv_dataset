# High-Resolution CCTV Surveillance Dataset Ingestion Pipeline

This repository hosts the automated data ingestion engine and structural framework designed to support multi-object face tracking and identification pipelines. 

---

## Dataset Profiles

### 1. The ChokePoint Dataset (Portal Entryway Tracking)
* **Spatial Resolution:** Raw, uncompressed frames calibrated to a sharp **$96 \times 96$ pixels**.
* **Vantage Profile:** Captures natural facial panning, dynamic head tilts, and multi-angle facial transitions as subjects walk through real-world, narrow security portal choke points.
* **Pipeline Value:** Ideal for testing geometric consistency and temporal tracking continuous frames.

### 2. The SCface Database (Surveillance Camera Face Array)
* **Structural Formatting:** Re-architected into **130 distinct identity subdirectories** (`identity_001` through `identity_130`) to support classification and face matching.
* **Various Look-Angles:** Each subject features multi-view face captures.
* **Environmental Variance:** Includes standard daylight surveillance frames alongside **Infrared captures** to test pipeline robustness under challenging lighting environments.

---

## Repository Structure

```text
cctv_surveillance_dataset/
├── face_dataset_ingestion/ 
│   ├── choke_point/  
│   └── scface_identities/      
├── face_pipeline_scrapper.py      
├── scface_scrapper.py        
└── README.md                   # System documentation and dataset catalog
