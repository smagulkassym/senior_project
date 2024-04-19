from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DataEntry(Base):
    __tablename__ = 'data_entries'

    id = Column(Integer, primary_key=True)
    nm_525 = Column(Integer)
    nm_680 = Column(Integer)
    nm_740 = Column(Integer)
    nm_980 = Column(Integer)
    nm_1450 = Column(Integer)
    nm_525_amb = Column(Integer)
    nm_680_amb = Column(Integer)
    nm_740_amb = Column(Integer)
    nm_980_amb = Column(Integer)
    nm_1450_amb = Column(Integer)
    longitude = Column(Float)
    latitude = Column(Float)
    tree_pos = Column(String)

    def __repr__(self):
        return f"<DataEntry(id={self.id}, nm_525={self.nm_525}, longitude={self.longitude}, latitude={self.latitude}, tree_pos={self.tree_pos})>"
