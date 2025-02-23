from abc import abstractmethod

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session


import models as db
from schemas import Citizen, Country, President


class AbcRepository:
    @abstractmethod
    def __init__(self, session: Session):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> President | Citizen | Country:
        raise NotImplementedError


class CitizenRepository(AbcRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id: int) -> Citizen:
        db_citizen = self._session.get(db.Citizen, id)
        if db_citizen is None:
            return "No such citizen!"
        return Citizen.model_validate(db_citizen)


class CountryRepository(AbcRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id: int) -> Country:
        db_country = self._session.get(db.Country, id)
        if db_country is None:
            return "No such country!"
        return Country.model_validate(db_country)

class PresidentRepository(AbcRepository):
    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, id: int) -> President:
        db_president = self._session.get(db.President, id)
        if db_president is None:
            return "No such president!"
        return President.model_validate(db_president)