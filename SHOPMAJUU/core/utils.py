import random
import string
from decimal import Decimal


TRACKING_PREFIX = "SF"


def generate_tracking_number() -> str:
    body = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return f"{TRACKING_PREFIX}-{body}"


class RateCalculator:
    """Simple rate logic – customize to your business rules.
    Billable weight = max(actual, volumetric). Rate = base + (per_kg * billable).
    """


    BASE_FEE = Decimal("5.00")
    PER_KG = Decimal("8.50")
    MIN_CHARGE = Decimal("12.00")


    @classmethod
    def estimate(cls, billable_weight_kg: float) -> Decimal:
        w = Decimal(str(billable_weight_kg))
        total = cls.BASE_FEE + (cls.PER_KG * w)
        return total if total >= cls.MIN_CHARGE else cls.MIN_CHARGE