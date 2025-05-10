# Generated EnumItem classes

from pycatia.enumeration import EnumItem


class AbqConcForceLoadType(EnumItem):
    POINTLOAD = 0
    DISTRIBUTEDLOAD = 1
    LOADDENSITY = 2


class AbqDatOutputVarType(EnumItem):
    ABQDATOUTPUTTYPE_NODE = 0
    ABQDATOUTPUTTYPE_ELEMENT = 1
    ABQDATOUTPUTTYPE_CONTACT = 2
    ABQDATOUTPUTTYPE_ENERGY = 3


class AbqEntityType(EnumItem):
    ABQ_NONE = 0
    ABQ_NODE = 1
    ABQ_ELEMENT = 2


class AbqLocalCsysType(EnumItem):
    ABQ_CARTESIAN = 0
    ABQ_CYLINDRICAL = 1
    ABQ_SPHERICAL = 2
    ABQ_DEFAULTAXIS = 3


class AbqMsFrequencyType(EnumItem):
    ABQ_INTERVAL = 0
    ABQ_INCREMENT = 1


class AbqMsTargetMethod(EnumItem):
    ABQ_BELOW_MIN = 0
    ABQ_UNIFORM = 1
    ABQ_SET_EQUAL = 2


class AbqOutputAtSecPts(EnumItem):
    ABQDEFAULTSECPTS = 0
    ABQALLSECPTS = 1


class AbqOutputRequestType(EnumItem):
    ABQFIELD = 0
    ABQHISTORY = 1
    ABQDATA = 2


class AbqOutputVariableType(EnumItem):
    ABQPRESELECTEDEFVAR = 0
    ABQALLVAR = 1


class AbqRequestedModesOption(EnumItem):
    ABQ_ALL = 0
    ABQ_VALUE = 1


class AbqRestartOption(EnumItem):
    ABQ_RESTART_NONE = 0
    ABQ_RESTART_EVERYINC = 1
    ABQ_RESTART_SPECINC = 2
    ABQ_RESTART_NUMINT = 3
    ABQ_RESTART_LASTINC = 4


class AbqRestartReadOption(EnumItem):
    ABQ_RESTART_END_OF_STEP = 0
    ABQ_RESTART_INTERVAL = 1


class AbqRestartReadStepSelOption(EnumItem):
    ABQ_STEP_OBJECT = 0
    ABQ_STEP_NUMBER = 1


class AccuracyType(EnumItem):
    ACCURACY_TYPE_DISTANCE = 0
    ACCURACY_TYPE_SPEED = 1


class AdjustMethodType(EnumItem):
    NOADJUST = 0
    OVERCLOSED = 1
    TOLERANCE = 2


class AutoTimeIncrementMethod(EnumItem):
    ABQ_ATI_GLOBAL = 0
    ABQ_ATI_ELEMENT_BY_ELEMENT = 1


class Cat3DColorInheritanceMode(EnumItem):
    cat3DColorInheritanceModeOff = 0
    cat3DColorInheritanceModeOn = 1


class Cat3DXmlGeomRepresentationType(EnumItem):
    cat3DXmlExact = 0
    cat3DXmlTessellation = 1
    cat3DXmlCompressedTessellation = 2
    cat3DXmlDynamicTessellation = 3
    cat3DXmlStaticTessellation = 4
    cat3DXmlXmlTessellation = 5


class Cat3DXmlPprSaveConfig(EnumItem):
    cat3DXmlProductAndResourceList = 0
    cat3DXmlProductList = 1
    cat3DXmlResourceList = 2


class CatAlgorithmType(EnumItem):
    catSimulatedAnnealing = 0
    catGradient = 1
    catCAAalgorithm = 2
    catLocalForConstraints = 3


class CatAnalysisSetSearchType(EnumItem):
    catAnalysisSetSearchIn = 0
    catAnalysisSetSearchOut = 1
    catAnalysisSetSearchNeutral = 2
    catAnalysisSetSearchAll = 3


class CatAnalysisSetType(EnumItem):
    catAnalysisSetIn = 0
    catAnalysisSetOut = 1
    catAnalysisSetNeutral = 2


class CatAnnotatedViewBehavior(EnumItem):
    CatAnnotatedViewBehaviorLink = 0
    CatAnnotatedViewBehaviorUnlink = 1


class CatAnnotationSetType(EnumItem):
    catAnnotationSetStandard = 0
    catAnnotationSetLight = 1
    catAnnotationSetResult = 2


class CatArrangeStyle(EnumItem):
    catArrangeCascade = 0
    catArrangeTiledHorizontal = 1
    catArrangeTiledVertical = 2


class CatArrangementAreaVisuMode(EnumItem):
    CatArrangementAreaVisuModeFlat = 0
    CatArrangementAreaVisuModeSolid = 1


class CatArrangementItemResVisuMode(EnumItem):
    CatArrangementItemReservationVisuModeAxis = 0
    CatArrangementItemReservationVisuModeFlat = 1
    CatArrangementItemReservationVisuModeSolid = 2


class CatArrangementRouteSection(EnumItem):
    CatArrangementRouteSectionNone = 0
    CatArrangementRouteSectionRectangular = 1
    CatArrangementRouteSectionRound = 2
    CatArrangementRouteSectionFlatOval = 3
    CatArrangementRouteSectionRadiusCorner = 4
    CatArrangementRouteSectionDoubleRidge = 5


class CatArrangementRouteVisuMode(EnumItem):
    CatArrangementRouteVisuModeCurve = 0
    CatArrangementRouteVisuModeFlat = 1
    CatArrangementRouteVisuModeSolid = 2


class CatAsmAutoSwitchToDesignMode(EnumItem):
    catAutoSwitchAvailable = 0
    catAutoSwitchUnavailable = 1


class CatAsmConstraintCreationMode(EnumItem):
    catUseAnyGeometry = 0
    catUsePublishedGeometryChildLevel = 1
    catUsePublishedGeometryAnyLevel = 2


class CatAsmExtendMoveToFixT(EnumItem):
    catNeverExtendMoveToFixT = 0
    catAskIfExtendMoveToFixT = 1
    catAlwaysExtendMoveToFixT = 2


class CatAsmPasteComponentMode(EnumItem):
    catPasteWithoutCsts = 0
    catPasteWithCstOnCopy = 1
    catPasteWithCstOnCut = 2
    catPasteWithCstOnCopyAndCut = 3


class CatAsmQuickConstraintMode(EnumItem):
    catSpecifiedOrder = 0
    catVerifiedConstraintFirst = 1


class CatAsmRedundancyMode(EnumItem):
    catUnChecked = 0
    catChecked = 1


class CatAsmUpdateMode(EnumItem):
    catManualUpdate = 0
    catAutomaticUpdate = 1


class CatAsmUpdateStatusComputeMode(EnumItem):
    catManualCompute = 0
    catAutomaticCompute = 1


class CatAxisOrientationType(EnumItem):
    catSamCoordinateSystem_Cartesian = 0
    catSamCoordinateSystem_Cylindrical = 1
    catSamCoordinateSystem_Spherical = 2
    catSamCoordinateSystem_Undefined = 3


class CatAxisSystemAxisType(EnumItem):
    catAxisSystemAxisSameDirection = 0
    catAxisSystemAxisByCoordinates = 1
    catAxisSystemAxisOppositeDirection = 2


class CatAxisSystemMainType(EnumItem):
    catAxisSystemStandard = 0
    catAxisSystemAxisRotation = 1
    catAxisSystemEulerAngles = 2
    catAxisSystemExplicit = 3


class CatAxisSystemOriginType(EnumItem):
    catAxisSystemOriginByPoint = 0
    catAxisSystemOriginByCoordinates = 1


class CatBackFaceCullingMode(EnumItem):
    CATBackFaceCullingOnSolidFaces = 0
    CATBackFaceCullingOnAllFaces = 1
    CATBackFaceCullingOnStandAloneFaces = 2
    CATBackFaceCullingOnNoFaces = 3


class CatBannerPosition(EnumItem):
    catBannerPositionNone = 0
    catBannerPositionBottom = 1
    catBannerPositionTop = 2
    catBannerPositionLeft = 3
    catBannerPositionRight = 4


class CatBlankingMode(EnumItem):
    catBlankingInactive = 0
    catBlankingActive = 1
    catBlankingOnGeom = 2


class CatCameraType(EnumItem):
    catCamera2D = 0
    catCamera3D = 1


class CatCaptureFormat(EnumItem):
    catCaptureFormatCGM = 0
    catCaptureFormatEMF = 1
    catCaptureFormatTIFF = 2
    catCaptureFormatTIFFGreyScale = 3
    catCaptureFormatBMP = 4
    catCaptureFormatJPEG = 5


class CatChamferMode(EnumItem):
    catTwoLengthChamfer = 0
    catLengthAngleChamfer = 1


class CatChamferOrientation(EnumItem):
    catNoReverseChamfer = 0
    catReverseChamfer = 1


class CatChamferPropagation(EnumItem):
    catTangencyChamfer = 0
    catMinimalChamfer = 1


