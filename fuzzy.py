
# uncomment in order to install scikil-fuzzy in colab enviroment.
# !pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

"""# Antecedent/Consequent objects"""

Chemistry = ctrl.Antecedent(np.arange(0, 20.25, 0.25), 'Chemistry')
Physics = ctrl.Antecedent(np.arange(0, 20.25, 0.25), 'Physics')
Math = ctrl.Antecedent(np.arange(0, 20.25, 0.25), 'Math')

"""# Auto-membership function population

"""

Computer_match = ctrl.Consequent(np.arange(0, 101, 1), 'Computer_match')
Construction_match = ctrl.Consequent(np.arange(0, 101, 1), 'Construction_match')
Automotive_match = ctrl.Consequent(np.arange(0, 101, 1), 'Automotive_match')

"""# Membership function population"""

Chemistry.automf(3)
Physics.automf(3)
Math.automf(3)

Computer_match.automf(3)
Construction_match.automf(3)
Automotive_match.automf(3)

Chemistry.view()
Physics.view()
Math.view()

"""# Reference rules"""

r1 = ctrl.Rule(Math['good'] , Computer_match['good'])
r2 = ctrl.Rule(Math['poor'], Computer_match['average'])
r3 = ctrl.Rule(Math['good'], Construction_match['average'])
r4 = ctrl.Rule(Physics['good'], Construction_match['good'])
r5 = ctrl.Rule(Chemistry['good'], Construction_match['good'])
r6 = ctrl.Rule(Physics['good'], Automotive_match['good'])
match_ctrl = ctrl.ControlSystem([r1, r2, r3,r4,r5,r6])

r1.view()
r2.view()
r3.view()
r4.view()
r5.view()
r6.view()

match = ctrl.ControlSystemSimulation(match_ctrl)

match.input['Math'] = 16.5
match.input['Chemistry'] = 19.8
match.input['Physics'] = 13.8

match.compute()

print(match.output)
Automotive_match.view(sim=match)
Construction_match.view(sim=match)
Computer_match.view(sim=match)

