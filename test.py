from sqlalchemy import create_engine

# SQLite উদাহরণ
engine = create_engine('sqlite:///example.db')
print(engine)
