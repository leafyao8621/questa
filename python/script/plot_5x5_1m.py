import numpy
import questa.plotter
import matplotlib.pyplot

if __name__ == "__main__":
    matplotlib.pyplot.rc('text', usetex=False)
    matplotlib.pyplot.rc('font', family='serif')
    data_5_1m_max_weight =\
        numpy.array([[1.00000000e-01, 5.44225800e-01, 5.43873909e-01, 5.44577691e-01],
            [2.00000000e-01, 1.19808230e+00, 1.19747852e+00, 1.19868608e+00],
            [3.00000000e-01, 2.00344720e+00, 2.00258198e+00, 2.00431242e+00],
            [4.00000000e-01, 3.03067497e+00, 3.02928500e+00, 3.03206493e+00],
            [5.00000000e-01, 4.40720827e+00, 4.40508924e+00, 4.40932730e+00],
            [6.00000000e-01, 6.40387787e+00, 6.40045434e+00, 6.40730139e+00],
            [7.00000000e-01, 9.67965103e+00, 9.67352242e+00, 9.68577965e+00],
            [8.00000000e-01, 1.62018920e+01, 1.61889581e+01, 1.62148259e+01],
            [9.00000000e-01, 3.49728726e+01, 3.49161375e+01, 3.50296077e+01],
            [9.10000000e-01, 3.90277355e+01, 3.89568764e+01, 3.90985946e+01],
            [9.20000000e-01, 4.40655118e+01, 4.39745726e+01, 4.41564510e+01],
            [9.30000000e-01, 5.05258187e+01, 5.04110920e+01, 5.06405455e+01],
            [9.40000000e-01, 5.91376121e+01, 5.89656145e+01, 5.93096097e+01],
            [9.50000000e-01, 7.11785875e+01, 7.09375905e+01, 7.14195846e+01],
            [9.60000000e-01, 8.92039189e+01, 8.88045644e+01, 8.96032734e+01],
            [9.61000000e-01, 9.14976006e+01, 9.10811731e+01, 9.19140282e+01],
            [9.62000000e-01, 9.39173792e+01, 9.34696036e+01, 9.43651548e+01],
            [9.63000000e-01, 9.64739779e+01, 9.60028333e+01, 9.69451225e+01],
            [9.64000000e-01, 9.91665741e+01, 9.86722763e+01, 9.96608719e+01],
            [9.65000000e-01, 1.02045994e+02, 1.01520978e+02, 1.02571010e+02],
            [9.66000000e-01, 1.05081123e+02, 1.04525421e+02, 1.05636825e+02],
            [9.67000000e-01, 1.08284732e+02, 1.07694244e+02, 1.08875219e+02],
            [9.68000000e-01, 1.11727854e+02, 1.11094329e+02, 1.12361378e+02],
            [9.69000000e-01, 1.15375348e+02, 1.14691753e+02, 1.16058943e+02],
            [9.70000000e-01, 1.19258609e+02, 1.18517945e+02, 1.19999274e+02],
            [9.71000000e-01, 1.23397353e+02, 1.22602674e+02, 1.24192032e+02],
            [9.72000000e-01, 1.27874257e+02, 1.27005950e+02, 1.28742563e+02],
            [9.73000000e-01, 1.32718340e+02, 1.31767900e+02, 1.33668780e+02],
            [9.74000000e-01, 1.37865628e+02, 1.36818509e+02, 1.38912747e+02],
            [9.75000000e-01, 1.43446113e+02, 1.42331637e+02, 1.44560590e+02],
            [9.76000000e-01, 1.49490910e+02, 1.48271495e+02, 1.50710326e+02],
            [9.77000000e-01, 1.56093349e+02, 1.54743193e+02, 1.57443505e+02],
            [9.78000000e-01, 1.63334979e+02, 1.61877667e+02, 1.64792290e+02],
            [9.79000000e-01, 1.71140241e+02, 1.69529013e+02, 1.72751470e+02],
            [9.80000000e-01, 1.79847245e+02, 1.78074690e+02, 1.81619801e+02],
            [9.81000000e-01, 1.89347182e+02, 1.87410103e+02, 1.91284262e+02],
            [9.82000000e-01, 2.00078581e+02, 1.97949628e+02, 2.02207533e+02],
            [9.83000000e-01, 2.12064103e+02, 2.09693964e+02, 2.14434243e+02],
            [9.84000000e-01, 2.25409297e+02, 2.22752260e+02, 2.28066333e+02],
            [9.85000000e-01, 2.40638213e+02, 2.37691198e+02, 2.43585227e+02],
            [9.86000000e-01, 2.57897738e+02, 2.54542609e+02, 2.61252866e+02],
            [9.87000000e-01, 2.77952106e+02, 2.74085188e+02, 2.81819024e+02],
            [9.88000000e-01, 3.01252526e+02, 2.96692758e+02, 3.05812294e+02],
            [9.89000000e-01, 3.28790385e+02, 3.23362031e+02, 3.34218740e+02],
            [9.90000000e-01, 3.61775222e+02, 3.55175629e+02, 3.68374815e+02],
            [9.91000000e-01, 4.02814536e+02, 3.94469638e+02, 4.11159433e+02],
            [9.92000000e-01, 4.54377377e+02, 4.43903862e+02, 4.64850891e+02],
            [9.93000000e-01, 5.21173948e+02, 5.07334206e+02, 5.35013690e+02],
            [9.94000000e-01, 6.09955036e+02, 5.91089960e+02, 6.28820112e+02],
            [9.95000000e-01, 7.32506533e+02, 7.04885264e+02, 7.60127801e+02],
            [9.96000000e-01, 9.14784657e+02, 8.72828091e+02, 9.56741223e+02],
            [9.97000000e-01, 1.21081124e+03, 1.14301949e+03, 1.27860298e+03],
            [9.98000000e-01, 1.75504676e+03, 1.63494304e+03, 1.87515047e+03],
            [9.99000000e-01, 3.03004302e+03, 2.81314606e+03, 3.24693998e+03]])
    data_5_1m_max_size =\
        numpy.array([[1.00000000e-01, 5.44231867e-01, 5.43879574e-01, 5.44584160e-01],
            [2.00000000e-01, 1.19821540e+00, 1.19760818e+00, 1.19882262e+00],
            [3.00000000e-01, 2.00383133e+00, 2.00295567e+00, 2.00470699e+00],
            [4.00000000e-01, 3.02876913e+00, 3.02735320e+00, 3.03018507e+00],
            [5.00000000e-01, 4.38877120e+00, 4.38664828e+00, 4.39089412e+00],
            [6.00000000e-01, 6.31049810e+00, 6.30725645e+00, 6.31373975e+00],
            [7.00000000e-01, 9.31544500e+00, 9.30935466e+00, 9.32153534e+00],
            [8.00000000e-01, 1.49988484e+01, 1.49871694e+01, 1.50105275e+01],
            [9.00000000e-01, 3.17235671e+01, 3.16693681e+01, 3.17777661e+01],
            [9.10000000e-01, 3.54860559e+01, 3.54094595e+01, 3.55626522e+01],
            [9.20000000e-01, 4.02211173e+01, 4.01188479e+01, 4.03233866e+01],
            [9.30000000e-01, 4.63456447e+01, 4.62121906e+01, 4.64790989e+01],
            [9.40000000e-01, 5.46449782e+01, 5.44412579e+01, 5.48486984e+01],
            [9.50000000e-01, 6.64826615e+01, 6.61613759e+01, 6.68039470e+01],
            [9.60000000e-01, 8.47601838e+01, 8.42387540e+01, 8.52816135e+01],
            [9.61000000e-01, 8.71066043e+01, 8.65368881e+01, 8.76763205e+01],
            [9.62000000e-01, 8.95532440e+01, 8.89529815e+01, 9.01535065e+01],
            [9.63000000e-01, 9.21730070e+01, 9.15250188e+01, 9.28209953e+01],
            [9.64000000e-01, 9.49001346e+01, 9.41903042e+01, 9.56099650e+01],
            [9.65000000e-01, 9.80185625e+01, 9.72779912e+01, 9.87591339e+01],
            [9.66000000e-01, 1.01235384e+02, 1.00463302e+02, 1.02007465e+02],
            [9.67000000e-01, 1.04475240e+02, 1.03669599e+02, 1.05280880e+02],
            [9.68000000e-01, 1.08113423e+02, 1.07228534e+02, 1.08998313e+02],
            [9.69000000e-01, 1.11951703e+02, 1.11012224e+02, 1.12891182e+02],
            [9.70000000e-01, 1.16128836e+02, 1.15115760e+02, 1.17141912e+02],
            [9.71000000e-01, 1.20534157e+02, 1.19409628e+02, 1.21658686e+02],
            [9.72000000e-01, 1.25497743e+02, 1.24292217e+02, 1.26703269e+02],
            [9.73000000e-01, 1.30523517e+02, 1.29194859e+02, 1.31852175e+02],
            [9.74000000e-01, 1.36119242e+02, 1.34688791e+02, 1.37549694e+02],
            [9.75000000e-01, 1.42385624e+02, 1.40735798e+02, 1.44035450e+02],
            [9.76000000e-01, 1.48961166e+02, 1.47137640e+02, 1.50784692e+02],
            [9.77000000e-01, 1.56271108e+02, 1.54255064e+02, 1.58287151e+02],
            [9.78000000e-01, 1.63982823e+02, 1.61830783e+02, 1.66134863e+02],
            [9.79000000e-01, 1.72909809e+02, 1.70369876e+02, 1.75449742e+02],
            [9.80000000e-01, 1.82834692e+02, 1.79954143e+02, 1.85715241e+02],
            [9.81000000e-01, 1.93567077e+02, 1.90134823e+02, 1.96999331e+02],
            [9.82000000e-01, 2.05920942e+02, 2.02166618e+02, 2.09675266e+02],
            [9.83000000e-01, 2.19537319e+02, 2.15149218e+02, 2.23925420e+02],
            [9.84000000e-01, 2.35071354e+02, 2.30188506e+02, 2.39954202e+02],
            [9.85000000e-01, 2.53247038e+02, 2.47565340e+02, 2.58928735e+02],
            [9.86000000e-01, 2.72742738e+02, 2.66111839e+02, 2.79373636e+02],
            [9.87000000e-01, 2.96639396e+02, 2.89025862e+02, 3.04252930e+02],
            [9.88000000e-01, 3.24749476e+02, 3.15640016e+02, 3.33858935e+02],
            [9.89000000e-01, 3.57396783e+02, 3.46612953e+02, 3.68180613e+02],
            [9.90000000e-01, 3.97739938e+02, 3.84977414e+02, 4.10502462e+02],
            [9.91000000e-01, 4.46902804e+02, 4.31132720e+02, 4.62672888e+02],
            [9.92000000e-01, 5.09763239e+02, 4.89983223e+02, 5.29543255e+02],
            [9.93000000e-01, 5.91798061e+02, 5.66420779e+02, 6.17175343e+02],
            [9.94000000e-01, 6.99945091e+02, 6.66612731e+02, 7.33277451e+02],
            [9.95000000e-01, 8.45531322e+02, 8.03740636e+02, 8.87322009e+02],
            [9.96000000e-01, 1.07509617e+03, 1.01508338e+03, 1.13510895e+03],
            [9.97000000e-01, 1.44859232e+03, 1.34096334e+03, 1.55622129e+03],
            [9.98000000e-01, 2.08467615e+03, 1.90021008e+03, 2.26914222e+03],
            [9.99000000e-01, 3.26346891e+03, 3.00039337e+03, 3.52654445e+03]])
    data_5_1m_msmw =\
        numpy.array([[1.00000000e-01, 5.44215033e-01, 5.43863031e-01, 5.44567035e-01],
            [2.00000000e-01, 1.19769313e+00, 1.19708926e+00, 1.19829701e+00],
            [3.00000000e-01, 1.99974103e+00, 1.99887680e+00, 2.00060527e+00],
            [4.00000000e-01, 3.01064487e+00, 3.00927588e+00, 3.01201386e+00],
            [5.00000000e-01, 4.32780960e+00, 4.32587887e+00, 4.32974033e+00],
            [6.00000000e-01, 6.13728943e+00, 6.13462479e+00, 6.13995408e+00],
            [7.00000000e-01, 8.85909247e+00, 8.85402521e+00, 8.86415973e+00],
            [8.00000000e-01, 1.37508974e+01, 1.37412373e+01, 1.37605574e+01],
            [9.00000000e-01, 2.70997304e+01, 2.70572581e+01, 2.71422027e+01],
            [9.10000000e-01, 2.99785830e+01, 2.99247912e+01, 3.00323748e+01],
            [9.20000000e-01, 3.35652551e+01, 3.34960507e+01, 3.36344594e+01],
            [9.30000000e-01, 3.81509004e+01, 3.80618657e+01, 3.82399350e+01],
            [9.40000000e-01, 4.42579256e+01, 4.41286337e+01, 4.43872174e+01],
            [9.50000000e-01, 5.28061023e+01, 5.26227648e+01, 5.29894397e+01],
            [9.60000000e-01, 6.56204984e+01, 6.53211613e+01, 6.59198355e+01],
            [9.61000000e-01, 6.72539351e+01, 6.69352102e+01, 6.75726600e+01],
            [9.62000000e-01, 6.89823380e+01, 6.86448962e+01, 6.93197798e+01],
            [9.63000000e-01, 7.07950310e+01, 7.04424033e+01, 7.11476587e+01],
            [9.64000000e-01, 7.27144978e+01, 7.23492185e+01, 7.30797771e+01],
            [9.65000000e-01, 7.47635438e+01, 7.43726419e+01, 7.51544457e+01],
            [9.66000000e-01, 7.69209802e+01, 7.65078923e+01, 7.73340681e+01],
            [9.67000000e-01, 7.91974548e+01, 7.87619364e+01, 7.96329732e+01],
            [9.68000000e-01, 8.16209727e+01, 8.11568589e+01, 8.20850865e+01],
            [9.69000000e-01, 8.42404749e+01, 8.37302508e+01, 8.47506990e+01],
            [9.70000000e-01, 8.70053710e+01, 8.64555245e+01, 8.75552175e+01],
            [9.71000000e-01, 8.99670005e+01, 8.93674890e+01, 9.05665120e+01],
            [9.72000000e-01, 9.31274581e+01, 9.24756731e+01, 9.37792431e+01],
            [9.73000000e-01, 9.65692823e+01, 9.58530371e+01, 9.72855275e+01],
            [9.74000000e-01, 1.00224364e+02, 9.94320369e+01, 1.01016691e+02],
            [9.75000000e-01, 1.04198761e+02, 1.03350290e+02, 1.05047231e+02],
            [9.76000000e-01, 1.08523913e+02, 1.07605512e+02, 1.09442313e+02],
            [9.77000000e-01, 1.13223391e+02, 1.12205834e+02, 1.14240948e+02],
            [9.78000000e-01, 1.18366554e+02, 1.17263355e+02, 1.19469752e+02],
            [9.79000000e-01, 1.23979756e+02, 1.22761283e+02, 1.25198228e+02],
            [9.80000000e-01, 1.30200139e+02, 1.28860952e+02, 1.31539326e+02],
            [9.81000000e-01, 1.37037824e+02, 1.35557162e+02, 1.38518486e+02],
            [9.82000000e-01, 1.44677352e+02, 1.43074998e+02, 1.46279707e+02],
            [9.83000000e-01, 1.53251205e+02, 1.51481692e+02, 1.55020717e+02],
            [9.84000000e-01, 1.62826947e+02, 1.60847697e+02, 1.64806196e+02],
            [9.85000000e-01, 1.73730024e+02, 1.71529778e+02, 1.75930271e+02],
            [9.86000000e-01, 1.86236269e+02, 1.83697224e+02, 1.88775315e+02],
            [9.87000000e-01, 2.00669014e+02, 1.97734658e+02, 2.03603371e+02],
            [9.88000000e-01, 2.17439633e+02, 2.13987866e+02, 2.20891400e+02],
            [9.89000000e-01, 2.37335868e+02, 2.33185340e+02, 2.41486397e+02],
            [9.90000000e-01, 2.61327262e+02, 2.56234349e+02, 2.66420174e+02],
            [9.91000000e-01, 2.90931321e+02, 2.84476778e+02, 2.97385864e+02],
            [9.92000000e-01, 3.28124849e+02, 3.20066098e+02, 3.36183600e+02],
            [9.93000000e-01, 3.76916009e+02, 3.66622001e+02, 3.87210016e+02],
            [9.94000000e-01, 4.41643111e+02, 4.27746491e+02, 4.55539731e+02],
            [9.95000000e-01, 5.31797170e+02, 5.11468064e+02, 5.52126276e+02],
            [9.96000000e-01, 6.65063748e+02, 6.33559200e+02, 6.96568296e+02],
            [9.97000000e-01, 8.85307957e+02, 8.33277452e+02, 9.37338463e+02],
            [9.98000000e-01, 1.29299627e+03, 1.19572387e+03, 1.39026867e+03],
            [9.99000000e-01, 2.28929236e+03, 2.10553736e+03, 2.47304737e+03]])
    data_5_1m_msmw_log =\
        numpy.array([[1.00000000e-01, 6.86716800e+00, 6.86271938e+00, 6.87161662e+00],
            [2.00000000e-01, 7.54100297e+00, 7.53780241e+00, 7.54420353e+00],
            [3.00000000e-01, 8.26362313e+00, 8.26113666e+00, 8.26610961e+00],
            [4.00000000e-01, 9.06669480e+00, 9.06468989e+00, 9.06869971e+00],
            [5.00000000e-01, 1.00058116e+01, 1.00036563e+01, 1.00079669e+01],
            [6.00000000e-01, 1.12052121e+01, 1.12033044e+01, 1.12071198e+01],
            [7.00000000e-01, 1.30079804e+01, 1.30041722e+01, 1.30117886e+01],
            [8.00000000e-01, 1.65805049e+01, 1.65732743e+01, 1.65877354e+01],
            [9.00000000e-01, 2.80522091e+01, 2.80147344e+01, 2.80896839e+01],
            [9.10000000e-01, 3.06923419e+01, 3.06426763e+01, 3.07420075e+01],
            [9.20000000e-01, 3.40168076e+01, 3.39507824e+01, 3.40828329e+01],
            [9.30000000e-01, 3.83252796e+01, 3.82441198e+01, 3.84064394e+01],
            [9.40000000e-01, 4.41173943e+01, 4.39972414e+01, 4.42375472e+01],
            [9.50000000e-01, 5.22829898e+01, 5.21047946e+01, 5.24611850e+01],
            [9.60000000e-01, 6.46456043e+01, 6.43601888e+01, 6.49310199e+01],
            [9.61000000e-01, 6.62216581e+01, 6.59171021e+01, 6.65262142e+01],
            [9.62000000e-01, 6.78862943e+01, 6.75650245e+01, 6.82075641e+01],
            [9.63000000e-01, 6.96457431e+01, 6.93071959e+01, 6.99842902e+01],
            [9.64000000e-01, 7.15031385e+01, 7.11469787e+01, 7.18592982e+01],
            [9.65000000e-01, 7.34940908e+01, 7.31172274e+01, 7.38709542e+01],
            [9.66000000e-01, 7.55782245e+01, 7.51772318e+01, 7.59792172e+01],
            [9.67000000e-01, 7.77937199e+01, 7.73656174e+01, 7.82218224e+01],
            [9.68000000e-01, 8.01467570e+01, 7.96898930e+01, 8.06036209e+01],
            [9.69000000e-01, 8.26719979e+01, 8.21819333e+01, 8.31620625e+01],
            [9.70000000e-01, 8.53487718e+01, 8.48199308e+01, 8.58776128e+01],
            [9.71000000e-01, 8.82311150e+01, 8.76528927e+01, 8.88093374e+01],
            [9.72000000e-01, 9.13024996e+01, 9.06839320e+01, 9.19210673e+01],
            [9.73000000e-01, 9.46533273e+01, 9.39670746e+01, 9.53395800e+01],
            [9.74000000e-01, 9.81875085e+01, 9.74283886e+01, 9.89466285e+01],
            [9.75000000e-01, 1.02069307e+02, 1.01259924e+02, 1.02878691e+02],
            [9.76000000e-01, 1.06237734e+02, 1.05364082e+02, 1.07111387e+02],
            [9.77000000e-01, 1.10794981e+02, 1.09829234e+02, 1.11760728e+02],
            [9.78000000e-01, 1.15782282e+02, 1.14722997e+02, 1.16841567e+02],
            [9.79000000e-01, 1.21224503e+02, 1.20066546e+02, 1.22382461e+02],
            [9.80000000e-01, 1.27259738e+02, 1.26000370e+02, 1.28519107e+02],
            [9.81000000e-01, 1.33860602e+02, 1.32477015e+02, 1.35244188e+02],
            [9.82000000e-01, 1.41290761e+02, 1.39789331e+02, 1.42792190e+02],
            [9.83000000e-01, 1.49549668e+02, 1.47884827e+02, 1.51214509e+02],
            [9.84000000e-01, 1.58830540e+02, 1.56968880e+02, 1.60692200e+02],
            [9.85000000e-01, 1.69387584e+02, 1.67315101e+02, 1.71460066e+02],
            [9.86000000e-01, 1.81489131e+02, 1.79104164e+02, 1.83874098e+02],
            [9.87000000e-01, 1.95395566e+02, 1.92645270e+02, 1.98145862e+02],
            [9.88000000e-01, 2.11576008e+02, 2.08299689e+02, 2.14852326e+02],
            [9.89000000e-01, 2.30816942e+02, 2.26921277e+02, 2.34712607e+02],
            [9.90000000e-01, 2.53795223e+02, 2.49035521e+02, 2.58554924e+02],
            [9.91000000e-01, 2.82149508e+02, 2.76154853e+02, 2.88144162e+02],
            [9.92000000e-01, 3.17682531e+02, 3.10198350e+02, 3.25166712e+02],
            [9.93000000e-01, 3.64114711e+02, 3.54432693e+02, 3.73796729e+02],
            [9.94000000e-01, 4.26085831e+02, 4.12983273e+02, 4.39188389e+02],
            [9.95000000e-01, 5.11578869e+02, 4.92476140e+02, 5.30681599e+02],
            [9.96000000e-01, 6.38269504e+02, 6.08323554e+02, 6.68215454e+02],
            [9.97000000e-01, 8.45904139e+02, 7.96543600e+02, 8.95264678e+02],
            [9.98000000e-01, 1.23396084e+03, 1.14210683e+03, 1.32581486e+03],
            [9.99000000e-01, 2.18978698e+03, 2.01305200e+03, 2.36652195e+03]])
    questa.plotter.plot(
        data_5_1m_max_weight,
        data_5_1m_max_size,
        data_5_1m_msmw,
        data_5_1m_msmw_log,
        5,
        (0, 100),
        "out/5x5_1m.pdf"
    )
    questa.plotter.plot_scaled(
        data_5_1m_max_weight,
        data_5_1m_max_size,
        data_5_1m_msmw,
        data_5_1m_msmw_log,
        5,
        (0.8, 0.99),
        "out/5x5_1m_scaled.pdf"
    )
