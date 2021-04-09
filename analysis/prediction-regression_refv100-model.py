import numpy as np
import matplotlib.pyplot as plt
import sys

v100_freqs = [135, 142, 150, 157, 165, 172, 180, 187, 195, 202, 210, 217, 225, 232, 240, 247, 255, 262, 270, 277, 285, 292, 300, 
307, 315, 322, 330, 337, 345, 352, 360, 367, 375, 382, 390, 397, 405, 412, 420, 427, 435, 442, 450, 457, 465, 472, 480, 487, 495, 502, 510, 517, 525, 532, 540, 547, 555, 562, 570, 577, 585, 592, 600, 607, 615, 622, 630, 637, 645, 652, 660, 667, 675, 682, 690, 697, 705, 712, 720, 727, 735, 742, 750, 757, 765, 772, 780, 787, 795, 802, 810, 817, 825, 832, 840, 847, 855, 862, 870, 877, 885, 892, 900, 907, 915, 922, 930, 937, 945, 952, 960, 967, 975, 982, 990, 997, 1005, 1012, 1020, 1027, 1035, 1042, 1050, 1057, 1065, 1072, 1080, 1087, 1095, 1102, 1110, 1117, 1125, 1132, 1140, 1147, 1155, 1162, 1170, 1177, 1185, 1192, 1200, 1207, 1215, 1222, 1230, 1237, 1245, 1252, 1260, 1267, 1275, 1282, 1290, 1297, 1305, 1312, 1320, 1327, 1335, 1342, 1350, 1357, 1365, 1372, 1380]
v100_frequency_array = np.array(v100_freqs)

freqs = [544, 556, 569, 582, 594, 607, 620, 632, 645, 658, 670, 683, 696, 708, 721, 734, 746, 759, 772, 784, 797, 810, 822, 
835, 847, 860, 873, 885, 898, 911, 923, 936, 949, 961, 974, 987, 999, 1012, 1025, 1037, 1050, 1063, 1075, 1088, 1101, 1113, 1126, 1139, 1151, 1164, 1177, 1189, 1202, 1215, 1227, 1240, 1252, 1265, 1278, 1290, 1303, 1316, 1328]
p100_frequency_array = np.array(freqs)

