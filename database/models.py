from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Table,
    Float
)

from datetime import datetime

Base = declarative_base()


class Organizations(Base):
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    inn = Column(Integer, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class Contractors(Base):
    __tablename_ = 'contractors'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    inn = Column(Integer, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class Builders(Base):
    __tablename_ = 'builders'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    inn = Column(Integer, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class Projects(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class WorkPacks(Base):
    __tablename__ = 'work_packs'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class Contracts(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    contractor_id = Column(Integer, ForeignKey('contractors.id'), nullable=False)
    from_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class Specs(Base):
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    contract_id = Column(Integer, ForeignKey('contracts.id'), nullable=False)
    work_pack_id = Column(Integer, ForeignKey('work_packs.id'), nullable=False)
    from_date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class MechanismType(Base):
    __tablename__ = 'mechanism_type'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class Services(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    mechanism_type_id = Column(Integer, ForeignKey('mechanism_type.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.now())



