# script-version: 2.0
# Catalyst state generated using paraview version 5.10.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1611, 725]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.0, -0.000701904296875, 500.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [1964.259862960441, -0.000701904296875, 500.0]
renderView1.CameraFocalPoint = [0.0, -0.000701904296875, 500.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraViewAngle = 21.60919540229885
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 508.3878620646296
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1611, 725)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XDMF Reader'
grid = XDMFReader(registrationName='grid', FileNames=['/scratch/ritali/project-ram-pressure/model-for-rps/final-setup-params/check/check-again/temp2e6/overpressurised/output/data.0000.dbl.xmf', '/scratch/ritali/project-ram-pressure/model-for-rps/final-setup-params/check/check-again/temp2e6/overpressurised/output/data.0001.dbl.xmf'])
grid.CellArrayStatus = ['PbykB', 'Temp', 'X', 'Y', 'Z', 'mach', 'ndens', 'prs', 'rho', 'tr1', 'tr2', 'tr3', 'vx1', 'vx2', 'vx3']
grid.GridStatus = ['node_mesh']

# create a new 'Annotate Time Filter'
annotateTimeFilter1 = AnnotateTimeFilter(registrationName='AnnotateTimeFilter1', Input=grid)
annotateTimeFilter1.Format = 'Time: {TEXT_time:.2f} Myr'
annotateTimeFilter1.Scale = 9.81

