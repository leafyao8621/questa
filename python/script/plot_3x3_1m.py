import numpy
import questa.plotter
import matplotlib.pyplot

if __name__ == "__main__":
    matplotlib.pyplot.rc('text', usetex=False)
    matplotlib.pyplot.rc('font', family='serif')
    data_3_1m_max_weight =\
        numpy.array([[1.00000000e-01, 3.22387600e-01, 3.22157086e-01, 3.22618114e-01],
            [2.00000000e-01, 6.99579700e-01, 6.99102977e-01, 7.00056423e-01],
            [3.00000000e-01, 1.15369150e+00, 1.15309940e+00, 1.15428360e+00],
            [4.00000000e-01, 1.72095083e+00, 1.72004943e+00, 1.72185224e+00],
            [5.00000000e-01, 2.46752777e+00, 2.46615043e+00, 2.46890510e+00],
            [6.00000000e-01, 3.52462620e+00, 3.52240295e+00, 3.52684945e+00],
            [7.00000000e-01, 5.18797563e+00, 5.18397257e+00, 5.19197869e+00],
            [8.00000000e-01, 8.30353053e+00, 8.29458124e+00, 8.31247982e+00],
            [9.00000000e-01, 1.69888663e+01, 1.69508106e+01, 1.70269220e+01],
            [9.10000000e-01, 1.88617409e+01, 1.88160450e+01, 1.89074367e+01],
            [9.20000000e-01, 2.12079195e+01, 2.11532785e+01, 2.12625605e+01],
            [9.30000000e-01, 2.42113927e+01, 2.41396478e+01, 2.42831376e+01],
            [9.40000000e-01, 2.81979491e+01, 2.81041875e+01, 2.82917107e+01],
            [9.50000000e-01, 3.37708823e+01, 3.36376863e+01, 3.39040783e+01],
            [9.60000000e-01, 4.20977978e+01, 4.18755891e+01, 4.23200066e+01],
            [9.61000000e-01, 4.31635146e+01, 4.29284255e+01, 4.33986037e+01],
            [9.62000000e-01, 4.42936397e+01, 4.40430226e+01, 4.45442569e+01],
            [9.63000000e-01, 4.54642987e+01, 4.51981236e+01, 4.57304738e+01],
            [9.64000000e-01, 4.67090824e+01, 4.64348457e+01, 4.69833191e+01],
            [9.65000000e-01, 4.80509686e+01, 4.77571691e+01, 4.83447682e+01],
            [9.66000000e-01, 4.94269506e+01, 4.91097339e+01, 4.97441673e+01],
            [9.67000000e-01, 5.08987224e+01, 5.05610893e+01, 5.12363555e+01],
            [9.68000000e-01, 5.24599682e+01, 5.21053873e+01, 5.28145491e+01],
            [9.69000000e-01, 5.41237279e+01, 5.37386063e+01, 5.45088495e+01],
            [9.70000000e-01, 5.59068792e+01, 5.54949287e+01, 5.63188297e+01],
            [9.71000000e-01, 5.78099923e+01, 5.73680099e+01, 5.82519746e+01],
            [9.72000000e-01, 5.98373647e+01, 5.93635038e+01, 6.03112256e+01],
            [9.73000000e-01, 6.20267341e+01, 6.15214120e+01, 6.25320561e+01],
            [9.74000000e-01, 6.43686248e+01, 6.38285874e+01, 6.49086623e+01],
            [9.75000000e-01, 6.68951585e+01, 6.63185582e+01, 6.74717588e+01],
            [9.76000000e-01, 6.96781198e+01, 6.90566231e+01, 7.02996164e+01],
            [9.77000000e-01, 7.26267139e+01, 7.19686784e+01, 7.32847494e+01],
            [9.78000000e-01, 7.58640976e+01, 7.51325495e+01, 7.65956457e+01],
            [9.79000000e-01, 7.94056676e+01, 7.86085093e+01, 8.02028259e+01],
            [9.80000000e-01, 8.33453102e+01, 8.24661579e+01, 8.42244625e+01],
            [9.81000000e-01, 8.76558460e+01, 8.66995297e+01, 8.86121624e+01],
            [9.82000000e-01, 9.24861479e+01, 9.14416160e+01, 9.35306798e+01],
            [9.83000000e-01, 9.79406025e+01, 9.67580090e+01, 9.91231959e+01],
            [9.84000000e-01, 1.04062180e+02, 1.02699922e+02, 1.05424438e+02],
            [9.85000000e-01, 1.10957896e+02, 1.09334009e+02, 1.12581783e+02],
            [9.86000000e-01, 1.18779402e+02, 1.16891861e+02, 1.20666942e+02],
            [9.87000000e-01, 1.27800629e+02, 1.25594845e+02, 1.30006412e+02],
            [9.88000000e-01, 1.38238378e+02, 1.35616518e+02, 1.40860238e+02],
            [9.89000000e-01, 1.50450959e+02, 1.47359211e+02, 1.53542706e+02],
            [9.90000000e-01, 1.65432635e+02, 1.61753177e+02, 1.69112093e+02],
            [9.91000000e-01, 1.83670738e+02, 1.79264465e+02, 1.88077011e+02],
            [9.92000000e-01, 2.06372483e+02, 2.01031671e+02, 2.11713295e+02],
            [9.93000000e-01, 2.34986072e+02, 2.28626011e+02, 2.41346133e+02],
            [9.94000000e-01, 2.72796433e+02, 2.64374545e+02, 2.81218321e+02],
            [9.95000000e-01, 3.23729735e+02, 3.11743023e+02, 3.35716448e+02],
            [9.96000000e-01, 4.01183992e+02, 3.82598444e+02, 4.19769541e+02],
            [9.97000000e-01, 5.26897312e+02, 4.94210407e+02, 5.59584218e+02],
            [9.98000000e-01, 7.81167861e+02, 7.05752501e+02, 8.56583220e+02],
            [9.99000000e-01, 1.41734667e+03, 1.22915284e+03, 1.60554051e+03]])
    data_3_1m_max_size =\
        numpy.array([[1.00000000e-01, 3.22392700e-01, 3.22162304e-01, 3.22623096e-01],
            [2.00000000e-01, 6.99721933e-01, 6.99247417e-01, 7.00196450e-01],
            [3.00000000e-01, 1.15456123e+00, 1.15397337e+00, 1.15514910e+00],
            [4.00000000e-01, 1.72388043e+00, 1.72294604e+00, 1.72481483e+00],
            [5.00000000e-01, 2.47548070e+00, 2.47400370e+00, 2.47695770e+00],
            [6.00000000e-01, 3.54715807e+00, 3.54487673e+00, 3.54943940e+00],
            [7.00000000e-01, 5.27746000e+00, 5.27259126e+00, 5.28232874e+00],
            [8.00000000e-01, 8.75224767e+00, 8.73894718e+00, 8.76554815e+00],
            [9.00000000e-01, 2.07247041e+01, 2.06212319e+01, 2.08281763e+01],
            [9.10000000e-01, 2.38949507e+01, 2.37454798e+01, 2.40444216e+01],
            [9.20000000e-01, 2.82777299e+01, 2.80429182e+01, 2.85125417e+01],
            [9.30000000e-01, 3.45941105e+01, 3.42071921e+01, 3.49810290e+01],
            [9.40000000e-01, 4.44723830e+01, 4.37202137e+01, 4.52245524e+01],
            [9.50000000e-01, 6.23091858e+01, 6.02683414e+01, 6.43500302e+01],
            [9.60000000e-01, 9.76867152e+01, 9.19909568e+01, 1.03382474e+02],
            [9.61000000e-01, 1.03706864e+02, 9.72065171e+01, 1.10207211e+02],
            [9.62000000e-01, 1.10623846e+02, 1.02171350e+02, 1.19076341e+02],
            [9.63000000e-01, 1.18362624e+02, 1.07990019e+02, 1.28735229e+02],
            [9.64000000e-01, 1.28273021e+02, 1.13416144e+02, 1.43129898e+02],
            [9.65000000e-01, 1.40759321e+02, 1.19304880e+02, 1.62213761e+02],
            [9.66000000e-01, 1.53147466e+02, 1.26855928e+02, 1.79439005e+02],
            [9.67000000e-01, 1.69033569e+02, 1.34418563e+02, 2.03648575e+02],
            [9.68000000e-01, 1.84237082e+02, 1.43490086e+02, 2.24984079e+02],
            [9.69000000e-01, 2.01474339e+02, 1.55139093e+02, 2.47809585e+02],
            [9.70000000e-01, 2.22113210e+02, 1.68277127e+02, 2.75949293e+02],
            [9.71000000e-01, 2.46356379e+02, 1.83580515e+02, 3.09132243e+02],
            [9.72000000e-01, 2.75297623e+02, 2.03373485e+02, 3.47221761e+02],
            [9.73000000e-01, 3.12078116e+02, 2.27997755e+02, 3.96158477e+02],
            [9.74000000e-01, 3.51454246e+02, 2.53703297e+02, 4.49205196e+02],
            [9.75000000e-01, 3.95292665e+02, 2.84180739e+02, 5.06404591e+02],
            [9.76000000e-01, 4.51489794e+02, 3.26163551e+02, 5.76816038e+02],
            [9.77000000e-01, 4.99718902e+02, 3.60710950e+02, 6.38726855e+02],
            [9.78000000e-01, 5.60054438e+02, 4.06132154e+02, 7.13976721e+02],
            [9.79000000e-01, 6.23501778e+02, 4.55405425e+02, 7.91598131e+02],
            [9.80000000e-01, 6.87052169e+02, 5.06442370e+02, 8.67661969e+02],
            [9.81000000e-01, 7.54746578e+02, 5.56563278e+02, 9.52929878e+02],
            [9.82000000e-01, 8.19513920e+02, 6.11214135e+02, 1.02781371e+03],
            [9.83000000e-01, 9.00112482e+02, 6.78813783e+02, 1.12141118e+03],
            [9.84000000e-01, 9.79518093e+02, 7.48634031e+02, 1.21040216e+03],
            [9.85000000e-01, 1.05037680e+03, 8.15668091e+02, 1.28508550e+03],
            [9.86000000e-01, 1.12829773e+03, 8.83645721e+02, 1.37294974e+03],
            [9.87000000e-01, 1.19205517e+03, 9.42147531e+02, 1.44196281e+03],
            [9.88000000e-01, 1.24399022e+03, 9.87342402e+02, 1.50063804e+03],
            [9.89000000e-01, 1.28895540e+03, 1.02835881e+03, 1.54955199e+03],
            [9.90000000e-01, 1.33467357e+03, 1.07323483e+03, 1.59611230e+03],
            [9.91000000e-01, 1.34975118e+03, 1.08400714e+03, 1.61549522e+03],
            [9.92000000e-01, 1.37380015e+03, 1.10524611e+03, 1.64235420e+03],
            [9.93000000e-01, 1.38445030e+03, 1.11740910e+03, 1.65149151e+03],
            [9.94000000e-01, 1.37595676e+03, 1.11014042e+03, 1.64177310e+03],
            [9.95000000e-01, 1.38234019e+03, 1.12022799e+03, 1.64445238e+03],
            [9.96000000e-01, 1.40187327e+03, 1.14633387e+03, 1.65741268e+03],
            [9.97000000e-01, 1.47504618e+03, 1.22772308e+03, 1.72236929e+03],
            [9.98000000e-01, 1.65565021e+03, 1.40687045e+03, 1.90442997e+03],
            [9.99000000e-01, 2.06598497e+03, 1.78085216e+03, 2.35111778e+03]])
    data_3_1m_msmw =\
        numpy.array([[1.00000000e-01, 3.22382833e-01, 3.22152466e-01, 3.22613201e-01],
            [2.00000000e-01, 6.99362567e-01, 6.98887663e-01, 6.99837470e-01],
            [3.00000000e-01, 1.15157297e+00, 1.15099321e+00, 1.15215272e+00],
            [4.00000000e-01, 1.70953407e+00, 1.70865613e+00, 1.71041200e+00],
            [5.00000000e-01, 2.42331647e+00, 2.42205777e+00, 2.42457517e+00],
            [6.00000000e-01, 3.38567543e+00, 3.38383084e+00, 3.38752003e+00],
            [7.00000000e-01, 4.80552377e+00, 4.80223691e+00, 4.80881062e+00],
            [8.00000000e-01, 7.31047587e+00, 7.30301971e+00, 7.31793202e+00],
            [9.00000000e-01, 1.41033148e+01, 1.40714357e+01, 1.41351938e+01],
            [9.10000000e-01, 1.55671222e+01, 1.55288457e+01, 1.56053987e+01],
            [9.20000000e-01, 1.73921067e+01, 1.73482198e+01, 1.74359936e+01],
            [9.30000000e-01, 1.97420313e+01, 1.96827380e+01, 1.98013246e+01],
            [9.40000000e-01, 2.28592841e+01, 2.27834029e+01, 2.29351654e+01],
            [9.50000000e-01, 2.72186122e+01, 2.71112958e+01, 2.73259286e+01],
            [9.60000000e-01, 3.37465081e+01, 3.35668885e+01, 3.39261277e+01],
            [9.61000000e-01, 3.45813634e+01, 3.43900433e+01, 3.47726835e+01],
            [9.62000000e-01, 3.54704524e+01, 3.52636614e+01, 3.56772434e+01],
            [9.63000000e-01, 3.63879086e+01, 3.61680765e+01, 3.66077407e+01],
            [9.64000000e-01, 3.73678912e+01, 3.71418664e+01, 3.75939160e+01],
            [9.65000000e-01, 3.84064493e+01, 3.81645101e+01, 3.86483886e+01],
            [9.66000000e-01, 3.94869770e+01, 3.92253988e+01, 3.97485552e+01],
            [9.67000000e-01, 4.06545537e+01, 4.03774129e+01, 4.09316945e+01],
            [9.68000000e-01, 4.18798593e+01, 4.15861102e+01, 4.21736084e+01],
            [9.69000000e-01, 4.31988810e+01, 4.28849643e+01, 4.35127977e+01],
            [9.70000000e-01, 4.45942966e+01, 4.42509504e+01, 4.49376427e+01],
            [9.71000000e-01, 4.61018653e+01, 4.57367804e+01, 4.64669502e+01],
            [9.72000000e-01, 4.77102066e+01, 4.73183561e+01, 4.81020572e+01],
            [9.73000000e-01, 4.94280251e+01, 4.90098978e+01, 4.98461523e+01],
            [9.74000000e-01, 5.12867224e+01, 5.08381439e+01, 5.17353009e+01],
            [9.75000000e-01, 5.32679023e+01, 5.27886201e+01, 5.37471845e+01],
            [9.76000000e-01, 5.54622050e+01, 5.49468114e+01, 5.59775985e+01],
            [9.77000000e-01, 5.77975901e+01, 5.72495941e+01, 5.83455861e+01],
            [9.78000000e-01, 6.03669076e+01, 5.97633688e+01, 6.09704463e+01],
            [9.79000000e-01, 6.31617530e+01, 6.25068105e+01, 6.38166954e+01],
            [9.80000000e-01, 6.62468445e+01, 6.55235679e+01, 6.69701211e+01],
            [9.81000000e-01, 6.96868456e+01, 6.88934247e+01, 7.04802664e+01],
            [9.82000000e-01, 7.35061276e+01, 7.26327283e+01, 7.43795269e+01],
            [9.83000000e-01, 7.77477713e+01, 7.67658055e+01, 7.87297371e+01],
            [9.84000000e-01, 8.26203802e+01, 8.14836051e+01, 8.37571552e+01],
            [9.85000000e-01, 8.81220615e+01, 8.67863831e+01, 8.94577400e+01],
            [9.86000000e-01, 9.43329637e+01, 9.27804057e+01, 9.58855217e+01],
            [9.87000000e-01, 1.01481721e+02, 9.96564181e+01, 1.03307024e+02],
            [9.88000000e-01, 1.09812447e+02, 1.07645050e+02, 1.11979845e+02],
            [9.89000000e-01, 1.19526149e+02, 1.16965212e+02, 1.22087086e+02],
            [9.90000000e-01, 1.31394622e+02, 1.28313268e+02, 1.34475976e+02],
            [9.91000000e-01, 1.45839625e+02, 1.42201298e+02, 1.49477952e+02],
            [9.92000000e-01, 1.63892024e+02, 1.59426159e+02, 1.68357889e+02],
            [9.93000000e-01, 1.86864317e+02, 1.81575822e+02, 1.92152813e+02],
            [9.94000000e-01, 2.17461164e+02, 2.10482222e+02, 2.24440105e+02],
            [9.95000000e-01, 2.58219476e+02, 2.48285271e+02, 2.68153682e+02],
            [9.96000000e-01, 3.20513698e+02, 3.04794043e+02, 3.36233352e+02],
            [9.97000000e-01, 4.21732583e+02, 3.94755768e+02, 4.48709397e+02],
            [9.98000000e-01, 6.29699594e+02, 5.64988924e+02, 6.94410265e+02],
            [9.99000000e-01, 1.16062866e+03, 9.91671698e+02, 1.32958563e+03]])

    data_3_1m_msmw_log =\
        numpy.array([[1.00000000e-01, 3.39593027e+00, 3.39464835e+00, 3.39721219e+00],
            [2.00000000e-01, 3.75342727e+00, 3.75208134e+00, 3.75477320e+00],
            [3.00000000e-01, 4.14345630e+00, 4.14242061e+00, 4.14449199e+00],
            [4.00000000e-01, 4.58713510e+00, 4.58614836e+00, 4.58812184e+00],
            [5.00000000e-01, 5.11647457e+00, 5.11533466e+00, 5.11761447e+00],
            [6.00000000e-01, 5.80746567e+00, 5.80599487e+00, 5.80893646e+00],
            [7.00000000e-01, 6.84231687e+00, 6.84000411e+00, 6.84462962e+00],
            [8.00000000e-01, 8.80182540e+00, 8.79582099e+00, 8.80782981e+00],
            [9.00000000e-01, 1.47625064e+01, 1.47322800e+01, 1.47927328e+01],
            [9.10000000e-01, 1.61186616e+01, 1.60818056e+01, 1.61555176e+01],
            [9.20000000e-01, 1.78240228e+01, 1.77795623e+01, 1.78684832e+01],
            [9.30000000e-01, 2.00465522e+01, 1.99893245e+01, 2.01037799e+01],
            [9.40000000e-01, 2.30247559e+01, 2.29509324e+01, 2.30985794e+01],
            [9.50000000e-01, 2.72285378e+01, 2.71245148e+01, 2.73325608e+01],
            [9.60000000e-01, 3.35574745e+01, 3.33826803e+01, 3.37322687e+01],
            [9.61000000e-01, 3.43728477e+01, 3.41854344e+01, 3.45602610e+01],
            [9.62000000e-01, 3.52341593e+01, 3.50338672e+01, 3.54344514e+01],
            [9.63000000e-01, 3.61321681e+01, 3.59197757e+01, 3.63445605e+01],
            [9.64000000e-01, 3.70852990e+01, 3.68639116e+01, 3.73066863e+01],
            [9.65000000e-01, 3.80990253e+01, 3.78657730e+01, 3.83322777e+01],
            [9.66000000e-01, 3.91604933e+01, 3.89070720e+01, 3.94139146e+01],
            [9.67000000e-01, 4.02914491e+01, 4.00201123e+01, 4.05627859e+01],
            [9.68000000e-01, 4.14833612e+01, 4.12026718e+01, 4.17640506e+01],
            [9.69000000e-01, 4.27685503e+01, 4.24626725e+01, 4.30744282e+01],
            [9.70000000e-01, 4.41360994e+01, 4.38088873e+01, 4.44633114e+01],
            [9.71000000e-01, 4.55972268e+01, 4.52454296e+01, 4.59490240e+01],
            [9.72000000e-01, 4.71751473e+01, 4.67955679e+01, 4.75547267e+01],
            [9.73000000e-01, 4.88570511e+01, 4.84525770e+01, 4.92615252e+01],
            [9.74000000e-01, 5.06617076e+01, 5.02267259e+01, 5.10966893e+01],
            [9.75000000e-01, 5.25894584e+01, 5.21251508e+01, 5.30537661e+01],
            [9.76000000e-01, 5.47238058e+01, 5.42244693e+01, 5.52231423e+01],
            [9.77000000e-01, 5.69850563e+01, 5.64592412e+01, 5.75108713e+01],
            [9.78000000e-01, 5.94770275e+01, 5.88946649e+01, 6.00593901e+01],
            [9.79000000e-01, 6.21950182e+01, 6.15656567e+01, 6.28243797e+01],
            [9.80000000e-01, 6.52295122e+01, 6.45363621e+01, 6.59226623e+01],
            [9.81000000e-01, 6.85445693e+01, 6.77859351e+01, 6.93032035e+01],
            [9.82000000e-01, 7.22683085e+01, 7.14377054e+01, 7.30989116e+01],
            [9.83000000e-01, 7.64225139e+01, 7.54916889e+01, 7.73533389e+01],
            [9.84000000e-01, 8.11563718e+01, 8.00840389e+01, 8.22287046e+01],
            [9.85000000e-01, 8.64861804e+01, 8.52152462e+01, 8.77571146e+01],
            [9.86000000e-01, 9.25159854e+01, 9.10382866e+01, 9.39936841e+01],
            [9.87000000e-01, 9.94646129e+01, 9.77370040e+01, 1.01192222e+02],
            [9.88000000e-01, 1.07544618e+02, 1.05484734e+02, 1.09604502e+02],
            [9.89000000e-01, 1.16980185e+02, 1.14533576e+02, 1.19426794e+02],
            [9.90000000e-01, 1.28455087e+02, 1.25520209e+02, 1.31389965e+02],
            [9.91000000e-01, 1.42303207e+02, 1.38852473e+02, 1.45753942e+02],
            [9.92000000e-01, 1.59701131e+02, 1.55438787e+02, 1.63963476e+02],
            [9.93000000e-01, 1.81703610e+02, 1.76602300e+02, 1.86804921e+02],
            [9.94000000e-01, 2.11081883e+02, 2.04369854e+02, 2.17793912e+02],
            [9.95000000e-01, 2.50594134e+02, 2.41046892e+02, 2.60141376e+02],
            [9.96000000e-01, 3.10035374e+02, 2.95126039e+02, 3.24944709e+02],
            [9.97000000e-01, 4.07203666e+02, 3.81659200e+02, 4.32748131e+02],
            [9.98000000e-01, 6.06990626e+02, 5.45880614e+02, 6.68100638e+02],
            [9.99000000e-01, 1.10688488e+03, 9.46854263e+02, 1.26691551e+03]])
    questa.plotter.plot(
        data_3_1m_max_weight,
        data_3_1m_max_size,
        data_3_1m_msmw,
        data_3_1m_msmw_log,
        3,
        (0, 50),
        "out/3x3_1m.pdf"
    )
    questa.plotter.plot_scaled(
        data_3_1m_max_weight,
        data_3_1m_max_size,
        data_3_1m_msmw,
        data_3_1m_msmw_log,
        3,
        (0.8, 0.99),
        "out/3x3_1m_scaled.pdf"
    )
