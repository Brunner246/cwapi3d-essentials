import dataclasses

from cwmath.cwvector3d import CwVector3d


@dataclasses.dataclass(slots=True, init=False)
class AxisSystem:
    p1: CwVector3d
    p2: CwVector3d
    p3: CwVector3d

    def __init__(self, start: CwVector3d, end: CwVector3d = None, height: CwVector3d = None):
        self.p1 = start
        self.p2 = end if end is not None else start + CwVector3d(1_000, 0, 0)
        self.p3 = height if height is not None else start + CwVector3d(0, 0, 1)
