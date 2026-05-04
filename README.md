# Reliable Rentals Database

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightblue?logo=sqlite)
![Status](https://img.shields.io/badge/DB-passing-brightgreen)
![Last Updated](https://img.shields.io/github/last-commit/Elk-dev/DSC623part3?label=Last%20Updated)

A vehicle hire management system built with Python and SQLite, implementing a full relational database schema with embedded SQL queries.

## Project Structure
- `schema/` — table creation scripts
- `seed/` — seed data insertion
- `queries/` — all 5 SQL queries
- `src/` — main entry point

## Relations
- OUTLET
- VEHICLE
- STAFF
- CLIENT
- HIRE_AGREEMENT

## How to Run Locally
```bash
python src/main.py
```

## Query Results
> Auto-updated on every push by GitHub Actions

<!-- RESULTS_START -->
```

============================================================
  Query 1 - Vehicles at Edinburgh (O001)
============================================================

SQL:

        SELECT
            v.RegistrationNumber,
            v.Make,
            v.Model,
            v.EngineSize,
            v.Capacity,
            v.DailyHireRate
        FROM VEHICLE v
        JOIN OUTLET o ON v.OutletNumber = o.OutletNumber
        WHERE o.OutletNumber = 'O001'
    

Results:
  RegistrationNumber | Make       | Model | EngineSize | Capacity | DailyHireRate
  -------------------------------------------------------------------------------
  EH21 XYZ           | Vauxhall   | Corsa | 1.2L       | 5        | 35.0         
  EH22 JKL           | Volkswagen | Golf  | 2.0L       | 5        | 50.0         

============================================================
  Query 2 - Hire history for Client C001 (Robert Thomson)
============================================================

SQL:

        SELECT
            h.HireNumber,
            h.StartDate,
            h.EndDate,
            h.MileageBefore,
            h.MileageAfter,
            v.Make,
            v.Model,
            v.RegistrationNumber
        FROM HIRE_AGREEMENT h
        JOIN CLIENT c ON h.ClientNumber = c.ClientNumber
        JOIN VEHICLE v ON h.RegistrationNumber = v.RegistrationNumber
        WHERE c.ClientNumber = 'C001'
    

Results:
  HireNumber | StartDate  | EndDate    | MileageBefore | MileageAfter | Make       | Model | RegistrationNumber
  -------------------------------------------------------------------------------------------------------------
  H001       | 2024-01-10 | 2024-01-15 | 12000         | 12350        | Vauxhall   | Corsa | EH21 XYZ          
  H005       | 2024-05-20 | 2024-05-25 | 31000         | 31540        | Volkswagen | Golf  | EH22 JKL          

============================================================
  Query 3 - Staff at Glasgow (O002)
============================================================

SQL:

        SELECT
            s.StaffNumber,
            s.FirstName,
            s.LastName,
            s.JobTitle,
            s.Salary
        FROM STAFF s
        JOIN OUTLET o ON s.OutletNumber = o.OutletNumber
        WHERE o.OutletNumber = 'O002'
    

Results:
  StaffNumber | FirstName | LastName | JobTitle       | Salary 
  -------------------------------------------------------------
  S003        | Hamish    | Stewart  | Branch Manager | 44000.0
  S004        | Morag     | Fraser   | Sales Advisor  | 27000.0

============================================================
  Query 4 - Mileage driven on Hire H003
============================================================

SQL:

        SELECT
            h.HireNumber,
            h.MileageBefore,
            h.MileageAfter,
            (h.MileageAfter - h.MileageBefore) AS MileageDriven,
            c.FirstName,
            c.LastName,
            c.PhoneNumber,
            v.Make,
            v.Model,
            v.EngineSize
        FROM HIRE_AGREEMENT h
        JOIN CLIENT c ON h.ClientNumber = c.ClientNumber
        JOIN VEHICLE v ON h.RegistrationNumber = v.RegistrationNumber
        WHERE h.HireNumber = 'H003'
        AND h.MileageAfter IS NOT NULL
    

Results:
  HireNumber | MileageBefore | MileageAfter | MileageDriven | FirstName | LastName | PhoneNumber    | Make   | Model   | EngineSize
  ---------------------------------------------------------------------------------------------------------------------------------
  H003       | 45000         | 45620        | 620           | David     | Brown    | 01224-555-2003 | Nissan | Qashqai | 1.5L      

============================================================
  Query 5 - Active hires at Aberdeen (O003)
============================================================

SQL:

        SELECT
            h.HireNumber,
            h.StartDate,
            h.EndDate,
            v.RegistrationNumber,
            v.Make,
            v.Model,
            c.FirstName,
            c.LastName,
            c.PhoneNumber
        FROM HIRE_AGREEMENT h
        JOIN VEHICLE v ON h.RegistrationNumber = v.RegistrationNumber
        JOIN OUTLET o ON v.OutletNumber = o.OutletNumber
        JOIN CLIENT c ON h.ClientNumber = c.ClientNumber
        WHERE o.OutletNumber = 'O003'
        AND h.MileageAfter IS NULL
        AND h.EndDate >= DATE('now')
    

Results:
  No results found.
```
<!-- RESULTS_END -->