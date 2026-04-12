-- Query 1: List all vehicles currently stocked at a given outlet (Edinburgh = O001)
SELECT 
    v.RegistrationNumber,
    v.Make,
    v.Model,
    v.EngineSize,
    v.Capacity,
    v.DailyHireRate
FROM VEHICLE v
JOIN OUTLET o ON v.OutletNumber = o.OutletNumber
WHERE o.OutletNumber = 'O001';

-- Query 2: Retrieve full hire history for a specific client (C001)
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
WHERE c.ClientNumber = 'C001';

-- Query 3: Find all staff employed at a specific outlet (Glasgow = O002)
SELECT 
    s.StaffNumber,
    s.FirstName,
    s.LastName,
    s.JobTitle,
    s.Salary
FROM STAFF s
JOIN OUTLET o ON s.OutletNumber = o.OutletNumber
WHERE o.OutletNumber = 'O002';

-- Query 4: Calculate mileage driven during a specific hire agreement (H003)
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
AND h.MileageAfter IS NOT NULL;

-- Query 5: Find all active hire agreements for vehicles at a given outlet (Aberdeen = O003)
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
AND h.EndDate >= DATE('now');