# Databricks-safe import check for src.bronze.ingestion_script_pyspark
import sys, os, importlib
from pathlib import Path

PROJECT_ROOT = "/Workspace/Users/justine.padayao@3cloudsolutions.com/.bundle/tech-summit-demo/dev/files"
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
BRONZE_DIR = os.path.join(SRC_DIR, "bronze")

# 1) Remove any accidental "src/bronze" entries (can break package-style imports)
sys.path = [p for p in sys.path if not p.rstrip("/").endswith("/src/bronze")]

# 2) Append project root and src (append, not insert)
for p in (PROJECT_ROOT, SRC_DIR):
    if p not in sys.path:
        sys.path.append(p)

print("✅ sys.path tail:")
print("\n".join(sys.path[-5:]))

# 3) Sanity checks
print("\n✅ Exists checks:")
print("PROJECT_ROOT:", os.path.isdir(PROJECT_ROOT))
print("SRC_DIR:", os.path.isdir(SRC_DIR))
print("BRONZE_DIR:", os.path.isdir(BRONZE_DIR))
print("ingestion_script_pyspark.py:",
      os.path.isfile(os.path.join(BRONZE_DIR, "ingestion_script_pyspark.py")))
