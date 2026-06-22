from enum import IntEnum

class TransmissionStatus(IntEnum):
    Ok = 0
    InvalidId = 1
    InvalidInstance = 2
    OutOfRange = 3
    InvalidStorage = 4
    Locked = 5
    NotNotifiable = 6
    OptionNotSupported = 7
    InvalidLength = 8
    InvalidType = 9
    InvalidBehavior = 10
    AlreadyInUse = 11
    TooManyDate = 11