class CatCircularPatternParameters(EnumItem):
    catInstancesandAngularSpacing = 0
    catCompleteCrown = 1
    catUnequalAngularSpacing = 2


class CatClashComputationType(EnumItem):
    catClashComputationTypeBetweenAll = 0
    catClashComputationTypeInsideOne = 1
    catClashComputationTypeAgainstAll = 2
    catClashComputationTypeBetweenTwo = 3


class CatClashExportType(EnumItem):
    CatClashExportTypeXMLResultOnly = 0


class CatClashImportType(EnumItem):
    CatClashImportTypeClashOnly = 0
    CatClashImportTypeStructureAndClash = 1


class CatClashInterferenceType(EnumItem):
    catClashInterferenceTypeContact = 0
    catClashInterferenceTypeClearance = 1
    catClashInterferenceAuthorizedPenetration = 2
    catClashInterferenceCaseRule = 3


class CatClippingFrameReframeOnMode(EnumItem):
    catOnViewContent = 0
    catOnViewBackground = 1


class CatClippingMode(EnumItem):
    catClippingModeClear = 0
    catClippingModeNear = 1
    catClippingModeFar = 2
    catClippingModeNearAndFar = 3


class CatCompositesType(EnumItem):
    Unknown = 0
    Stacking = 1
    PlyGroup = 2
    Sequence = 3
    CutPieceGroup = 4
    Ply = 5
    Core = 6
    CutPiece = 7


class CatConflictComparison(EnumItem):
    catConflictComparisonNew = 0
    catConflictComparisonOld = 1
    catConflictComparisonNo = 2


class CatConflictStatus(EnumItem):
    catConflictStatusNotInspected = 0
    catConflictStatusRelevant = 1
    catConflictStatusIrrelevant = 2
    catConflictStatusSolved = 3


class CatConflictType(EnumItem):
    catConflictTypeClash = 0
    catConflictTypeContact = 1
    catConflictTypeClearance = 2


class CatConstraintAngleSector(EnumItem):
    catCstAngleSector0 = 0
    catCstAngleSector1 = 1
    catCstAngleSector2 = 2
    catCstAngleSector3 = 3


class CatConstraintDistConfig(EnumItem):
    catCstDCUnspec = 0
    catCstDCParallel = 1
    catCstDCParallelSameOrient = 2
    catCstDCParallelOppOrient = 3


class CatConstraintDistDirection(EnumItem):
    catCstDistDirectionNone = 0
    catCstDistDirection1 = 1
    catCstDistDirection2 = 2
    catCstDistDirection3 = 3


class CatConstraintMode(EnumItem):
    catCstModeDrivingDimension = 0
    catCstModeDrivenDimension = 1


class CatConstraintOrientation(EnumItem):
    catCstOrientSame = 0
    catCstOrientOpposite = 1
    catCstOrientUndefined = 2


class CatConstraintRefAxis(EnumItem):
    catCstRefAxisX = 0
    catCstRefAxisY = 1
    catCstRefAxisZ = 2


class CatConstraintRefType(EnumItem):
    catCstRefTypeRelative = 0
    catCstRefTypeFixInSpace = 1


class CatConstraintSide(EnumItem):
    catCstSidePositive = 0
    catCstSideNegative = 1
    catCstSideSameAsValue = 2
    catCstSideOppositeToValue = 3
    catCstSideUndefined = 4


class CatConstraintStatus(EnumItem):
    catCstStatusOK = 0
    catCstStatusKOStronglyNotSatisfied = 1
    catCstStatusKOWrongOrientOrSide = 2
    catCstStatusKOWrongValue = 3
    catCstStatusKOWrongGeomEltType = 4
    catCstStatusKOBroken = 5


class CatConstraintType(EnumItem):
    catCstTypeReference = 0
    catCstTypeDistance = 1
    catCstTypeOn = 2
    catCstTypeConcentricity = 3
    catCstTypeTangency = 4
    catCstTypeLength = 5
    catCstTypeAngle = 6
    catCstTypePlanarAngle = 7
    catCstTypeParallelism = 8
    catCstTypeAxisParallelism = 9
    catCstTypeHorizontality = 10
    catCstTypePerpendicularity = 11
    catCstTypeAxisPerpendicularity = 12
    catCstTypeVerticality = 13
    catCstTypeRadius = 14
    catCstTypeSymmetry = 15
    catCstTypeMidPoint = 16
    catCstTypeEquidistance = 17
    catCstTypeMajorRadius = 18
    catCstTypeMinorRadius = 19
    catCstTypeSurfContact = 20
    catCstTypeLinContact = 21
    catCstTypePoncContact = 22
    catCstTypeChamfer = 23
    catCstTypeChamferPerpend = 24
    catCstTypeAnnulContact = 25
    catCstTypeCylinderRadius = 26
    catCstTypeStContinuity = 27
    catCstTypeStDistance = 28
    catCstTypeSdContinuity = 29
    catCstTypeSdShape = 30


class CatCsHoleMode(EnumItem):
    catCSModeDepthAngle = 0
    catCSModeDepthDiameter = 1
    catCSModeAngleDiameter = 2


class CatCdHoleMode(EnumItem):
    catCDModeNoCountersunkDiameter = 0
    catCDModeCountersunkDiameter = 1


class CatDedicatedFilterType(EnumItem):
    catDisplayInBackground = 0
    catMaskInBackground = 1


class CatDescriptionLengthType(EnumItem):
    ShortText = 0
    LongText = 1


class CatDftWeldFinishSymbol(EnumItem):
    catFinishWeldingNone = 0
    catDftLetterCWelding = 1
    catDftLetterFWelding = 2
    catDftLetterGWelding = 3
    catDftLetterHWelding = 4
    catDftLetterMWelding = 5
    catDftLetterRWelding = 6
    catDftLetterUWelding = 7


class CatDftWeldingTail(EnumItem):
    catDftWeldingTailNO = 0
    catDftWeldingTailYES = 1


class CatDimAnalyse(EnumItem):
    catDimOnGenItems = 0
    catUnUpdatableDim = 1
    catFakeDim = 2
    catDrivingDim = 3
    catBrokenDim = 4
    catTrueDim = 5
    catBasic = 6
    cat3DDrivableDim = 7
    cat3DDrivedDim = 8
    catIsolatedDim = 9
    catDimOnHideGeom = 10
    cat3DFeatureDim = 11


class CatDimDualDisplay(EnumItem):
    catDualNone = 0
    catDualBellow = 1
    catDualFractional = 2
    catDualSideBySide = 3


class CatDimFake(EnumItem):
    catDimFakeNone = 0
    catDimFakeNumValue = 1
    catDimFakeText = 2


class CatDimFrame(EnumItem):
    catFraNone = 0
    catFraCircle = 1
    catFraScoredCircle = 2
    catFraDiamondShaped = 3
    catFraSquare = 4
    catFraRectangle = 5
    catFraOblong = 6
    catFraRightFlag = 7
    catFraRightTriangle = 8


class CatDimFramedElement(EnumItem):
    catFraValue = 0
    catFraValueTol = 1
    catFraValueTolText = 2


class CatDimFramedGroup(EnumItem):
    catFraMain = 0
    catFraDual = 1
    catFraMainAndDual = 2
    catFraBoth = 3


class CatDimLineGraphRep(EnumItem):
    catDimLine1Part = 0
    catDimLine2Parts = 1
    catDimLineLeader1Part = 2
    catDimLineLeader2Part = 3


class CatDimLineRep(EnumItem):
    catDimUndef = 0
    catDimHoriz = 1
    catDimVert = 2
    catDimAuto = 3
    catDimUserDefined = 4
    catDimTrueDim = 5
    catDimParallel = 6
    catDimOffset = 7


class CatDimMode(EnumItem):
    catDimClassical = 0
    catDimCumulate = 1
    catDimHalfDim = 2
    catDimChained = 3
    catDimStacked = 4
    catDimCumulatesystem = 5
    catDimHalfDimSystem = 6


class CatDimOrientation(EnumItem):
    catHorizontal = 0
    catVertical = 1
    catParallel = 2
    catPerpandicular = 3
    catAngle = 4


class CatDimReference(EnumItem):
    catScreen = 0
    catView = 1
    catDimLine = 2


class CatDimScore(EnumItem):
    catDimScoreNone = 0
    catDimUnderScored = 1
    catDimScored = 2
    catCATDrwDimOverScored = 3


class CatDimSymbols(EnumItem):
    catDimSymbNone = 0
    catDimSymbOpenArrow = 1
    catDimSymbClosedArrow = 2
    catDimSymbFilledArrow = 3
    catDimSymbSymArrow = 4
    catDimSymbSlash = 5
    catDimSymbCircle = 6
    catDimSymbFilledCircle = 7
    catDimSymbScoredCircle = 8
    catDimSymbCircledCross = 9
    catDimSymbTriangle = 10
    catDimSymbFilledTriangle = 11
    catDimSymbCross = 12
    catDimSymbXCross = 13


