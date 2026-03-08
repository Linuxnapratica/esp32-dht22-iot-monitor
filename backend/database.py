from sqlalchemy import Column, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class SensorReading(Base):
    __tablename__ = 'sensor_readings'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    temperature = Column(Float)
    humidity = Column(Float)

    def __repr__(self):
        return f"<SensorReading(timestamp={self.timestamp}, temperature={self.temperature}, humidity={self.humidity})>"

# Database setup
DATABASE_URL = 'sqlite:///sensor_readings.db'
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)