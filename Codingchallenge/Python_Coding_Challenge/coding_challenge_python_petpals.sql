create database petpals;

use petpals

SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'pets';

INSERT INTO pets (Name, Age, Breed, Type, Extra)
VALUES 
('Shinzo', 10, 'Labrador', 'Dog', 'Golden Retriever'),
('Luna', 5, 'Siamese', 'Cat', 'White'),
('Max', 7, 'Beagle', 'Dog', 'Tri-color');

SELECT * FROM pets;

CREATE TABLE Pets (
    PetID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT NOT NULL CHECK (Age > 0),
    Breed VARCHAR(100),
    Type VARCHAR(50), -- 'Dog' or 'Cat'
    Extra VARCHAR(100) -- DogBreed or CatColor
);


CREATE TABLE Donations (
    DonationID INT IDENTITY(1,1) PRIMARY KEY,
    DonorName VARCHAR(100) NOT NULL,
    Amount DECIMAL(10,2) CHECK (Amount >= 10),
    DonationDate DATETIME,
    ItemType VARCHAR(100),
    Type VARCHAR(50) -- 'Cash' or 'Item'
);
select * from Donations;

CREATE TABLE Adoption_Events (
    EventID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Date DATETIME
);

INSERT INTO Adoption_Events (Name, Date)
VALUES ('Summer Adoption Drive', '2025-06-15 10:00:00');

CREATE TABLE Participants (
    ParticipantID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    EventID INT,
    FOREIGN KEY (EventID) REFERENCES Adoption_Events(EventID)
);
select * from Participants;