class CatDimType(EnumItem):
    catDimDistance = 0
    catDimDistanceOffset = 1
    catDimLength = 2
    catDimLengthCurvilinear = 3
    catDimAngle = 4
    catDimRadius = 5
    catDimRadiusTangent = 6
    catDimRadiusCylinder = 7
    catDimRadiusEdge = 8
    catDimDiameter = 9
    catDimDiameterTangent = 10
    catDimDiameterCylinder = 11
    catDimDiameterEdge = 12
    catDimDiameterCone = 13
    catDimChamfer = 14
    catDimSlope = 15
    catDimLengthCircular = 16
    catDimRadiusFillet = 17
    catDimDiameterTorus = 18
    catDimRadiusTorus = 19
    catDimDistanceMin = 20


class CatDistanceComputationType(EnumItem):
    catDistanceComputationTypeInsideOne = 0
    catDistanceComputationTypeAgainstAll = 1
    catDistanceComputationTypeBetweenTwo = 2


class CatDistanceMeasureType(EnumItem):
    catDistanceMeasureTypeMinimum = 0
    catDistanceMeasureTypeAlongX = 1
    catDistanceMeasureTypeAlongY = 2
    catDistanceMeasureTypeAlongZ = 3
    catDistanceMeasureTypeBand = 4


class CatDmuGroupPreviewHiddenObjectsDisplayMode(EnumItem):
    CatDMUGroupPreviewShowHidden = 0
    CatDMUGroupPreviewShowHiddenCustom = 1


class CatDocContextualPriority(EnumItem):
    CATDocContextualTechDoc = 0
    CATDocContextualUserComp = 1


class CatDraftMode(EnumItem):
    catStandardDraftMode = 0
    catReflectKeepFaceDraftMode = 1
    catReflectKeepEdgeDraftMode = 2


class CatDraftMultiselectionMode(EnumItem):
    catNoneDraftMultiselectionMode = 0
    catDraftMultiselectionByNeutralMode = 1


class CatDraftNeutralPropagationMode(EnumItem):
    catNoneDraftNeutralPropagationMode = 0
    catSmoothDraftNeutralPropagationMode = 1


class CatDrawingStandard(EnumItem):
    catANSI = 0
    catISO = 1
    catJIS = 2


class CatDrawingViewType(EnumItem):
    catViewBackground = 0
    catViewFront = 1
    catViewLeft = 2
    catViewRight = 3
    catViewTop = 4
    catViewBottom = 5
    catViewRear = 6
    catViewAuxiliary = 7
    catViewIsom = 8
    catViewSection = 9
    catViewSectionCut = 10
    catViewDetail = 11
    catViewUntyped = 12
    catViewMain = 13
    catViewPure_Sketch = 14
    catViewUnfolded = 15


class CatDrwNewSheetFrom(EnumItem):
    catDrwFirstSheet = 0
    catDrwStyle = 1


class CatDxfExportBlocksEnum(EnumItem):
    catDxfExportBlocksEnumNone = 0
    catDxfExportBlocksEnum1Level = 1
    catDxfExportBlocksEnumFull = 2


class CatDxfExportModeEnum(EnumItem):
    catDxfExportModeEnumSemantic = 0
    catDxfExportModeEnumGraphic = 1


class CatDxfExportSheetsEnum(EnumItem):
    catDxfExportSheetsEnumAll = 0
    catDxfExportSheetsEnumOnlyCurrent = 1


class CatDxfExportVersionEnum(EnumItem):
    catDxfExportVersionEnumR12 = 0
    catDxfExportVersionEnumR13 = 1
    catDxfExportVersionEnumR14 = 2
    catDxfExportVersionEnum2000 = 3
    catDxfExportVersionEnum2004 = 4
    catDxfExportVersionEnum2007 = 5


class CatDxfImportCreateEndPointsEnum(EnumItem):
    catDxfImportCreateEndPointsEnumNever = 0
    catDxfImportCreateEndPointsEnumFewEntities = 1
    catDxfImportCreateEndPointsEnumAlways = 2


class CatDxfImportDimensionsEnum(EnumItem):
    catDxfImportDimensionsEnumDimensions = 0
    catDxfImportDimensionsEnumDetails = 1
    catDxfImportDimensionsEnumGeometry = 2


class CatDxfImportUnitEnum(EnumItem):
    catDxfImportUnitEnumMillimeter = 0
    catDxfImportUnitEnumCentimeter = 1
    catDxfImportUnitEnumMeter = 2
    catDxfImportUnitEnumInch = 3
    catDxfImportUnitEnumFoot = 4
    catDxfImportUnitEnumScaleFactor = 5
    catDxfImportUnitEnumAutomatic = 6


class CatElectronicType(EnumItem):
    BOARD = 0
    PANEL = 1
    COMPONENT = 2
    AREA = 3
    PCBHOLE = 4
    PCBPATTERN = 5
    NOPCBBEHAVIOUR = 6


class CatFileSelectionMode(EnumItem):
    CatFileSelectionModeOpen = 0
    CatFileSelectionModeSave = 1


class CatFileType(EnumItem):
    catFileTypeText = 0
    catFileTypeMotif = 1
    catFileTypeHTML = 2


class CatFilletBitangencyType(EnumItem):
    catSphereBitangencyType = 0
    catCircleBitangencyType = 1


class CatFilletBoundaryRelimitation(EnumItem):
    catAutomaticFilletBoundaryRelimitation = 0
    catUVFilletBoundaryRelimitation = 1
    catConnectFilletBoundaryRelimitation = 2
    catMinimumFilletBoundaryRelimitation = 3
    catMaximumFilletBoundaryRelimitation = 4


class CatFilletEdgePropagation(EnumItem):
    catMinimalFilletEdgePropagation = 0
    catTangencyFilletEdgePropagation = 1


class CatFilletRepresentation(EnumItem):
    catFilletRepNone = 0
    catFilletRepBoundary = 1
    catFilletRepSymbolic = 2
    catFilletRepOriginalEdge = 3
    catFilletRepProjectedOriginalEdge = 4


class CatFilletTrimSupport(EnumItem):
    catTrimFilletSupport = 0
    catNoTrimFilletSupport = 1


class CatFilletVariation(EnumItem):
    catLinearFilletVariation = 0
    catCubicFilletVariation = 1


class CatFittingShuttleVector(EnumItem):
    CATFittingShuttleVectorX = 0
    CATFittingShuttleVectorY = 1
    CATFittingShuttleVectorZ = 2


class CatFullSceneAntiAliasingMode(EnumItem):
    CATFSAAMode_Deactivated = 0
    CATFSAAMode_2xSuperSampling = 1
    CATFSAAMode_4xSuperSampling = 2
    CATFSAAMode_8xSuperSampling = 3
    CATFSAAMode_16xSuperSampling = 4


class CatFunctOrientationDirection(EnumItem):
    CATFunctNotOriented = 0
    CATFunctOrientedUnidirectional = 1
    CATFunctOrientedBidirectional = 2


class CatGenConferencing(EnumItem):
    NetMeeting = 0
    Backbone = 1


class CatGenDataSave(EnumItem):
    NoAutoBackup = 0
    AutoBackupEvery = 1
    IncrBackup = 2


class CatGenUiStyle(EnumItem):
    UIStyleP1 = 0
    UIStyleP2 = 1
    UIStyleP3 = 2


class CatGeometricType(EnumItem):
    catGeoTypeUnknown = 0
    catGeoTypeAxis2D = 1
    catGeoTypePoint2D = 2
    catGeoTypeLine2D = 3
    catGeoTypeControlPoint2D = 4
    catGeoTypeCircle2D = 5
    catGeoTypeHyperbola2D = 6
    catGeoTypeParabola2D = 7
    catGeoTypeEllipse2D = 8
    catGeoTypeSpline2D = 9
    catGeoTypePoint = 10
    catGeoTypeLine = 11
    catGeoTypePlane = 12


class CatGridPositionMode(EnumItem):
    catGridPositionMode_Absolute = 0
    catGridPositionMode_Relative = 1


class CatHiddenLineMode(EnumItem):
    catHlrModeOff = 0
    catHlrModeOn = 1


class CatHoleAnchorMode(EnumItem):
    catExtremPointHoleAnchor = 0
    catMiddlePointHoleAnchor = 1


class CatHoleBottomType(EnumItem):
    catFlatHoleBottom = 0
    catVHoleBottom = 1
    catTrimmedHoleBottom = 2


class CatHoleThreadSide(EnumItem):
    catRightThreadSide = 0
    catLeftThreadSide = 1


class CatHoleThreadStandard(EnumItem):
    catHoleMetricThinPitch = 0
    catHoleMetricThickPitch = 1


class CatHoleThreadingMode(EnumItem):
    catThreadedHoleThreading = 0
    catSmoothHoleThreading = 1


class CatHoleType(EnumItem):
    catSimpleHole = 0
    catTaperedHole = 1
    catCounterboredHole = 2
    catCountersunkHole = 3
    catCounterdrilledHole = 4


class CatIg2ExportModeEnum(EnumItem):
    catIg2ExportModeEnumSemantic = 0
    catIg2ExportModeEnumStructured = 1
    catIg2ExportModeEnumGraphic = 2


