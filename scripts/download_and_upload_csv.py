import os
import sys
import argparse
import tempfile
from typing import Optional

import requests
import pandas as pd
from google.cloud import storage


def download_csv(csv_url: str) -> str:
    resp = requests.get(csv_url, timeout=60)
    resp.raise_for_status()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp_file:
        tmp_file.write(resp.content)
        return tmp_file.name


def clean_csv(raw_csv_path: str) -> str:
    df = pd.read_csv(raw_csv_path)
    mask_empty = df.isnull().all(axis=1)
    dropped = df[mask_empty]
    if not dropped.empty:
        print("Removed empty rows:")
        print(dropped)
    else:
        print("No completely empty rows were removed.")
    df_clean = df.dropna(how="all")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as clean_file:
        df_clean.to_csv(clean_file.name, index=False)
        return clean_file.name


def upload_to_gcs(bucket_name: str, gcs_path: str, local_path: str) -> str:
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(gcs_path)
    blob.upload_from_filename(local_path, content_type="text/csv")
    return f"gs://{bucket_name}/{gcs_path}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download a CSV, clean empty rows, and upload to GCS.",
    )
    parser.add_argument(
        "--csv-url",
        dest="csv_url",
        default=os.getenv("CSV_URL", "https://example.com/data.csv"),
        help="CSV URL to download (env: CSV_URL)",
    )
    parser.add_argument(
        "--gcs-bucket",
        dest="gcs_bucket",
        default=os.getenv("GCS_BUCKET", "meu-bucket"),
        help="Target GCS bucket (env: GCS_BUCKET)",
    )
    parser.add_argument(
        "--gcs-path",
        dest="gcs_path",
        default=os.getenv("GCS_PATH", "raw/data.csv"),
        help="Target object path in bucket (env: GCS_PATH)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        print(
            "Warning: GOOGLE_APPLICATION_CREDENTIALS not set. Make sure default credentials are configured.",
            file=sys.stderr,
        )

    try:
        raw_path = download_csv(args.csv_url)
        clean_path = clean_csv(raw_path)
        gcs_uri = upload_to_gcs(args.gcs_bucket, args.gcs_path, clean_path)
        print("Upload completed to:", gcs_uri)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
