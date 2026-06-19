from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.main import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


# @router.get("")
# async def get_bookings():
#     s=await BookingDAO.find_one_or_none(room_id=1)
#     print(s)
#     # return await BookingDAO.find_one_or_none(room_id=1)

        
@router.get("")
async def get_bookings() -> list[SBooking]:
    print("DIR:", dir(BookingDAO))
    print("FILE:", BookingDAO.__mro__[1].__module__)
    import app.dao.base as b
    print("BASE PATH:", b.__file__)
    return await BookingDAO.find_all()