class CatIg2ExportSheetsEnum(EnumItem):
    catIg2ExportSheetsEnumAll = 0
    catIg2ExportSheetsEnumOnlyCurrent = 1


class CatIg2ImportCreateEndPointsEnum(EnumItem):
    catIg2ImportCreateEndPointsEnumNever = 0
    catIg2ImportCreateEndPointsEnumFewEntities = 1
    catIg2ImportCreateEndPointsEnumAlways = 2


class CatIg2ImportDestinationViewEnum(EnumItem):
    catIg2ImportDestinationViewEnumWorkingViews = 0
    catIg2ImportDestinationViewEnumBackground = 1


class CatIg2ImportDimensionsEnum(EnumItem):
    catIg2ImportDimensionsEnumDimensions = 0
    catIg2ImportDimensionsEnumDetails = 1
    catIg2ImportDimensionsEnumGeometry = 2


class CatIg2ImportUnitEnum(EnumItem):
    catIg2ImportUnitEnumMillimeter = 0
    catIg2ImportUnitEnumCentimeter = 1
    catIg2ImportUnitEnumMeter = 2
    catIg2ImportUnitEnumInch = 3
    catIg2ImportUnitEnumFoot = 4
    catIg2ImportUnitEnumAutomatic = 5


class CatImageRotation(EnumItem):
    catImageNoRotation = 0
    catImageRotation90 = 1
    catImageRotation180 = 2
    catImageRotation270 = 3
    catImageBestRotation = 4


class CatImageViewMode(EnumItem):
    catImageModeOff = 0
    catImageModeHRD = 1


class CatInsureViewNamesUniquenessScope(EnumItem):
    catInSheet = 0
    catInLayout = 1


class CatJustification(EnumItem):
    catLeft = 0
    catCenter = 1
    catRight = 2


class CatLightingMode(EnumItem):
    catInfiniteLightSource = 0
    catNeonLightSource = 1


class CatLimitMode(EnumItem):
    catOffsetLimit = 0
    catUpToNextLimit = 1
    catUpToLastLimit = 2
    catUpToPlaneLimit = 3
    catUpToSurfaceLimit = 4
    catUpThruNextLimit = 5


class CatManipAutoInsertMode(EnumItem):
    CATOnMouseRelease = 0
    CATWhileMouseMoving = 1


class CatManipClashMode(EnumItem):
    CATManipClashModeNo = 0
    CATManipClashModeOn = 1
    CATManipClashModeStop = 2


class CatManufacturingPrecedenceType(EnumItem):
    catPrecedenceTypeJustBefore = 0
    catPrecedenceTypeBefore = 1


class CatMarker2DType(EnumItem):
    catMarker2DTypeLine = 0
    catMarker2DTypeArrow = 1
    catMarker2DTypeRectangle = 2
    catMarker2DTypeCircle = 3
    catMarker2DTypeFreeHand = 4
    catMarker2DTypeText = 5
    catMarker2DTypePicture = 6


class CatMarker3DType(EnumItem):
    catMarker3DTypeText = 0


class CatMarkerTextOrientation(EnumItem):
    CatMarkerTextOrientationRight = 0
    CatMarkerTextOrientationUp = 1
    CatMarkerTextOrientationLeft = 2
    CatMarkerTextOrientationDown = 3


class CatMeasurableName(EnumItem):
    CatMeasurableUnknown = 0
    CatMeasurable = 1
    CatMeasurableVolume = 2
    CatMeasurableSurface = 3
    CatMeasurableCylinder = 4
    CatMeasurableSphere = 5
    CatMeasurableCone = 6
    CatMeasurablePlane = 7
    CatMeasurableCurve = 8
    CatMeasurableCircle = 9
    CatMeasurableLine = 10
    CatMeasurablePoint = 11
    CatMeasurableAxisSystem = 12


class CatMergeMode(EnumItem):
    catMergeOff = 0
    catMergeOn = 1


class CatMultiSelectionMode(EnumItem):
    CATMonoSel = 0
    CATMultiSelTriggWhenSelPerf = 1
    CATMultiSelTriggWhenUserValidatesSelection = 2


class CatNavigationStyle(EnumItem):
    catNavigationExamine = 0
    catNavigationWalk = 1
    catNavigationFly = 2


class CatOptimizationType(EnumItem):
    catMinimum = 0
    catMaximum = 1
    catTargetValue = 2
    catOnlyBoundedVariation = 3
    catNone = 4
    catCstOnly = 5


class CatOutPutFormatType(EnumItem):
    KWEHtml = 0
    KWEText = 1
    KWEPrint = 2
    KWEEmail = 3


class CatPaperOrientation(EnumItem):
    catPaperPortrait = 0
    catPaperLandscape = 1
    catPaperBestFit = 2


class CatPaperSize(EnumItem):
    catPaperLetter = 0
    catPaperLegal = 1
    catPaperA0 = 2
    catPaperA1 = 3
    catPaperA2 = 4
    catPaperA3 = 5
    catPaperA4 = 6
    catPaperA = 7
    catPaperB = 8
    catPaperC = 9
    catPaperD = 10
    catPaperE = 11
    catPaperF = 12
    catPaperUser = 13


class CatPartElementsNamingMode(EnumItem):
    catNoNamingCheck = 0
    catNamingCheckUnderSameNode = 1
    catNamingCheckWithinUIActiveObject = 2


class CatPartSurfaceElementsLocation(EnumItem):
    catPartBodyLocation = 0
    catXGSLocation = 1


class CatPartUpdateMode(EnumItem):
    catManualUpdate = 0
    catAutomaticUpdate = 1


class CatPictureFormat(EnumItem):
    catPictureNONE = 0
    catPicturePNG = 1
    catPictureJPEG = 2
    catPictureCCITTG3 = 3


class CatPointsProjectionMode(EnumItem):
    catPointsProjectionModeOff = 0
    catPointsProjectionModeOn = 1


class CatPrintColor(EnumItem):
    catColorTrueColor = 0
    catColorGreyScale = 1
    catColorMonochrome = 2


class CatPrintLineCap(EnumItem):
    catPrintFlat = 0
    catPrintSquare = 1
    catPrintRound = 2


class CatPrintLineSpecification(EnumItem):
    catPrintAbsolute = 0
    catPrintScaled = 1
    catPrintNoThickness = 2


class CatPrintQuality(EnumItem):
    catPrintQualityDraft = 0
    catPrintQualityLow = 1
    catPrintQualityMedium = 2
    catPrintQualityHigh = 3
    catPrintQualityCustom = 4


class CatPrintRenderingMode(EnumItem):
    catPrintRenderingModeDefault = 0
    catPrintRenderingModeWireframe = 1
    catPrintRenderingModeHiddenLineRemoval = 2
    catPrintRenderingModeShadingWithTriangles = 3
    catPrintRenderingModeDynamicHiddenLineRemoval = 4
    catPrintRenderingModeOnScreen = 5


class CatPrinterDirState(EnumItem):
    CatPrinterDirFree = 0
    CatPrinterDirProtect = 1


class CatPrismExtrusionDirection(EnumItem):
    catNormalToSketchDirection = 0
    catNotNormalToSketchDirection = 1


class CatPrismOrientation(EnumItem):
    catRegularOrientation = 0
    catInverseOrientation = 1


class CatProductSource(EnumItem):
    catProductSourceUnknown = 0
    catProductMade = 1
    catProductBought = 2


class CatProjViewType(EnumItem):
    catRightView = 0
    catLeftView = 1
    catTopView = 2
    catBottomView = 3
    catRearView = 4


class CatProjectionMode(EnumItem):
    catProjectionConic = 0
    catProjectionCylindric = 1
    catProjectionUndefined = 2


class CatPspIdlApplicationId(EnumItem):
    catPspIDLCATPiping = 0
    catPspIDLCATHVAC = 1
    catPspIDLCATEquipment = 2
    catPspIDLCATWaveguide = 3
    catPspIDLCATTubing = 4
    catPspIDLCATHanger = 5
    catPspIDLCATRaceway = 6
    catPspIDLCATConduit = 7
    catPspIDLCATCompAccess = 8
    catPspIDLCATElectrical = 9
    catPspIDLCATPID = 10
    catPspIDLCATHVACDiagram = 11
    catPspIDLCATTubingDiagram = 12
    catPspIDLCATWaveguideDiagram = 13
    catPspIDLCATElectricalDiagram = 14


class CatPspIdlAttrDataType(EnumItem):
    catPspIDLInteger = 0
    catPspIDLDouble = 1
    catPspIDLString = 2
    catPspIDLMultiString = 3
    catPspIDLBoolean = 4


class CatPspIdlDomainId(EnumItem):
    catPspIDLNone = 0
    catPspIDLCATPIP = 1
    catPspIDLCATINS = 2
    catPspIDLCATHVA = 3
    catPspIDLCATEQT = 4
    catPspIDLCATTUB = 5
    catPspIDLCATMLD = 6
    catPspIDLCATWVG = 7
    catPspIDLCATRWY = 8
    catPspIDLCATCND = 9
    catPspIDLCATHGR = 10
    catPspIDLCATCAM = 11
    catPspIDLCATELE = 12