# create a new 'Ruler'
ruler1 = Ruler(registrationName='Ruler1')
ruler1.Point1 = [0.0, 130.0, 290.0]
ruler1.Point2 = [0.0, 230.0, 290.0]

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=grid)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.0, -0.00069427490234375, 500.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.0, -0.00069427490234375, 500.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from slice1
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'mach'
machLUT = GetColorTransferFunction('mach')
machLUT.RGBPoints = [0.0, 0.267004, 0.004874, 0.329415, 0.022976725191467543, 0.26851, 0.009605, 0.335427, 0.04594759196243751, 0.269944, 0.014625, 0.341379, 0.06892431715390505, 0.271305, 0.019942, 0.347269, 0.09189518392487502, 0.272594, 0.025563, 0.353093, 0.11487190911634257, 0.273809, 0.031497, 0.358853, 0.13784277588731253, 0.274952, 0.037752, 0.364543, 0.16081950107878007, 0.276022, 0.044167, 0.370164, 0.1837962262702476, 0.277018, 0.050344, 0.375715, 0.20676709304121757, 0.277941, 0.056324, 0.381191, 0.22974381823268514, 0.278791, 0.062145, 0.386592, 0.2527146850036551, 0.279566, 0.067836, 0.391917, 0.2756914101951226, 0.280267, 0.073417, 0.397163, 0.2986622769660926, 0.280894, 0.078907, 0.402329, 0.32163900215756014, 0.281446, 0.08432, 0.407414, 0.3446157273490277, 0.281924, 0.089666, 0.412415, 0.3675865941199976, 0.282327, 0.094955, 0.417331, 0.3905633193114652, 0.282656, 0.100196, 0.42216, 0.41353418608243514, 0.28291, 0.105393, 0.426902, 0.43651091127390274, 0.283091, 0.110553, 0.431554, 0.45948177804487267, 0.283197, 0.11568, 0.436115, 0.4824585032363402, 0.283229, 0.120777, 0.440584, 0.5054352284278077, 0.283187, 0.125848, 0.44496, 0.5284060951987777, 0.283072, 0.130895, 0.449241, 0.5513828203902452, 0.282884, 0.13592, 0.453427, 0.5743536871612153, 0.282623, 0.140926, 0.457517, 0.5973304123526828, 0.28229, 0.145912, 0.46151, 0.6203012791236527, 0.281887, 0.150881, 0.465405, 0.6432780043151203, 0.281412, 0.155834, 0.469201, 0.6662488710860903, 0.280868, 0.160771, 0.472899, 0.6892255962775579, 0.280255, 0.165693, 0.476498, 0.7122023214690253, 0.279574, 0.170599, 0.479997, 0.7351731882399952, 0.278826, 0.17549, 0.483397, 0.7581499134314629, 0.278012, 0.180367, 0.486697, 0.7811207802024329, 0.277134, 0.185228, 0.489898, 0.8040975053939003, 0.276194, 0.190074, 0.493001, 0.8270683721648703, 0.275191, 0.194905, 0.496005, 0.8500450973563379, 0.274128, 0.199721, 0.498911, 0.8730218225478055, 0.273006, 0.20452, 0.501721, 0.8959926893187754, 0.271828, 0.209303, 0.504434, 0.9189694145102429, 0.270595, 0.214069, 0.507052, 0.941940281281213, 0.269308, 0.218818, 0.509577, 0.9649170064726804, 0.267968, 0.223549, 0.512008, 0.9878878732436505, 0.26658, 0.228262, 0.514349, 1.0108645984351181, 0.265145, 0.232956, 0.516599, 1.0338413236265855, 0.263663, 0.237631, 0.518762, 1.0568121903975554, 0.262138, 0.242286, 0.520837, 1.079788915589023, 0.260571, 0.246922, 0.522828, 1.102759782359993, 0.258965, 0.251537, 0.524736, 1.1257365075514605, 0.257322, 0.25613, 0.526563, 1.1487073743224305, 0.255645, 0.260703, 0.528312, 1.1716840995138982, 0.253935, 0.265254, 0.529983, 1.1946608247053656, 0.252194, 0.269783, 0.531579, 1.2176316914763357, 0.250425, 0.27429, 0.533103, 1.240608416667803, 0.248629, 0.278775, 0.534556, 1.263579283438773, 0.246811, 0.283237, 0.535941, 1.2865560086302406, 0.244972, 0.287675, 0.53726, 1.3095268754012106, 0.243113, 0.292092, 0.538516, 1.332503600592678, 0.241237, 0.296485, 0.539709, 1.3554803257841457, 0.239346, 0.300855, 0.540844, 1.3784511925551157, 0.237441, 0.305202, 0.541921, 1.4014279177465832, 0.235526, 0.309527, 0.542944, 1.4243987845175532, 0.233603, 0.313828, 0.543914, 1.4473755097090206, 0.231674, 0.318106, 0.544834, 1.4703463764799904, 0.229739, 0.322361, 0.545706, 1.4933231016714583, 0.227802, 0.326594, 0.546532, 1.5162998268629257, 0.225863, 0.330805, 0.547314, 1.5392706936338958, 0.223925, 0.334994, 0.548053, 1.5622474188253632, 0.221989, 0.339161, 0.548752, 1.5852182855963333, 0.220057, 0.343307, 0.549413, 1.6081950107878007, 0.21813, 0.347432, 0.550038, 1.6311658775587707, 0.21621, 0.351535, 0.550627, 1.6541426027502384, 0.214298, 0.355619, 0.551184, 1.6771193279417058, 0.212395, 0.359683, 0.55171, 1.7000901947126759, 0.210503, 0.363727, 0.552206, 1.7230669199041433, 0.208623, 0.367752, 0.552675, 1.7460377866751133, 0.206756, 0.371758, 0.553117, 1.7690145118665808, 0.204903, 0.375746, 0.553533, 1.7919853786375508, 0.203063, 0.379716, 0.553925, 1.8149621038290185, 0.201239, 0.38367, 0.554294, 1.8379329705999883, 0.19943, 0.387607, 0.554642, 1.860909695791456, 0.197636, 0.391528, 0.554969, 1.8838864209829234, 0.19586, 0.395433, 0.555276, 1.9068572877538934, 0.1941, 0.399323, 0.555565, 1.9298340129453608, 0.192357, 0.403199, 0.555836, 1.9528048797163309, 0.190631, 0.407061, 0.556089, 1.9757816049077985, 0.188923, 0.41091, 0.556326, 1.9987524716787683, 0.187231, 0.414746, 0.556547, 2.0217291968702362, 0.185556, 0.41857, 0.556753, 2.0447059220617034, 0.183898, 0.422383, 0.556944, 2.0676767888326735, 0.182256, 0.426184, 0.55712, 2.090653514024141, 0.180629, 0.429975, 0.557282, 2.1136243807951107, 0.179019, 0.433756, 0.55743, 2.1366011059865784, 0.177423, 0.437527, 0.557565, 2.1595719727575484, 0.175841, 0.44129, 0.557685, 2.182548697949016, 0.174274, 0.445044, 0.557792, 2.2055254231404837, 0.172719, 0.448791, 0.557885, 2.2284962899114538, 0.171176, 0.45253, 0.557965, 2.251473015102921, 0.169646, 0.456262, 0.55803, 2.274443881873891, 0.168126, 0.459988, 0.558082, 2.2974206070653587, 0.166617, 0.463708, 0.558119, 2.3203914738363283, 0.165117, 0.467423, 0.558141, 2.3433681990277964, 0.163625, 0.471133, 0.558148, 2.3663449242192636, 0.162142, 0.474838, 0.55814, 2.3893157909902336, 0.160665, 0.47854, 0.558115, 2.4122925161817013, 0.159194, 0.482237, 0.558073, 2.4352633829526713, 0.157729, 0.485932, 0.558013, 2.4582401081441385, 0.15627, 0.489624, 0.557936, 2.4812109749151086, 0.154815, 0.493313, 0.55784, 2.504187700106576, 0.153364, 0.497, 0.557724, 2.527164425298044, 0.151918, 0.500685, 0.557587, 2.550135292069014, 0.150476, 0.504369, 0.55743, 2.573112017260481, 0.149039, 0.508051, 0.55725, 2.596082884031451, 0.147607, 0.511733, 0.557049, 2.619059609222919, 0.14618, 0.515413, 0.556823, 2.642030475993889, 0.144759, 0.519093, 0.556572, 2.665007201185356, 0.143343, 0.522773, 0.556295, 2.6879839263768237, 0.141935, 0.526453, 0.555991, 2.7109547931477938, 0.140536, 0.530132, 0.555659, 2.7339315183392614, 0.139147, 0.533812, 0.555298, 2.7569023851102314, 0.13777, 0.537492, 0.554906, 2.7798791103016987, 0.136408, 0.541173, 0.554483, 2.8028499770726687, 0.135066, 0.544853, 0.554029, 2.8258267022641363, 0.133743, 0.548535, 0.553541, 2.848803427455604, 0.132444, 0.552216, 0.553018, 2.871774294226574, 0.131172, 0.555899, 0.552459, 2.8947510194180412, 0.129933, 0.559582, 0.551864, 2.9177218861890113, 0.128729, 0.563265, 0.551229, 2.940698611380479, 0.127568, 0.566949, 0.550556, 2.963669478151449, 0.126453, 0.570633, 0.549841, 2.9866462033429166, 0.125394, 0.574318, 0.549086, 3.0096170701138862, 0.124395, 0.578002, 0.548287, 3.032593795305354, 0.123463, 0.581687, 0.547445, 3.055570520496821, 0.122606, 0.585371, 0.546557, 3.0785413872677916, 0.121831, 0.589055, 0.545623, 3.101518112459259, 0.121148, 0.592739, 0.544641, 3.124488979230229, 0.120565, 0.596422, 0.543611, 3.1474657044216965, 0.120092, 0.600104, 0.54253, 3.1704365711926665, 0.119738, 0.603785, 0.5414, 3.1934132963841337, 0.119512, 0.607464, 0.540218, 3.2163900215756014, 0.119423, 0.611141, 0.538982, 3.2393608883465714, 0.119483, 0.614817, 0.537692, 3.262337613538039, 0.119699, 0.61849, 0.536347, 3.2853084803090087, 0.120081, 0.622161, 0.534946, 3.3082852055004768, 0.120638, 0.625828, 0.533488, 3.3312560722714464, 0.12138, 0.629492, 0.531973, 3.354232797462914, 0.122312, 0.633153, 0.530398, 3.3772095226543812, 0.123444, 0.636809, 0.528763, 3.4001803894253517, 0.12478, 0.640461, 0.527068, 3.423157114616819, 0.126326, 0.644107, 0.525311, 3.446127981387789, 0.128087, 0.647749, 0.523491, 3.469104706579257, 0.130067, 0.651384, 0.521608, 3.4920755733502267, 0.132268, 0.655014, 0.519661, 3.515052298541694, 0.134692, 0.658636, 0.517649, 3.5380290237331615, 0.137339, 0.662252, 0.515571, 3.5609998905041316, 0.14021, 0.665859, 0.513427, 3.583976615695599, 0.143303, 0.669459, 0.511215, 3.606947482466569, 0.146616, 0.67305, 0.508936, 3.629924207658037, 0.150148, 0.676631, 0.506589, 3.6528950744290065, 0.153894, 0.680203, 0.504172, 3.675871799620474, 0.157851, 0.683765, 0.501686, 3.6988485248119414, 0.162016, 0.687316, 0.499129, 3.721819391582912, 0.166383, 0.690856, 0.496502, 3.7447961167743795, 0.170948, 0.694384, 0.493803, 3.767766983545349, 0.175707, 0.6979, 0.491033, 3.790743708736817, 0.180653, 0.701402, 0.488189, 3.813714575507787, 0.185783, 0.704891, 0.485273, 3.836691300699254, 0.19109, 0.708366, 0.482284, 3.8596680258907217, 0.196571, 0.711827, 0.479221, 3.882638892661692, 0.202219, 0.715272, 0.476084, 3.9056156178531594, 0.20803, 0.718701, 0.472873, 3.928586484624129, 0.214, 0.722114, 0.469588, 3.951563209815597, 0.220124, 0.725509, 0.466226, 3.9745340765865667, 0.226397, 0.728888, 0.462789, 3.9975108017780343, 0.232815, 0.732247, 0.459277, 4.020487526969502, 0.239374, 0.735588, 0.455688, 4.0434583937404724, 0.24607, 0.73891, 0.452024, 4.066435118931939, 0.252899, 0.742211, 0.448284, 4.089405985702909, 0.259857, 0.745492, 0.444467, 4.1123827108943765, 0.266941, 0.748751, 0.440573, 4.135353577665347, 0.274149, 0.751988, 0.436601, 4.158330302856815, 0.281477, 0.755203, 0.432552, 4.181301169627785, 0.288921, 0.758394, 0.428426, 4.204277894819252, 0.296479, 0.761561, 0.424223, 4.2272546200107195, 0.304148, 0.764704, 0.419943, 4.250225486781689, 0.311925, 0.767822, 0.415586, 4.273202211973157, 0.319809, 0.770914, 0.411152, 4.296173078744127, 0.327796, 0.77398, 0.40664, 4.319149803935595, 0.335885, 0.777018, 0.402049, 4.3421206707065645, 0.344074, 0.780029, 0.397381, 4.365097395898032, 0.35236, 0.783011, 0.392636, 4.3880741210895, 0.360741, 0.785964, 0.387814, 4.411044987860469, 0.369214, 0.788888, 0.382914, 4.434021713051937, 0.377779, 0.791781, 0.377939, 4.4569925798229075, 0.386433, 0.794644, 0.372886, 4.479969305014374, 0.395174, 0.797475, 0.367757, 4.502940171785344, 0.404001, 0.800275, 0.362552, 4.525916896976812, 0.412913, 0.803041, 0.357269, 4.54889362216828, 0.421908, 0.805774, 0.35191, 4.57186448893925, 0.430983, 0.808473, 0.346476, 4.594841214130717, 0.440137, 0.811138, 0.340967, 4.617812080901687, 0.449368, 0.813768, 0.335384, 4.640788806093155, 0.458674, 0.816363, 0.329727, 4.663759672864124, 0.468053, 0.818921, 0.323998, 4.686736398055593, 0.477504, 0.821444, 0.318195, 4.7097131232470595, 0.487026, 0.823929, 0.312321, 4.73268399001803, 0.496615, 0.826376, 0.306377, 4.755660715209497, 0.506271, 0.828786, 0.300362, 4.778631581980467, 0.515992, 0.831158, 0.294279, 4.801608307171935, 0.525776, 0.833491, 0.288127, 4.8245791739429045, 0.535621, 0.835785, 0.281908, 4.847555899134372, 0.545524, 0.838039, 0.275626, 4.87053262432584, 0.555484, 0.840254, 0.269281, 4.893503491096809, 0.565498, 0.84243, 0.262877, 4.916480216288277, 0.575563, 0.844566, 0.256415, 4.9394510830592475, 0.585678, 0.846661, 0.249897, 4.962427808250715, 0.595839, 0.848717, 0.243329, 4.985398675021685, 0.606045, 0.850733, 0.236712, 5.008375400213152, 0.616293, 0.852709, 0.230052, 5.03135212540462, 0.626579, 0.854645, 0.223353, 5.05432299217559, 0.636902, 0.856542, 0.21662, 5.077299717367057, 0.647257, 0.8584, 0.209861, 5.100270584138028, 0.657642, 0.860219, 0.203082, 5.123247309329495, 0.668054, 0.861999, 0.196293, 5.146218176100465, 0.678489, 0.863742, 0.189503, 5.169194901291933, 0.688944, 0.865448, 0.182725, 5.1921716264834, 0.699415, 0.867117, 0.175971, 5.21514249325437, 0.709898, 0.868751, 0.169257, 5.238119218445838, 0.720391, 0.87035, 0.162603, 5.261090085216807, 0.730889, 0.871916, 0.156029, 5.284066810408275, 0.741388, 0.873449, 0.149561, 5.3070376771792445, 0.751884, 0.874951, 0.143228, 5.330014402370712, 0.762373, 0.876424, 0.137064, 5.352985269141683, 0.772852, 0.877868, 0.131109, 5.37596199433315, 0.783315, 0.879285, 0.125405, 5.398938719524617, 0.79376, 0.880678, 0.120005, 5.4219095862955875, 0.804182, 0.882046, 0.114965, 5.444886311487055, 0.814576, 0.883393, 0.110347, 5.467857178258025, 0.82494, 0.88472, 0.106217, 5.490833903449492, 0.83527, 0.886029, 0.102646, 5.513804770220463, 0.845561, 0.887322, 0.099702, 5.53678149541193, 0.85581, 0.888601, 0.097452, 5.559758220603397, 0.866013, 0.889868, 0.095953, 5.582729087374368, 0.876168, 0.891125, 0.09525, 5.6057058125658354, 0.886271, 0.892374, 0.095374, 5.628676679336805, 0.89632, 0.893616, 0.096335, 5.651653404528273, 0.906311, 0.894855, 0.098125, 5.674624271299242, 0.916242, 0.896091, 0.100717, 5.69760099649071, 0.926106, 0.89733, 0.104071, 5.720577721682178, 0.935904, 0.89857, 0.108131, 5.743548588453148, 0.945636, 0.899815, 0.112838, 5.766525313644616, 0.9553, 0.901065, 0.118128, 5.789496180415585, 0.964894, 0.902323, 0.123941, 5.812472905607052, 0.974417, 0.90359, 0.130215, 5.835443772378023, 0.983868, 0.904867, 0.136897, 5.85842049756949, 0.993248, 0.906157, 0.143936]
machLUT.NanColor = [1.0, 0.0, 0.0]
machLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['CELLS', 'mach']
slice1Display.LookupTable = machLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 48.0
slice1Display.SelectScaleArray = 'rho'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'rho'
slice1Display.GaussianRadius = 2.4
slice1Display.SetScaleArray = [None, '']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = [None, '']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# show data from annotateTimeFilter1
annotateTimeFilter1Display = Show(annotateTimeFilter1, renderView1, 'TextSourceRepresentation')

