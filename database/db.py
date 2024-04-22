from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DataEntry(Base):
    __tablename__ = 'data_entries'

    id = Column(Integer, primary_key=True)
    nm_365 = Column(Integer)
    nm_365_amb = Column(Integer)
    nm_405 = Column(Integer)
    nm_405_amb = Column(Integer)
    nm_525 = Column(Integer)
    nm_525_amb = Column(Integer)
    nm_680 = Column(Integer)
    nm_680_amb = Column(Integer)
    nm_740 = Column(Integer)
    nm_740_amb = Column(Integer)
    nm_980 = Column(Integer)
    nm_980_amb = Column(Integer)
    nm_1450 = Column(Integer)
    nm_1450_amb = Column(Integer)
    nm_0 = Column(Integer)
    nm_0_amb = Column(Integer)
    longitude = Column(Float)
    latitude = Column(Float)
    tree_pos = Column(String)

    def __repr__(self):
        # return f"<DataEntry(id={self.id}, nm_365 = {self.nm_365}, nm_365_amb = {self.nm_365_amb}, nm_405 = {self.nm_405}, nm_405_amb = {self.nm_405_amb}, nm_525={self.nm_525}, nm_525_amb={self.nm_525_amb}, nm_680={self.nm_680}, nm_680_amb={self.nm_680_amb}, nm_740={self.nm_740}, nm_740_amb={self.nm_740_amb}, nm_980={self.nm_980}, nm_980_amb={self.nm_980_amb}, nm_1450={self.nm_1450}, nm_1450_amb={self.nm_1450_amb}, nm_0={self.nm_0}, nm_0_amb={self.nm_0_amb}, longitude={self.longitude}, latitude={self.latitude}, tree_pos={self.tree_pos})>"
        # return f"<DataEntry(id={self.id}, nm_365 = {self.nm_365}, nm_405 = {self.nm_405}, nm_525={self.nm_525}, nm_680={self.nm_680},nm_740={self.nm_740},nm_980 = {self.nm_980}, nm_1450 = {self.nm_1450},nm_0 = {self.nm_0}, nm_365_amb = {self.nm_365_amb}, nm_405_amb = {self.nm_405_amb}, nm_525_amb={self.nm_525_amb}, nm_680_amb={self.nm_680_amb},nm_740_amb={self.nm_740_amb},nm_980_amb = {self.nm_980_amb}, nm_1450_amb = {self.nm_1450_amb},nm_0_amb = {self.nm_0_amb},  longitude={self.longitude}, latitude={self.latitude}, tree_pos={self.tree_pos})>"
        return f"<DataEntry(id={self.id}, nm_525={self.nm_525}, longitude={self.longitude}, latitude={self.latitude}, tree_pos={self.tree_pos})>"
