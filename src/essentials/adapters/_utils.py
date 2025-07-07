import cadwork
from cwmath.cwvector3d import CwVector3d


def to_cadwork_vector(vector: CwVector3d) -> cadwork.point_3d:
    return cadwork.point_3d(vector.x, vector.y, vector.z)
