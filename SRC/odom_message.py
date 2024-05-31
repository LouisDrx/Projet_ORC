from dataclasses import dataclass, fields, is_dataclass
from typing import Type, TypeVar

T = TypeVar('T')

class JsonMixin:

    @classmethod
    def from_dict(cls: Type[T], input_dict: dict) -> T:
        loaded = input_dict

        for f in fields(cls):
            if is_dataclass(loaded):
                return loaded

            if issubclass(f.type, JsonMixin):
                loaded[f.name] = f.type.from_dict(loaded[f.name])

        return cls(**loaded)

    def to_dict(self):
        dumped = {}
        for k, v in self.__dict__.items():
            if hasattr(v, "to_dict"):
                dumped[k] = v.to_dict()
            else:
                dumped[k] = v
        return dumped


@dataclass
class Stamp(JsonMixin):
    secs: int
    nsecs: int


@dataclass
class Header(JsonMixin):
    seq: int
    stamp: Stamp
    frame_id: str = "odom"


@dataclass
class Coordinates3D(JsonMixin):
    x: float
    y: float
    z: float


@dataclass
class Quaternion(JsonMixin):
    x: float
    y: float
    z: float
    w: float


@dataclass
class Pose(JsonMixin):
    position: Coordinates3D
    orientation: Quaternion


@dataclass
class Twist(JsonMixin):
    linear: Coordinates3D
    angular: Coordinates3D


@dataclass
class Odometry(JsonMixin):
    header: Header
    pose: Pose
    twist: Twist
    child_frame_id: str = "base_footprint"
