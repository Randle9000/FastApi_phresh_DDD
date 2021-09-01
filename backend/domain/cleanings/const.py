from enum import Enum


class CleaningType(str, Enum):
    DUST_UP = "dust_up"
    SPOT_CLEAN = "spot_clean"
    FULL_CLEAN = "full_clean"
