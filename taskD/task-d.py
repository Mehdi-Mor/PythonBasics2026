# Copyright (c) 2026 Ville Heikkiniemi, Luka Hietala, Luukas Kola
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by Mehdi according to given taskD

from datetime import datetime, date

DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def convert_data(line: list) -> list:
    """
    Convert data types to meet program requirements

    Parameters:
     line (list): Unconverted line -> 7 columns

    Returns:
     converted (list): Converted data types
    """
    converted = []
    converted.append(datetime.fromisoformat(line[0]))
    converted.append(int(line[1]))
    converted.append(int(line[2]))
    converted.append(int(line[3]))
    converted.append(int(line[4]))
    converted.append(int(line[5]))
    converted.append(int(line[6]))

    return converted


def read_data(filename: str) -> list:
    """
    Reads the CSV file and returns the rows in a suitable structure.

    Parameters:
        filename (str): Name of the file containing the electricity consumption and production

    Returns:
        weekly (list): Read and converted consumption and production
    """
    consumption_and_production = []

    with open(filename, "r", encoding="utf-8") as f:
        next(f)
        for line in f:
            line = line.strip()
            fields = line.split(";")
            consumption_and_production.append(convert_data(fields))

    return consumption_and_production

def day_info(day: date, database: list ) -> str:
    """
    Reads the consumption and production per day.

    Parameters:
        day (data): Reportable day
        database (list): Consumption and production date + dates

    Returns:
        printable string
    """

    consumption_phase1 = 0
    consumption_phase2 = 0
    consumption_phase3 = 0

    production_phase1 = 0
    production_phase2 = 0
    production_phase3 = 0
    for per_hour in database:
        if per_hour[0].date() == day:
            consumption_phase1 += per_hour[1]/1000
            consumption_phase2 += per_hour[2]/1000
            consumption_phase3 += per_hour[3]/1000
            production_phase1 += per_hour[4]/1000
            production_phase2 += per_hour[5]/1000
            production_phase3 += per_hour[6]/1000

    cp1 = f"{consumption_phase1:.2f}".replace(".", ",")
    cp2 = f"{consumption_phase2:.2f}".replace(".", ",")
    cp3 = f"{consumption_phase3:.2f}".replace(".", ",")
    pp4 = f"{production_phase1:.2f}".replace(".", ",")
    pp5 = f"{production_phase2:.2f}".replace(".", ",")
    pp6 = f"{production_phase3:.2f}".replace(".", ",")

    return f'{day.strftime("%d.%m.%Y"):<15}' + f"{cp1:<8}"+f"{cp2:<8}"+f"{cp3:<15}"+f"{pp4:<8}"+f"{pp5:<8}"+f"{pp6:<8}"

def main() -> None:
    """Main function: reads data, computes daily totals, and prints the report."""

    db = read_data("week42.csv")
    print("Week 42 electricity consumption and production (kWh, by phase)", end="\n\n")
    print("Day        Date           Consumption [kWh]               Production [kWh]")
    print("           (dd.mm.yyyy)   v1      v2      v3              v1      v2      v3")
    print("---------------------------------------------------------------------------")
    print(f"{DAYS[0]:<10}", day_info(date(2025, 10, 13), db))
    print(f"{DAYS[1]:<10}", day_info(date(2025, 10, 14), db))
    print(f"{DAYS[2]:<10}", day_info(date(2025, 10, 15), db))
    print(f"{DAYS[3]:<10}", day_info(date(2025, 10, 16), db))
    print(f"{DAYS[4]:<10}", day_info(date(2025, 10, 17), db))
    print(f"{DAYS[5]:<10}", day_info(date(2025, 10, 18), db))
    print(f"{DAYS[6]:<10}", day_info(date(2025, 10, 19), db))

if __name__ == "__main__":
    main()