import sqlite3

def create_tables(conn):
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS OUTLET (
            OutletNumber    TEXT PRIMARY KEY NOT NULL,
            Address         TEXT NOT NULL,
            PhoneNumber     TEXT NOT NULL,
            FaxNumber       TEXT NOT NULL,
            CHECK (PhoneNumber != FaxNumber)
        );

        CREATE TABLE IF NOT EXISTS VEHICLE (
            RegistrationNumber  TEXT PRIMARY KEY NOT NULL,
            Model               TEXT NOT NULL,
            Make                TEXT NOT NULL,
            EngineSize          TEXT NOT NULL,
            Capacity            INTEGER NOT NULL CHECK (Capacity >= 1),
            CurrentMileage      INTEGER NOT NULL CHECK (CurrentMileage >= 0),
            DailyHireRate       REAL NOT NULL CHECK (DailyHireRate > 0),
            OutletNumber        TEXT NOT NULL,
            FOREIGN KEY (OutletNumber) REFERENCES OUTLET(OutletNumber)
                ON DELETE RESTRICT ON UPDATE CASCADE
        );

        CREATE TABLE IF NOT EXISTS STAFF (
            StaffNumber         TEXT PRIMARY KEY NOT NULL,
            FirstName           TEXT NOT NULL,
            LastName            TEXT NOT NULL,
            HomeAddress         TEXT NOT NULL,
            HomePhoneNumber     TEXT NOT NULL,
            DateOfBirth         DATE NOT NULL,
            Sex                 TEXT NOT NULL CHECK (Sex IN ('M', 'F', 'O')),
            DateJoined          DATE NOT NULL,
            JobTitle            TEXT NOT NULL,
            Salary              REAL NOT NULL CHECK (Salary > 0),
            OutletNumber        TEXT NOT NULL,
            FOREIGN KEY (OutletNumber) REFERENCES OUTLET(OutletNumber)
                ON DELETE RESTRICT ON UPDATE CASCADE
        );

        CREATE TABLE IF NOT EXISTS CLIENT (
            ClientNumber            TEXT PRIMARY KEY NOT NULL,
            FirstName               TEXT NOT NULL,
            LastName                TEXT NOT NULL,
            HomeAddress             TEXT NOT NULL,
            PhoneNumber             TEXT NOT NULL,
            DateOfBirth             DATE NOT NULL,
            DrivingLicenseNumber    TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS HIRE_AGREEMENT (
            HireNumber          TEXT PRIMARY KEY NOT NULL,
            StartDate           DATE NOT NULL,
            EndDate             DATE NOT NULL,
            MileageBefore       INTEGER NOT NULL CHECK (MileageBefore >= 0),
            MileageAfter        INTEGER CHECK (MileageAfter >= MileageBefore),
            ClientNumber        TEXT NOT NULL,
            RegistrationNumber  TEXT NOT NULL,
            CHECK (EndDate >= StartDate),
            FOREIGN KEY (ClientNumber) REFERENCES CLIENT(ClientNumber)
                ON DELETE RESTRICT ON UPDATE CASCADE,
            FOREIGN KEY (RegistrationNumber) REFERENCES VEHICLE(RegistrationNumber)
                ON DELETE RESTRICT ON UPDATE CASCADE
        );
    """)
    conn.commit()
    print("Tables created.")