DGEMM_orig = [91.26015830023837, 92.96322729994432, 94.49664985885224, 96.32860645674836, 97.99876472010011, 102.52375378362328, 101.16297484747064, 102.82955955734624, 104.1701935206025, 105.99215876499608, 107.86014443868262, 109.52251912603498, 111.11436902150511, 112.93952611026309, 114.59780175232343, 116.09249163795808, 117.81460058285779, 119.39434083592258, 120.77155934317729, 122.53673382937629, 123.89264935563699, 129.0974398227696, 127.58549738691038, 128.21502554094351, 129.71913067146474, 130.82994408487903, 132.58815318192887, 134.21456080616784, 135.8489846651567, 137.5391549749082, 139.25583423381207, 140.89996991406937, 142.5185506174653, 144.3036277846969, 145.89328932035545, 147.468940884592, 149.28975659458135, 154.83052334884306, 152.60193816833547, 156.40130905461032, 160.16292562608055, 161.9745711252697, 165.59543894073462, 170.02344771251433, 174.63686605014573, 179.1699872062947, 180.82539698497703, 189.24698596007832, 191.21859082431783, 196.0538772479383, 205.6546708713073, 207.39194593301568, 213.81515063646293, 219.66280345218453, 226.16067317446183, 236.22427840357565, 238.7729733891685, 244.7947815264349, 245.24169769872015, 245.34169530828407, 245.45492471779139, 245.7671618087434, 245.48677175471778]
STREAM_orig = [70.6187111155978, 70.73495160224957, 70.8858580787229, 70.9871962029616, 71.12031758797963, 71.94585423058653, 71.23897283370766, 71.32500606785038, 71.45243245329257, 71.55999229970408, 71.6183545873943, 71.76951530936398, 71.85613050205144, 71.94370978621026, 72.01853072396803, 72.11779475670758, 72.20086615007259, 72.30223153746851, 72.37146223051371, 72.47048333286403, 72.61476967614928, 73.48278855524502, 72.96503143206579, 72.97023909420189, 73.2104862336105, 73.29638526000547, 73.51753422876494, 73.54786732601848, 73.68963131776734, 73.81774902213414, 73.98414476605723, 74.23841507442732, 74.20438124045934, 74.27504809935719, 74.28243937308594, 74.68210808693102, 74.65004600795763, 75.84438298856415, 74.8876552794241, 74.98480347565867, 75.12984735076441, 75.30486044461068, 75.34204268761043, 76.66395924532696, 77.54052596209999, 77.5954173856553, 78.53968215825026, 79.43171964952926, 80.54716681172678, 81.5772200369611, 82.77017934363799, 83.46030358099618, 84.87898184629756, 85.99709000835344, 87.14247094541336, 87.1931272599602, 89.3747083421758, 90.59227387521533, 91.73158746690181, 92.05975468295983, 93.30413202576229, 94.87734694778467, 96.61403099080458]
FS_orig = [91.90040077772422, 93.55251345300556, 94.9755206871032, 96.88295345982931, 98.45768962847943, 102.9960453344312, 101.62066559272297, 103.09263469518136, 104.63081095210241, 106.26589066733371, 108.01132391246539, 109.69802105909852, 111.25078929549443, 112.9810433735894, 114.7127011338979, 116.23210124135562, 117.94904704323208, 119.5644531589289, 121.19680365385963, 122.97684831301983, 124.49040200507896, 129.6238846289278, 127.97797962627583, 129.3305631608876, 130.95045226932902, 132.14544109222263, 134.29215262196212, 135.9631493640822, 136.31129042212976, 138.7076198967757, 139.2184661036195, 141.24400624637894, 142.59229602771634, 144.31903045634385, 145.94465294197542, 147.5392126781328, 149.34197007645136, 155.5916656340885, 152.96241122388327, 157.03093215645018, 160.48199150383292, 162.60601644392736, 166.31242807959913, 170.48333806546816, 175.1571707135506, 180.18015958305034, 181.1795983326214, 188.84154507504738, 191.64573388680253, 197.77763938845985, 205.4822263821075, 207.32258451385883, 213.5252296034202, 219.2092543590473, 226.4041392780531, 236.00188807797605, 237.62922387557094, 245.79278911869883, 247.54819984458507, 247.68252377686142, 248.00437452156146, 247.07130956003155, 247.56521250342502]
#v100_DGEMM_orig = [115.64149291147305, 117.09390100601755, 117.64771886517413, 117.09740222520954, 119.19710117179773, 119.94902968927069, 120.29193885590288, 121.47411021820663, 123.64538335527804, 124.80047157510258, 125.9783197293173, 127.080405567942, 129.15914229168155, 129.87173561588696, 131.2017036816628, 132.41175588842825, 133.8556898376859, 135.6464586619529, 137.1055755745011, 137.6178838229994, 139.26280985925047, 140.89375409479044, 142.3647326910089, 143.09222789400957, 144.5826859354116, 146.08672192658267, 147.3557751036727, 148.5071242524379, 149.93350260828578, 150.93739185780979, 152.3899503702467, 153.2807956624927, 154.26021486610713, 155.386362074177, 156.37313108604278, 157.20936632632328, 159.0968617206687, 160.1906831271612, 161.6979424640088, 162.20324398371463, 163.47931197241374, 164.81791827452622, 166.20505691142966, 167.15282974947203, 168.5878924055946, 169.256685580167, 170.68695231916723, 172.13742815396742, 173.31530054375605, 174.54070223594167, 175.6558028214274, 176.48544842057373, 178.12941114554155, 179.6589809367121, 181.2835631771238, 181.83466383525717, 183.3864160555582, 184.68101681538832, 186.25192492995873, 187.33888663375572, 188.45775161316362, 189.618794535759, 190.68844158212514, 191.63880942114022, 192.94916202028006, 193.60545041412277, 195.37202971301943, 195.96205569635762, 197.07351689864123, 198.22848209770768, 199.72659031466264, 200.6859938594766, 202.2117273225572, 202.9403584962649, 204.84351088266592, 206.22770481360203, 207.69288338644986, 209.94758976027234, 214.16482952702162, 214.20001234132326, 219.44672660553456, 219.8088217673224, 225.26857826824838, 227.04664378665518, 231.5411296890296, 231.6893123064417, 235.12948939239536, 237.83939231872216, 240.63907692635155, 240.7199529899759, 245.03340684371125, 245.0146227481885, 246.42877678084454, 246.42493284305525, 246.81150432813195, 246.88646773591415, 246.92280117360562, 247.1033093324652, 247.09416584615943, 247.0896789291464, 247.17004496619714, 247.20308523719572, 247.1773572409752, 247.22188004142407, 247.18025125029448, 247.1454899818961, 247.2053817426396, 247.18367285067885, 247.16052268277036, 247.1693709741218, 247.20141296478798, 247.2268735532823, 247.06930881347006]
v100_DGEMM_orig = [47.158270038153105, 47.41008620099005, 47.394178377238696, 47.3981931352748, 47.386117195162726, 47.37293161399153, 47.38547703414482, 47.38194385962243, 47.38321260328696, 47.40086721028623, 47.167723583341576, 47.209552737605925, 47.209832510082066, 47.22035537757563, 47.19568653847231, 47.184869586421954, 67.02451722519933, 67.02941781341839, 67.03092997821501, 67.03027765435776, 67.00542002215147, 66.98586108050957, 66.97963413682677, 66.96416381276005, 66.95297622176932, 66.95743591015717, 66.98260893269372, 66.99663184839407, 67.0086797774629, 66.98793317612483, 66.95974094501315, 67.01509159692193, 67.01210962302972, 67.02942776401838, 67.01862905894635, 66.99919977386486, 67.01706870864899, 67.01752933875775, 67.02877476740773, 67.01183965801391, 67.01165978491036, 67.04408242158928, 67.03781455949097, 67.06441370892306, 67.05099829936938, 67.07125328963396, 67.07362390547583, 67.1240633477911, 67.90307173811487, 68.51505313542255, 112.61718550169064, 111.93842591459273, 114.7285483722066, 114.134551732829, 115.63593266486029, 117.0858815320634, 117.64124426511526, 117.08930880451173, 119.18979631676268, 119.94048687105756, 120.28349113127359, 121.46938228966393, 123.6358024328805, 124.790224458562, 125.97264983665005, 127.07414221404505, 129.1465210368699, 129.8605400366234, 131.19205089417588, 132.39777210743563, 133.84984395202218, 135.63734848284224, 137.09348449297823, 137.6112339224784, 139.25264484905745, 140.88147089954217, 142.35170038027616, 143.08427720221601, 144.5692735602701, 146.07562335494663, 147.3471784715784, 148.4924459941144, 149.9195206594532, 150.92880135816537, 152.3812987329209, 153.2631640031597, 154.24446258368422, 155.37639428998506, 156.359933040815, 157.19558675629438, 159.0968617206687, 160.1906831271612, 161.69495710939813, 162.20324398371463, 163.47931197241374, 164.81791827452622, 166.20505691142966, 167.15282974947203, 168.5878924055946, 169.256685580167, 170.68695231916723, 172.13742815396742, 173.31161967974268, 174.53704273491803, 175.6558028214274, 176.48544842057373, 178.12941114554155, 179.6589809367121, 181.2835631771238, 181.83466383525717, 183.3864160555582, 184.68101681538832, 186.24741562010897, 187.33888663375572, 188.45775161316362, 189.61402738704192, 190.6835462549062, 191.63880942114022, 192.94916202028006, 193.59543407756135, 195.36681116414255, 195.95684639899036, 197.07351689864123, 198.22848209770768, 199.72659031466264, 200.6859938594766, 202.2117273225572, 202.9403584962649, 204.83741173837558, 206.22770481360203, 207.69288338644986, 209.94758976027234, 214.16482952702162, 214.19322130732138, 219.44672660553456, 219.8088217673224, 225.26857826824838, 227.03904553294362, 231.5411296890296, 231.6893123064417, 235.12948939239536, 237.8227502977454, 240.63907692635155, 240.7199529899759, 245.03340684371125, 245.0146227481885, 246.42877678084454, 246.42493284305525, 246.81150432813195, 246.88646773591415, 246.91390758564876, 247.09431028013623, 247.09416584615943, 247.08083668942544, 247.17004496619714, 247.20308523719572, 247.1773572409752, 247.21285140189812, 247.18025125029448, 247.1454899818961, 247.2053817426396, 247.18367285067885, 247.16052268277036, 247.1693709741218, 247.20141296478798, 247.2268735532823, 247.06930881347006]
#voltages = np.sqrt(np.array(DGEMM_orig)/F)
#print('Drived Frequencies: ', voltages)
v100_STREAM_orig = [70.6187111155978, 70.73495160224957, 70.8858580787229, 70.9871962029616, 71.12031758797963, 71.94585423058653, 71.23897283370766, 71.32500606785038, 71.45243245329257, 71.55999229970408, 71.6183545873943, 71.76951530936398, 71.85613050205144, 71.94370978621026, 72.01853072396803, 72.11779475670758, 72.20086615007259, 72.30223153746851, 72.37146223051371, 72.47048333286403, 72.61476967614928, 73.48278855524502, 72.96503143206579, 72.97023909420189, 73.2104862336105, 73.29638526000547, 73.51753422876494, 73.54786732601848, 73.68963131776734, 73.81774902213414, 73.98414476605723, 74.23841507442732, 74.20438124045934, 74.27504809935719, 74.28243937308594, 74.68210808693102, 74.65004600795763, 75.84438298856415, 74.8876552794241, 74.98480347565867, 75.12984735076441, 75.30486044461068, 75.34204268761043, 76.66395924532696, 77.54052596209999, 77.5954173856553, 78.53968215825026, 79.43171964952926, 80.54716681172678, 81.5772200369611, 82.77017934363799, 83.46030358099618, 84.87898184629756, 85.99709000835344, 87.14247094541336, 87.1931272599602, 89.3747083421758, 90.59227387521533, 91.73158746690181, 92.05975468295983, 93.30413202576229, 94.87734694778467, 96.61403099080458]
#v100_FS_orig = [91.90040077772422, 93.55251345300556, 94.9755206871032, 96.88295345982931, 98.45768962847943, 102.9960453344312, 101.62066559272297, 103.09263469518136, 104.63081095210241, 106.26589066733371, 108.01132391246539, 109.69802105909852, 111.25078929549443, 112.9810433735894, 114.7127011338979, 116.23210124135562, 117.94904704323208, 119.5644531589289, 121.19680365385963, 122.97684831301983, 124.49040200507896, 129.6238846289278, 127.97797962627583, 129.3305631608876, 130.95045226932902, 132.14544109222263, 134.29215262196212, 135.9631493640822, 136.31129042212976, 138.7076198967757, 139.2184661036195, 141.24400624637894, 142.59229602771634, 144.31903045634385, 145.94465294197542, 147.5392126781328, 149.34197007645136, 155.5916656340885, 152.96241122388327, 157.03093215645018, 160.48199150383292, 162.60601644392736, 166.31242807959913, 170.48333806546816, 175.1571707135506, 180.18015958305034, 181.1795983326214, 188.84154507504738, 191.64573388680253, 197.77763938845985, 205.4822263821075, 207.32258451385883, 213.5252296034202, 219.2092543590473, 226.4041392780531, 236.00188807797605, 237.62922387557094, 245.79278911869883, 247.54819984458507, 247.68252377686142, 248.00437452156146, 247.07130956003155, 247.56521250342502]    
v100_FS_orig = [47.38500810964761, 47.37711800514539, 47.40432239255377, 47.41691952877924, 47.39371372943754, 47.396533084700756, 47.37411077084517, 47.381650621423724, 47.405562545523665, 47.40068210027356, 47.4170781424098, 47.37993455169595, 47.41734057372372, 47.37654178181854, 47.379249832568696, 47.44053328403669, 67.49682097483206, 67.50318526049308, 67.52143681439509, 67.50822131429571, 67.51895621661635, 67.57442160264827, 67.56192090777037, 67.57739739017526, 67.57415168460948, 67.53687915208037, 67.51772848533345, 67.53083066956664, 67.5186248206744, 67.48169902730247, 67.54667770846653, 67.55921429295114, 67.54665588589621, 67.57510130367153, 67.4995043911048, 67.48737849480442, 67.4666075312601, 67.4675645300943, 67.47526772726961, 67.4343509330909, 67.50974361427356, 67.53119624794498, 67.49647618640553, 67.53568446399382, 67.57064323769248, 67.56200409966112, 67.55621775882413, 67.59937335424482, 68.35747409293177, 82.18679038312519, 110.2892756938365, 111.01603609423346, 112.23159618091283, 113.26543675643298, 114.2174584649568, 115.33962183351301, 116.18474068269968, 117.38620707054241, 119.36360173134563, 120.19195680699022, 121.01694655239591, 122.3954418777867, 124.6455620993133, 125.77605210600154, 126.98904725286876, 128.11233280267763, 130.41230133510996, 130.9052810578362, 132.11146322786698, 133.5457019490167, 134.77017619068184, 136.64559051804972, 138.43519878672714, 138.537348018569, 140.40850748802197, 141.78338106985407, 143.46445279817465, 144.35974639159397, 145.4478320232289, 146.84898388561967, 148.10460468071673, 149.44644852200088, 149.83633721524927, 151.38929795899696, 152.85469057771815, 154.35720221442392, 155.36648742941824, 156.1432856447791, 157.04528512744645, 158.31765446565092, 159.82626123127207, 160.61948996789917, 162.85442451348996, 163.00959865168534, 164.60252165795904, 165.26667686767988, 167.20771556251853, 168.57564850658338, 169.60009435520118, 170.37666581861583, 171.48945392606453, 172.78063584898686, 174.2002411431741, 175.1673976068341, 176.5730337833191, 177.2621206355289, 179.05730325444281, 180.8404377369861, 182.4834600827653, 182.64928270835236, 183.99196724727318, 185.48530040181637, 186.68804885087164, 187.99909141619895, 189.72143341657699, 190.72991541089314, 191.38596115247907, 192.92467297734026, 194.2552589938543, 195.1862114608869, 197.0505791337922, 198.3978497063621, 199.30704269419587, 200.89897003684135, 202.3267509398542, 203.4275690030682, 204.9300381809836, 206.017005296299, 207.47168401174184, 209.12816253478098, 210.35153545056772, 212.38693649808056, 217.65309338024596, 217.71127452927158, 223.72946186101373, 223.73420723085994, 230.42370981937717, 230.87072778600455, 236.53545678240602, 236.68825738992513, 239.4213035608987, 240.61875840510325, 245.64239289182026, 245.22197765262047, 246.42839395261785, 246.50400755733017, 246.73660574496682, 246.84932750443934, 246.85521642326393, 246.92950109038955, 247.0088946477654, 247.05700340026402, 247.07509806959848, 247.13863676732092, 247.1864192085035, 247.18980840971147, 247.1074147356135, 247.21710654426792, 247.18119935726477, 247.1766146900569, 247.20927279381658, 247.28351793097485, 247.2118251114183, 247.1888296363975, 247.32570426805668, 247.2631966513927, 246.749585031889]
    
