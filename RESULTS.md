# Reliable Rentals - Query Results

Last updated: Sun Apr 12 21:29:38 UTC 2026

```
Tables created.
Seed data inserted.

============================================================
  Query 1 - Vehicles at Edinburgh (O001)
============================================================
  RegistrationNumber | Make       | Model | EngineSize | Capacity | DailyHireRate
  -------------------------------------------------------------------------------
  EH21 XYZ           | Vauxhall   | Corsa | 1.2L       | 5        | 35.0         
  EH22 JKL           | Volkswagen | Golf  | 2.0L       | 5        | 50.0         

============================================================
  Query 2 - Hire history for Client C001 (Robert Thomson)
============================================================
  HireNumber | StartDate  | EndDate    | MileageBefore | MileageAfter | Make       | Model | RegistrationNumber
  -------------------------------------------------------------------------------------------------------------
  H001       | 2024-01-10 | 2024-01-15 | 12000         | 12350        | Vauxhall   | Corsa | EH21 XYZ          
  H005       | 2024-05-20 | 2024-05-25 | 31000         | 31540        | Volkswagen | Golf  | EH22 JKL          

============================================================
  Query 3 - Staff at Glasgow (O002)
============================================================
  StaffNumber | FirstName | LastName | JobTitle       | Salary 
  -------------------------------------------------------------
  S003        | Hamish    | Stewart  | Branch Manager | 44000.0
  S004        | Morag     | Fraser   | Sales Advisor  | 27000.0

============================================================
  Query 4 - Mileage driven on Hire H003
============================================================
  HireNumber | MileageBefore | MileageAfter | MileageDriven | FirstName | LastName | PhoneNumber    | Make   | Model   | EngineSize
  ---------------------------------------------------------------------------------------------------------------------------------
  H003       | 45000         | 45620        | 620           | David     | Brown    | 01224-555-2003 | Nissan | Qashqai | 1.5L      

============================================================
  Query 5 - Active hires at Aberdeen (O003)
============================================================
  HireNumber | StartDate  | EndDate    | RegistrationNumber | Make | Model | FirstName | LastName | PhoneNumber  
  ---------------------------------------------------------------------------------------------------------------
  H007       | 2024-06-05 | 2026-04-30 | AB20 PQR           | Ford | Kuga  | Emma      | Scott    | 0131-555-2006

Done. Connection closed.
```
