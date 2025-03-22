import numpy
import questa.plotter
import matplotlib.pyplot

if __name__ == "__main__":
    matplotlib.pyplot.rc('text', usetex=False)
    matplotlib.pyplot.rc('font', family='serif')

    data_4_10m_max_weight =\
        numpy.array([[1.00000000e-01, 4.33319833e-01, 4.33030819e-01, 4.33608848e-01],
            [2.00000000e-01, 9.48714800e-01, 9.48258679e-01, 9.49170921e-01],
            [3.00000000e-01, 1.57845677e+00, 1.57787299e+00, 1.57904054e+00],
            [4.00000000e-01, 2.37575907e+00, 2.37473501e+00, 2.37678312e+00],
            [5.00000000e-01, 3.43892077e+00, 3.43711346e+00, 3.44072807e+00],
            [6.00000000e-01, 4.97233707e+00, 4.96946316e+00, 4.97521097e+00],
            [7.00000000e-01, 7.45611023e+00, 7.45123771e+00, 7.46098276e+00],
            [8.00000000e-01, 1.22789662e+01, 1.22682044e+01, 1.22897280e+01],
            [9.00000000e-01, 2.59433799e+01, 2.59083026e+01, 2.59784572e+01],
            [9.10000000e-01, 2.89011266e+01, 2.88578670e+01, 2.89443862e+01],
            [9.20000000e-01, 3.25746799e+01, 3.25123041e+01, 3.26370557e+01],
            [9.30000000e-01, 3.72763102e+01, 3.71971181e+01, 3.73555023e+01],
            [9.40000000e-01, 4.35256986e+01, 4.34049539e+01, 4.36464433e+01],
            [9.50000000e-01, 5.22706180e+01, 5.20963051e+01, 5.24449309e+01],
            [9.60000000e-01, 6.53357613e+01, 6.50657114e+01, 6.56058112e+01],
            [9.61000000e-01, 6.70055990e+01, 6.67275736e+01, 6.72836244e+01],
            [9.62000000e-01, 6.87443670e+01, 6.84574455e+01, 6.90312886e+01],
            [9.63000000e-01, 7.06051842e+01, 7.03026417e+01, 7.09077268e+01],
            [9.64000000e-01, 7.25757119e+01, 7.22546721e+01, 7.28967516e+01],
            [9.65000000e-01, 7.46629814e+01, 7.43334281e+01, 7.49925347e+01],
            [9.66000000e-01, 7.68674106e+01, 7.65266253e+01, 7.72081959e+01],
            [9.67000000e-01, 7.91810760e+01, 7.88139106e+01, 7.95482414e+01],
            [9.68000000e-01, 8.16405610e+01, 8.12636585e+01, 8.20174635e+01],
            [9.69000000e-01, 8.42929761e+01, 8.38911390e+01, 8.46948132e+01],
            [9.70000000e-01, 8.70756133e+01, 8.66510821e+01, 8.75001445e+01],
            [9.71000000e-01, 9.00954049e+01, 8.96411363e+01, 9.05496735e+01],
            [9.72000000e-01, 9.32835794e+01, 9.27926726e+01, 9.37744861e+01],
            [9.73000000e-01, 9.67430150e+01, 9.62060677e+01, 9.72799623e+01],
            [9.74000000e-01, 1.00468617e+02, 9.99082468e+01, 1.01028988e+02],
            [9.75000000e-01, 1.04436008e+02, 1.03845524e+02, 1.05026492e+02],
            [9.76000000e-01, 1.08782330e+02, 1.08151407e+02, 1.09413252e+02],
            [9.77000000e-01, 1.13525261e+02, 1.12838174e+02, 1.14212347e+02],
            [9.78000000e-01, 1.18689676e+02, 1.17954792e+02, 1.19424559e+02],
            [9.79000000e-01, 1.24379328e+02, 1.23569545e+02, 1.25189110e+02],
            [9.80000000e-01, 1.30688615e+02, 1.29784866e+02, 1.31592364e+02],
            [9.81000000e-01, 1.37605818e+02, 1.36594822e+02, 1.38616814e+02],
            [9.82000000e-01, 1.45287455e+02, 1.44137547e+02, 1.46437363e+02],
            [9.83000000e-01, 1.53902809e+02, 1.52569481e+02, 1.55236136e+02],
            [9.84000000e-01, 1.63492564e+02, 1.61972225e+02, 1.65012902e+02],
            [9.85000000e-01, 1.74445053e+02, 1.72734365e+02, 1.76155741e+02],
            [9.86000000e-01, 1.86788206e+02, 1.84783433e+02, 1.88792978e+02],
            [9.87000000e-01, 2.01229376e+02, 1.98830156e+02, 2.03628595e+02],
            [9.88000000e-01, 2.17948976e+02, 2.15078419e+02, 2.20819532e+02],
            [9.89000000e-01, 2.37534754e+02, 2.34113866e+02, 2.40955643e+02],
            [9.90000000e-01, 2.61076251e+02, 2.56959633e+02, 2.65192869e+02],
            [9.91000000e-01, 2.89655846e+02, 2.84520253e+02, 2.94791439e+02],
            [9.92000000e-01, 3.25499230e+02, 3.18887108e+02, 3.32111353e+02],
            [9.93000000e-01, 3.71373036e+02, 3.62845937e+02, 3.79900134e+02],
            [9.94000000e-01, 4.32398278e+02, 4.20525426e+02, 4.44271130e+02],
            [9.95000000e-01, 5.17460666e+02, 5.00446706e+02, 5.34474627e+02],
            [9.96000000e-01, 6.45293198e+02, 6.18214701e+02, 6.72371694e+02],
            [9.97000000e-01, 8.63659980e+02, 8.10086982e+02, 9.17232977e+02],
            [9.98000000e-01, 1.31364538e+03, 1.20445779e+03, 1.42283297e+03],
            [9.99000000e-01, 2.64896671e+03, 2.34615689e+03, 2.95177652e+03]])
    data_4_10m_max_size =\
        numpy.array([[1.00000000e-01, 4.33325833e-01, 4.33036700e-01, 4.33614967e-01],
            [2.00000000e-01, 9.48863700e-01, 9.48411024e-01, 9.49316376e-01],
            [3.00000000e-01, 1.57924627e+00, 1.57866397e+00, 1.57982856e+00],
            [4.00000000e-01, 2.37712040e+00, 2.37613258e+00, 2.37810822e+00],
            [5.00000000e-01, 3.43612937e+00, 3.43430046e+00, 3.43795827e+00],
            [6.00000000e-01, 4.94032250e+00, 4.93725635e+00, 4.94338865e+00],
            [7.00000000e-01, 7.31557943e+00, 7.31063073e+00, 7.32052814e+00],
            [8.00000000e-01, 1.18571372e+01, 1.18439052e+01, 1.18703692e+01],
            [9.00000000e-01, 2.51274072e+01, 2.50699781e+01, 2.51848364e+01],
            [9.10000000e-01, 2.80982282e+01, 2.80281431e+01, 2.81683132e+01],
            [9.20000000e-01, 3.18468775e+01, 3.17551067e+01, 3.19386484e+01],
            [9.30000000e-01, 3.66905243e+01, 3.65707222e+01, 3.68103264e+01],
            [9.40000000e-01, 4.32445443e+01, 4.30650282e+01, 4.34240604e+01],
            [9.50000000e-01, 5.25397586e+01, 5.22794580e+01, 5.28000591e+01],
            [9.60000000e-01, 6.69757897e+01, 6.65894755e+01, 6.73621040e+01],
            [9.61000000e-01, 6.88756099e+01, 6.84604584e+01, 6.92907615e+01],
            [9.62000000e-01, 7.07952839e+01, 7.03564301e+01, 7.12341377e+01],
            [9.63000000e-01, 7.29182769e+01, 7.24681721e+01, 7.33683816e+01],
            [9.64000000e-01, 7.51927299e+01, 7.47078405e+01, 7.56776192e+01],
            [9.65000000e-01, 7.76000183e+01, 7.70869258e+01, 7.81131108e+01],
            [9.66000000e-01, 8.01372498e+01, 7.95753931e+01, 8.06991065e+01],
            [9.67000000e-01, 8.28052129e+01, 8.22277245e+01, 8.33827012e+01],
            [9.68000000e-01, 8.56762416e+01, 8.50529668e+01, 8.62995165e+01],
            [9.69000000e-01, 8.87282238e+01, 8.80735948e+01, 8.93828528e+01],
            [9.70000000e-01, 9.20595174e+01, 9.13263990e+01, 9.27926359e+01],
            [9.71000000e-01, 9.56914701e+01, 9.49027830e+01, 9.64801572e+01],
            [9.72000000e-01, 9.95832220e+01, 9.86790518e+01, 1.00487392e+02],
            [9.73000000e-01, 1.03743713e+02, 1.02719782e+02, 1.04767645e+02],
            [9.74000000e-01, 1.08122438e+02, 1.07111788e+02, 1.09133088e+02],
            [9.75000000e-01, 1.12990263e+02, 1.11849602e+02, 1.14130925e+02],
            [9.76000000e-01, 1.18257021e+02, 1.17054651e+02, 1.19459391e+02],
            [9.77000000e-01, 1.23925754e+02, 1.22617170e+02, 1.25234339e+02],
            [9.78000000e-01, 1.30428944e+02, 1.29041457e+02, 1.31816431e+02],
            [9.79000000e-01, 1.37371109e+02, 1.35873412e+02, 1.38868806e+02],
            [9.80000000e-01, 1.45277385e+02, 1.43417492e+02, 1.47137279e+02],
            [9.81000000e-01, 1.54188983e+02, 1.52115222e+02, 1.56262744e+02],
            [9.82000000e-01, 1.63996868e+02, 1.61640051e+02, 1.66353686e+02],
            [9.83000000e-01, 1.74852023e+02, 1.71879898e+02, 1.77824148e+02],
            [9.84000000e-01, 1.87531679e+02, 1.84047357e+02, 1.91016002e+02],
            [9.85000000e-01, 2.01849573e+02, 1.97653085e+02, 2.06046062e+02],
            [9.86000000e-01, 2.18345544e+02, 2.13066153e+02, 2.23624935e+02],
            [9.87000000e-01, 2.38406436e+02, 2.31550455e+02, 2.45262417e+02],
            [9.88000000e-01, 2.62534647e+02, 2.54278751e+02, 2.70790543e+02],
            [9.89000000e-01, 2.91697633e+02, 2.80365211e+02, 3.03030056e+02],
            [9.90000000e-01, 3.26364165e+02, 3.11356738e+02, 3.41371591e+02],
            [9.91000000e-01, 3.72171514e+02, 3.47585870e+02, 3.96757159e+02],
            [9.92000000e-01, 4.30306713e+02, 3.94940951e+02, 4.65672475e+02],
            [9.93000000e-01, 5.06764619e+02, 4.64121128e+02, 5.49408109e+02],
            [9.94000000e-01, 6.09681589e+02, 5.54441489e+02, 6.64921689e+02],
            [9.95000000e-01, 7.81355558e+02, 6.89799622e+02, 8.72911494e+02],
            [9.96000000e-01, 1.08341435e+03, 9.46107753e+02, 1.22072095e+03],
            [9.97000000e-01, 1.63721044e+03, 1.40216606e+03, 1.87225482e+03],
            [9.98000000e-01, 2.58747108e+03, 2.22435777e+03, 2.95058440e+03],
            [9.99000000e-01, 4.38124368e+03, 3.89965451e+03, 4.86283284e+03]])
    data_4_10m_msmw =\
        numpy.array([[1.00000000e-01, 4.33312367e-01, 4.33023594e-01, 4.33601139e-01],
            [2.00000000e-01, 9.48401667e-01, 9.47947187e-01, 9.48856146e-01],
            [3.00000000e-01, 1.57543633e+00, 1.57486220e+00, 1.57601047e+00],
            [4.00000000e-01, 2.35944223e+00, 2.35848504e+00, 2.36039943e+00],
            [5.00000000e-01, 3.37498793e+00, 3.37333915e+00, 3.37663672e+00],
            [6.00000000e-01, 4.76256527e+00, 4.76015226e+00, 4.76497827e+00],
            [7.00000000e-01, 6.83870373e+00, 6.83480179e+00, 6.84260568e+00],
            [8.00000000e-01, 1.05509497e+01, 1.05426634e+01, 1.05592360e+01],
            [9.00000000e-01, 2.06667073e+01, 2.06378698e+01, 2.06955447e+01],
            [9.10000000e-01, 2.28524983e+01, 2.28178057e+01, 2.28871909e+01],
            [9.20000000e-01, 2.55559594e+01, 2.55058780e+01, 2.56060407e+01],
            [9.30000000e-01, 2.90301562e+01, 2.89673251e+01, 2.90929874e+01],
            [9.40000000e-01, 3.36516806e+01, 3.35574221e+01, 3.37459391e+01],
            [9.50000000e-01, 4.01033843e+01, 3.99687673e+01, 4.02380012e+01],
            [9.60000000e-01, 4.97577481e+01, 4.95534269e+01, 4.99620693e+01],
            [9.61000000e-01, 5.09994515e+01, 5.07816021e+01, 5.12173009e+01],
            [9.62000000e-01, 5.23005059e+01, 5.20746410e+01, 5.25263708e+01],
            [9.63000000e-01, 5.36684482e+01, 5.34360780e+01, 5.39008185e+01],
            [9.64000000e-01, 5.51362669e+01, 5.48930201e+01, 5.53795138e+01],
            [9.65000000e-01, 5.66622221e+01, 5.64038989e+01, 5.69205454e+01],
            [9.66000000e-01, 5.82915257e+01, 5.80211109e+01, 5.85619406e+01],
            [9.67000000e-01, 6.00022509e+01, 5.97277581e+01, 6.02767438e+01],
            [9.68000000e-01, 6.18259666e+01, 6.15326140e+01, 6.21193192e+01],
            [9.69000000e-01, 6.37779813e+01, 6.34715033e+01, 6.40844593e+01],
            [9.70000000e-01, 6.58525850e+01, 6.55272564e+01, 6.61779135e+01],
            [9.71000000e-01, 6.80730478e+01, 6.77221733e+01, 6.84239224e+01],
            [9.72000000e-01, 7.04368673e+01, 7.00645086e+01, 7.08092259e+01],
            [9.73000000e-01, 7.29874367e+01, 7.25830705e+01, 7.33918029e+01],
            [9.74000000e-01, 7.57586820e+01, 7.53393317e+01, 7.61780323e+01],
            [9.75000000e-01, 7.87326388e+01, 7.82837815e+01, 7.91814962e+01],
            [9.76000000e-01, 8.19539920e+01, 8.14778401e+01, 8.24301438e+01],
            [9.77000000e-01, 8.54875262e+01, 8.49619126e+01, 8.60131398e+01],
            [9.78000000e-01, 8.93258254e+01, 8.87686622e+01, 8.98829885e+01],
            [9.79000000e-01, 9.35902885e+01, 9.29737817e+01, 9.42067954e+01],
            [9.80000000e-01, 9.82812217e+01, 9.75778342e+01, 9.89846092e+01],
            [9.81000000e-01, 1.03466777e+02, 1.02668173e+02, 1.04265381e+02],
            [9.82000000e-01, 1.09242164e+02, 1.08348199e+02, 1.10136129e+02],
            [9.83000000e-01, 1.15705784e+02, 1.14640108e+02, 1.16771459e+02],
            [9.84000000e-01, 1.22921300e+02, 1.21695723e+02, 1.24146877e+02],
            [9.85000000e-01, 1.31159225e+02, 1.29776878e+02, 1.32541573e+02],
            [9.86000000e-01, 1.40501394e+02, 1.38845612e+02, 1.42157176e+02],
            [9.87000000e-01, 1.51377265e+02, 1.49386862e+02, 1.53367669e+02],
            [9.88000000e-01, 1.63973758e+02, 1.61627946e+02, 1.66319571e+02],
            [9.89000000e-01, 1.78755024e+02, 1.75998754e+02, 1.81511295e+02],
            [9.90000000e-01, 1.96421822e+02, 1.93082204e+02, 1.99761440e+02],
            [9.91000000e-01, 2.17890163e+02, 2.13782111e+02, 2.21998214e+02],
            [9.92000000e-01, 2.45197750e+02, 2.39974912e+02, 2.50420589e+02],
            [9.93000000e-01, 2.80042747e+02, 2.73237981e+02, 2.86847513e+02],
            [9.94000000e-01, 3.25990584e+02, 3.16851502e+02, 3.35129666e+02],
            [9.95000000e-01, 3.90833499e+02, 3.77559596e+02, 4.04107403e+02],
            [9.96000000e-01, 4.87143303e+02, 4.66594020e+02, 5.07692586e+02],
            [9.97000000e-01, 6.53005890e+02, 6.11697317e+02, 6.94314462e+02],
            [9.98000000e-01, 1.00111378e+03, 9.12756051e+02, 1.08947152e+03],
            [9.99000000e-01, 2.02199650e+03, 1.75473231e+03, 2.28926069e+03]])
    data_4_10m_msmw_log =\
        numpy.array([[1.00000000e-01, 5.14044117e+00, 5.13751570e+00, 5.14336663e+00],
            [2.00000000e-01, 5.64856393e+00, 5.64700550e+00, 5.65012237e+00],
            [3.00000000e-01, 6.19932247e+00, 6.19803879e+00, 6.20060614e+00],
            [4.00000000e-01, 6.81647973e+00, 6.81499671e+00, 6.81796276e+00],
            [5.00000000e-01, 7.54451630e+00, 7.54325370e+00, 7.54577890e+00],
            [6.00000000e-01, 8.48781523e+00, 8.48629745e+00, 8.48933301e+00],
            [7.00000000e-01, 9.90968230e+00, 9.90698600e+00, 9.91237860e+00],
            [8.00000000e-01, 1.26810399e+01, 1.26750777e+01, 1.26870021e+01],
            [9.00000000e-01, 2.14223060e+01, 2.13952318e+01, 2.14493802e+01],
            [9.10000000e-01, 2.34372488e+01, 2.34029536e+01, 2.34715439e+01],
            [9.20000000e-01, 2.59607840e+01, 2.59146258e+01, 2.60069421e+01],
            [9.30000000e-01, 2.92311451e+01, 2.91694640e+01, 2.92928263e+01],
            [9.40000000e-01, 3.36269279e+01, 3.35369107e+01, 3.37169452e+01],
            [9.50000000e-01, 3.98227941e+01, 3.96918800e+01, 3.99537082e+01],
            [9.60000000e-01, 4.91543030e+01, 4.89557438e+01, 4.93528622e+01],
            [9.61000000e-01, 5.03599377e+01, 5.01522484e+01, 5.05676269e+01],
            [9.62000000e-01, 5.16118047e+01, 5.13974115e+01, 5.18261980e+01],
            [9.63000000e-01, 5.29365365e+01, 5.27081523e+01, 5.31649208e+01],
            [9.64000000e-01, 5.43600476e+01, 5.41208678e+01, 5.45992274e+01],
            [9.65000000e-01, 5.58458378e+01, 5.55996789e+01, 5.60919967e+01],
            [9.66000000e-01, 5.74283139e+01, 5.71640961e+01, 5.76925318e+01],
            [9.67000000e-01, 5.91012151e+01, 5.88300887e+01, 5.93723415e+01],
            [9.68000000e-01, 6.08654332e+01, 6.05814451e+01, 6.11494213e+01],
            [9.69000000e-01, 6.27479159e+01, 6.24461122e+01, 6.30497196e+01],
            [9.70000000e-01, 6.47609832e+01, 6.44412512e+01, 6.50807151e+01],
            [9.71000000e-01, 6.69274326e+01, 6.65875957e+01, 6.72672694e+01],
            [9.72000000e-01, 6.92117140e+01, 6.88502370e+01, 6.95731910e+01],
            [9.73000000e-01, 7.16995548e+01, 7.13094617e+01, 7.20896480e+01],
            [9.74000000e-01, 7.43985538e+01, 7.39940597e+01, 7.48030480e+01],
            [9.75000000e-01, 7.72666032e+01, 7.68388133e+01, 7.76943931e+01],
            [9.76000000e-01, 8.04168490e+01, 7.99646907e+01, 8.08690073e+01],
            [9.77000000e-01, 8.38282013e+01, 8.33292084e+01, 8.43271941e+01],
            [9.78000000e-01, 8.75439253e+01, 8.69995888e+01, 8.80882619e+01],
            [9.79000000e-01, 9.16623255e+01, 9.10582568e+01, 9.22663942e+01],
            [9.80000000e-01, 9.61941875e+01, 9.55100906e+01, 9.68782844e+01],
            [9.81000000e-01, 1.01250032e+02, 1.00480404e+02, 1.02019661e+02],
            [9.82000000e-01, 1.06816162e+02, 1.05950808e+02, 1.07681515e+02],
            [9.83000000e-01, 1.13083703e+02, 1.12070316e+02, 1.14097090e+02],
            [9.84000000e-01, 1.20092287e+02, 1.18919570e+02, 1.21265003e+02],
            [9.85000000e-01, 1.28037256e+02, 1.26708288e+02, 1.29366224e+02],
            [9.86000000e-01, 1.37032947e+02, 1.35469221e+02, 1.38596674e+02],
            [9.87000000e-01, 1.47484830e+02, 1.45591636e+02, 1.49378024e+02],
            [9.88000000e-01, 1.59709604e+02, 1.57460390e+02, 1.61958819e+02],
            [9.89000000e-01, 1.73831961e+02, 1.71190369e+02, 1.76473553e+02],
            [9.90000000e-01, 1.90936541e+02, 1.87729080e+02, 1.94144001e+02],
            [9.91000000e-01, 2.11622256e+02, 2.07655853e+02, 2.15588658e+02],
            [9.92000000e-01, 2.37663097e+02, 2.32634188e+02, 2.42692006e+02],
            [9.93000000e-01, 2.70858573e+02, 2.64363556e+02, 2.77353589e+02],
            [9.94000000e-01, 3.14717855e+02, 3.06008758e+02, 3.23426953e+02],
            [9.95000000e-01, 3.76020293e+02, 3.63790920e+02, 3.88249666e+02],
            [9.96000000e-01, 4.68437834e+02, 4.49170947e+02, 4.87704721e+02],
            [9.97000000e-01, 6.22398846e+02, 5.84199680e+02, 6.60598012e+02],
            [9.98000000e-01, 9.47604579e+02, 8.69635231e+02, 1.02557393e+03],
            [9.99000000e-01, 1.88190442e+03, 1.64749016e+03, 2.11631869e+03]])
    questa.plotter.plot(
        data_4_10m_max_weight,
        data_4_10m_max_size,
        data_4_10m_msmw,
        data_4_10m_msmw_log,
        2,
        (0, 80),
        "out/4x4_10m.pdf"
    )
    questa.plotter.plot_scaled(
        data_4_10m_max_weight,
        data_4_10m_max_size,
        data_4_10m_msmw,
        data_4_10m_msmw_log,
        2,
        (0.8, 0.99),
        "out/4x4_10m_scaled.pdf"
    )
