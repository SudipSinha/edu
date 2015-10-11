from math import exp

import matplotlib.pyplot as plt

m = range( 1, 1001 )

time = [0.000469,0.000473,0.000484,0.000494,0.000502,0.000517,0.00113,0.000534,0.00116,0.000553,0.00117,0.000588,0.00119,0.000598,0.00133,0.00062,0.00136,0.000638,0.00138,0.000661,0.0014,0.000686,0.00142,0.000712,0.00145,0.000735,0.0016,0.00137,0.00166,0.00155,0.00378,0.00155,0.00178,0.0015,0.00173,0.00151,0.00178,0.00153,0.00182,0.00156,0.00184,0.00161,0.00187,0.00163,0.00191,0.00167,0.00194,0.00171,0.00194,0.00173,0.00198,0.00176,0.00201,0.00179,0.00205,0.00183,0.00202,0.00187,0.00206,0.00199,0.00378,0.00205,0.00391,0.00213,0.00393,0.00217,0.00401,0.00221,0.00404,0.00224,0.00405,0.00227,0.00411,0.00232,0.00416,0.00238,0.00421,0.0024,0.00411,0.00246,0.00413,0.00249,0.00442,0.00254,0.00442,0.00257,0.0045,0.00265,0.00454,0.00267,0.00459,0.00273,0.00466,0.00279,0.00469,0.00282,0.00473,0.00287,0.00479,0.0029,0.00485,0.00294,0.00467,0.00286,0.00458,0.00313,0.00495,0.00319,0.00525,0.00474,0.00531,0.00474,0.00537,0.00493,0.00546,0.00496,0.00552,0.00504,0.00557,0.00509,0.00562,0.00513,0.00567,0.00523,0.00572,0.00525,0.00577,0.0053,0.00584,0.00536,0.00587,0.00541,0.00593,0.00543,0.0061,0.00551,0.00622,0.00558,0.00626,0.00561,0.00632,0.00568,0.00643,0.00574,0.00648,0.0058,0.00656,0.00587,0.00657,0.00595,0.00662,0.00601,0.00672,0.00606,0.00677,0.00615,0.00669,0.00622,0.00662,0.00629,0.00666,0.00635,0.00672,0.00639,0.00659,0.00661,0.00689,0.00676,0.00943,0.00688,0.0106,0.0069,0.0109,0.00701,0.0109,0.00708,0.011,0.00713,0.0111,0.00724,0.0111,0.00729,0.0112,0.00741,0.0113,0.0075,0.0115,0.00759,0.0115,0.00766,0.0116,0.00772,0.0117,0.00789,0.0117,0.00791,0.0118,0.00796,0.0119,0.00825,0.0122,0.00815,0.0125,0.00828,0.0127,0.00836,0.0129,0.00844,0.0129,0.00852,0.0131,0.00862,0.0131,0.00871,0.0132,0.0088,0.0133,0.0089,0.0134,0.00888,0.0135,0.00902,0.0136,0.00913,0.0137,0.00916,0.0138,0.00925,0.0135,0.00936,0.0128,0.00946,0.013,0.00941,0.0131,0.00964,0.0136,0.00977,0.0135,0.00985,0.0142,0.0102,0.0143,0.0127,0.0144,0.0133,0.0154,0.0136,0.0156,0.0135,0.0157,0.0137,0.0159,0.0139,0.0161,0.0144,0.0162,0.0145,0.0164,0.0145,0.0164,0.0148,0.0165,0.0149,0.0167,0.0151,0.0169,0.0152,0.0169,0.0153,0.0171,0.0156,0.0172,0.0157,0.0173,0.0157,0.0175,0.0159,0.0179,0.016,0.018,0.0162,0.0181,0.0163,0.0183,0.0165,0.0184,0.0166,0.0186,0.0167,0.0186,0.0168,0.0188,0.017,0.019,0.0171,0.0191,0.0172,0.0193,0.0174,0.0192,0.0175,0.0193,0.0177,0.0194,0.0176,0.0184,0.0178,0.0186,0.0175,0.0187,0.0176,0.0187,0.0178,0.0189,0.018,0.019,0.018,0.0191,0.0182,0.0189,0.0184,0.019,0.0188,0.0189,0.0187,0.0195,0.0189,0.0197,0.0191,0.0226,0.0192,0.0246,0.0194,0.0263,0.0197,0.0269,0.0197,0.027,0.0201,0.028,0.0202,0.0286,0.0206,0.0289,0.0211,0.0285,0.0207,0.0287,0.021,0.0288,0.0211,0.029,0.0213,0.0292,0.0216,0.0294,0.0217,0.0297,0.0219,0.0299,0.0222,0.0299,0.0224,0.0301,0.0223,0.0302,0.0226,0.0305,0.0228,0.0306,0.0229,0.0311,0.023,0.0313,0.0233,0.0318,0.0234,0.0319,0.0237,0.0321,0.0238,0.0324,0.0241,0.0326,0.024,0.033,0.0245,0.0331,0.0244,0.0333,0.0247,0.0335,0.0251,0.0333,0.025,0.0334,0.0252,0.0334,0.0254,0.0337,0.0257,0.0339,0.0258,0.0334,0.0262,0.0333,0.0263,0.0337,0.0266,0.0329,0.0268,0.0331,0.0269,0.0333,0.0271,0.0337,0.0269,0.0338,0.0271,0.0353,0.0273,0.0353,0.0273,0.0349,0.0277,0.0354,0.0282,0.0351,0.0285,0.0353,0.0293,0.0367,0.0331,0.0371,0.0337,0.0381,0.034,0.038,0.0341,0.0382,0.0354,0.0387,0.0356,0.039,0.0358,0.0396,0.0363,0.0409,0.0365,0.0411,0.0369,0.041,0.0371,0.0413,0.0375,0.0414,0.0376,0.0417,0.0378,0.042,0.0382,0.0425,0.0384,0.043,0.0387,0.0432,0.0388,0.0433,0.0391,0.0436,0.0395,0.0437,0.04,0.044,0.04,0.0442,0.0404,0.0448,0.0404,0.0449,0.0409,0.0454,0.0408,0.0453,0.0415,0.0457,0.0414,0.0463,0.0416,0.0455,0.0421,0.0452,0.042,0.0456,0.0423,0.0458,0.0426,0.046,0.0429,0.0463,0.0434,0.0468,0.0434,0.0469,0.0437,0.0471,0.0441,0.0475,0.0442,0.0475,0.0444,0.0476,0.0447,0.0481,0.0451,0.0484,0.0452,0.0487,0.0456,0.0491,0.0459,0.0492,0.0461,0.0492,0.0463,0.0498,0.0466,0.0502,0.0471,0.0487,0.0476,0.0481,0.0481,0.049,0.0486,0.0487,0.0489,0.0502,0.0494,0.0505,0.0496,0.0512,0.0501,0.0516,0.0504,0.052,0.0508,0.0594,0.0509,0.0603,0.0515,0.0611,0.0518,0.0617,0.0518,0.0619,0.0522,0.0623,0.0526,0.0625,0.0529,0.0654,0.0532,0.0661,0.0535,0.0663,0.0537,0.0664,0.0541,0.067,0.0544,0.0674,0.0547,0.0678,0.0551,0.0676,0.0555,0.068,0.0558,0.0684,0.0561,0.0695,0.0563,0.0704,0.0569,0.0703,0.0568,0.0711,0.0572,0.0714,0.0573,0.0721,0.0578,0.0729,0.0574,0.0728,0.0581,0.0736,0.0582,0.0741,0.0585,0.0738,0.059,0.0717,0.0591,0.0728,0.0594,0.0729,0.06,0.0738,0.0602,0.0735,0.0605,0.074,0.0595,0.0744,0.0598,0.0751,0.0604,0.0751,0.0604,0.0756,0.061,0.0753,0.0614,0.0761,0.0616,0.076,0.062,0.077,0.0623,0.0768,0.063,0.0771,0.063,0.0777,0.0637,0.078,0.0638,0.0767,0.0643,0.077,0.0643,0.0765,0.0649,0.0769,0.0652,0.0775,0.0659,0.0778,0.0652,0.0783,0.0653,0.0788,0.0648,0.0784,0.0643,0.0786,0.0662,0.081,0.0663,0.081,0.0667,0.0813,0.0671,0.0825,0.0683,0.0827,0.0691,0.0822,0.0697,0.0828,0.0702,0.0828,0.0757,0.0833,0.0769,0.0837,0.0773,0.0843,0.0783,0.0838,0.079,0.0842,0.0796,0.0848,0.08,0.0865,0.0803,0.0865,0.0806,0.0868,0.0809,0.0874,0.0816,0.0881,0.082,0.0882,0.0825,0.0891,0.0831,0.0892,0.0837,0.0893,0.0846,0.09,0.0853,0.0912,0.086,0.0916,0.086,0.0922,0.0865,0.0925,0.0867,0.0933,0.0874,0.094,0.0877,0.0937,0.0881,0.094,0.0886,0.0951,0.0896,0.0952,0.0897,0.0963,0.09,0.0966,0.0903,0.0972,0.0907,0.0979,0.0913,0.0982,0.0918,0.0985,0.0927,0.0993,0.0925,0.0992,0.0929,0.0998,0.0934,0.0998,0.0937,0.101,0.0945,0.101,0.0949,0.102,0.0953,0.102,0.0958,0.103,0.0961,0.103,0.0968,0.103,0.0973,0.104,0.0975,0.105,0.0986,0.105,0.0988,0.105,0.0988,0.106,0.0995,0.106,0.1,0.107,0.1,0.107,0.101,0.108,0.102,0.109,0.102,0.109,0.102,0.108,0.103,0.108,0.104,0.109,0.104,0.108,0.104,0.109,0.105,0.106,0.106,0.107,0.107,0.108,0.107,0.108,0.107,0.108,0.108,0.111,0.109,0.111,0.11,0.112,0.11,0.112,0.11,0.113,0.111,0.114,0.112,0.115,0.112,0.125,0.112,0.127,0.113,0.128,0.114,0.129,0.114,0.131,0.115,0.132,0.115,0.132,0.116,0.132,0.116,0.134,0.117,0.135,0.118,0.135,0.118,0.136,0.119,0.136,0.119,0.136,0.12,0.137,0.12,0.138,0.121,0.139,0.122,0.139,0.122,0.141,0.123,0.141,0.123,0.141,0.124,0.143,0.124,0.143,0.125,0.143,0.126,0.144,0.126,0.145,0.127,0.146,0.128,0.147,0.128,0.148,0.129,0.148,0.129,0.148,0.13,0.149,0.131,0.15,0.131,0.15,0.132,0.151,0.133,0.152,0.133,0.153,0.134,0.153,0.134,0.154,0.135,0.155,0.136,0.155,0.137,0.156,0.137,0.157,0.138,0.157,0.138,0.158,0.139,0.159,0.143,0.159,0.14,0.158,0.141,0.159,0.142,0.16,0.142,0.161,0.143,0.161,0.143,0.161,0.144,0.163,0.144,0.163,0.144,0.164,0.145,0.164,0.146,0.165,0.16,0.169,0.148,0.176,0.15,0.172,0.148,0.17,0.149,0.169,0.147,0.169,0.146,0.17,0.147,0.171,0.151,0.174,0.151,0.177,0.154,0.177,0.161,0.177,0.153,0.185,0.16,0.182,0.155,0.181,0.154,0.177,0.155,0.177,0.155,0.18,0.164,0.185,0.16,0.185,0.178,0.181,0.169,0.182,0.17,0.182,0.172,0.182,0.171,0.183,0.172,0.184,0.174,0.185,0.175,0.188,0.18,0.189,0.177,0.191,0.178,0.192,0.18,0.192,0.18,0.193,0.181]

trend = [(2e-7 * i * i + 1e-5 * i + 0.004) for i in m]
expplot = [(0.004 * 2 ** (0.007*i)) for i in m]

pts, = plt.plot(m, time, color = 'b', marker = '.', markersize = 1e-3)
quad, = plt.plot(m, trend, color = 'g', linewidth = 2.0)
expt, = plt.plot(m, expplot, color = 'r', linestyle = '-', linewidth = 1.5)
plt.axis([0, 1000, 0, 0.3])
plt.legend([pts, quad, expt], ['points', r'Quadratic: $ t = 2 \cdot 10^{-7} m^2 + 10^{-5} m + 0.004 $', r'Exponential: $ t = 0.004 \cdot 2^{0.007 m} $'], loc=2)
plt.tight_layout()

plt.xlabel('m')
plt.ylabel('time (s)')
plt.title('Timing the singular points method ' + r'$ ( \sigma = 0.2 ) $' )
plt.grid(True)

plt.show()
