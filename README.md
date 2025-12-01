# Full Data Engineer Project

Automates downloading, cleaning, and uploading CSV files to Google Cloud Storage.

## Structure
- `scripts/` — Python scripts for data ingestion
- `infra/` — infrastructure and gcloud commands
- `sql/` — SQL transformations
- `data/` — sample data
- `credentials/` — store keys (gitignored)

## Main usage
1. Install dependencies:
   ```zsh
   pip3 install -r requirements.txt
   ```
2. Authenticate with GCP:
   - Local: `gcloud auth application-default login`
   - Production: export service account key
     ```zsh
     export GOOGLE_APPLICATION_CREDENTIALS="$PWD/credentials/csv-ingest-sa-key.json"
     ```
3. Run ingestion:
   ```zsh
   python3 scripts/download_and_upload_csv.py \
     --csv-url "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv" \
     --gcs-bucket "projeto-full-data-engineer-bucket" \
     --gcs-path "raw/titanic.csv"
   ```

The file is cleaned (empty rows removed) and uploaded to the GCS bucket.

## Security
- Never commit JSON key files.
- The `credentials/` folder is protected by `.gitignore`.
# Full Data Engineer Project

Automates downloading, cleaning, and uploading CSV files to Google Cloud Storage.

## Structure
- `scripts/` — Python scripts for data ingestion
- `infra/` — infrastructure and gcloud commands
- `sql/` — SQL transformations
- `data/` — sample data
- `credentials/` — store keys (gitignored)

## Main usage
1. Install dependencies:
   ```zsh
   pip3 install -r requirements.txt
   ```
2. Authenticate with GCP:
   - Local: `gcloud auth application-default login`
   - Production: export service account key
     ```zsh
     export GOOGLE_APPLICATION_CREDENTIALS="$PWD/credentials/csv-ingest-sa-key.json"
     ```
3. Run ingestion:
   ```zsh
   python3 scripts/download_and_upload_csv.py \
     --csv-url "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv" \
     --gcs-bucket "projeto-full-data-engineer-bucket" \
     --gcs-path "raw/titanic.csv"
   ```

The file is cleaned (empty rows removed) and uploaded to the GCS bucket.

## Security
- Never commit JSON key files.
- The `credentials/` folder is protected by `.gitignore`.