class CatPspIdlFlowCapability(EnumItem):
    catPspIDLFlowCapability_Undefined = 0
    catPspIDLFlowCapability_InDirection = 1
    catPspIDLFlowCapability_OutDirection = 2
    catPspIDLFlowCapability_InOutDirection = 3


class CatPspIdlFlowReality(EnumItem):
    catPspIDLFlowReality_Undefined = 0
    catPspIDLFlowReality_InDirection = 1
    catPspIDLFlowReality_OutDirection = 2
    catPspIDLFlowReality_InOutDirection = 3


class CatPspIdlFunctionStatus(EnumItem):
    catPspIDLFuncUndefined = 0
    catPspIDLInFuncNet = 1
    catPspIDLFuncNetPhysType = 2
    catPspIDLFuncNetPhysNoPos = 3
    catPspIDLFuncNoNetPhys = 4
    catPspIDLFuncNetPhys = 5


class CatPspIdlPartConnectorType(EnumItem):
    catPspIDLPartCtrTypeNotRecognized = 0
    catPspIDLPartCtrTypeFace = 1
    catPspIDLPartCtrTypeSupport = 2
    catPspIDLPartCtrTypeCenter = 3
    catPspIDLPartCtrTypeTop = 4
    catPspIDLPartCtrTypeBottom = 5
    catPspIDLPartCtrTypeLeft = 6
    catPspIDLPartCtrTypeRight = 7
    catPspIDLPartCtrTypeTopLeft = 8
    catPspIDLPartCtrTypeTopRight = 9
    catPspIDLPartCtrTypeBottomLeft = 10
    catPspIDLPartCtrTypeBottomRight = 11
    catPspIDLPartCtrTypeCircular = 12
    catPspIDLPartCtrTypeRectangular = 13
    catPspIDLPartCtrTypeUpOnly = 14


class CatRectangularPatternParameters(EnumItem):
    catInstancesandSpacing = 0
    catUnequalSpacing = 1


class CatRenderingMode(EnumItem):
    catRenderShading = 0
    catRenderShadingWithEdges = 1
    catRenderWireFrame = 2
    catRenderHiddenLinesRemoval = 3
    catRenderQuickHiddenLinesRemoval = 4
    catRenderMaterial = 5
    catRenderMaterialWithEdges = 6
    catRenderShadingWithEdgesAndHiddenEdges = 7
    catRenderShadingWithEdgesWithoutSmoothEdges = 8
    catRenderWireFrameWithoutSmoothEdgesWithoutVertices = 9
    catRenderWireFrameWithHalfSmoothEdgesWithoutVertices = 10
    catRenderShadingWithEdgesWithOutlines = 11
    catRenderQuickHiddenLinesRemovalWithoutVertices = 12
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithOutlines = 13
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithOutlinesWithoutVertices = 14
    catRenderWireFrameWithHalfSmoothEdgeWithOutlinesWithoutVertices = 15
    catRenderWireFrameWithOutlinesWithoutSmoothEdgesWithoutVertices = 16
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithoutSmoothEdgesWithoutVertices = (
        17
    )
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithHalfSmoothEdgeWithoutVertices = (
        18
    )
    catRenderQuickHiddenLinesRemovalWithoutSmoothEdgesWithoutVertices = 19
    catRenderQuickHiddenLinesRemovalWithHalfSmoothEdgeWithoutVertices = 20
    catRenderShadingWithEdgesWithHalfSmoothEdgeWithoutVertices = 21
    catRenderShadingWithEdgesWithHalfSmoothEdge = 22


class CatRepType(EnumItem):
    catRep3D = 0
    catRep2D = 1
    catRepText = 2


class CatRepresentationMode(EnumItem):
    catExactMode = 0
    catPolyhedricMode = 1
    catVisualMode = 2


class CatSacSettingsEnum(EnumItem):
    CatSacSettingsEnumNoInsert = 0
    CatSacSettingsEnumAutomatic = 1
    CatSacSettingsEnumUserPrompt = 2


class CatSampledAnalysisMode(EnumItem):
    CatSampledAnalysisOff = 0
    CatSampledAnalysisOn = 1
    CatSampledAnalysisStop = 2
    CatSampledAnalysisVerbose = 3


class CatSampledSplitType(EnumItem):
    CatSampledSplitOnSeg = 0
    CatSampledSplitOnShot = 1


class CatSceneType(EnumItem):
    CatSceneTypeDelta = 0
    CatSceneTypeFull = 1


class CatSchIdlApplicationId(EnumItem):
    catSchIDLCATPID = 0
    catSchIDLCATHVACDiagram = 1
    catSchIDLCATWaveguideDiagram = 2
    catSchIDLCATTubingDiagram = 3
    catSchIDLCATElectricalDiagram = 4


class CatSchIdlArrowFrequency(EnumItem):
    catSchIDLArrowAllSegs = 0
    catSchIDLArrowAllButLastSeg = 1
    catSchIDLArrowInteriorSegs = 2
    catSchIDLArrowMiddleSeg = 3


class CatSchIdlArrowPosition(EnumItem):
    catSchIDLMidSegArrow = 0
    catSchIDLEndSegArrow = 1


class CatSchIdlArrowStyle(EnumItem):
    catSchIDLFillArrow = 0
    catSchIDLNotFillArrow = 1
    catSchIDLStandardArrow = 2


class CatSchIdlCntrFlowCapability(EnumItem):
    catSchIDLCntrFlowCapability_Undefined = 0
    catSchIDLCntrFlowCapability_InDirection = 1
    catSchIDLCntrFlowCapability_OutDirection = 2
    catSchIDLCntrFlowCapability_InOutDirection = 3


class CatSchIdlCntrFlowReality(EnumItem):
    catSchIDLCntrFlowReality_Undefined = 0
    catSchIDLCntrFlowReality_InDirection = 1
    catSchIDLCntrFlowReality_OutDirection = 2
    catSchIDLCntrFlowReality_InOutDirection = 3


class CatSchIdlCntrSymbolType(EnumItem):
    catSchIDLCntrSymbol_Undefined = 0
    catSchIDLCntrSymbol_Point = 1
    catSchIDLCntrSymbol_PtVector = 2
    catSchIDLCntrSymbol_OnOffSheet = 3
    catSchIDLCntrSymbol_LineBoundary = 4


class CatSchIdlDisplayMode(EnumItem):
    catSchIDLDisplayMode_Default = 0
    catSchIDLDisplayMode_Alternate = 1


class CatSchIdlExtensionType(EnumItem):
    catSchIDLComponent_Extension = 0
    catSchIDLRoute_Extension = 1
    catSchIDLCompConnector_Extension = 2
    catSchIDLRouteConnector_Extension = 3
    catSchIDLZone_Extension = 4


class CatSchIdlGapPriority(EnumItem):
    catSchIDLGapThisRoute = 0
    catSchIDLGapInputRoute = 1
    catSchIDLGapNoPriority = 2
    catSchIDLGapHorizontalSeg = 3
    catSchIDLGapVerticalSeg = 4


class CatSchIdlGapStyle(EnumItem):
    catSchIDLBlankGap = 0
    catSchIDLJumpGap = 1
    catSchIDLWavyGap = 2


class CatSchIdlInternalFlowStatus(EnumItem):
    catSchIDLInternFlowStatus_Undefined = 0
    catSchIDLInternFlowStatus_Open = 1
    catSchIDLInternFlowStatus_Close = 2


class CatSchIdlInternalFlowType(EnumItem):
    catSchIDLInternFlowType_Undefined = 0
    catSchIDLInternFlowType_Corner = 1
    catSchIDLInternFlowType_Linear = 2


class CatSchIdlMultiImageStatus(EnumItem):
    catSchIDLImage_IsUpToDate = 0
    catSchIDLImage_MasterNotFound = 1
    catSchIDLImage_MasterDocNotFound = 2
    catSchIDLImage_InvalidReference = 3
    catSchIDLImage_AttrsNotUpToDate = 4


class CatSchIdlRouteAlternateGraphicStyle(EnumItem):
    catSchIDLRouteAlternateGraphicStyle_ellipse = 0


class CatSchIdlRouteCompressMode(EnumItem):
    catSchIDLCompressOff = 0
    catSchIDLCompressOn = 1


class CatSchIdlRouteMode(EnumItem):
    catSchIDLRouteMode_Undefined = 0
    catSchIDLRouteMode_HorizontalVertical = 1
    catSchIDLRouteMode_HorizontalVertical45 = 2
    catSchIDLRouteMode_PointToPoint = 3
    catSchIDLRouteMode_AroundObject = 4


class CatSchIdlRouteSymbolUpdateMode(EnumItem):
    catSchIDLSymbolUpdateOff = 0
    catSchIDLSymbolUpdateOn = 1


class CatSchIdlRouteUnsetGapsMode(EnumItem):
    catSchIDLUnsetGapsOff = 0
    catSchIDLUnsetGapsOn = 1


