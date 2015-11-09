import unittest
import random

import numpy as np

import dotdot
import learners
from learners import tools

random.seed(0)
np.random.seed(0)

def random_linear(n, m):
    """Create a random linear function from R^n -> R^m"""
    M = np.random.rand(n,m)
    return lambda x : np.dot(np.array(x), M).ravel()


class TestOptimize(unittest.TestCase):

    def test_lwr1D_linear(self):
        """Simplest test possible (well, not quite, but close)."""
        f = lambda x : 2.0*x

        cfg = {'m_channels'  : [learners.Channel('x', (0.0, 1.0))],
               's_channels'  : [learners.Channel('y', (0.0, 1.0))],
               'm_uniformize': True}

        learner = learners.OptimizeLearner(cfg)

        for i in range(10):
            x = np.random.rand(1)
            y = f(x)
            learner.update(tools.to_signal(x, cfg['m_channels']),
                           tools.to_signal(y, cfg['s_channels']))

        for i in range(10):
            y = np.random.rand(1).ravel()
            xp = learner.infer(tools.to_signal(y, cfg['s_channels']))
            xp = np.array(tools.to_vector(xp, cfg['m_channels']))
            self.assertTrue(np.allclose(f(xp), y, rtol = 1e-5, atol = 1e-5))


    def test_lwr_linear(self):
        """Test LWLR on random linear models of dimensions from 1 to 20.
         It should return exact results, give of take floating point imprecisions."""

        for i in range(20):
            n = random.randint(1, 20)
            m = random.randint(1, 5)
            f = random_linear(n, m)
            cfg = {'m_channels'  : [learners.Channel('x_{}'.format(i), (0.0, 1.0))
                                    for i in range(n)],
                   's_channels'  : [learners.Channel('y_{}'.format(i), (0.0, 1.0))
                                    for i in range(m)],
                   'm_uniformize': True,
                   'options.maxiter': 500}

            learner = learners.OptimizeLearner(cfg)

            for i in range(4*n):
                x = np.random.rand(n)
                y = f(x)
                learner.update(tools.to_signal(x, cfg['m_channels']),
                               tools.to_signal(y, cfg['s_channels']))

            for i in range(10):
                x = np.random.rand(n).ravel()
                y = f(x)
                xp = learner.infer(tools.to_signal(y, cfg['s_channels']))
                xp = np.array(tools.to_vector(xp, cfg['m_channels']))
                self.assertTrue(np.allclose(f(xp), y, rtol = 1e-1, atol = 1e-1))

if __name__ == '__main__':
    unittest.main()
