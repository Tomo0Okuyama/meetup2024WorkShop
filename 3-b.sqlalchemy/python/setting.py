from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# 接続先DBのURL設定
DATABASE = 'iris://_system:minamoto@localhost:51774/USER'

# Engine の作成
Engine = create_engine(
  DATABASE,
  echo=False
)

# Sessionの作成
session = scoped_session(
  # ORM実行時の設定
  sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = Engine
  )
)

# modelに必要な基底クラスの設定
Base = declarative_base()
Base.query = session.query_property()