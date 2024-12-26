from app.api.user.models import User


async def fetch_user(idt: int):
    user = await User.get_or_none(id=idt)
    return user
