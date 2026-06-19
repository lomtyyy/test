from app.dao.base import BaseDAO
from app.bookings.models import Bookings

print(">>> ЗАГРУЖЕН НОВЫЙ dao.py <<<")


class BookingDAO(BaseDAO):
    model = Bookings

