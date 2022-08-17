from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Float,
    Date,
    DateTime,
    ForeignKey,
    Boolean,
)
import sqlalchemy
from connection.databases import database_url

metabase = MetaData()

Engine = Table(
    "engines",
    metabase,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True, unique=True),
)

Maker = Table(
    "makers",
    metabase,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True, unique=True),
)

Sold = Table(
    "solds",
    metabase,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True, unique=True),
)

Car = Table(
    "cars",
    metabase,
    Column("id", Integer, primary_key=True, index=True),
    Column("model", String, nullable=False),
    Column("year", Date, nullable=False),
    Column("price", Float, nullable=False),
    Column("autonomus", Boolean, nullable=False),
    Column("engine_id", ForeignKey("engines.id"), nullable=False),
    Column("maker_id", ForeignKey("makers.id"), nullable=False),
    Column("sold_id", ForeignKey("solds.id"), nullable=False),
)

engine = sqlalchemy.create_engine(database_url)
metabase.create_all(engine)