# trace defaults for the display properties.
annotateTimeFilter1Display.WindowLocation = 'Upper Center'
annotateTimeFilter1Display.Position = [0.45061728395061723, 0.9375862068965517]
annotateTimeFilter1Display.Bold = 1
annotateTimeFilter1Display.FontSize = 23

# show data from ruler1
ruler1Display = Show(ruler1, renderView1, 'RulerSourceRepresentation')

# trace defaults for the display properties.
ruler1Display.LabelFormat = '%6.3g kpc'
ruler1Display.RulerMode = 1
ruler1Display.Graduation = 25.0
ruler1Display.AxisColor = [0.6666666666666666, 0.6666666666666666, 1.0]
ruler1Display.Color = [0.6666666666666666, 0.6666666666666666, 1.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for machLUT in view renderView1
machLUTColorBar = GetScalarBar(machLUT, renderView1)
machLUTColorBar.WindowLocation = 'Any Location'
machLUTColorBar.Position = [0.7262569832402234, 0.25241379310344825]
machLUTColorBar.Title = 'mach'
machLUTColorBar.ComponentTitle = ''
machLUTColorBar.ScalarBarLength = 0.5258620689655173

# set color bar visibility
machLUTColorBar.Visibility = 1

# show color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'mach'
machPWF = GetOpacityTransferFunction('mach')
machPWF.Points = [0.0, 0.0, 0.5, 0.0, 5.85842049756949, 1.0, 0.5, 0.0]
machPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
# trace defaults for the extractor.
pNG1.Trigger = 'TimeValue'

# init the 'TimeValue' selected for 'Trigger'
pNG1.Trigger.Length = 0.5

# init the 'PNG' selected for 'Writer'
pNG1.Writer.FileName = 'mach_{timestep:06d}.png'
pNG1.Writer.ImageResolution = [1215, 725]
pNG1.Writer.FontScaling = 'Do not scale fonts'
pNG1.Writer.OverrideColorPalette = 'BlackBackground'
pNG1.Writer.Format = 'PNG'

# init the 'PNG' selected for 'Format'
pNG1.Writer.Format.CompressionLevel = '0'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(grid)
# ----------------------------------------------------------------

# ------------------------------------------------------------------------------
# Catalyst options
from paraview import catalyst
options = catalyst.Options()
options.ExtractsOutputDirectory = 'output/catalyst/mach'
options.GenerateCinemaSpecification = 1
options.GlobalTrigger = 'TimeValue'
options.EnableCatalystLive = 1
options.CatalystLiveTrigger = 'TimeStep'

# init the 'TimeValue' selected for 'GlobalTrigger'
options.GlobalTrigger.Length = 0.001

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    from paraview.simple import SaveExtractsUsingCatalystOptions
    # Code for non in-situ environments; if executing in post-processing
    # i.e. non-Catalyst mode, let's generate extracts using Catalyst options
    SaveExtractsUsingCatalystOptions(options)
