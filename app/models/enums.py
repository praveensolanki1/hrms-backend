from enum import Enum

class AttendanceStatus(str, Enum):
    present = "present"
    absent = "absent"
    leave = "leave"