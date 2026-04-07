from datetime import datetime, timedelta

class Guest:
    def __init__(self,name,budget):
        self.name = name
        self.budget = budget


class Room:
    def __init__(self,number,price_per_day):
        self.number = number
        self.price_per_day = price_per_day
        self.bookings=[]

    def is_available(self,start_day,end_day):
        for b_start,b_end,_ in self.bookings:
            if not(end_day <= b_start or start_day >= b_end):
                return False
        return True

    def get_guests_at(self, check_date):
        for b_start,b_end,guest in self.bookings:
            if b_start <= check_date < b_end:
                return guest
        return None

class Hotel:
    def __init__(self,name):
        self.name = name
        self.rooms = []
    def add_room(self,room):
        self.rooms.append(room)

    def count_free_rooms(self, check_date):
        count = 0
        for room in self.rooms:
            if room.is_available(check_date, check_date + timedelta(days=1)):
                count += 1
        return count

    def find_available_room(self, start_date, end_date, budget=None):
        days = (end_date - start_date).days
        for room in self.rooms:
            total_price = room.price_per_day * days
            if room.is_available(start_date, end_date):
                if budget is None or total_price <= budget:
                    return room
        return None

    def check_in(self, guest, start_date, end_date):
        room = self.find_available_room(start_date, end_date, guest.budget)
        if room:
            room.bookings.append((start_date, end_date, guest))
            return f"Успіх: {guest.name} поселений у номер {room.number}"
        return "Помилка: Немає доступних номерів за вашим бюджетом/датами"

    def get_total_profit(self, start_period, end_period):
        total = 0
        for room in self.rooms:
            for b_start, b_end, _ in room.bookings:
                # Рахуємо перетин дат бронювання та запитуваного періоду
                actual_start = max(start_period, b_start)
                actual_end = min(end_period, b_end)

                if actual_start < actual_end:
                    days = (actual_end - actual_start).days
                    total += days * room.price_per_day
        return total

    def find_guest(self, guest_name, check_date):
        for room in self.rooms:
            guest = room.get_guests_at(check_date)
            if guest and guest.name == guest_name:
                return f"Гість {guest_name} знайдений у номері {room.number}"
        return f"Гість {guest_name} не знайдений на дату {check_date.date()}"


if __name__ == '__main__':
    my_hotel = Hotel("Lux")
    my_hotel.add_room(Room(101, 500))
    my_hotel.add_room(Room(102, 1000))

    d1 = datetime(2024, 6, 1)
    d2 = datetime(2024, 6, 5)

    ivan = Guest("Ivan", 3000)
    print(my_hotel.check_in(ivan, d1, d2))

    print(f"Вільних номерів: {my_hotel.count_free_rooms(datetime(2024, 6, 2))}")

    print(my_hotel.find_guest("Ivan", datetime(2024, 6, 2)))

    print(f"Прибуток готелю: {my_hotel.get_total_profit(datetime(2024, 6, 1), datetime(2024, 6, 10))} грн")