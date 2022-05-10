-- create trips table
CREATE TABLE IF NOT EXISTS tripdata (
    region VARCHAR NOT NULL,
    origin_coord geometry(Point, 4326) NOT NULL,
    destination_coord geometry(Point, 4326) NOT NULL,
    datetime timestamp NOT NULL,
    datasource VARCHAR NOT NULL);