"""
Reusable Snowflake connection helper.

Usage
-----
>>> from snowflake_connection import get_connection
>>> with get_connection() as conn:
...     cur = conn.cursor()
...     print(cur.execute("SELECT current_version()").fetchone()[0])
"""

from __future__ import annotations
import os
from contextlib import contextmanager

import snowflake.connector
from dotenv import load_dotenv

# Load variables from .env (if present)
load_dotenv()

def _kwargs() -> dict:
    """Collect connection parameters from environment variables."""
    try:
        return {
            "account":   os.environ["SNOWFLAKE_ACCOUNT"],
            "user":      os.environ["SNOWFLAKE_USER"],
            "password":  os.environ.get("SNOWFLAKE_PASSWORD", ""),
            "role":      os.environ.get("SNOWFLAKE_ROLE", "PUBLIC"),
            "warehouse": os.environ.get("SNOWFLAKE_WAREHOUSE", "COMPUTE_XS"),
            "database":  os.environ.get("SNOWFLAKE_DATABASE", "DEV"),
            "schema":    os.environ.get("SNOWFLAKE_SCHEMA", "PUBLIC"),
        }
    except KeyError as err:
        missing = err.args[0]
        raise RuntimeError(
            f"Missing required env var '{missing}'. "
            "Did you copy `.env.template` to `.env`?"
        ) from None

@contextmanager
def get_connection():
    """Yield an open Snowflake connection and close it automatically."""
    ctx = snowflake.connector.connect(**_kwargs())
    try:
        yield ctx
    finally:
        ctx.close()
