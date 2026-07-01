from app.db.base import Base

from app.db.session import engine


def init_database():

    Base.metadata.create_all(

        bind=engine

    )


if __name__ == "__main__":

    init_database()

    print(

        "All database tables created."

    )

    