p100_dgemm_orig = np.array(DGEMM_orig)
p100_fs_orig = np.array(FS_orig)
    
v100_dgemm_orig = np.array(v100_DGEMM_orig)
v100_fs_orig = np.array(v100_FS_orig)

# start MEAN STD 
v100_freqs_mean = np.mean(v100_frequency_array)
v100_freqs_std = np.std(v100_frequency_array)
v100_pwr_mean = np.mean((v100_dgemm_orig))
v100_pwr_std = np.std(v100_dgemm_orig)
# start standardization and co-efficient
freqs_standard = (v100_frequency_array - v100_freqs_mean) / v100_freqs_std 
pwr_standard = (v100_dgemm_orig - v100_pwr_mean) / v100_pwr_std
coefficient = np.mean(freqs_standard * pwr_standard)
# power slope and power intercept
pwr_slope = coefficient * (v100_pwr_std/v100_freqs_std)
pwr_intercept = v100_pwr_mean - (pwr_slope * v100_freqs_mean)

print ('V100 Frequency Mean: ',v100_freqs_mean,'V100 Slope:',pwr_slope,'Intercept: ',pwr_intercept,'coefficient:', coefficient)
fff = 1380
predicted_pwr = pwr_slope * fff + pwr_intercept

print('Predicted power for',fff, 'MHz:', predicted_pwr)
# sys.exit(0)
p100_computed_voltage = np.sqrt(p100_frequency_array/p100_dgemm_orig)
v100_computed_voltage = np.sqrt(v100_frequency_array/v100_dgemm_orig)

