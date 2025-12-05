# Full Data Engineer Project

Automates downloading, cleaning, and uploading CSV files to Google Cloud Storage.

## Structure
- `scripts/` — Python scripts for data ingestion
- `infra/` — infrastructure and gcloud commands
- `sql/` — SQL transformations
- `data/` — sample data
- `credentials/` — store keys (gitignored)

## Quick Start

### 1️⃣ Initial Setup (after cloning)

```zsh
# Install dependencies
pip3 install -r requirements.txt

# Set up environment variables (automatic)
python setup_env.py

# Authenticate with GCP
gcloud auth application-default login
```

### 2️⃣ Run

```zsh
python3 scripts/download_and_upload_csv.py
```

## Environment Variables

The variables are loaded from `.env` (protected by `.gitignore`):

- `CSV_URL` — CSV URL to download
- `GCS_BUCKET` — GCS bucket name
- `GCS_PATH` — Path in the bucket (e.g., `raw/data.csv`)

**First time:** Run `python setup_env.py` to create `.env` from `.env.example`.

## Security
- Never commit JSON key files.
- The `credentials/` folder is protected by `.gitignore`.
- `.env` contains credentials — never commit!


