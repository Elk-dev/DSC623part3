def insert_data(conn):
    cursor = conn.cursor()

    outlets = [
        ('O001', '12 High Street, Edinburgh, EH1 1TB',       '0131-555-0101',  '0131-555-0102'),
        ('O002', '45 Sauchiehall Street, Glasgow, G2 3AH',   '0141-555-0201',  '0141-555-0202'),
        ('O003', '8 Union Street, Aberdeen, AB10 1DQ',        '01224-555-0301', '01224-555-0302'),
        ('O004', '22 Princes Street, Dundee, DD1 4ER',        '01382-555-0401', '01382-555-0402'),
        ('O005', '5 Castle Road, Inverness, IV2 3EA',         '01463-555-0501', '01463-555-0502'),
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO OUTLET
        (OutletNumber, Address, PhoneNumber, FaxNumber)
        VALUES (?, ?, ?, ?)
    """, outlets)

    vehicles = [
        ('EH21 XYZ', 'Corsa',   'Vauxhall',  '1.2L', 5, 12000, 35.00, 'O001'),
        ('GW19 ABC', 'Focus',   'Ford',       '1.6L', 5, 23000, 40.00, 'O002'),
        ('AB18 DEF', 'Qashqai', 'Nissan',     '1.5L', 5, 45000, 55.00, 'O003'),
        ('DD20 GHI', 'Fiesta',  'Ford',       '1.0L', 5,  8000, 30.00, 'O004'),
        ('EH22 JKL', 'Golf',    'Volkswagen', '2.0L', 5, 31000, 50.00, 'O001'),
        ('GW21 MNO', 'Astra',   'Vauxhall',   '1.4L', 5, 17500, 38.00, 'O002'),
        ('AB20 PQR', 'Kuga',    'Ford',       '2.0L', 7, 52000, 60.00, 'O003'),
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO VEHICLE
        (RegistrationNumber, Model, Make, EngineSize, Capacity, CurrentMileage, DailyHireRate, OutletNumber)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, vehicles)

    staff = [
        ('S001', 'James',  'MacDonald', '10 Elm Street, Edinburgh, EH3 5TN',  '0131-555-1001',  '1985-06-15', 'M', '2010-03-01', 'Branch Manager',    42000.00, 'O001'),
        ('S002', 'Fiona',  'Campbell',  '3 Oak Avenue, Edinburgh, EH4 2PL',   '0131-555-1002',  '1990-11-22', 'F', '2015-07-14', 'Sales Advisor',      28000.00, 'O001'),
        ('S003', 'Hamish', 'Stewart',   '77 Birch Lane, Glasgow, G3 6QR',     '0141-555-1003',  '1978-04-30', 'M', '2008-01-20', 'Branch Manager',    44000.00, 'O002'),
        ('S004', 'Morag',  'Fraser',    '14 Pine Road, Glasgow, G4 9ST',      '0141-555-1004',  '1995-08-10', 'F', '2019-09-03', 'Sales Advisor',      27000.00, 'O002'),
        ('S005', 'Callum', 'Ross',      '29 Cedar Close, Aberdeen, AB11 7UV', '01224-555-1005', '1988-02-17', 'M', '2012-05-11', 'Branch Manager',    43000.00, 'O003'),
        ('S006', 'Isla',   'Murray',    '6 Maple Drive, Aberdeen, AB12 3WX',  '01224-555-1006', '1993-12-05', 'F', '2018-04-22', 'Fleet Coordinator', 31000.00, 'O003'),
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO STAFF
        (StaffNumber, FirstName, LastName, HomeAddress, HomePhoneNumber,
         DateOfBirth, Sex, DateJoined, JobTitle, Salary, OutletNumber)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, staff)

    clients = [
        ('C001', 'Robert', 'Thomson',   '55 Baker Street, Edinburgh, EH6 4YZ',  '0131-555-2001',  '1982-03-14', 'DL-100001'),
        ('C002', 'Sarah',  'Wilson',    '8 Victoria Road, Glasgow, G5 0AB',      '0141-555-2002',  '1990-07-28', 'DL-100002'),
        ('C003', 'David',  'Brown',     '33 Albert Terrace, Aberdeen, AB13 5CD', '01224-555-2003', '1975-11-03', 'DL-100003'),
        ('C004', 'Laura',  'Mitchell',  '19 George Square, Dundee, DD2 1EF',     '01382-555-2004', '1998-05-19', 'DL-100004'),
        ('C005', 'Mark',   'Henderson', '42 Queen Street, Inverness, IV3 8GH',   '01463-555-2005', '1985-09-30', 'DL-100005'),
        ('C006', 'Emma',   'Scott',     '7 King Avenue, Edinburgh, EH7 2IJ',     '0131-555-2006',  '1992-01-15', 'DL-100006'),
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO CLIENT
        (ClientNumber, FirstName, LastName, HomeAddress, PhoneNumber, DateOfBirth, DrivingLicenseNumber)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, clients)

    hire_agreements = [
        ('H001', '2024-01-10', '2024-01-15', 12000, 12350, 'C001', 'EH21 XYZ'),
        ('H002', '2024-02-05', '2024-02-10', 23000, 23480, 'C002', 'GW19 ABC'),
        ('H003', '2024-03-01', '2024-03-07', 45000, 45620, 'C003', 'AB18 DEF'),
        ('H004', '2024-04-12', '2024-04-14',  8000,  8210, 'C004', 'DD20 GHI'),
        ('H005', '2024-05-20', '2024-05-25', 31000, 31540, 'C001', 'EH22 JKL'),
        ('H006', '2024-06-01', '2026-04-30', 17500,  None, 'C005', 'GW21 MNO'),
        ('H007', '2024-06-05', '2026-04-30', 52000,  None, 'C006', 'AB20 PQR'),
    ]
    cursor.executemany("""
        INSERT OR IGNORE INTO HIRE_AGREEMENT
        (HireNumber, StartDate, EndDate, MileageBefore, MileageAfter, ClientNumber, RegistrationNumber)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, hire_agreements)

    conn.commit()
    print("Seed data inserted.")