class CatSchIdlgrrRouteReshapeMode(EnumItem):
    catSchIDLFixedShapeOff = 0
    catSchIDLFixedShapeOn = 1


class CatScriptLanguage(EnumItem):
    CATVBScriptLanguage = 0
    CATVBALanguage = 1
    CATBasicScriptLanguage = 2
    CATJavaLanguage = 3
    CATJScriptLanguage = 4


class CatScriptLibraryType(EnumItem):
    catScriptLibraryTypeDocument = 0
    catScriptLibraryTypeDirectory = 1
    catScriptLibraryTypeVBAProject = 2


class CatSearchContextScope(EnumItem):
    Everywhere = 0
    InWorkbench = 1
    FromWorkbench = 2
    FromSelection = 3
    VisibleOnScreen = 4


class CatSecWindowOpenMode(EnumItem):
    catSecWindow_DefaultSize = 0
    catSecWindow_TileVertically = 1


class CatSectionBehavior(EnumItem):
    catSectionBehaviorManual = 0
    catSectionBehaviorAutomatic = 1
    catSectionBehaviorFreeze = 2


class CatSectionClippingMode(EnumItem):
    catSection_Software = 0
    catSection_OpenGL = 1


class CatSectionGridStyle(EnumItem):
    catSectionGridStyle_Lines = 0
    catSectionGridStyle_Crosses = 1


class CatSectionPlaneNormal(EnumItem):
    catSectionNormal_X = 0
    catSectionNormal_Y = 1
    catSectionNormal_Z = 2


class CatSectionPlaneOrigin(EnumItem):
    catSectionOrigin_0 = 0
    catSectionOrigin_Selection = 1


class CatSectionType(EnumItem):
    catSectionTypePlane = 0
    catSectionTypeSlice = 1
    catSectionTypeBox = 2


class CatSelectionFilter(EnumItem):
    ZeroDim = 0
    MonoDim = 1
    MonoDimInfinite = 2
    RectilinearMonoDim = 3
    RectilinearMonoDimInfinite = 4
    BiDim = 5
    BiDimInfinite = 6
    PlanarBiDim = 7
    PlanarBiDimInfinite = 8
    CylindricalBiDim = 9
    TriDim = 10


class CatSewingIntersectionMode(EnumItem):
    catSewingNoIntersect = 0
    catSewingIntersect = 1


class CatSheetGenViewsPosMode(EnumItem):
    catFixedCG = 0
    catFixedAxis = 1


class CatSheetProjectionMethod(EnumItem):
    catFirstAngle = 0
    catThirdAngle = 1


class CatShowResultType(EnumItem):
    ByRule = 0
    ByObject = 1
    ByState = 2


class CatShuttleMoveMode(EnumItem):
    CatShuttle = 0
    CatAxis = 1


class CatShuttleVector(EnumItem):
    CatShuttleVectorX = 0
    CatShuttleVectorY = 1
    CatShuttleVectorZ = 2


class CatSolveType(EnumItem):
    ManualSolveType = 0
    AutomaticOptimizedSolveType = 1
    AutomaticCompleteSolveType = 2


class CatSpecsAndGeomWindowLayout(EnumItem):
    catWindowSpecsOnly = 0
    catWindowGeomOnly = 1
    catWindowSpecsAndGeom = 2


class CatSpecsLayout(EnumItem):
    catSpecsViewerHorizontalIndented = 0
    catSpecsViewerHorizontalUp = 1
    catSpecsViewerHorizontalCentered = 2
    catSpecsViewerVerticalCentered = 3
    catSpecsViewerHorizontalRelational = 4
    catSpecsViewerVerticalRelational = 5


class CatSplitSide(EnumItem):
    catPositiveSide = 0
    catNegativeSide = 1


class CatStrCreationMode(EnumItem):
    catStrPartMode = 0
    catStrSheetMetalMode = 1


class CatStrCutbackType(EnumItem):
    catStrNoneType = 0
    catStrNormalType = 1
    catStrWeldedType = 2
    catStrMiteredType = 3
    catStrNotchingType = 4


class CatStrLinkMode(EnumItem):
    catStrWithLinkMode = 0
    catStrNoLinkMode = 1
    catStrRefRefWithLinkMode = 2
    catStrRefRefNoLinkMode = 3


class CatStrMaterialOrientation(EnumItem):
    catStrStandardOrientation = 0
    catStrReverseOrientation = 1


class CatStrMemberExtremity(EnumItem):
    catStartExtremity = 0
    catEndExtremity = 1
    catBothExtremity = 2


class CatStrPlacementPoint(EnumItem):
    catStrDefault = 0
    catStrBottomLeft = 1
    catStrBottomCenter = 2
    catStrBottomRight = 3
    catStrCenterLeft = 4
    catStrCenterCenter = 5
    catStrCenterRight = 6
    catStrTopLeft = 7
    catStrTopCenter = 8
    catStrTopRight = 9
    catStrGravity = 10
    catStrGravityBottom = 11
    catStrGravityLeft = 12
    catStrGravityRight = 13
    catStrGravityTop = 14
    catStrUserPoint = 15


class CatStrPlaneMode(EnumItem):
    catStrNoneMode = 0
    catStrOnPlane = 1
    catStrParallelToPlane = 2


class CatStrSectionProperties(EnumItem):
    CatStrArea = 0
    CatStrInertiaXX = 1
    CatStrInertiaYY = 2
    CatStrModuleInertiaX = 3
    CatStrModuleInertiaY = 4
    CatStrGirationModuleX = 5
    CatStrGirationModuleY = 6


class CatSymbolType(EnumItem):
    catNotUsed = 0
    catCross = 1
    catPlus = 2
    catConcentric = 3
    catCoincident = 4
    catFullCircle = 5
    catFullSquare = 6
    catStar = 7
    catDot = 8
    catSmallDot = 9
    catMisc1 = 10
    catMisc2 = 11
    catFullCircle2 = 12
    catFullSquare2 = 13
    catOpenArrow = 14
    catUnfilledArrow = 15
    catBlankedArrow = 16
    catFilledArrow = 17
    catUnfilledCircle = 18
    catBlankedCircle = 19
    catFilledCircle = 20
    catCrossedCircle = 21
    catBlankedSquare = 22
    catFilledSquare = 23
    catBlankedTriangle = 24
    catFilledTriangle = 25
    catManipulatorSquare = 26
    catMamipulatorDiamond = 27
    catManipulatorCircle = 28
    catManipulatorTriangle = 29
    catDoubleOpenArrow = 30
    catWave = 31


class CatTableBorderType(EnumItem):
    CatTableNone = 0
    CatTableLeft = 1
    CatTableTop = 2
    CatTableRight = 3
    CatTableBottom = 4
    CatTableBackSlashed = 5
    CatTableSlashed = 6
    CatTableHorStrikedOut = 7
    CatTableVerStrikedOut = 8
    CatTableOutLine = 9
    CatTableInside = 10
    CatTableCross = 11


class CatTableComputeMode(EnumItem):
    CatTableComputeOFF = 0
    CatTableComputeON = 1


class CatTableInvertMode(EnumItem):
    CatInvertColumn = 0
    CatInvertRow = 1
    CatInvertAll = 2


class CatTablePosition(EnumItem):
    CatTableTopLeft = 0
    CatTableMiddleLeft = 1
    CatTableBottomLeft = 2
    CatTableTopCenter = 3
    CatTableMiddleCenter = 4
    CatTableBottomCenter = 5
    CatTableTopRight = 6
    CatTableMiddleRight = 7
    CatTableBottomRight = 8


class CatTextAnchorPosition(EnumItem):
    catUnsusedValue1 = 0
    catTopLeft = 1
    catMiddleLeft = 2
    catBottomLeft = 3
    catTopCenter = 4
    catMiddleCenter = 5
    catBottomCenter = 6
    catTopRight = 7
    catMiddleRight = 8
    catBottomRight = 9
    catUnsusedValue2 = 10
    catCapLeft = 11
    catHalfLeft = 12
    catBaseLeft = 13
    catCapCenter = 14
    catHalfCenter = 15
    catBaseCenter = 16
    catCapRight = 17
    catHalfRight = 18
    catBaseRight = 19


class CatTextFlipMode(EnumItem):
    catTextNoFlip = 0
    catTextHorizontalFlip = 1
    catTextVerticalFlip = 2
    catTextHorizontalAndVerticalFlip = 3
    catTextAutoFlip = 4


class CatTextFrameType(EnumItem):
    catNone = 0
    catRectangle = 1
    catSquare = 2
    catCircle = 3
    catScoredCircle = 4
    catDiamond = 5
    catTriangle = 6
    catRightFlag = 7
    catLeftFlag = 8
    catBothFlag = 9
    catOblong = 10
    catEllipse = 11
    catCustom = 12


class CatTextProperty(EnumItem):
    catBold = 0
    catItalic = 1
    catUnderline = 2
    catOverline = 3
    catStrikethrough = 4
    catSubscript = 5
    catSuperscript = 6
    catFontSize = 7
    catParagraph = 8
    catPlain = 9
    catColor = 10
    catFontName = 11
    catBorder = 12
    catAlignment = 13
    catCharRatio = 14
    catCharSpacing = 15
    catKerning = 16


