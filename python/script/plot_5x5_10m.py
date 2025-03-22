import numpy
import questa.plotter
import matplotlib.pyplot

if __name__ == "__main__":
    matplotlib.pyplot.rc('text', usetex=False)
    matplotlib.pyplot.rc('font', family='serif')
    matplotlib.pyplot.rc('figure', figsize=(8, 8))
    data_5_10m_max_weight =\
        numpy.array([[1.00000000e-01, 5.44325900e-01, 5.43964725e-01, 5.44687075e-01],
            [2.00000000e-01, 1.19805047e+00, 1.19730755e+00, 1.19879339e+00],
            [3.00000000e-01, 2.00320963e+00, 2.00215638e+00, 2.00426289e+00],
            [4.00000000e-01, 3.02991337e+00, 3.02824463e+00, 3.03158211e+00],
            [5.00000000e-01, 4.40707370e+00, 4.40471447e+00, 4.40943293e+00],
            [6.00000000e-01, 6.40232480e+00, 6.39815819e+00, 6.40649141e+00],
            [7.00000000e-01, 9.67957647e+00, 9.67269990e+00, 9.68645303e+00],
            [8.00000000e-01, 1.62055112e+01, 1.61897418e+01, 1.62212805e+01],
            [9.00000000e-01, 3.49582396e+01, 3.48898572e+01, 3.50266219e+01],
            [9.10000000e-01, 3.90169273e+01, 3.89339497e+01, 3.90999049e+01],
            [9.20000000e-01, 4.40474520e+01, 4.39331701e+01, 4.41617339e+01],
            [9.30000000e-01, 5.05086898e+01, 5.03590203e+01, 5.06583594e+01],
            [9.40000000e-01, 5.90724355e+01, 5.88625171e+01, 5.92823539e+01],
            [9.50000000e-01, 7.10267573e+01, 7.07278950e+01, 7.13256196e+01],
            [9.60000000e-01, 8.89822103e+01, 8.85132834e+01, 8.94511372e+01],
            [9.61000000e-01, 9.12658362e+01, 9.07743458e+01, 9.17573266e+01],
            [9.62000000e-01, 9.36674627e+01, 9.31369142e+01, 9.41980111e+01],
            [9.63000000e-01, 9.62017298e+01, 9.56421525e+01, 9.67613071e+01],
            [9.64000000e-01, 9.88895886e+01, 9.82999781e+01, 9.94791992e+01],
            [9.65000000e-01, 1.01751419e+02, 1.01124170e+02, 1.02378668e+02],
            [9.66000000e-01, 1.04755936e+02, 1.04081289e+02, 1.05430582e+02],
            [9.67000000e-01, 1.07943916e+02, 1.07234493e+02, 1.08653339e+02],
            [9.68000000e-01, 1.11331673e+02, 1.10585268e+02, 1.12078078e+02],
            [9.69000000e-01, 1.14968219e+02, 1.14161440e+02, 1.15774999e+02],
            [9.70000000e-01, 1.18782167e+02, 1.17920193e+02, 1.19644142e+02],
            [9.71000000e-01, 1.22887045e+02, 1.21968443e+02, 1.23805648e+02],
            [9.72000000e-01, 1.27271637e+02, 1.26277726e+02, 1.28265548e+02],
            [9.73000000e-01, 1.31955180e+02, 1.30900762e+02, 1.33009599e+02],
            [9.74000000e-01, 1.37046872e+02, 1.35927371e+02, 1.38166373e+02],
            [9.75000000e-01, 1.42499084e+02, 1.41305924e+02, 1.43692244e+02],
            [9.76000000e-01, 1.48413427e+02, 1.47141365e+02, 1.49685488e+02],
            [9.77000000e-01, 1.54856436e+02, 1.53491314e+02, 1.56221557e+02],
            [9.78000000e-01, 1.61909808e+02, 1.60421465e+02, 1.63398152e+02],
            [9.79000000e-01, 1.69660991e+02, 1.68046126e+02, 1.71275855e+02],
            [9.80000000e-01, 1.78217405e+02, 1.76452705e+02, 1.79982105e+02],
            [9.81000000e-01, 1.87561978e+02, 1.85650084e+02, 1.89473871e+02],
            [9.82000000e-01, 1.98028814e+02, 1.95931695e+02, 2.00125933e+02],
            [9.83000000e-01, 2.09623285e+02, 2.07309771e+02, 2.11936799e+02],
            [9.84000000e-01, 2.22680776e+02, 2.20126236e+02, 2.25235316e+02],
            [9.85000000e-01, 2.37661489e+02, 2.34739636e+02, 2.40583342e+02],
            [9.86000000e-01, 2.54585986e+02, 2.51345176e+02, 2.57826796e+02],
            [9.87000000e-01, 2.73985586e+02, 2.70239149e+02, 2.77732023e+02],
            [9.88000000e-01, 2.96735132e+02, 2.92386966e+02, 3.01083298e+02],
            [9.89000000e-01, 3.23786682e+02, 3.18701375e+02, 3.28871988e+02],
            [9.90000000e-01, 3.55891101e+02, 3.49714210e+02, 3.62067991e+02],
            [9.91000000e-01, 3.95476018e+02, 3.87957315e+02, 4.02994722e+02],
            [9.92000000e-01, 4.45643078e+02, 4.36114033e+02, 4.55172123e+02],
            [9.93000000e-01, 5.10007758e+02, 4.97666873e+02, 5.22348642e+02],
            [9.94000000e-01, 5.94353685e+02, 5.77646899e+02, 6.11060471e+02],
            [9.95000000e-01, 7.13867092e+02, 6.89930610e+02, 7.37803574e+02],
            [9.96000000e-01, 8.88487586e+02, 8.51404979e+02, 9.25570193e+02],
            [9.97000000e-01, 1.16999116e+03, 1.11165123e+03, 1.22833110e+03],
            [9.98000000e-01, 1.72559736e+03, 1.61487346e+03, 1.83632126e+03],
            [9.99000000e-01, 3.45726204e+03, 3.12279276e+03, 3.79173132e+03]])
    data_5_10m_max_size =\
        numpy.array([[1.00000000e-01, 5.44333367e-01, 5.43972497e-01, 5.44694236e-01],
            [2.00000000e-01, 1.19817507e+00, 1.19743846e+00, 1.19891168e+00],
            [3.00000000e-01, 2.00351433e+00, 2.00245645e+00, 2.00457222e+00],
            [4.00000000e-01, 3.02797997e+00, 3.02628795e+00, 3.02967199e+00],
            [5.00000000e-01, 4.38870060e+00, 4.38648729e+00, 4.39091391e+00],
            [6.00000000e-01, 6.30821937e+00, 6.30393428e+00, 6.31250446e+00],
            [7.00000000e-01, 9.31354250e+00, 9.30721063e+00, 9.31987437e+00],
            [8.00000000e-01, 1.49972834e+01, 1.49832020e+01, 1.50113648e+01],
            [9.00000000e-01, 3.16823763e+01, 3.16092941e+01, 3.17554586e+01],
            [9.10000000e-01, 3.54394835e+01, 3.53502200e+01, 3.55287470e+01],
            [9.20000000e-01, 4.01849503e+01, 4.00697633e+01, 4.03001373e+01],
            [9.30000000e-01, 4.63297773e+01, 4.61739338e+01, 4.64856208e+01],
            [9.40000000e-01, 5.46250248e+01, 5.43887069e+01, 5.48613426e+01],
            [9.50000000e-01, 6.64153227e+01, 6.60582225e+01, 6.67724230e+01],
            [9.60000000e-01, 8.45390137e+01, 8.39431722e+01, 8.51348551e+01],
            [9.61000000e-01, 8.67762376e+01, 8.61439539e+01, 8.74085212e+01],
            [9.62000000e-01, 8.92488318e+01, 8.85636235e+01, 8.99340401e+01],
            [9.63000000e-01, 9.19118616e+01, 9.12182139e+01, 9.26055092e+01],
            [9.64000000e-01, 9.46371856e+01, 9.39166156e+01, 9.53577555e+01],
            [9.65000000e-01, 9.75730201e+01, 9.67603094e+01, 9.83857307e+01],
            [9.66000000e-01, 1.00718770e+02, 9.98909485e+01, 1.01546591e+02],
            [9.67000000e-01, 1.04021668e+02, 1.03147943e+02, 1.04895393e+02],
            [9.68000000e-01, 1.07510749e+02, 1.06618383e+02, 1.08403114e+02],
            [9.69000000e-01, 1.11226236e+02, 1.10288117e+02, 1.12164355e+02],
            [9.70000000e-01, 1.15310720e+02, 1.14311479e+02, 1.16309962e+02],
            [9.71000000e-01, 1.19640866e+02, 1.18539430e+02, 1.20742302e+02],
            [9.72000000e-01, 1.24203554e+02, 1.23068996e+02, 1.25338111e+02],
            [9.73000000e-01, 1.29258934e+02, 1.28019935e+02, 1.30497934e+02],
            [9.74000000e-01, 1.34806419e+02, 1.33539312e+02, 1.36073526e+02],
            [9.75000000e-01, 1.40632534e+02, 1.39218127e+02, 1.42046941e+02],
            [9.76000000e-01, 1.46973803e+02, 1.45410035e+02, 1.48537571e+02],
            [9.77000000e-01, 1.53933561e+02, 1.52278825e+02, 1.55588298e+02],
            [9.78000000e-01, 1.61767834e+02, 1.59973643e+02, 1.63562025e+02],
            [9.79000000e-01, 1.70212839e+02, 1.68224621e+02, 1.72201056e+02],
            [9.80000000e-01, 1.79594056e+02, 1.77301105e+02, 1.81887007e+02],
            [9.81000000e-01, 1.90270830e+02, 1.87860113e+02, 1.92681547e+02],
            [9.82000000e-01, 2.02244490e+02, 1.99353543e+02, 2.05135436e+02],
            [9.83000000e-01, 2.15412937e+02, 2.12110532e+02, 2.18715342e+02],
            [9.84000000e-01, 2.30467124e+02, 2.26802851e+02, 2.34131396e+02],
            [9.85000000e-01, 2.47877975e+02, 2.43492961e+02, 2.52262990e+02],
            [9.86000000e-01, 2.67699260e+02, 2.62580158e+02, 2.72818361e+02],
            [9.87000000e-01, 2.91091121e+02, 2.84754258e+02, 2.97427985e+02],
            [9.88000000e-01, 3.18529566e+02, 3.10589477e+02, 3.26469655e+02],
            [9.89000000e-01, 3.51595137e+02, 3.41513210e+02, 3.61677065e+02],
            [9.90000000e-01, 3.92063782e+02, 3.79312167e+02, 4.04815398e+02],
            [9.91000000e-01, 4.40596198e+02, 4.24951656e+02, 4.56240741e+02],
            [9.92000000e-01, 5.02617840e+02, 4.83290504e+02, 5.21945176e+02],
            [9.93000000e-01, 5.82031323e+02, 5.58011512e+02, 6.06051133e+02],
            [9.94000000e-01, 6.85735798e+02, 6.55667066e+02, 7.15804530e+02],
            [9.95000000e-01, 8.33426295e+02, 7.93987482e+02, 8.72865108e+02],
            [9.96000000e-01, 1.05604584e+03, 9.98681166e+02, 1.11341052e+03],
            [9.97000000e-01, 1.45417877e+03, 1.34429038e+03, 1.56406717e+03],
            [9.98000000e-01, 2.26398386e+03, 2.03880906e+03, 2.48915865e+03],
            [9.99000000e-01, 4.47239439e+03, 3.98536191e+03, 4.95942688e+03]])
    data_5_10m_msmw =\
        numpy.array([[1.00000000e-01, 5.44317567e-01, 5.43956893e-01, 5.44678240e-01],
            [2.00000000e-01, 1.19766387e+00, 1.19692325e+00, 1.19840448e+00],
            [3.00000000e-01, 1.99947070e+00, 1.99843625e+00, 2.00050515e+00],
            [4.00000000e-01, 3.00988650e+00, 3.00826409e+00, 3.01150891e+00],
            [5.00000000e-01, 4.32765193e+00, 4.32549504e+00, 4.32980883e+00],
            [6.00000000e-01, 6.13573247e+00, 6.13202625e+00, 6.13943868e+00],
            [7.00000000e-01, 8.85779457e+00, 8.85250372e+00, 8.86308542e+00],
            [8.00000000e-01, 1.37562068e+01, 1.37446024e+01, 1.37678112e+01],
            [9.00000000e-01, 2.70933299e+01, 2.70419016e+01, 2.71447582e+01],
            [9.10000000e-01, 2.99810241e+01, 2.99179111e+01, 3.00441371e+01],
            [9.20000000e-01, 3.35536417e+01, 3.34680383e+01, 3.36392451e+01],
            [9.30000000e-01, 3.81410645e+01, 3.80272950e+01, 3.82548340e+01],
            [9.40000000e-01, 4.42190755e+01, 4.40625631e+01, 4.43755879e+01],
            [9.50000000e-01, 5.27245757e+01, 5.24964704e+01, 5.29526809e+01],
            [9.60000000e-01, 6.54512294e+01, 6.50999978e+01, 6.58024609e+01],
            [9.61000000e-01, 6.70789894e+01, 6.67122854e+01, 6.74456934e+01],
            [9.62000000e-01, 6.87960832e+01, 6.84017718e+01, 6.91903945e+01],
            [9.63000000e-01, 7.05878438e+01, 7.01665052e+01, 7.10091824e+01],
            [9.64000000e-01, 7.24948382e+01, 7.20470359e+01, 7.29426405e+01],
            [9.65000000e-01, 7.45208508e+01, 7.40473714e+01, 7.49943302e+01],
            [9.66000000e-01, 7.66778526e+01, 7.61703830e+01, 7.71853223e+01],
            [9.67000000e-01, 7.89543102e+01, 7.84178136e+01, 7.94908068e+01],
            [9.68000000e-01, 8.13454367e+01, 8.07764722e+01, 8.19144013e+01],
            [9.69000000e-01, 8.39151835e+01, 8.33077150e+01, 8.45226520e+01],
            [9.70000000e-01, 8.66806951e+01, 8.60257446e+01, 8.73356456e+01],
            [9.71000000e-01, 8.95695723e+01, 8.88714010e+01, 9.02677436e+01],
            [9.72000000e-01, 9.26878884e+01, 9.19354396e+01, 9.34403372e+01],
            [9.73000000e-01, 9.60548333e+01, 9.52470309e+01, 9.68626357e+01],
            [9.74000000e-01, 9.96649544e+01, 9.88072702e+01, 1.00522638e+02],
            [9.75000000e-01, 1.03537809e+02, 1.02622757e+02, 1.04452862e+02],
            [9.76000000e-01, 1.07746743e+02, 1.06768277e+02, 1.08725209e+02],
            [9.77000000e-01, 1.12347283e+02, 1.11300465e+02, 1.13394101e+02],
            [9.78000000e-01, 1.17344179e+02, 1.16203975e+02, 1.18484383e+02],
            [9.79000000e-01, 1.22918371e+02, 1.21683447e+02, 1.24153295e+02],
            [9.80000000e-01, 1.29034337e+02, 1.27698949e+02, 1.30369724e+02],
            [9.81000000e-01, 1.35703402e+02, 1.34236368e+02, 1.37170436e+02],
            [9.82000000e-01, 1.43227508e+02, 1.41600466e+02, 1.44854551e+02],
            [9.83000000e-01, 1.51595191e+02, 1.49818969e+02, 1.53371414e+02],
            [9.84000000e-01, 1.61036102e+02, 1.59070246e+02, 1.63001958e+02],
            [9.85000000e-01, 1.71787735e+02, 1.69543208e+02, 1.74032263e+02],
            [9.86000000e-01, 1.83951784e+02, 1.81462847e+02, 1.86440721e+02],
            [9.87000000e-01, 1.97992878e+02, 1.95116243e+02, 2.00869514e+02],
            [9.88000000e-01, 2.14402058e+02, 2.11083723e+02, 2.17720392e+02],
            [9.89000000e-01, 2.33886842e+02, 2.30094559e+02, 2.37679126e+02],
            [9.90000000e-01, 2.57032424e+02, 2.52454691e+02, 2.61610157e+02],
            [9.91000000e-01, 2.85624554e+02, 2.80090041e+02, 2.91159067e+02],
            [9.92000000e-01, 3.21927171e+02, 3.14851344e+02, 3.29002998e+02],
            [9.93000000e-01, 3.68575485e+02, 3.59319712e+02, 3.77831257e+02],
            [9.94000000e-01, 4.29520350e+02, 4.16786783e+02, 4.42253916e+02],
            [9.95000000e-01, 5.16967396e+02, 4.98808653e+02, 5.35126139e+02],
            [9.96000000e-01, 6.45270550e+02, 6.17204894e+02, 6.73336206e+02],
            [9.97000000e-01, 8.53205634e+02, 8.08615722e+02, 8.97795545e+02],
            [9.98000000e-01, 1.26943235e+03, 1.18469661e+03, 1.35416808e+03],
            [9.99000000e-01, 2.57880408e+03, 2.30219163e+03, 2.85541652e+03]])
    data_5_10m_msmw_log =\
        numpy.array([[1.00000000e-01, 6.86505647e+00, 6.86128882e+00, 6.86882411e+00],
            [2.00000000e-01, 7.54154110e+00, 7.53893637e+00, 7.54414583e+00],
            [3.00000000e-01, 8.26374730e+00, 8.26121762e+00, 8.26627698e+00],
            [4.00000000e-01, 9.06702927e+00, 9.06487254e+00, 9.06918599e+00],
            [5.00000000e-01, 1.00037052e+01, 1.00010456e+01, 1.00063647e+01],
            [6.00000000e-01, 1.12045709e+01, 1.12011777e+01, 1.12079640e+01],
            [7.00000000e-01, 1.30078248e+01, 1.30035571e+01, 1.30120925e+01],
            [8.00000000e-01, 1.65838643e+01, 1.65750151e+01, 1.65927135e+01],
            [9.00000000e-01, 2.80481966e+01, 2.80017190e+01, 2.80946741e+01],
            [9.10000000e-01, 3.06920644e+01, 3.06333990e+01, 3.07507299e+01],
            [9.20000000e-01, 3.40138518e+01, 3.39344036e+01, 3.40933000e+01],
            [9.30000000e-01, 3.83144241e+01, 3.82071003e+01, 3.84217479e+01],
            [9.40000000e-01, 4.40869290e+01, 4.39346061e+01, 4.42392518e+01],
            [9.50000000e-01, 5.22246488e+01, 5.20048275e+01, 5.24444701e+01],
            [9.60000000e-01, 6.45113359e+01, 6.41709264e+01, 6.48517454e+01],
            [9.61000000e-01, 6.60755762e+01, 6.57198338e+01, 6.64313187e+01],
            [9.62000000e-01, 6.77346665e+01, 6.73518584e+01, 6.81174746e+01],
            [9.63000000e-01, 6.94856358e+01, 6.90809222e+01, 6.98903494e+01],
            [9.64000000e-01, 7.13198881e+01, 7.08883348e+01, 7.17514414e+01],
            [9.65000000e-01, 7.32884885e+01, 7.28318664e+01, 7.37451106e+01],
            [9.66000000e-01, 7.53638098e+01, 7.48746273e+01, 7.58529923e+01],
            [9.67000000e-01, 7.75715305e+01, 7.70502464e+01, 7.80928146e+01],
            [9.68000000e-01, 7.99019665e+01, 7.93506885e+01, 8.04532445e+01],
            [9.69000000e-01, 8.23999443e+01, 8.18106358e+01, 8.29892528e+01],
            [9.70000000e-01, 8.50708167e+01, 8.44344388e+01, 8.57071945e+01],
            [9.71000000e-01, 8.78853012e+01, 8.72115952e+01, 8.85590072e+01],
            [9.72000000e-01, 9.09109647e+01, 9.01805319e+01, 9.16413974e+01],
            [9.73000000e-01, 9.41484946e+01, 9.33716781e+01, 9.49253110e+01],
            [9.74000000e-01, 9.76702640e+01, 9.68396410e+01, 9.85008870e+01],
            [9.75000000e-01, 1.01429145e+02, 1.00534896e+02, 1.02323394e+02],
            [9.76000000e-01, 1.05533611e+02, 1.04576251e+02, 1.06490971e+02],
            [9.77000000e-01, 1.09981358e+02, 1.08968054e+02, 1.10994661e+02],
            [9.78000000e-01, 1.14847196e+02, 1.13754119e+02, 1.15940272e+02],
            [9.79000000e-01, 1.20253918e+02, 1.19064180e+02, 1.21443657e+02],
            [9.80000000e-01, 1.26170118e+02, 1.24885712e+02, 1.27454523e+02],
            [9.81000000e-01, 1.32621383e+02, 1.31213450e+02, 1.34029316e+02],
            [9.82000000e-01, 1.39962878e+02, 1.38412603e+02, 1.41513153e+02],
            [9.83000000e-01, 1.48016331e+02, 1.46308389e+02, 1.49724274e+02],
            [9.84000000e-01, 1.57131456e+02, 1.55258248e+02, 1.59004665e+02],
            [9.85000000e-01, 1.67586165e+02, 1.65445404e+02, 1.69726925e+02],
            [9.86000000e-01, 1.79326537e+02, 1.76975048e+02, 1.81678026e+02],
            [9.87000000e-01, 1.92862919e+02, 1.90166647e+02, 1.95559192e+02],
            [9.88000000e-01, 2.08716917e+02, 2.05584293e+02, 2.11849541e+02],
            [9.89000000e-01, 2.27487522e+02, 2.23943087e+02, 2.31031957e+02],
            [9.90000000e-01, 2.49816681e+02, 2.45554510e+02, 2.54078853e+02],
            [9.91000000e-01, 2.77183581e+02, 2.72048675e+02, 2.82318486e+02],
            [9.92000000e-01, 3.11901903e+02, 3.05432488e+02, 3.18371318e+02],
            [9.93000000e-01, 3.56590566e+02, 3.48108125e+02, 3.65073008e+02],
            [9.94000000e-01, 4.14975490e+02, 4.03133868e+02, 4.26817112e+02],
            [9.95000000e-01, 4.97206607e+02, 4.80347087e+02, 5.14066126e+02],
            [9.96000000e-01, 6.18722418e+02, 5.92786837e+02, 6.44657998e+02],
            [9.97000000e-01, 8.15431498e+02, 7.73529640e+02, 8.57333357e+02],
            [9.98000000e-01, 1.20640297e+03, 1.12629899e+03, 1.28650696e+03],
            [9.99000000e-01, 2.40955978e+03, 2.15153441e+03, 2.66758514e+03]])
    questa.plotter.plot(
        data_5_10m_max_weight,
        data_5_10m_max_size,
        data_5_10m_msmw,
        data_5_10m_msmw_log,
        5,
        (0, 100),
        "out/5x5_10m.pdf"
    )
    questa.plotter.plot_scaled(
        data_5_10m_max_weight,
        data_5_10m_max_size,
        data_5_10m_msmw,
        data_5_10m_msmw_log,
        5,
        (0.8, 0.99),
        "out/5x5_10m_scaled.pdf"
    )
