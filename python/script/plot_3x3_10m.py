import numpy
import questa.plotter
import matplotlib.pyplot

if __name__ == "__main__":
    matplotlib.pyplot.rc('text', usetex=False)
    matplotlib.pyplot.rc('font', family='serif')

    data_3_10m_max_weight =\
        numpy.array([[1.00000000e-01, 3.22110300e-01, 3.21791057e-01, 3.22429543e-01],
            [2.00000000e-01, 6.99006033e-01, 6.98589271e-01, 6.99422795e-01],
            [3.00000000e-01, 1.15251933e+00, 1.15179750e+00, 1.15324116e+00],
            [4.00000000e-01, 1.71987053e+00, 1.71879747e+00, 1.72094359e+00],
            [5.00000000e-01, 2.46636510e+00, 2.46470623e+00, 2.46802397e+00],
            [6.00000000e-01, 3.52416347e+00, 3.52169257e+00, 3.52663436e+00],
            [7.00000000e-01, 5.18732797e+00, 5.18306046e+00, 5.19159547e+00],
            [8.00000000e-01, 8.30281717e+00, 8.29538049e+00, 8.31025385e+00],
            [9.00000000e-01, 1.69816987e+01, 1.69486233e+01, 1.70147741e+01],
            [9.10000000e-01, 1.88610036e+01, 1.88194890e+01, 1.89025181e+01],
            [9.20000000e-01, 2.11997510e+01, 2.11453426e+01, 2.12541594e+01],
            [9.30000000e-01, 2.41979546e+01, 2.41311423e+01, 2.42647670e+01],
            [9.40000000e-01, 2.82033734e+01, 2.81168654e+01, 2.82898814e+01],
            [9.50000000e-01, 3.37806420e+01, 3.36527211e+01, 3.39085630e+01],
            [9.60000000e-01, 4.21381385e+01, 4.19484160e+01, 4.23278610e+01],
            [9.61000000e-01, 4.32166571e+01, 4.30197424e+01, 4.34135718e+01],
            [9.62000000e-01, 4.43417435e+01, 4.41355950e+01, 4.45478920e+01],
            [9.63000000e-01, 4.55227935e+01, 4.53051350e+01, 4.57404520e+01],
            [9.64000000e-01, 4.67759900e+01, 4.65486879e+01, 4.70032920e+01],
            [9.65000000e-01, 4.81054522e+01, 4.78664770e+01, 4.83444273e+01],
            [9.66000000e-01, 4.95182299e+01, 4.92710572e+01, 4.97654026e+01],
            [9.67000000e-01, 5.09919628e+01, 5.07309581e+01, 5.12529676e+01],
            [9.68000000e-01, 5.25527247e+01, 5.22748017e+01, 5.28306477e+01],
            [9.69000000e-01, 5.42472216e+01, 5.39459378e+01, 5.45485054e+01],
            [9.70000000e-01, 5.60543566e+01, 5.57270647e+01, 5.63816485e+01],
            [9.71000000e-01, 5.79615024e+01, 5.76068327e+01, 5.83161720e+01],
            [9.72000000e-01, 5.99892723e+01, 5.96076673e+01, 6.03708773e+01],
            [9.73000000e-01, 6.21721149e+01, 6.17573939e+01, 6.25868359e+01],
            [9.74000000e-01, 6.45239920e+01, 6.40855825e+01, 6.49624015e+01],
            [9.75000000e-01, 6.70842243e+01, 6.66058173e+01, 6.75626312e+01],
            [9.76000000e-01, 6.98683051e+01, 6.93329110e+01, 7.04036992e+01],
            [9.77000000e-01, 7.28275855e+01, 7.22422709e+01, 7.34129001e+01],
            [9.78000000e-01, 7.61003258e+01, 7.54526725e+01, 7.67479791e+01],
            [9.79000000e-01, 7.96807328e+01, 7.89530588e+01, 8.04084067e+01],
            [9.80000000e-01, 8.35994568e+01, 8.27755238e+01, 8.44233898e+01],
            [9.81000000e-01, 8.79635481e+01, 8.70535860e+01, 8.88735101e+01],
            [9.82000000e-01, 9.28152314e+01, 9.17771082e+01, 9.38533546e+01],
            [9.83000000e-01, 9.83053300e+01, 9.71203090e+01, 9.94903509e+01],
            [9.84000000e-01, 1.04417725e+02, 1.03042614e+02, 1.05792835e+02],
            [9.85000000e-01, 1.11266834e+02, 1.09670243e+02, 1.12863425e+02],
            [9.86000000e-01, 1.19089445e+02, 1.17237057e+02, 1.20941833e+02],
            [9.87000000e-01, 1.28090399e+02, 1.25912534e+02, 1.30268265e+02],
            [9.88000000e-01, 1.38533356e+02, 1.36028339e+02, 1.41038373e+02],
            [9.89000000e-01, 1.50987586e+02, 1.48041370e+02, 1.53933803e+02],
            [9.90000000e-01, 1.65957752e+02, 1.62487399e+02, 1.69428105e+02],
            [9.91000000e-01, 1.84454399e+02, 1.80403699e+02, 1.88505100e+02],
            [9.92000000e-01, 2.07701778e+02, 2.02685258e+02, 2.12718298e+02],
            [9.93000000e-01, 2.37500454e+02, 2.30992996e+02, 2.44007912e+02],
            [9.94000000e-01, 2.77530646e+02, 2.68682708e+02, 2.86378585e+02],
            [9.95000000e-01, 3.31478003e+02, 3.19085841e+02, 3.43870166e+02],
            [9.96000000e-01, 4.11602890e+02, 3.91929100e+02, 4.31276680e+02],
            [9.97000000e-01, 5.42004560e+02, 5.09203154e+02, 5.74805966e+02],
            [9.98000000e-01, 8.02903745e+02, 7.23794057e+02, 8.82013432e+02],
            [9.99000000e-01, 1.73037355e+03, 1.43966118e+03, 2.02108592e+03]])

    data_3_10m_max_size =\
        numpy.array([[1.00000000e-01, 3.22116133e-01, 3.21796226e-01, 3.22436041e-01],
            [2.00000000e-01, 6.99150967e-01, 6.98729134e-01, 6.99572800e-01],
            [3.00000000e-01, 1.15336360e+00, 1.15264104e+00, 1.15408616e+00],
            [4.00000000e-01, 1.72280633e+00, 1.72168382e+00, 1.72392884e+00],
            [5.00000000e-01, 2.47448817e+00, 2.47281579e+00, 2.47616055e+00],
            [6.00000000e-01, 3.54736560e+00, 3.54507673e+00, 3.54965447e+00],
            [7.00000000e-01, 5.27811183e+00, 5.27348607e+00, 5.28273760e+00],
            [8.00000000e-01, 8.75836883e+00, 8.74744797e+00, 8.76928970e+00],
            [9.00000000e-01, 2.08064862e+01, 2.07181271e+01, 2.08948453e+01],
            [9.10000000e-01, 2.39883889e+01, 2.38640922e+01, 2.41126856e+01],
            [9.20000000e-01, 2.83101552e+01, 2.81166659e+01, 2.85036445e+01],
            [9.30000000e-01, 3.46565180e+01, 3.43304503e+01, 3.49825856e+01],
            [9.40000000e-01, 4.45869415e+01, 4.39064878e+01, 4.52673951e+01],
            [9.50000000e-01, 6.22602954e+01, 6.02731306e+01, 6.42474601e+01],
            [9.60000000e-01, 1.00391094e+02, 9.45818717e+01, 1.06200316e+02],
            [9.61000000e-01, 1.06312541e+02, 9.95981755e+01, 1.13026907e+02],
            [9.62000000e-01, 1.12727897e+02, 1.04869316e+02, 1.20586478e+02],
            [9.63000000e-01, 1.20181737e+02, 1.11177597e+02, 1.29185877e+02],
            [9.64000000e-01, 1.28528399e+02, 1.18024107e+02, 1.39032691e+02],
            [9.65000000e-01, 1.37651867e+02, 1.26148858e+02, 1.49154876e+02],
            [9.66000000e-01, 1.48765397e+02, 1.35533136e+02, 1.61997657e+02],
            [9.67000000e-01, 1.61960246e+02, 1.46614987e+02, 1.77305506e+02],
            [9.68000000e-01, 1.76785185e+02, 1.58380152e+02, 1.95190219e+02],
            [9.69000000e-01, 1.96729563e+02, 1.72984217e+02, 2.20474909e+02],
            [9.70000000e-01, 2.19693803e+02, 1.87073332e+02, 2.52314273e+02],
            [9.71000000e-01, 2.54423198e+02, 1.98809279e+02, 3.10037118e+02],
            [9.72000000e-01, 2.88308402e+02, 2.14068647e+02, 3.62548156e+02],
            [9.73000000e-01, 3.21617788e+02, 2.35085655e+02, 4.08149920e+02],
            [9.74000000e-01, 3.63526034e+02, 2.58001608e+02, 4.69050460e+02],
            [9.75000000e-01, 4.30042376e+02, 3.03591886e+02, 5.56492866e+02],
            [9.76000000e-01, 5.34039624e+02, 3.81051250e+02, 6.87027997e+02],
            [9.77000000e-01, 6.49044213e+02, 4.60345027e+02, 8.37743400e+02],
            [9.78000000e-01, 8.67317635e+02, 5.98147283e+02, 1.13648799e+03],
            [9.79000000e-01, 1.17408280e+03, 8.19552772e+02, 1.52861282e+03],
            [9.80000000e-01, 1.57802804e+03, 1.12711093e+03, 2.02894515e+03],
            [9.81000000e-01, 2.08108443e+03, 1.53400564e+03, 2.62816322e+03],
            [9.82000000e-01, 2.61560132e+03, 1.98370045e+03, 3.24750220e+03],
            [9.83000000e-01, 3.17217948e+03, 2.45239156e+03, 3.89196741e+03],
            [9.84000000e-01, 3.79740687e+03, 3.01158232e+03, 4.58323142e+03],
            [9.85000000e-01, 4.37441707e+03, 3.55816055e+03, 5.19067358e+03],
            [9.86000000e-01, 4.87367658e+03, 4.02313758e+03, 5.72421557e+03],
            [9.87000000e-01, 5.28448507e+03, 4.41023060e+03, 6.15873953e+03],
            [9.88000000e-01, 5.58670168e+03, 4.69318025e+03, 6.48022310e+03],
            [9.89000000e-01, 5.81760557e+03, 4.92059457e+03, 6.71461657e+03],
            [9.90000000e-01, 6.02404601e+03, 5.11032820e+03, 6.93776382e+03],
            [9.91000000e-01, 6.09431286e+03, 5.19589150e+03, 6.99273422e+03],
            [9.92000000e-01, 6.09692826e+03, 5.18427434e+03, 7.00958218e+03],
            [9.93000000e-01, 5.97124801e+03, 5.06001062e+03, 6.88248539e+03],
            [9.94000000e-01, 5.72355237e+03, 4.80617440e+03, 6.64093033e+03],
            [9.95000000e-01, 5.41981399e+03, 4.50933135e+03, 6.33029664e+03],
            [9.96000000e-01, 5.04965580e+03, 4.16831233e+03, 5.93099927e+03],
            [9.97000000e-01, 4.64840064e+03, 3.80142685e+03, 5.49537443e+03],
            [9.98000000e-01, 4.25500009e+03, 3.46699866e+03, 5.04300153e+03],
            [9.99000000e-01, 4.37292947e+03, 3.64898520e+03, 5.09687374e+03]])
    data_3_10m_msmw =\
        numpy.array([[1.00000000e-01, 3.22106000e-01, 3.21786769e-01, 3.22425231e-01],
            [2.00000000e-01, 6.98796433e-01, 6.98379844e-01, 6.99213022e-01],
            [3.00000000e-01, 1.15041047e+00, 1.14970239e+00, 1.15111855e+00],
            [4.00000000e-01, 1.70845953e+00, 1.70744394e+00, 1.70947513e+00],
            [5.00000000e-01, 2.42233810e+00, 2.42086830e+00, 2.42380790e+00],
            [6.00000000e-01, 3.38515930e+00, 3.38308558e+00, 3.38723302e+00],
            [7.00000000e-01, 4.80545573e+00, 4.80209535e+00, 4.80881611e+00],
            [8.00000000e-01, 7.30972217e+00, 7.30358103e+00, 7.31586330e+00],
            [9.00000000e-01, 1.40990255e+01, 1.40719406e+01, 1.41261103e+01],
            [9.10000000e-01, 1.55605597e+01, 1.55259869e+01, 1.55951325e+01],
            [9.20000000e-01, 1.73891936e+01, 1.73456021e+01, 1.74327850e+01],
            [9.30000000e-01, 1.97351520e+01, 1.96829564e+01, 1.97873476e+01],
            [9.40000000e-01, 2.28582423e+01, 2.27895943e+01, 2.29268903e+01],
            [9.50000000e-01, 2.72124065e+01, 2.71130651e+01, 2.73117480e+01],
            [9.60000000e-01, 3.37680501e+01, 3.36192942e+01, 3.39168059e+01],
            [9.61000000e-01, 3.46106333e+01, 3.44545503e+01, 3.47667162e+01],
            [9.62000000e-01, 3.54879326e+01, 3.53251283e+01, 3.56507370e+01],
            [9.63000000e-01, 3.64306538e+01, 3.62611544e+01, 3.66001532e+01],
            [9.64000000e-01, 3.74091826e+01, 3.72276029e+01, 3.75907623e+01],
            [9.65000000e-01, 3.84513908e+01, 3.82600885e+01, 3.86426931e+01],
            [9.66000000e-01, 3.95558223e+01, 3.93590973e+01, 3.97525472e+01],
            [9.67000000e-01, 4.07180754e+01, 4.05084157e+01, 4.09277352e+01],
            [9.68000000e-01, 4.19604541e+01, 4.17304714e+01, 4.21904368e+01],
            [9.69000000e-01, 4.33010786e+01, 4.30548717e+01, 4.35472855e+01],
            [9.70000000e-01, 4.47258136e+01, 4.44634191e+01, 4.49882082e+01],
            [9.71000000e-01, 4.62270775e+01, 4.59435435e+01, 4.65106115e+01],
            [9.72000000e-01, 4.78238743e+01, 4.75170694e+01, 4.81306792e+01],
            [9.73000000e-01, 4.95455669e+01, 4.92171511e+01, 4.98739826e+01],
            [9.74000000e-01, 5.13971807e+01, 5.10422461e+01, 5.17521153e+01],
            [9.75000000e-01, 5.34304831e+01, 5.30463437e+01, 5.38146225e+01],
            [9.76000000e-01, 5.56390055e+01, 5.52060454e+01, 5.60719656e+01],
            [9.77000000e-01, 5.79973476e+01, 5.75211973e+01, 5.84734980e+01],
            [9.78000000e-01, 6.05711019e+01, 6.00396250e+01, 6.11025787e+01],
            [9.79000000e-01, 6.34071166e+01, 6.28073615e+01, 6.40068718e+01],
            [9.80000000e-01, 6.64927881e+01, 6.58034216e+01, 6.71821546e+01],
            [9.81000000e-01, 6.99516149e+01, 6.91795805e+01, 7.07236494e+01],
            [9.82000000e-01, 7.37677558e+01, 7.28879900e+01, 7.46475215e+01],
            [9.83000000e-01, 7.81312514e+01, 7.71311357e+01, 7.91313672e+01],
            [9.84000000e-01, 8.29628029e+01, 8.18181216e+01, 8.41074841e+01],
            [9.85000000e-01, 8.84089609e+01, 8.70805120e+01, 8.97374099e+01],
            [9.86000000e-01, 9.46023330e+01, 9.30578407e+01, 9.61468254e+01],
            [9.87000000e-01, 1.01777942e+02, 9.99797959e+01, 1.03576087e+02],
            [9.88000000e-01, 1.10074073e+02, 1.08016705e+02, 1.12131442e+02],
            [9.89000000e-01, 1.19971634e+02, 1.17594207e+02, 1.22349061e+02],
            [9.90000000e-01, 1.31930062e+02, 1.29111479e+02, 1.34748644e+02],
            [9.91000000e-01, 1.46822202e+02, 1.43526122e+02, 1.50118281e+02],
            [9.92000000e-01, 1.65600224e+02, 1.61438116e+02, 1.69762331e+02],
            [9.93000000e-01, 1.89520873e+02, 1.84093914e+02, 1.94947833e+02],
            [9.94000000e-01, 2.21618479e+02, 2.14082858e+02, 2.29154101e+02],
            [9.95000000e-01, 2.64983176e+02, 2.54363908e+02, 2.75602444e+02],
            [9.96000000e-01, 3.29697420e+02, 3.13127153e+02, 3.46267688e+02],
            [9.97000000e-01, 4.35126326e+02, 4.08585264e+02, 4.61667389e+02],
            [9.98000000e-01, 6.48199505e+02, 5.81982651e+02, 7.14416359e+02],
            [9.99000000e-01, 1.40205521e+03, 1.14205442e+03, 1.66205601e+03]])
    data_3_10m_msmw_log =\
        numpy.array([[1.00000000e-01, 3.39353633e+00, 3.39225962e+00, 3.39481304e+00],
            [2.00000000e-01, 3.75193273e+00, 3.75052081e+00, 3.75334466e+00],
            [3.00000000e-01, 4.14254877e+00, 4.14137478e+00, 4.14372275e+00],
            [4.00000000e-01, 4.58578667e+00, 4.58465182e+00, 4.58692151e+00],
            [5.00000000e-01, 5.11532103e+00, 5.11407970e+00, 5.11656237e+00],
            [6.00000000e-01, 5.80684307e+00, 5.80507440e+00, 5.80861173e+00],
            [7.00000000e-01, 6.84126607e+00, 6.83871167e+00, 6.84382046e+00],
            [8.00000000e-01, 8.79938900e+00, 8.79401631e+00, 8.80476169e+00],
            [9.00000000e-01, 1.47535379e+01, 1.47293985e+01, 1.47776773e+01],
            [9.10000000e-01, 1.61094883e+01, 1.60780775e+01, 1.61408990e+01],
            [9.20000000e-01, 1.78198711e+01, 1.77790130e+01, 1.78607292e+01],
            [9.30000000e-01, 2.00411700e+01, 1.99915026e+01, 2.00908374e+01],
            [9.40000000e-01, 2.30265481e+01, 2.29608496e+01, 2.30922466e+01],
            [9.50000000e-01, 2.72162328e+01, 2.71191773e+01, 2.73132882e+01],
            [9.60000000e-01, 3.35822189e+01, 3.34390645e+01, 3.37253733e+01],
            [9.61000000e-01, 3.44008208e+01, 3.42525989e+01, 3.45490427e+01],
            [9.62000000e-01, 3.52544556e+01, 3.50987309e+01, 3.54101802e+01],
            [9.63000000e-01, 3.61616560e+01, 3.60007515e+01, 3.63225606e+01],
            [9.64000000e-01, 3.71195984e+01, 3.69475355e+01, 3.72916613e+01],
            [9.65000000e-01, 3.81430051e+01, 3.79567225e+01, 3.83292877e+01],
            [9.66000000e-01, 3.92158193e+01, 3.90214710e+01, 3.94101675e+01],
            [9.67000000e-01, 4.03529040e+01, 4.01451504e+01, 4.05606577e+01],
            [9.68000000e-01, 4.15524590e+01, 4.13292493e+01, 4.17756688e+01],
            [9.69000000e-01, 4.28560345e+01, 4.26177508e+01, 4.30943181e+01],
            [9.70000000e-01, 4.42556379e+01, 4.39989451e+01, 4.45123307e+01],
            [9.71000000e-01, 4.57098799e+01, 4.54379860e+01, 4.59817738e+01],
            [9.72000000e-01, 4.72616353e+01, 4.69704297e+01, 4.75528409e+01],
            [9.73000000e-01, 4.89381741e+01, 4.86226957e+01, 4.92536526e+01],
            [9.74000000e-01, 5.07613782e+01, 5.04200971e+01, 5.11026592e+01],
            [9.75000000e-01, 5.27411876e+01, 5.23691277e+01, 5.31132474e+01],
            [9.76000000e-01, 5.48878798e+01, 5.44685623e+01, 5.53071972e+01],
            [9.77000000e-01, 5.71894724e+01, 5.67251252e+01, 5.76538196e+01],
            [9.78000000e-01, 5.96940608e+01, 5.91779297e+01, 6.02101918e+01],
            [9.79000000e-01, 6.24692310e+01, 6.18818447e+01, 6.30566174e+01],
            [9.80000000e-01, 6.54877329e+01, 6.48239685e+01, 6.61514973e+01],
            [9.81000000e-01, 6.88562668e+01, 6.81076934e+01, 6.96048402e+01],
            [9.82000000e-01, 7.25811014e+01, 7.17242904e+01, 7.34379124e+01],
            [9.83000000e-01, 7.68139255e+01, 7.58382058e+01, 7.77896452e+01],
            [9.84000000e-01, 8.15027550e+01, 8.03930080e+01, 8.26125021e+01],
            [9.85000000e-01, 8.67462462e+01, 8.54552769e+01, 8.80372156e+01],
            [9.86000000e-01, 9.27765973e+01, 9.12828625e+01, 9.42703321e+01],
            [9.87000000e-01, 9.97327187e+01, 9.79860681e+01, 1.01479369e+02],
            [9.88000000e-01, 1.07773359e+02, 1.05751208e+02, 1.09795510e+02],
            [9.89000000e-01, 1.17331138e+02, 1.15004002e+02, 1.19658274e+02],
            [9.90000000e-01, 1.29011041e+02, 1.26270575e+02, 1.31751506e+02],
            [9.91000000e-01, 1.43425276e+02, 1.40211292e+02, 1.46639259e+02],
            [9.92000000e-01, 1.61584026e+02, 1.57519901e+02, 1.65648151e+02],
            [9.93000000e-01, 1.84478435e+02, 1.79189455e+02, 1.89767416e+02],
            [9.94000000e-01, 2.15475483e+02, 2.08247416e+02, 2.22703550e+02],
            [9.95000000e-01, 2.57061152e+02, 2.46915098e+02, 2.67207206e+02],
            [9.96000000e-01, 3.18667888e+02, 3.03121689e+02, 3.34214087e+02],
            [9.97000000e-01, 4.18909008e+02, 3.93473681e+02, 4.44344335e+02],
            [9.98000000e-01, 6.22516828e+02, 5.59023169e+02, 6.86010487e+02],
            [9.99000000e-01, 1.32290319e+03, 1.08418307e+03, 1.56162332e+03]])
    questa.plotter.plot(
        data_3_10m_max_weight,
        data_3_10m_max_size,
        data_3_10m_msmw,
        data_3_10m_msmw_log,
        2,
        (0, 50),
        "out/3x3_10m.pdf"
    )
    questa.plotter.plot_scaled(
        data_3_10m_max_weight,
        data_3_10m_max_size,
        data_3_10m_msmw,
        data_3_10m_msmw_log,
        2,
        (0.8, 0.99),
        "out/3x3_10m_scaled.pdf"
    )
