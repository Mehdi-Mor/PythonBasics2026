# Copyright (c) 2026 Ville Heikkiniemi, Luka Hietala, Luukas Kola
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

# Modified by Mehdi according to given taskG

"""
A program that prints reservation information according to requirements

The data structure and example data record:

reservationId | name | email | phone | reservationDate | reservationTime | durationHours | price | confirmed | reservedResource | createdAt
------------------------------------------------------------------------
201 | Moomin Valley | moomin@whitevalley.org | 0509876543 | 2025-11-12 | 09:00:00 | 2 | 18.50 | True | Forest Area 1 | 2025-08-12 14:33:20
int | str | str | str | date | time | int | float | bool | str | datetime

"""

from datetime import datetime

class Reservation:
    def __init__(self, data):
        self.reservation_id = int(data[0])
        self.name = str(data[1])
        self.email = str(data[2])
        self.phone = str(data[3])
        self.date = datetime.strptime(data[4], "%Y-%m-%d").date()
        self.time = datetime.strptime(data[5], "%H:%M").time()
        self.duration = int(data[6])
        self.price = float(data[7])
        self.confirmed = (True if data[8].strip() == 'True' else False)
        self.resource = str(data[9])
        self.created = datetime.strptime(str(data[10]).strip(), "%Y-%m-%d %H:%M:%S")

    def is_confirmed(self):
        return self.confirmed

    def is_long(self):
        return self.duration >= 3

    def total_price(self):
        return self.duration * self.price
    
    def finnish_day(self):
        return self.date.strftime("%d.%m.%Y")
    
    def finnish_time(self):
        return self.time.strftime("%H.%M")

    def revenue(self):
        revenue = self.total_price() if self.confirmed else 0
        return revenue
    

def revenue_finnish(revenue_total: float) -> str:
    """
    Change the revenue to the finnish version (euro + comma)

    Parameters:
     revenue_total (float): Total revenue

    Returns:
     revenue_total (str): Total revenue with euro and comma
    """
    return f'{revenue_total:.2f} €'.replace('.', ',')

def fetch_reservations(reservations_file: str) -> list[list]:
    """
    Reads reservations from a file and returns the reservations converted
    You don't need to modify this function!

    Parameters:
     reservation_file (str): Name of the file containing the reservations

    Returns:
     reservations (list): Read and converted reservations
    """
    reservations = []
    with open(reservations_file, "r", encoding="utf-8") as f:
        for line in f:
            if len(line) > 1:
                fields = line.split("|")
                reservations.append(Reservation(fields))
    return reservations

def confirmed_reservations(reservations: list[Reservation]) -> None:
    """
    Print confirmed reservations

    Parameters:
     reservations (list[Reservations]): Reservations
    """
    for reservation in reservations:
        if reservation.is_confirmed():
            print(f'- {reservation.name}, {reservation.resource}, {reservation.finnish_day()} at {reservation.finnish_time()}')

def long_reservations(reservations : list[Reservation]) -> None:
    """
    Print long reservations

    Parameters:
     reservations (list[Reservation]): Reservations
    """
    for reservation in reservations:
        if reservation.is_long():
            print(f'- {reservation.name}, {reservation.finnish_day()} at {reservation.finnish_time()}, duration {reservation.duration} h, {reservation.resource}')


def confirmation_statuses(reservations: list[Reservation]) -> None:
    """
    Print confirmation statuses

    Parameters:
     reservations (list[Reservation]): Reservations
    """
    for reservation in reservations:
        name : str = reservation.name
        confirmed : bool = reservation.confirmed

        print(f'{name} → {"Confirmed" if confirmed else "NOT Confirmed"}')

def confirmation_summary(reservations: list[Reservation]) -> None:
    """
    Print confirmation summary

    Parameters:
     reservations (list[Reservation]): Reservations
    """
    confirmed : int = len([x for x in reservations if x.confirmed])
    print(f'- Confirmed reservations: {confirmed} pcs\n- Not confirmed reservations: {len(reservations) - confirmed} pcs')

def total_revenue(reservations: list[Reservation]) -> None:
    """
    Print total revenue

    Parameters:
     reservations (list): Reservations
    """
    total = 0
    for reservation in reservations:
        total += reservation.revenue()

    print(f'Total revenue from confirmed reservations: {revenue_finnish(total)}')

def main():
    """
    Prints reservation information according to requirements
    Reservation-specific printing is done in functions
    """
    reservations = fetch_reservations("reservations.txt")
    print("1) Confirmed Reservations")
    confirmed_reservations(reservations)
    print("2) Long Reservations (≥ 3 h)")
    long_reservations(reservations)
    print("3) Reservation Confirmation Status")
    confirmation_statuses(reservations)
    print("4) Confirmation Summary")
    confirmation_summary(reservations)
    print("5) Total Revenue from Confirmed Reservations")
    total_revenue(reservations)

if __name__ == "__main__":
    main()