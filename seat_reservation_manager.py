import heapq


class SeatManager:
    def __init__(self, n: int):
        self.seats = {i: True for i in range(1, n + 1)}

    def reserve(self) -> int:
        for seat, value in self.seats.items():
            if value:
                self.seats[seat] = False
                break
        return seat

    def unreserve(self, seat_number: int) -> None:
        self.seats[seat_number] = True


class SeatManager:
    def __init__(self, n: int):
        self.seats = [True for i in range(n + 1)]

    def reserve(self) -> int:
        for num, seat in enumerate(self.seats, start=1):
            if seat:
                self.seats[num] = False
                break
        return num

    def unreserve(self, seat_number: int) -> None:
        self.seats[seat_number] = True


class SeatManager:
    def __init__(self, n: int):
        self.seats = []
        for i in range(1, n + 1):
            heapq.heappush(self.seats, i)

    def reserve(self) -> int:
        return heapq.heappop(self.seats)

    def unreserve(self, seat_number: int) -> None:
        heapq.heappush(self.seats, seat_number)

    def __repr__(self) -> str:
        return str(self.seats)


# Your SeatManager object will be instantiated and called as such:
obj = SeatManager(10)
obj.reserve()
obj.reserve()
obj.reserve()
obj.reserve()
param_1 = obj.reserve()
print(param_1)
obj.unreserve(5)
print(obj)
