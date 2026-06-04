import pandas as pd
from sqlalchemy import create_engine

# SQLite DB
engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

datasets = {
    "fund_master":
        "data/processed/fund_master_clean.csv",

    "nav_history":
        "data/processed/nav_history_clean.csv",

    "investor_transactions":
        "data/processed/investor_transactions_clean.csv",

    "scheme_performance":
        "data/processed/scheme_performance_clean.csv",

    "aum_by_fund_house":
        "data/processed/aum_by_fund_house_clean.csv",

    "monthly_sip_inflows":
        "data/processed/monthly_sip_inflows_clean.csv",

    "category_inflows":
        "data/processed/category_inflows_clean.csv",

    "industry_folio_count":
        "data/processed/industry_folio_count_clean.csv",

    "portfolio_holdings":
        "data/processed/portfolio_holdings_clean.csv",

    "benchmark_indices":
        "data/processed/benchmark_indices_clean.csv"
}

for table_name, file_path in datasets.items():

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists='replace',
        index=False
    )

    print(f"✓ {table_name} loaded")

    from sqlalchemy import inspect
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

inspector = inspect(engine)

print(
    inspector.get_table_names()
)

import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "bluestock_mf.db"
)

for table_name, file_path in datasets.items():

    csv_rows = len(
        pd.read_csv(file_path)
    )

    db_rows = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table_name}",
        conn
    )['cnt'][0]

    print(
        f"{table_name}: CSV={csv_rows}, DB={db_rows}"
    )