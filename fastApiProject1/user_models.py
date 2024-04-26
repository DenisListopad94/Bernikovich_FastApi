__all__ = ("User")

from uuid import UUID

from enums import UserRole, PaymentStatus
from sqlalchemy import Column, ForeignKey, DateTime, Enum, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func

from core_models import str_30
from .base_model import Base


class User(Base):


    first_name: Mapped[str_30] = mapped_column(nullable=True)
last_name: Mapped[str_30] = mapped_column(nullable=True)
role: Mapped[UserRole] = mapped_column(nullable=True)
created_at: Mapped[created_at]
updated_at: Mapped[updated_at]
booking: Mapped[list["Booking"]] = relationship("Booking", back_populates="user")


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'public'}

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False,
                server_default=func.uuid_generate_v4())
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    role = Column(Enum(UserRole), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    booking = relationship("Booking", back_populates="user")


class Booking(Base):
    __tablename__ = 'booking'
    __table_args__ = {'schema': 'public'}

    confirmation_id = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False,
                             server_default=func.uuid_generate_v4())
    description = Column(String(300), nullable=True)
    created_at = Column(DateTime, default=func.now())
    payment_status = Column(Enum(PaymentStatus), nullable=True)
    payment_time = Column(DateTime, nullable=True)

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id', ondelete="CASCADE"))
    user = relationship("User", back_populates="booking")