def plotData(DGEMM_predicted_pwr, FS_predicted_pwr, STREAM_predicted_pwr,v100_DGEMM_predicted_pwr,a100_DGEMM_predicted_pwr,v100_FS_predicted_pwr):
    #from sklearn.metrics import mean_squared_error
    #from math import sqrt

    #rms = sqrt(mean_squared_error(pgP100, DGEMM_predicted_pwr))
    p100_dgemm_loss = np.sqrt(np.mean(np.square(((p100_dgemm_orig - DGEMM_predicted_pwr) / p100_dgemm_orig)), axis=0))
    p100_dgemm_loss = int(p100_dgemm_loss*100)
    print ('p100_dgemm_loss',p100_dgemm_loss)
    p100_fs_loss = np.sqrt(np.mean(np.square(((p100_fs_orig - FS_predicted_pwr) / p100_fs_orig)), axis=0))
    p100_fs_loss = int(p100_fs_loss*100)
    print ('p100_fs_loss',p100_fs_loss)
    
    v100_dgemm_loss = np.sqrt(np.mean(np.square(((v100_dgemm_orig - v100_DGEMM_predicted_pwr) / v100_dgemm_orig)), axis=0))
    v100_dgemm_loss = int(v100_dgemm_loss*100)
    print ('v100_dgemm_loss',v100_dgemm_loss)
    v100_fs_loss = np.sqrt(np.mean(np.square(((v100_fs_orig - v100_FS_predicted_pwr) / v100_fs_orig)), axis=0))
    v100_fs_loss = int(v100_fs_loss*100)
    print ('v100_fs_loss',v100_fs_loss)
   
    pltPath = 'C:/rf/lbnl/plots/examples/'    
    
    # combine
    plt.figure(1)
    plt.style.use('classic')

    plt.plot(p100_frequency_array,p100_dgemm_orig,linestyle='solid', label='P100 DGEMM (Real Power)',c='red')
    plt.plot(p100_frequency_array,DGEMM_predicted_pwr,linestyle='dashed', marker='.', markersize=6,label="P100 DGEMM (Predicted Power), Accuracy:"+str(100-p100_dgemm_loss)+"%",c='red')
    
    plt.plot(v100_frequency_array,v100_dgemm_orig,linestyle='solid', label='V100 DGEMM (Real Power)',c='green')
    plt.plot(v100_frequency_array,v100_DGEMM_predicted_pwr,linestyle='dashed', marker='.', markersize=6,label="V100 DGEMM (Predicted Power), Accuracy:"+str(100-v100_dgemm_loss)+"%",c='green')
    
    plt.plot(v100_frequency_array,a100_DGEMM_predicted_pwr,linestyle='dashed', marker='.', markersize=6,label="A100 DGEMM (Predicted Power)",c='blue')

    plt.xlabel('Core Frequency (MHz)')
    plt.ylabel('Power (W)')
    #axis = plt.gca()
    #axis.set_ylim ( [1,410])
    plt.grid(True)
    plt.legend(loc='upper left',prop={'size': 9})
    plt.savefig(pltPath+'combine-predicted-dgemmreg_refv100.png')
    
    # P100
    plt.figure(2)
    plt.style.use('classic')

    plt.plot(p100_frequency_array,p100_dgemm_orig,linestyle='solid', label='P100 DGEMM (Real Power)',c='red')
    plt.plot(p100_frequency_array,DGEMM_predicted_pwr,linestyle='dashed', marker='d', markersize=3,label="P100 DGEMM (Predicted Power), Accuracy:"+str(100-p100_dgemm_loss)+"%",c='red')
    
    # plt.plot(p100_frequency_array,p100_fs_orig,linestyle='solid', label='P100 FIRESTARTER (Real Power)',c='blue')
    # plt.plot(p100_frequency_array,FS_predicted_pwr,linestyle='dashed', marker='.', markersize=3,label="P100 FIRESTARTER (Predicted Power), Accuracy:"+str(100-p100_fs_loss)+"%",c='blue')
    plt.axhline(y=250, color='orange', lw=2,linestyle='--',label="GP100 TDP")
    plt.ylim(0, 260)
    plt.xlabel('Core Frequency (MHz)',weight='bold',fontsize=10)
    plt.ylabel('Power (W)',weight='bold',fontsize=10)
    plt.grid(True)
    plt.legend(loc='lower right',prop={'size': 10})
    plt.savefig(pltPath+'p100-pwr-predictionreg_refv100.png')
    
    # V100
    plt.figure(3)
    plt.style.use('classic')

    plt.plot(v100_frequency_array,v100_dgemm_orig,linestyle='solid', label='V100 DGEMM (Real Power)',c='red')
    plt.plot(v100_frequency_array,v100_DGEMM_predicted_pwr,linestyle='dashed', marker='d', markersize=3,c='red',label="V100 DGEMM (Predicted Power), Accuracy:"+str(100-v100_dgemm_loss)+"%")
    
    # plt.plot(v100_frequency_array,v100_fs_orig,linestyle='solid', label='V100 FIRESTARTER (Real Power)',c='blue')
    # plt.plot(v100_frequency_array,v100_FS_predicted_pwr,linestyle='dashed', marker='.', markersize=3,c='blue',label="V100 FIRESTARTER (Predicted Power), Accuracy:"+str(100-v100_fs_loss)+"%")
    plt.axhline(y=250, color='orange', lw=2,linestyle='--',label="GV100 TDP")
    plt.ylim(0, 260)
    plt.xlabel('Core Frequency (MHz)',weight='bold',fontsize=10)
    plt.ylabel('Power (W)',weight='bold',fontsize=10)
    plt.grid(True)
    plt.legend(loc='lower right',prop={'size': 10})
    plt.savefig(pltPath+'v100-pwr-predictionreg_refv100.png')
    
    # A100
    plt.figure(4)
    plt.style.use('classic')

    plt.plot(v100_frequency_array,a100_DGEMM_predicted_pwr,linestyle='dashed', marker='d',markersize=3, c='red',label="A100 DGEMM (Predicted Power)")
    plt.axhline(y=400, color='orange', lw=2,linestyle='--',label="GA100 TDP")
    plt.ylim(0, 410)
    plt.xlabel('Core Frequency (MHz)',weight='bold',fontsize=10)
    plt.ylabel('Power (W)',weight='bold',fontsize=10)
    plt.grid(True)
    plt.legend(loc='center left',prop={'size': 10})
    plt.savefig(pltPath+'a100-pwr-prediction-reg_refv100.png')
    
    
    
    
    '''    
    # FIRESTARTER
    plt.figure(2)
    plt.style.use('classic')

    plt.plot(F,FS_orig,linestyle='solid', label='FIRESTARTER Real Power Usage')
    plt.plot(F,FS_predicted_pwr,linestyle='dashed', marker='.', markersize=6,label="FIRESTARTER Predicted Power Usage")
    
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('Power (W)')
    axis = plt.gca()
    axis.set_ylim ( [1,410])
    plt.grid(True)
    plt.legend(loc='upper left',prop={'size': 9})
    plt.savefig('FS.png')

    # STREAM
    plt.figure(3)
    plt.style.use('classic')
    
    plt.plot(F,STREAM_orig,linestyle='solid', label='STREAM Real Power Usage')
    plt.plot(F,STREAM_predicted_pwr,linestyle='dashed', marker='.', markersize=6,label="STREAM Predicted Power Usage")
    
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('Power (W)')
    plt.grid(True)
    axis = plt.gca()
    axis.set_ylim ( [1,410])
    plt.legend(loc='upper left',prop={'size': 9})
    plt.savefig('stream.png')
    '''
    