class CatThreadLinkedTo(EnumItem):
    catNotDefined = 0
    catNoLink = 1
    cat2DPoint = 2
    cat2DCircle = 3
    cat3DGeom = 4
    cat3DHole = 5
    cat3DThread = 6


class CatThreadPolarity(EnumItem):
    catThread = 0
    catTap = 1


class CatThreadSide(EnumItem):
    catRightSide = 0
    catLeftSide = 1


class CatThreadStandard(EnumItem):
    catMetricThinPitch = 0
    catMetricThickPitch = 1


class CatThreadType(EnumItem):
    catThreaded = 0
    catTaped = 1


class CatTreeOrientationEnum(EnumItem):
    catTreeOrientationVertical = 0
    catTreeOrientationHorizontal = 1


class CatTreeSizeTypeEnum(EnumItem):
    catTreeSizeTypeFixedSize = 0
    catTreeSizeTypeTextDependentSize = 1


class CatTreeTypeEnum(EnumItem):
    catTreeTypeClassical = 0
    catTreeTypeStructural = 1
    catTreeTypeHistorical = 2
    catTreeTypeRelational = 3


class CatView2DModeVisu(EnumItem):
    catView2DModeNotActivated = 0
    catView2DModeNoShow = 1


class CatViewBackgroundMode(EnumItem):
    catStandard = 0
    catInvisible = 1
    catUnpickable = 2
    catLowIntensity = 3
    catUnpickableLowIntensity = 4


class CatViewFilterCreationMode(EnumItem):
    catDefaultFilter = 0
    catDisplayFilterDialogBox = 1
    catDedicatedFilter = 2


class CatViewSide(EnumItem):
    catTopSide = 0
    catBottomSide = 1
    catLeftSide = 2
    catRightSide = 3
    catTLCorner = 4
    catTRCorner = 5
    catBLCorner = 6
    catBRCorner = 7


class CatViewType(EnumItem):
    catAuxiliaryView = 0
    catSectionView = 1
    catSectionCutView = 2


class CatVisLayerType(EnumItem):
    catVisLayerBasic = 0
    catVisLayerNone = 1


class CatVisPropertyPick(EnumItem):
    catVisPropertyPickAttr = 0
    catVisPropertyNoPickAttr = 1


class CatVisPropertyShow(EnumItem):
    catVisPropertyShowAttr = 0
    catVisPropertyNoShowAttr = 1


class CatVisPropertyStatus(EnumItem):
    catVisPropertyDefined = 0
    catVisPropertyUnDefined = 1


class CatVisPropertyType(EnumItem):
    catVisPropertyLineType = 0
    catVisPropertyWidth = 1
    catVisPropertyColor = 2
    catVisPropertyOpacity = 3


class CatVisuBackgroundMode(EnumItem):
    catNoBackground = 0
    catPick = 1
    catNoPick = 2
    catLowIntPick = 3
    catLowIntNoPick = 4


class CatVisuIn3DMode(EnumItem):
    catShowAll = 0
    catHideAll = 1


class CatVisualizationType(EnumItem):
    Passed = 0
    Failed = 1
    Both = 2


class CatWeldAdditionalSymbol(EnumItem):
    catNoneAddWelding = 0
    catFlatWelding = 1
    catConvexWelding = 2
    catConcaveWelding = 3
    catFlushWelding = 4
    catSmoothWelding = 5


class CatWelding(EnumItem):
    catNoneWelding = 0
    catFirstWelding = 1
    catSecondWelding = 2


class CatWeldingField(EnumItem):
    catWeldingNone = 0
    catWeldingFieldOne = 1
    catWeldingFieldTwo = 2
    catWeldingFieldThree = 3
    catWeldingFieldFour = 4
    catWeldingFieldFive = 5
    catWeldingFieldSix = 6
    catWeldingFieldSeven = 7


class CatWeldingSide(EnumItem):
    catWeldingUp = 0
    catWeldingDown = 1


class CatWeldingSymbol(EnumItem):
    catNoneMainWelding = 0
    catSquareWelding = 1
    catVGrooveWelding = 2
    catHVGrooveWelding = 3
    catYGrooveWelding = 4
    catHYGrooveWelding = 5
    catUGrooveWelding = 6
    catHUGrooveWelding = 7
    catFilletWelding = 8
    catCFlangeWelding = 9
    catEFlangeWelding = 10
    catVFlareWelding = 11
    catHVFlareWelding = 12
    catSpotWelding = 13
    catBackWelding = 14
    catHVOGrooveWelding = 15
    catVOGrooveWelding = 16
    catPlugWelding = 17
    catMRWelding = 18
    catMWelding = 19
    catRechargWelding = 20
    catSpotJISWelding = 21
    catEFlangeISOWelding = 22
    catSeamWelding = 23
    catScarfWelding = 24
    catStudWelding = 25
    catEdgeWelding = 26
    catMeltThruWelding = 27
    catSurfaceJointWelding = 28
    catInclinedJointWelding = 29


class CatWindowState(EnumItem):
    catWindowStateMaximized = 0
    catWindowStateMinimized = 1
    catWindowStateNormal = 2


class CatWorkModeType(EnumItem):
    DEFAULT_MODE = 0
    VISUALIZATION_MODE = 1
    DESIGN_MODE = 2


class CatftaDimConfigureSnapping(EnumItem):
    CATFTADimSnappingUndefined = 0
    CATFTADimSnappingOnGrid = 1
    CATFTADimSnappingValue = 2
    CATFTADimSnappingBoth = 3


class CatftaDimCreateOn(EnumItem):
    CATFTADimCreateOnUndefined = 0
    CATFTADimCreateOnCenter = 1
    CATFTADimCreateOnEdge = 2


class CatftaLeaderAssociativity(EnumItem):
    CATFTALeaderAssociativityUndefined = 0
    CATFTALeaderAssociativityFree = 1
    CATFTALeaderAssociativityPerpendicular = 2


class Catv4Iv4V5SpecDraftMigrationEnum(EnumItem):
    squareMode = 0
    coneMode = 1


class Catv4Iv5V4AssociativityModeEnum(EnumItem):
    AssociativeMode = 0
    NonAssociativeMode = 1
    NonAssociativityModeAndNoSolidCreation = 2


class Catv4Iv5V4ErrorFeatureCreationEnum(EnumItem):
    NeverCreateErrorFeatures = 0
    CreateAnErrorFeatureAfterUserAgreement = 1
    AlwaysCreateErrorFeatures = 2


class Catv4Iv5V4InternalCurveCreationEnum(EnumItem):
    AllCurvesAreCreated = 0
    OnlyConicsAreCreated = 1
    NoInternalCurveIsCreated = 2


class Cd5SaveItemStatus(EnumItem):
    CD5SaveItem_New = 0
    CD5SaveItem_Modified = 1
    CD5SaveItem_Exists = 2
    CD5SaveItem_ECNameNotUnique = 3
    CD5SaveItem_ModifiedNotLockedByYou = 4
    CD5SaveItem_Obsolete = 5
    CD5SaveItem_UUIDConflict = 6
    CD5SaveItem_NotFound = 7


class Cd5SaveOperationScope(EnumItem):
    CD5SaveOperation_ActiveDocument = 0
    CD5SaveOperation_CurrentEditor = 1
    CD5SaveOperation_Session = 2


class ContactStiffnessType(EnumItem):
    DEFAULT = 0
    STIFF_VALUE = 1


class DistributionType(EnumItem):
    UNIFORM = 0
    JOB = 1
    USERDEFINED = 2
    JOB_USERDEFINED = 3


class DmuTrackMoveMode(EnumItem):
    DMUTrackSpeedMode = 0
    DMUTrackTimeMode = 1


class DnbActBehaviorType(EnumItem):
    DNBBehaviorProcess = 0
    DNBBehaviorParent = 1


class DnbAnalysisLevel(EnumItem):
    DNBAnalysisLevelOff = 0
    DNBAnalysisLevelHighlight = 1
    DNBAnalysisLevelVerbose = 2
    DNBAnalysisLevelInterrupt = 3


class DnbAssignStatus(EnumItem):
    DNBUnknownState = 0
    DNBSuccess = 1
    DNBAlreadyAssigned = 2
    DNBInvalidObjetAssignment = 3
    DNBInvalidProcessVersion = 4
    DNBPartsNotLoaded = 5


class DnbAuxilliaryDeviceType(EnumItem):
    AuxilliaryDeviceType_RailTrackGantry = 0
    AuxilliaryDeviceType_EndOfArmTooling = 1
    AuxilliaryDeviceType_WorkpiecePositioner = 2
    AuxilliaryDeviceType_Conveyor = 3


class DnbHlnkBehaviorType(EnumItem):
    DNBBehaviorContinue = 0
    DNBBehaviorPause = 1


class DnbSimGraphUpdateMode(EnumItem):
    DNBSimGraphUpdateDisabled = 0
    DNBSimGraphUpdateEnabled = 1


