def print_results(title, cursor):
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

    if not rows:
        print("  No results found.")
        return

    col_widths = [max(len(str(col)), max(len(str(row[i])) for row in rows)) for i, col in enumerate(columns)]

    header = " | ".join(f"{col:<{col_widths[i]}}" for i, col in enumerate(columns))
    print(f"  {header}")
    print(f"  {'-' * len(header)}")

    for row in rows:
        line = " | ".join(f"{str(row[i]):<{col_widths[i]}}" for i in range(len(columns)))
        print(f"  {line}")


def run_queries(conn):
    cursor = conn.cursor()

    # Query 1 — Vehicles at a given outlet
    cursor.execute("""
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
    """)
    print_results("Query 1 — Vehicles at Edinburgh (O001)", cursor)

    # Query 2 — Full hire history for a specific client
    cursor.execute("""
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
    """)
    print_results("Query 2 — Hire history for Client C001 (Robert Thomson)", cursor)

    # Query 3 — Staff at a specific outlet
    cursor.execute("""
        SELECT
            s.StaffNumber,
            s.FirstName,
            s.LastName,
            s.JobTitle,
            s.Salary
        FROM STAFF s
        JOIN OUTLET o ON s.OutletNumber = o.OutletNumber
        WHERE o.OutletNumber = 'O002'
    """)
    print_results("Query 3 — Staff at Glasgow (O002)", cursor)

    # Query 4 — Mileage driven during a specific hire agreement
    cursor.execute("""
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
    """)
    print_results("Query 4 — Mileage driven on Hire H003", cursor)

    # Query 5 — Active hire agreements at a given outlet
    cursor.execute("""
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
    """)
    print_results("Query 5 — Active hires at Aberdeen (O003)", cursor)