# P100
min_freq_volt = 1.8#0.8 #0.55
max_freq_volt = 1.9
volt_inc_step = (max_freq_volt - min_freq_volt)/len(freqs)
voltage_array = np.arange(min_freq_volt, max_freq_volt, volt_inc_step)
#voltage_array = np.ones(len(freqs)) * max_freq_volt
#voltage_array = np.delete (voltage_array,-1)
#print ("Voltages: ", voltage_array)

min_freq = 544
max_freq = 1328
freq_ranges = 63

Idle_Power = 25
HBM_Power = 30

ref_SMs = 80
given_SMs = 56
new_arch_pwr_factor = given_SMs/ref_SMs

#Min_Freq_Power + Unit_Freq_Power * (Given_Freq – Min_Freq) * pow(V,2)
Base_Freq_Dynamic_Power = 91.26
unit_frequency_power = (Base_Freq_Dynamic_Power - (Idle_Power+HBM_Power))/min_freq
Activity = 1
Base_Freq_Core_Pwr = unit_frequency_power * min_freq * pow(0.85,2) - Idle_Power
#DGEMM_predicted_pwr = Idle_Power + HBM_Power + unit_frequency_power * (p100_frequency_array - 544) * pow(p100_computed_voltage,2) * new_arch_pwr_factor
FS_predicted_pwr = Idle_Power + HBM_Power + unit_frequency_power * (p100_frequency_array - 544) * pow(voltage_array,2) * new_arch_pwr_factor
DGEMM_predicted_pwr = (pwr_slope * p100_frequency_array + pwr_intercept) * new_arch_pwr_factor
#Base_Freq_Dynamic_Power = 70.61
#Activity = 1/6
#unit_dynamic_frequency_power = 0.1176
STREAM_predicted_pwr = Idle_Power + HBM_Power +  Activity * unit_frequency_power * (p100_frequency_array - 544) * pow(voltage_array,2) * new_arch_pwr_factor