class DnbSimInitStateAttr(EnumItem):
    DNBVisInitStateAttr = 0
    DNBPosInitStateAttr = 1
    DNBColInitStateAttr = 2
    DNBOpacInitStateAttr = 3
    DNBVisPosInitStateAttr = 4
    DNBVisColInitStateAttr = 5
    DNBVisOpacInitStateAttr = 6
    DNBVisPosColInitStateAttr = 7
    DNBVisPosOpacInitStateAttr = 8
    DNBVisColOpacInitStateAttr = 9
    DNBPosColInitStateAttr = 10
    DNBPosOpacInitStateAttr = 11
    DNBPosColOpacInitStateAttr = 12
    DNBColOpacInitStateAttr = 13
    DNBAllInitStateAttr = 14


class DnbSimNavigationMode(EnumItem):
    DNBSimNavigationModeStep = 0
    DNBSimNavigationModeAnimate = 1


class DnbVisualizationMode(EnumItem):
    DNBVisualizationModeHighlight = 0
    DNBVisualizationModeCurves = 1


class DnbiaMfgAssemblyType(EnumItem):
    manufacturingAssembly = 0
    manufacturingKit = 1
    assemblySpecTree = 2
    manufacturingOutput = 3
    notSpecified = 4


class DnbpprRemoveStatus(EnumItem):
    DNBFastenerUnknownStatus = 0
    DNBFastenerAssignedStatus = 1
    DNBFastenerSuccessStatus = 2


class DnbtcpTraceLegends(EnumItem):
    DNBTCPTraceLegendAllLegend = 0
    DNBTCPTraceLegendName = 1
    DNBTCPTraceLegendX = 2
    DNBTCPTraceLegendY = 3
    DNBTCPTraceLegendZ = 4
    DNBTCPTraceLegendYaw = 5
    DNBTCPTraceLegendPitch = 6
    DNBTCPTraceLegendRoll = 7
    DNBTCPTraceLegendCycleTime = 8
    DNBTCPTraceLegendHighlight = 9
    DNBTCPTraceLegendAlwaysVisible = 10


class DnbtcpTraceReps(EnumItem):
    DNBTCPTraceRepAllRep = 0
    DNBTCPTraceRepPoint = 1
    DNBTCPTraceRepLine = 2
    DNBTCPTraceRepAxis = 3


class ElemBehavEnum(EnumItem):
    BEHAVIOR_NONE = 0
    SHELL = 1
    MEMBRANE = 2
    SOLID3D = 3
    CONTINUUM_SHELL = 4
    BEAM = 5
    GASKET = 6


class ElemIdEnum(EnumItem):
    TET_LINEAR = 0
    TET_PARABOLIC = 1
    HEX_LINEAR = 2
    HEX_PARABOLIC = 3
    WEDG_LINEAR = 4
    WEDG_PARABOLIC = 5
    TRI_LINEAR = 6
    TRI_PARABOLIC = 7
    QUAD_LINEAR = 8
    QUAD_PARABOLIC = 9
    LINE_LINEAR = 10
    LINE_PARABOLIC = 11


class FixedTimeIncrementMethod(EnumItem):
    ABQ_FTI_ELEMENT_BY_ELEMENT = 0
    ABQ_FTI_USER_DEFINED = 1


class FormulationOptionType(EnumItem):
    SOLVERDEFAULT = 0
    SURFACETOSURFACE = 1
    NODETOSURFACE = 2


class FormulationType(EnumItem):
    FRICTIONLESS = 0
    PENALTY = 1


class FrameVisibility(EnumItem):
    VisNo = 0
    VisYes = 1
    VisRetain = 2


class HtsActivityGroupMotionBasis(EnumItem):
    HAGMOTBASIS_DEFAULT = 0
    HAGMOTBASIS_USERSPEED = 1
    HAGMOTBASIS_USERTIME = 2


class HtsBodyPoseOptions(EnumItem):
    BODYPOSE_CURRENT = 0
    BODYPOSE_RESET = 1


class HtsEndEffector(EnumItem):
    EE_LEFTHAND = 0
    EE_RIGHTHAND = 1
    EE_LEFTLEG = 2
    EE_RIGHTLEG = 3
    EE_LINEOFSIGHT = 4
    EE_BODY = 5
    EE_NECK = 6


class HtsHand(EnumItem):
    HAND_RIGHT = 0
    HAND_LEFT = 1


class HtsManikinReferential(EnumItem):
    REF_EYEPOINT = 0
    REF_HPOINT = 1
    REF_LEFTFOOT = 2
    REF_RIGHTFOOT = 3
    REF_LOWESTFOOT = 4
    REF_CROTCH = 5
    REF_LEFTHAND = 6
    REF_RIGHTHAND = 7
    REF_BETWEENFEET = 8
    REF_HPOINTPROJECTION = 9


class HtsMotionBasis(EnumItem):
    MOTBASIS_SPEED = 0
    MOTBASIS_TIME = 1


class HtsPickType(EnumItem):
    SINGLE_HAND = 0
    BOTH_HANDS = 1


class HtsSearchIntensity(EnumItem):
    FINESEARCH = 0
    NORMALSEARCH = 1
    COARSESEARCH = 2


class HtsStrideOptions(EnumItem):
    STRIDE_SHORT = 0
    STRIDE_MEDIUM = 1
    STRIDE_LONG = 2


class HtsSwingOptions(EnumItem):
    SWING_BOTHARMS = 0
    SWING_LEFTARM = 1
    SWING_RIGHTARM = 2
    SWING_CURRENT = 3


class HtsWalkMotionBasis(EnumItem):
    WALKMOTBASIS_DEFAULT = 0
    WALKMOTBASIS_USERSPEED = 1
    WALKMOTBASIS_USERTIME = 2


class IncrementationType(EnumItem):
    AUTO_INCREMENT = 0
    FIXED_INCREMENT = 1


class InitialThicknessType(EnumItem):
    USE_NODAL_COORDINATES = 0
    INITIAL_THICKNESS_SPECIFY = 1


class ItemAssignmentType(EnumItem):
    ProcessProcesses = 0
    ProcessFirstProcesses = 1
    ProcessRemoves = 2
    ProcessImplementsRequirementPartial = 3
    ProcessImplementsRequirementComplete = 4
    productviewpoint = 5
    productvisualization = 6


class JobType(EnumItem):
    ANALYSIS = 0
    DATACHECK = 1
    CONTINUE = 2
    FROMINPUTFILE = 3
    SYNTAXCHECK = 4
    RESTART = 5


class MaxStiffnessType(EnumItem):
    MAX_STIFF_DEFAULT = 0
    MAX_STIFF_VALUE = 1


class MemoryUnitType(EnumItem):
    MEGABYTES = 0
    PERCENT = 1


class MotionBasis(EnumItem):
    MOTION_ABSOLUTE = 0
    MOTION_PERCENT = 1
    MOTION_TIME = 2


class ParallelMethodStdType(EnumItem):
    TREE = 0
    SUPERNODE = 1


class PositionToleranceType(EnumItem):
    COMPUTED = 0
    SPECIFIED = 1


class PressureOverclosureType(EnumItem):
    HARD = 0
    EXPONENTIAL = 1
    LINEAR = 2
    TABULAR = 3


class RasterLevelOfDetail(EnumItem):
    LowQuality = 0
    NormalQuality = 1
    HighQuality = 2
    Customize = 3


class ResponseType(EnumItem):
    STEADY_STATE = 0
    TRANSIENT = 1


class SlidingType(EnumItem):
    FINITE = 0
    SMALL = 1


class SpmDistributionMode(EnumItem):
    SPM_LINEAR = 0
    SPM_HISTOGRAM = 1
    SPM_LOG = 2


class SpringDefType(EnumItem):
    ABQ_LINE = 0
    ABQ_NON_LINEAR = 1


class SpringDofType(EnumItem):
    U1_DOF = 0
    U2_DOF = 1
    U3_DOF = 2
    UR1_DOF = 3
    UR2_DOF = 4
    UR3_DOF = 5


class SpringTypeType(EnumItem):
    AXIAL = 0
    GENERAL = 1


class StabilizationStiffnessType(EnumItem):
    STABILIZATION_DEFAULT = 0
    STABILIZATION_SPECIFY = 1


class StabilizationType(EnumItem):
    NONE = 0
    DISSIPATION = 1
    FACTOR = 2


class SwkAnthroSex(EnumItem):
    Male = 0
    Female = 1


class SwkPostureSpec(EnumItem):
    SWKPostureSpecDefault = 0
    SWKPostureSpecStand = 1
    SWKPostureSpecSit = 2
    SWKPostureSpecReach = 3
    SWKPostureSpecExtendedReach = 4
    SWKPostureSpecSpan = 5
    SWKPostureSpecKneel = 6
    SWKPostureSpecInitial = 7


class TimeSpanType(EnumItem):
    STEP_TIME = 0
    TOTAL_TIME = 1


class GeometricalFeatureType(EnumItem):
    Unknown = 0
    Point = 1
    Curve = 2
    Line = 3
    Circle = 4
    Surface = 5
    Plane = 6
    Solid_or_Volume = 7
