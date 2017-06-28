# api wrapper for three.js
__pragma__ ('noanno')

def _ctor(obj):
    def _c_(*args):
        return __new__(obj (*args))
    return _c_

api = __pragma__ ('js',
    '{}',
    'THREE'
    ,
    __include__('org/threejs/__javascript__/three.js')
)

WebGLRenderTargetCube = _ctor(api.WebGLRenderTargetCube)
WebGLRenderTarget = _ctor(api.WebGLRenderTarget)
WebGLRenderer = _ctor(api.WebGLRenderer)
ShaderLib = _ctor(api.ShaderLib)
UniformsLib = _ctor(api.UniformsLib)
UniformsUtils = _ctor(api.UniformsUtils)
ShaderChunk = _ctor(api.ShaderChunk)
FogExp2 = _ctor(api.FogExp2)
Fog = _ctor(api.Fog)
Scene = _ctor(api.Scene)
LensFlare = _ctor(api.LensFlare)
Sprite = _ctor(api.Sprite)
LOD = _ctor(api.LOD)
SkinnedMesh = _ctor(api.SkinnedMesh)
Skeleton = _ctor(api.Skeleton)
Bone = _ctor(api.Bone)
Mesh = _ctor(api.Mesh)
LineSegments = _ctor(api.LineSegments)
LineLoop = _ctor(api.LineLoop)
Line = _ctor(api.Line)
Points = _ctor(api.Points)
Group = _ctor(api.Group)
VideoTexture = _ctor(api.VideoTexture)
DataTexture = _ctor(api.DataTexture)
CompressedTexture = _ctor(api.CompressedTexture)
CubeTexture = _ctor(api.CubeTexture)
CanvasTexture = _ctor(api.CanvasTexture)
DepthTexture = _ctor(api.DepthTexture)
Texture = _ctor(api.Texture)
CompressedTextureLoader = _ctor(api.CompressedTextureLoader)
DataTextureLoader = _ctor(api.DataTextureLoader)
CubeTextureLoader = _ctor(api.CubeTextureLoader)
TextureLoader = _ctor(api.TextureLoader)
ObjectLoader = _ctor(api.ObjectLoader)
MaterialLoader = _ctor(api.MaterialLoader)
BufferGeometryLoader = _ctor(api.BufferGeometryLoader)
DefaultLoadingManager = _ctor(api.DefaultLoadingManager)
LoadingManager = _ctor(api.LoadingManager)
JSONLoader = _ctor(api.JSONLoader)
ImageLoader = _ctor(api.ImageLoader)
FontLoader = _ctor(api.FontLoader)
FileLoader = _ctor(api.FileLoader)
Loader = _ctor(api.Loader)
Cache = _ctor(api.Cache)
AudioLoader = _ctor(api.AudioLoader)
SpotLightShadow = _ctor(api.SpotLightShadow)
SpotLight = _ctor(api.SpotLight)
PointLight = _ctor(api.PointLight)
RectAreaLight = _ctor(api.RectAreaLight)
HemisphereLight = _ctor(api.HemisphereLight)
DirectionalLightShadow = _ctor(api.DirectionalLightShadow)
DirectionalLight = _ctor(api.DirectionalLight)
AmbientLight = _ctor(api.AmbientLight)
LightShadow = _ctor(api.LightShadow)
Light = _ctor(api.Light)
StereoCamera = _ctor(api.StereoCamera)
PerspectiveCamera = _ctor(api.PerspectiveCamera)
OrthographicCamera = _ctor(api.OrthographicCamera)
CubeCamera = _ctor(api.CubeCamera)
ArrayCamera = _ctor(api.ArrayCamera)
Camera = _ctor(api.Camera)
AudioListener = _ctor(api.AudioListener)
PositionalAudio = _ctor(api.PositionalAudio)
AudioContext = _ctor(api.AudioContext)
AudioAnalyser = _ctor(api.AudioAnalyser)
Audio = _ctor(api.Audio)
VectorKeyframeTrack = _ctor(api.VectorKeyframeTrack)
StringKeyframeTrack = _ctor(api.StringKeyframeTrack)
QuaternionKeyframeTrack = _ctor(api.QuaternionKeyframeTrack)
NumberKeyframeTrack = _ctor(api.NumberKeyframeTrack)
ColorKeyframeTrack = _ctor(api.ColorKeyframeTrack)
BooleanKeyframeTrack = _ctor(api.BooleanKeyframeTrack)
PropertyMixer = _ctor(api.PropertyMixer)
PropertyBinding = _ctor(api.PropertyBinding)
KeyframeTrack = _ctor(api.KeyframeTrack)
AnimationUtils = _ctor(api.AnimationUtils)
AnimationObjectGroup = _ctor(api.AnimationObjectGroup)
AnimationMixer = _ctor(api.AnimationMixer)
AnimationClip = _ctor(api.AnimationClip)
Uniform = _ctor(api.Uniform)
InstancedBufferGeometry = _ctor(api.InstancedBufferGeometry)
BufferGeometry = _ctor(api.BufferGeometry)
GeometryIdCount = _ctor(api.GeometryIdCount)
Geometry = _ctor(api.Geometry)
InterleavedBufferAttribute = _ctor(api.InterleavedBufferAttribute)
InstancedInterleavedBuffer = _ctor(api.InstancedInterleavedBuffer)
InterleavedBuffer = _ctor(api.InterleavedBuffer)
InstancedBufferAttribute = _ctor(api.InstancedBufferAttribute)
Face3 = _ctor(api.Face3)
Object3D = _ctor(api.Object3D)
Raycaster = _ctor(api.Raycaster)
Layers = _ctor(api.Layers)
EventDispatcher = _ctor(api.EventDispatcher)
Clock = _ctor(api.Clock)
QuaternionLinearInterpolant = _ctor(api.QuaternionLinearInterpolant)
LinearInterpolant = _ctor(api.LinearInterpolant)
DiscreteInterpolant = _ctor(api.DiscreteInterpolant)
CubicInterpolant = _ctor(api.CubicInterpolant)
Interpolant = _ctor(api.Interpolant)
Triangle = _ctor(api.Triangle)
Math = _ctor(api.Math)
Spherical = _ctor(api.Spherical)
Cylindrical = _ctor(api.Cylindrical)
Plane = _ctor(api.Plane)
Frustum = _ctor(api.Frustum)
Sphere = _ctor(api.Sphere)
Ray = _ctor(api.Ray)
Matrix4 = _ctor(api.Matrix4)
Matrix3 = _ctor(api.Matrix3)
Box3 = _ctor(api.Box3)
Box2 = _ctor(api.Box2)
Line3 = _ctor(api.Line3)
Euler = _ctor(api.Euler)
Vector3 = _ctor(api.Vector3)
Quaternion = _ctor(api.Quaternion)
Color = _ctor(api.Color)
MorphBlendMesh = _ctor(api.MorphBlendMesh)
ImmediateRenderObject = _ctor(api.ImmediateRenderObject)
VertexNormalsHelper = _ctor(api.VertexNormalsHelper)
SpotLightHelper = _ctor(api.SpotLightHelper)
SkeletonHelper = _ctor(api.SkeletonHelper)
PointLightHelper = _ctor(api.PointLightHelper)
RectAreaLightHelper = _ctor(api.RectAreaLightHelper)
HemisphereLightHelper = _ctor(api.HemisphereLightHelper)
GridHelper = _ctor(api.GridHelper)
PolarGridHelper = _ctor(api.PolarGridHelper)
FaceNormalsHelper = _ctor(api.FaceNormalsHelper)
DirectionalLightHelper = _ctor(api.DirectionalLightHelper)
CameraHelper = _ctor(api.CameraHelper)
BoxHelper = _ctor(api.BoxHelper)
ArrowHelper = _ctor(api.ArrowHelper)
AxisHelper = _ctor(api.AxisHelper)
CatmullRomCurve3 = _ctor(api.CatmullRomCurve3)
CubicBezierCurve3 = _ctor(api.CubicBezierCurve3)
QuadraticBezierCurve3 = _ctor(api.QuadraticBezierCurve3)
LineCurve3 = _ctor(api.LineCurve3)
ArcCurve = _ctor(api.ArcCurve)
EllipseCurve = _ctor(api.EllipseCurve)
SplineCurve = _ctor(api.SplineCurve)
CubicBezierCurve = _ctor(api.CubicBezierCurve)
QuadraticBezierCurve = _ctor(api.QuadraticBezierCurve)
LineCurve = _ctor(api.LineCurve)
Shape = _ctor(api.Shape)
Path = _ctor(api.Path)
ShapePath = _ctor(api.ShapePath)
Font = _ctor(api.Font)
CurvePath = _ctor(api.CurvePath)
Curve = _ctor(api.Curve)
ShapeUtils = _ctor(api.ShapeUtils)
SceneUtils = _ctor(api.SceneUtils)
WireframeGeometry = _ctor(api.WireframeGeometry)
ParametricGeometry = _ctor(api.ParametricGeometry)
ParametricBufferGeometry = _ctor(api.ParametricBufferGeometry)
TetrahedronGeometry = _ctor(api.TetrahedronGeometry)
TetrahedronBufferGeometry = _ctor(api.TetrahedronBufferGeometry)
OctahedronGeometry = _ctor(api.OctahedronGeometry)
OctahedronBufferGeometry = _ctor(api.OctahedronBufferGeometry)
IcosahedronGeometry = _ctor(api.IcosahedronGeometry)
IcosahedronBufferGeometry = _ctor(api.IcosahedronBufferGeometry)
DodecahedronGeometry = _ctor(api.DodecahedronGeometry)
DodecahedronBufferGeometry = _ctor(api.DodecahedronBufferGeometry)
PolyhedronGeometry = _ctor(api.PolyhedronGeometry)
PolyhedronBufferGeometry = _ctor(api.PolyhedronBufferGeometry)
TubeGeometry = _ctor(api.TubeGeometry)
TubeBufferGeometry = _ctor(api.TubeBufferGeometry)
TorusKnotGeometry = _ctor(api.TorusKnotGeometry)
TorusKnotBufferGeometry = _ctor(api.TorusKnotBufferGeometry)
TorusGeometry = _ctor(api.TorusGeometry)
TorusBufferGeometry = _ctor(api.TorusBufferGeometry)
TextGeometry = _ctor(api.TextGeometry)
TextBufferGeometry = _ctor(api.TextBufferGeometry)
SphereGeometry = _ctor(api.SphereGeometry)
SphereBufferGeometry = _ctor(api.SphereBufferGeometry)
RingGeometry = _ctor(api.RingGeometry)
RingBufferGeometry = _ctor(api.RingBufferGeometry)
PlaneGeometry = _ctor(api.PlaneGeometry)
PlaneBufferGeometry = _ctor(api.PlaneBufferGeometry)
LatheGeometry = _ctor(api.LatheGeometry)
LatheBufferGeometry = _ctor(api.LatheBufferGeometry)
ShapeGeometry = _ctor(api.ShapeGeometry)
ShapeBufferGeometry = _ctor(api.ShapeBufferGeometry)
ExtrudeGeometry = _ctor(api.ExtrudeGeometry)
ExtrudeBufferGeometry = _ctor(api.ExtrudeBufferGeometry)
EdgesGeometry = _ctor(api.EdgesGeometry)
ConeGeometry = _ctor(api.ConeGeometry)
ConeBufferGeometry = _ctor(api.ConeBufferGeometry)
CylinderGeometry = _ctor(api.CylinderGeometry)
CylinderBufferGeometry = _ctor(api.CylinderBufferGeometry)
CircleGeometry = _ctor(api.CircleGeometry)
CircleBufferGeometry = _ctor(api.CircleBufferGeometry)
BoxGeometry = _ctor(api.BoxGeometry)
BoxBufferGeometry = _ctor(api.BoxBufferGeometry)
ShadowMaterial = _ctor(api.ShadowMaterial)
SpriteMaterial = _ctor(api.SpriteMaterial)
RawShaderMaterial = _ctor(api.RawShaderMaterial)
ShaderMaterial = _ctor(api.ShaderMaterial)
PointsMaterial = _ctor(api.PointsMaterial)
MeshPhysicalMaterial = _ctor(api.MeshPhysicalMaterial)
MeshStandardMaterial = _ctor(api.MeshStandardMaterial)
MeshPhongMaterial = _ctor(api.MeshPhongMaterial)
MeshToonMaterial = _ctor(api.MeshToonMaterial)
MeshNormalMaterial = _ctor(api.MeshNormalMaterial)
MeshLambertMaterial = _ctor(api.MeshLambertMaterial)
MeshDepthMaterial = _ctor(api.MeshDepthMaterial)
MeshBasicMaterial = _ctor(api.MeshBasicMaterial)
LineDashedMaterial = _ctor(api.LineDashedMaterial)
LineBasicMaterial = _ctor(api.LineBasicMaterial)
Material = _ctor(api.Material)
Float64BufferAttribute = _ctor(api.Float64BufferAttribute)
Float32BufferAttribute = _ctor(api.Float32BufferAttribute)
Uint32BufferAttribute = _ctor(api.Uint32BufferAttribute)
Int32BufferAttribute = _ctor(api.Int32BufferAttribute)
Uint16BufferAttribute = _ctor(api.Uint16BufferAttribute)
Int16BufferAttribute = _ctor(api.Int16BufferAttribute)
Uint8ClampedBufferAttribute = _ctor(api.Uint8ClampedBufferAttribute)
Uint8BufferAttribute = _ctor(api.Uint8BufferAttribute)
Int8BufferAttribute = _ctor(api.Int8BufferAttribute)
BufferAttribute = _ctor(api.BufferAttribute)
REVISION = _ctor(api.REVISION)
MOUSE = _ctor(api.MOUSE)
CullFaceNone = _ctor(api.CullFaceNone)
CullFaceBack = _ctor(api.CullFaceBack)
CullFaceFront = _ctor(api.CullFaceFront)
CullFaceFrontBack = _ctor(api.CullFaceFrontBack)
FrontFaceDirectionCW = _ctor(api.FrontFaceDirectionCW)
FrontFaceDirectionCCW = _ctor(api.FrontFaceDirectionCCW)
BasicShadowMap = _ctor(api.BasicShadowMap)
PCFShadowMap = _ctor(api.PCFShadowMap)
PCFSoftShadowMap = _ctor(api.PCFSoftShadowMap)
FrontSide = _ctor(api.FrontSide)
BackSide = _ctor(api.BackSide)
DoubleSide = _ctor(api.DoubleSide)
FlatShading = _ctor(api.FlatShading)
SmoothShading = _ctor(api.SmoothShading)
NoColors = _ctor(api.NoColors)
FaceColors = _ctor(api.FaceColors)
VertexColors = _ctor(api.VertexColors)
NoBlending = _ctor(api.NoBlending)
NormalBlending = _ctor(api.NormalBlending)
AdditiveBlending = _ctor(api.AdditiveBlending)
SubtractiveBlending = _ctor(api.SubtractiveBlending)
MultiplyBlending = _ctor(api.MultiplyBlending)
CustomBlending = _ctor(api.CustomBlending)
AddEquation = _ctor(api.AddEquation)
SubtractEquation = _ctor(api.SubtractEquation)
ReverseSubtractEquation = _ctor(api.ReverseSubtractEquation)
MinEquation = _ctor(api.MinEquation)
MaxEquation = _ctor(api.MaxEquation)
ZeroFactor = _ctor(api.ZeroFactor)
OneFactor = _ctor(api.OneFactor)
SrcColorFactor = _ctor(api.SrcColorFactor)
OneMinusSrcColorFactor = _ctor(api.OneMinusSrcColorFactor)
SrcAlphaFactor = _ctor(api.SrcAlphaFactor)
OneMinusSrcAlphaFactor = _ctor(api.OneMinusSrcAlphaFactor)
DstAlphaFactor = _ctor(api.DstAlphaFactor)
OneMinusDstAlphaFactor = _ctor(api.OneMinusDstAlphaFactor)
DstColorFactor = _ctor(api.DstColorFactor)
OneMinusDstColorFactor = _ctor(api.OneMinusDstColorFactor)
SrcAlphaSaturateFactor = _ctor(api.SrcAlphaSaturateFactor)
NeverDepth = _ctor(api.NeverDepth)
AlwaysDepth = _ctor(api.AlwaysDepth)
LessDepth = _ctor(api.LessDepth)
LessEqualDepth = _ctor(api.LessEqualDepth)
EqualDepth = _ctor(api.EqualDepth)
GreaterEqualDepth = _ctor(api.GreaterEqualDepth)
GreaterDepth = _ctor(api.GreaterDepth)
NotEqualDepth = _ctor(api.NotEqualDepth)
MultiplyOperation = _ctor(api.MultiplyOperation)
MixOperation = _ctor(api.MixOperation)
AddOperation = _ctor(api.AddOperation)
NoToneMapping = _ctor(api.NoToneMapping)
LinearToneMapping = _ctor(api.LinearToneMapping)
ReinhardToneMapping = _ctor(api.ReinhardToneMapping)
Uncharted2ToneMapping = _ctor(api.Uncharted2ToneMapping)
CineonToneMapping = _ctor(api.CineonToneMapping)
UVMapping = _ctor(api.UVMapping)
CubeReflectionMapping = _ctor(api.CubeReflectionMapping)
CubeRefractionMapping = _ctor(api.CubeRefractionMapping)
EquirectangularReflectionMapping = _ctor(api.EquirectangularReflectionMapping)
EquirectangularRefractionMapping = _ctor(api.EquirectangularRefractionMapping)
SphericalReflectionMapping = _ctor(api.SphericalReflectionMapping)
CubeUVReflectionMapping = _ctor(api.CubeUVReflectionMapping)
CubeUVRefractionMapping = _ctor(api.CubeUVRefractionMapping)
RepeatWrapping = _ctor(api.RepeatWrapping)
ClampToEdgeWrapping = _ctor(api.ClampToEdgeWrapping)
MirroredRepeatWrapping = _ctor(api.MirroredRepeatWrapping)
NearestFilter = _ctor(api.NearestFilter)
NearestMipMapNearestFilter = _ctor(api.NearestMipMapNearestFilter)
NearestMipMapLinearFilter = _ctor(api.NearestMipMapLinearFilter)
LinearFilter = _ctor(api.LinearFilter)
LinearMipMapNearestFilter = _ctor(api.LinearMipMapNearestFilter)
LinearMipMapLinearFilter = _ctor(api.LinearMipMapLinearFilter)
UnsignedByteType = _ctor(api.UnsignedByteType)
ByteType = _ctor(api.ByteType)
ShortType = _ctor(api.ShortType)
UnsignedShortType = _ctor(api.UnsignedShortType)
IntType = _ctor(api.IntType)
UnsignedIntType = _ctor(api.UnsignedIntType)
FloatType = _ctor(api.FloatType)
HalfFloatType = _ctor(api.HalfFloatType)
UnsignedShort4444Type = _ctor(api.UnsignedShort4444Type)
UnsignedShort5551Type = _ctor(api.UnsignedShort5551Type)
UnsignedShort565Type = _ctor(api.UnsignedShort565Type)
UnsignedInt248Type = _ctor(api.UnsignedInt248Type)
AlphaFormat = _ctor(api.AlphaFormat)
RGBFormat = _ctor(api.RGBFormat)
RGBAFormat = _ctor(api.RGBAFormat)
LuminanceFormat = _ctor(api.LuminanceFormat)
LuminanceAlphaFormat = _ctor(api.LuminanceAlphaFormat)
RGBEFormat = _ctor(api.RGBEFormat)
DepthFormat = _ctor(api.DepthFormat)
DepthStencilFormat = _ctor(api.DepthStencilFormat)
RGB_S3TC_DXT1_Format = _ctor(api.RGB_S3TC_DXT1_Format)
RGBA_S3TC_DXT1_Format = _ctor(api.RGBA_S3TC_DXT1_Format)
RGBA_S3TC_DXT3_Format = _ctor(api.RGBA_S3TC_DXT3_Format)
RGBA_S3TC_DXT5_Format = _ctor(api.RGBA_S3TC_DXT5_Format)
RGB_PVRTC_4BPPV1_Format = _ctor(api.RGB_PVRTC_4BPPV1_Format)
RGB_PVRTC_2BPPV1_Format = _ctor(api.RGB_PVRTC_2BPPV1_Format)
RGBA_PVRTC_4BPPV1_Format = _ctor(api.RGBA_PVRTC_4BPPV1_Format)
RGBA_PVRTC_2BPPV1_Format = _ctor(api.RGBA_PVRTC_2BPPV1_Format)
RGB_ETC1_Format = _ctor(api.RGB_ETC1_Format)
LoopOnce = _ctor(api.LoopOnce)
LoopRepeat = _ctor(api.LoopRepeat)
LoopPingPong = _ctor(api.LoopPingPong)
InterpolateDiscrete = _ctor(api.InterpolateDiscrete)
InterpolateLinear = _ctor(api.InterpolateLinear)
InterpolateSmooth = _ctor(api.InterpolateSmooth)
ZeroCurvatureEnding = _ctor(api.ZeroCurvatureEnding)
ZeroSlopeEnding = _ctor(api.ZeroSlopeEnding)
WrapAroundEnding = _ctor(api.WrapAroundEnding)
TrianglesDrawMode = _ctor(api.TrianglesDrawMode)
TriangleStripDrawMode = _ctor(api.TriangleStripDrawMode)
TriangleFanDrawMode = _ctor(api.TriangleFanDrawMode)
LinearEncoding = _ctor(api.LinearEncoding)
sRGBEncoding = _ctor(api.sRGBEncoding)
GammaEncoding = _ctor(api.GammaEncoding)
RGBEEncoding = _ctor(api.RGBEEncoding)
LogLuvEncoding = _ctor(api.LogLuvEncoding)
RGBM7Encoding = _ctor(api.RGBM7Encoding)
RGBM16Encoding = _ctor(api.RGBM16Encoding)
RGBDEncoding = _ctor(api.RGBDEncoding)
BasicDepthPacking = _ctor(api.BasicDepthPacking)
RGBADepthPacking = _ctor(api.RGBADepthPacking)
CubeGeometry = _ctor(api.CubeGeometry)
Face4 = _ctor(api.Face4)
LineStrip = _ctor(api.LineStrip)
LinePieces = _ctor(api.LinePieces)
MeshFaceMaterial = _ctor(api.MeshFaceMaterial)
MultiMaterial = _ctor(api.MultiMaterial)
PointCloud = _ctor(api.PointCloud)
Particle = _ctor(api.Particle)
ParticleSystem = _ctor(api.ParticleSystem)
PointCloudMaterial = _ctor(api.PointCloudMaterial)
ParticleBasicMaterial = _ctor(api.ParticleBasicMaterial)
ParticleSystemMaterial = _ctor(api.ParticleSystemMaterial)
Vertex = _ctor(api.Vertex)
DynamicBufferAttribute = _ctor(api.DynamicBufferAttribute)
Int8Attribute = _ctor(api.Int8Attribute)
Uint8Attribute = _ctor(api.Uint8Attribute)
Uint8ClampedAttribute = _ctor(api.Uint8ClampedAttribute)
Int16Attribute = _ctor(api.Int16Attribute)
Uint16Attribute = _ctor(api.Uint16Attribute)
Int32Attribute = _ctor(api.Int32Attribute)
Uint32Attribute = _ctor(api.Uint32Attribute)
Float32Attribute = _ctor(api.Float32Attribute)
Float64Attribute = _ctor(api.Float64Attribute)
ClosedSplineCurve3 = _ctor(api.ClosedSplineCurve3)
SplineCurve3 = _ctor(api.SplineCurve3)
Spline = _ctor(api.Spline)
BoundingBoxHelper = _ctor(api.BoundingBoxHelper)
EdgesHelper = _ctor(api.EdgesHelper)
WireframeHelper = _ctor(api.WireframeHelper)
XHRLoader = _ctor(api.XHRLoader)
BinaryTextureLoader = _ctor(api.BinaryTextureLoader)
GeometryUtils = _ctor(api.GeometryUtils)
ImageUtils = _ctor(api.ImageUtils)
Projector = _ctor(api.Projector)
CanvasRenderer = _ctor(api.CanvasRenderer)

