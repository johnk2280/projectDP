from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Float
)

from datetime import datetime

Base = declarative_base()


class Organizations(Base):
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    full_name = Column(String, unique=True, nullable=False)
    short_name = Column(String, unique=True, nullable=False)
    inn = Column(Integer, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)


class Contractors(Base):
    __tablename__ = 'contractors'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    full_name = Column(String, unique=True, nullable=False)
    short_name = Column(String, unique=True, nullable=False)
    inn = Column(Integer, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)


class Builders(Base):
    __tablename__ = 'builders'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    full_name = Column(String, unique=True, nullable=False)
    short_name = Column(String, unique=True, nullable=False)
    inn = Column(Integer, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)


class Projects(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, unique=True,  nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    organization = relationship('Organizations', backref='projects')
    created_at = Column(DateTime, default=datetime.now(), nullable=False)


class WorkPacks(Base):
    __tablename__ = 'work_packs'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)


class Contracts(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    organization = relationship('Organizations', backref='contracts')
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    project = relationship('Projects', backref='contracts')
    contractor_id = Column(Integer, ForeignKey('contractors.id'), nullable=False)
    contractor = relationship('Contractors', backref='contracts')
    from_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)


class Specs(Base):
    __tablename__ = 'specs'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    contract_id = Column(Integer, ForeignKey('contracts.id'), nullable=False)
    contract = relationship('Contracts', backref='specs')
    work_pack_id = Column(Integer, ForeignKey('work_packs.id'), nullable=False)
    work_pack = relationship('WorkPacks', backref='specs')
    from_date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)


class MechanismTypes(Base):
    __tablename__ = 'mechanism_types'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)


class Services(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    mechanism_type_id = Column(Integer, ForeignKey('mechanism_types.id'), nullable=False)
    mechanism_type = relationship('MechanismTypes')
    created_at = Column(DateTime, default=datetime.now(), nullable=False)


class Applications(Base):
    __tablename__ = 'applications'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    from_date = Column(DateTime, nullable=False)
    to_date = Column(DateTime, nullable=False)
    organization_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    organization = relationship('Organizations', backref='applications')
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    project = relationship('Projects', backref='applications')
    contract_id = Column(Integer, ForeignKey('contracts.id'), nullable=False)
    contract = relationship('Contracts', backref='applications')
    work_pack_id = Column(Integer, ForeignKey('work_packs.id'), nullable=False)
    work_pack = relationship('WorkPacks', backref='applications')
    mechanism_type_id = Column(Integer, ForeignKey('mechanism_types.id'), nullable=False)
    mechanism_type = relationship('MechanismTypes', backref='applications')
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    service = relationship('Services', backref='applications')
    builder_id = Column(Integer, ForeignKey('builders.id'), nullable=False)
    builder = relationship('Builders', backref='applications')
    responsible = Column(String, nullable=True)
    is_deleted = Column(Boolean, default=0, nullable=False)

    def __init__(self, **kwargs):
        self.from_date = kwargs['from_date']
        self.to_date = kwargs['to_date']
        self.organization_id = kwargs['organization_id']
        self.project_id = kwargs['project_id']
        self.contract_id = kwargs['contract_id']
        self.work_pack_id = kwargs['work_pack_id']
        self.mechanism_type_id = kwargs['mechanism_type_id']
        self.service_id = kwargs['service_id']
        self.builder_id = kwargs['builder_id']
        self.responsible = kwargs['responsible']


