from datetime import datetime
from decimal import Decimal
from typing import Optional
from sqlalchemy import ForeignKey, String, Numeric, Integer, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Bank(Base):
    __tablename__ = "bank"

    id: Mapped[int] = mapped_column(primary_key=True)
    total_supply: Mapped[Decimal] = mapped_column(
        Numeric(precision=20, scale=2), default=1000000
    )
    initialized: Mapped[bool] = mapped_column(Boolean, default=False)
    last_distribution: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class UserBalance(Base):
    __tablename__ = "user_balances"

    id: Mapped[int] = mapped_column(primary_key=True)
    discord_id: Mapped[str] = mapped_column(String, unique=True)
    balance: Mapped[Decimal] = mapped_column(Numeric(precision=20, scale=2), default=0)
    last_transaction: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    description: Mapped[str] = mapped_column(String)
    buy_price: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    sell_price: Mapped[Decimal] = mapped_column(Numeric(precision=10, scale=2))
    supply: Mapped[int] = mapped_column(Integer)
    max_supply: Mapped[int] = mapped_column(Integer)


class UserInventory(Base):
    __tablename__ = "user_inventories"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_balances.id"))
    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
    quantity: Mapped[int] = mapped_column(Integer, default=0)

    user: Mapped["UserBalance"] = relationship()
    item: Mapped["Item"] = relationship()
