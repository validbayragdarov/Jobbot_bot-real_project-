from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy import DateTime, func, Text, BigInteger

engine = create_async_engine("postgresql+asyncpg://postgres:root@localhost:5432/localtest")
session_factory = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=True)


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=True)


class UserData(Base):
    pass


class UserInfo(Base):
    name: Mapped[str] = mapped_column(nullable=True)
    surname: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=True)
    feedback: Mapped[str] = mapped_column(Text, nullable=True)
    registered_at = mapped_column(DateTime, server_default=func.now())


class Application(Base):
    cv_photo: Mapped[str] = mapped_column(Text, nullable=True)
    text: Mapped[str] = mapped_column(Text, nullable=True)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
