# main.py - Entry point to run model scripts

import argparse
from download_artifacts import run as run_download
from export_model_to_onnx import run as run_export

def main():
    parser = argparse.ArgumentParser(description="Run deployment scripts")
    parser.add_argument("--script", type=str, required=True, choices=["download", "export"])
    args = parser.parse_args()

    if args.script == "download":
        run_download()
    elif args.script == "export":
        run_export()

if __name__ == "__main__":
    main()
