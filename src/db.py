from dotenv import load_dotenv
import os
import snowflake.connector

load_dotenv()  # pulls values from .env into os.environ

def get_conn():
    """Return a live Snowflake connection using env-vars."""
    return snowflake.connector.connect(
        account   = os.getenv("SNOWFLAKE_ACCOUNT"),
        user      = os.getenv("SNOWFLAKE_USER"),
        password  = os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse = os.getenv("SNOWFLAKE_WAREHOUSE"),
        database  = os.getenv("SNOWFLAKE_DATABASE"),
        schema    = os.getenv("SNOWFLAKE_SCHEMA"),
    )


# --- keep everything above intact ----------------------------------

def cli() -> None:
    """Poetry script entry-point: prints the current Snowflake version."""
    cur = get_conn().cursor()
    print("Snowflake version →", cur.execute("select current_version()").fetchone()[0])
    cur.close()

