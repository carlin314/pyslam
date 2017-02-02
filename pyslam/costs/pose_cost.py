import numpy as np

class PoseCost:
    """Unary pose cost given absolute pose measurement in SE2/SE3."""

    def __init__(self, T_obs, stiffness):
        self.T_obs = T_obs
        self.stiffness = stiffness
        self.obstype = type(T_obs)

    def evaluate(self, params, compute_jacobians=None):
        T_est = params[0]

        residual = np.dot(self.stiffness,
                          self.obstype.log(T_est * self.T_obs.inv()))

        if compute_jacobians:
            jacobians = [None for _ in enumerate(params)]

            if compute_jacobians[0]:
                jacobians[0] = np.dot(self.stiffness,
                                      np.identity(self.obstype.dof))

            return residual, jacobians

        return residual