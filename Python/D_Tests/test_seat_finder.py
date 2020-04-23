import unittest

from B_Logic.SeatFinder import SeatFinder


class SeatFinderTest(unittest.TestCase):

    def test_prefer_near_the_front(self):
        finder = SeatFinder(available_seats)={"A6", "B6", "C7"}
        seats = finder.find_seats(1)
        assert seats == {"A6"}

    def test_finds_adjacent_sets_when_more_than_one_requested(self):
        finder = SeatFinder(available_seats)={"A6", "A8", "C6", "C7"}
        seats = finder.find_seats(2)
        assert seats == {"C6","C7"}

    def test_finds_separate_seats_when_adjacent_not_available(self):
        finder = SeatFinder(available_seats)={"A6", "B6", "C6"}
        seats = finder.find_seats(2)
        assert seats == {"B6","A6"}

    def testFindSeatsFailsWhenNotEnoughAvailable(self):
        finder = SeatFinder(available_seats)={"A6", "B6", "C6"}
        seats = finder.find_seats(5)
        assert seats == {}

    def testFindSeatsForWheelchairUsers(self):
        finder = SeatFinder(available_seats)={"A1","B1W", "B6", "C6"}
        seats = finder.find_seats(1, wheelchairCount=1)
        assert seats == {"B1W"}