# V100
min_freq_volt = 0.8
max_freq_volt = 1.25
volt_inc_step = (max_freq_volt - min_freq_volt)/len(v100_freqs)
v100_voltage_array = np.arange(min_freq_volt, max_freq_volt, volt_inc_step)
#v100_voltage_array = np.delete (v100_voltage_array,-1)

min_freq = 135
max_freq = 1328

Idle_Power = 27
HBM_Power = 35
ref_SMs = 80
given_SMs = 80

new_arch_pwr_factor = given_SMs/ref_SMs
#new_arch_pwr_factor = (21.1/15.3)
#Min_Freq_Power + Unit_Freq_Power * (Given_Freq – Min_Freq) * pow(V,2)
#Base_Freq_Dynamic_Power = 91.26
#unit_frequency_power = 0.1176
Activity = 1 #Base_Freq_Core_Pwr + 
#Base_Freq_Core_Pwr = unit_frequency_power * 135 * pow(0.85,2) - Idle_Power
#v100_DGEMM_predicted_pwr = Idle_Power + HBM_Power + unit_frequency_power * (v100_frequency_array - 135) * pow(v100_computed_voltage,2) * new_arch_pwr_factor
v100_DGEMM_predicted_pwr = (pwr_slope * v100_frequency_array + pwr_intercept) * new_arch_pwr_factor
#Base_Freq_Dynamic_Power = 91.9
v100_FS_predicted_pwr = Idle_Power + HBM_Power + unit_frequency_power * (v100_frequency_array - 135) * pow(v100_voltage_array,2) * new_arch_pwr_factor
#Base_Freq_Dynamic_Power = 70.61
#Activity = 1/6
#v100_STREAM_predicted_pwr = Idle_Power + HBM_Power +  Activity * unit_dynamic_frequency_power * (frequency_array - 544) * pow(voltage_array,2) * new_arch_pwr_factor

#A100
min_freq_volt = 0.5 #0.55
max_freq_volt = 1.35
volt_inc_step = (max_freq_volt - min_freq_volt)/len(v100_freqs)
a100_voltage_array = np.arange(min_freq_volt, max_freq_volt, volt_inc_step)

Idle_Power = 30
HBM_Power = 60
ref_SMs = 80
given_SMs = 108
new_arch_pwr_factor = given_SMs/ref_SMs
#new_arch_pwr_factor = (54.2/15.3) #Base_Freq_Core_Pwr +
a100_DGEMM_predicted_pwr = (pwr_slope * v100_frequency_array + pwr_intercept) * new_arch_pwr_factor

#predicted_pwr = pwr_slope * 544 + pwr_intercept
#a100_DGEMM_predicted_pwr = Idle_Power + HBM_Power +  unit_frequency_power * (v100_frequency_array - 100) * pow(a100_voltage_array,2) * new_arch_pwr_factor
                                                                                                          
plotData(DGEMM_predicted_pwr, FS_predicted_pwr, STREAM_predicted_pwr,v100_DGEMM_predicted_pwr,a100_DGEMM_predicted_pwr,v100_FS_predicted_pwr)