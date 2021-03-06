# libARNetworkAL/Includes/libARNetworkAL/ARNETWORKAL_Manager.h
ARNETWORKAL_MANAGER_DEFAULT_ID_MAX  = 256

# ARNETWORKAL_Frame_tidentifiers
BD_NET_CD_NONACK_ID = 10
BD_NET_CD_ACK_ID = 11
BD_NET_CD_EMERGENCY_ID = 12
BD_NET_CD_VIDEO_ACK_ID = 13
BD_NET_DC_VIDEO_DATA_ID = 125
BD_NET_DC_EVENT_ID = 126
BD_NET_DC_NAVDATA_ID = 127

# eARMEDIA_ENCAPSULER_CODEC
CODEC_UNKNNOWN = 0
CODEC_VLIB = 1
CODEC_P264 = 2
CODEC_MPEG4_VISUAL = 3
CODEC_MPEG4_AVC = 4
CODEC_MOTION_JPEG = 5

# eARCOMMANDS_ARDRONE3_ANIMATIONS_FLIP_DIRECTION : Format "I"
ARCOMMANDS_ARDRONE3_ANIMATIONS_FLIP_DIRECTION_FRONT = 0
ARCOMMANDS_ARDRONE3_ANIMATIONS_FLIP_DIRECTION_BACK = 1
ARCOMMANDS_ARDRONE3_ANIMATIONS_FLIP_DIRECTION_RIGHT = 2
ARCOMMANDS_ARDRONE3_ANIMATIONS_FLIP_DIRECTION_LEFT = 3

# eARCOMMANDS_ARDRONE3_MEDIARECORD_VIDEO_RECORD
ARCOMMANDS_ARDRONE3_MEDIARECORD_VIDEO_RECORD_STOP = 0
ARCOMMANDS_ARDRONE3_MEDIARECORD_VIDEO_RECORD_START = 1

# eARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE;
ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_LANDED = 0
ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_TAKINGOFF = 1
ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_HOVERING = 2
ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_FLYING = 3
ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_LANDING = 4
ARCOMMANDS_ARDRONE3_PILOTINGSTATE_FLYINGSTATECHANGED_STATE_EMERGENCY = 5

# eARCOMMANDS_ID_ARDRONE3_ANIMATIONS_CMD : Format "B"
ARCOMMANDS_ID_ARDRONE3_ANIMATIONS_CMD_FLIP = 0

# ARCOMMANDS_ID_ARDRONE3_ANTIFLICKERING_CMD
ARCOMMANDS_ID_ARDRONE3_ANTIFLICKERING_CMD_ELECTRICFREQUENCY = 0
ARCOMMANDS_ID_ARDRONE3_ANTIFLICKERING_CMD_SETMODE = 1

# ARCOMMANDS_ID_ARDRONE3_ANTIFLICKERINGSTATE_CMD
ARCOMMANDS_ID_ARDRONE3_ANTIFLICKERINGSTATE_CMD_ELECTRICFREQUENCYCHANGED = 0
ARCOMMANDS_ID_ARDRONE3_ANTIFLICKERINGSTATE_CMD_MODECHANGED = 1

# eARCOMMANDS_ID_ARDRONE3_CAMERA_CMD
ARCOMMANDS_ID_ARDRONE3_CAMERA_CMD_ORIENTATION = 0

# ARCOMMANDS_ID_ARDRONE3_CAMERASTATE_CMD
ARCOMMANDS_ID_ARDRONE3_CAMERASTATE_CMD_ORIENTATION = 0
ARCOMMANDS_ID_ARDRONE3_CAMERASTATE_CMD_DEFAULTCAMERAORIENTATION = 1

# eARCOMMANDS_ID_ARDRONE3_CLASS
ARCOMMANDS_ID_ARDRONE3_CLASS_PILOTING = 0
ARCOMMANDS_ID_ARDRONE3_CLASS_ANIMATIONS = 5
ARCOMMANDS_ID_ARDRONE3_CLASS_CAMERA = 1
ARCOMMANDS_ID_ARDRONE3_CLASS_MEDIARECORD = 7
ARCOMMANDS_ID_ARDRONE3_CLASS_MEDIARECORDSTATE= 8
ARCOMMANDS_ID_ARDRONE3_CLASS_MEDIARECORDEVENT= 3
ARCOMMANDS_ID_ARDRONE3_CLASS_PILOTINGSTATE= 4
ARCOMMANDS_ID_ARDRONE3_CLASS_NETWORK= 13
ARCOMMANDS_ID_ARDRONE3_CLASS_NETWORKSTATE= 14
ARCOMMANDS_ID_ARDRONE3_CLASS_PILOTINGSETTINGS= 2
ARCOMMANDS_ID_ARDRONE3_CLASS_PILOTINGSETTINGSSTATE= 6
ARCOMMANDS_ID_ARDRONE3_CLASS_SPEEDSETTINGS= 11
ARCOMMANDS_ID_ARDRONE3_CLASS_SPEEDSETTINGSSTATE= 12
ARCOMMANDS_ID_ARDRONE3_CLASS_NETWORKSETTINGS= 9
ARCOMMANDS_ID_ARDRONE3_CLASS_NETWORKSETTINGSSTATE= 10
ARCOMMANDS_ID_ARDRONE3_CLASS_SETTINGS= 15
ARCOMMANDS_ID_ARDRONE3_CLASS_SETTINGSSTATE= 16
ARCOMMANDS_ID_ARDRONE3_CLASS_DIRECTORMODE= 17
ARCOMMANDS_ID_ARDRONE3_CLASS_DIRECTORMODESTATE= 18
ARCOMMANDS_ID_ARDRONE3_CLASS_PICTURESETTINGS= 19
ARCOMMANDS_ID_ARDRONE3_CLASS_PICTURESETTINGSSTATE= 20
ARCOMMANDS_ID_ARDRONE3_CLASS_MEDIASTREAMING= 21
ARCOMMANDS_ID_ARDRONE3_CLASS_MEDIASTREAMINGSTATE= 22
ARCOMMANDS_ID_ARDRONE3_CLASS_GPSSETTINGS= 23
ARCOMMANDS_ID_ARDRONE3_CLASS_GPSSETTINGSSTATE= 24
ARCOMMANDS_ID_ARDRONE3_CLASS_CAMERASTATE= 25
ARCOMMANDS_ID_ARDRONE3_CLASS_ANTIFLICKERING= 29
ARCOMMANDS_ID_ARDRONE3_CLASS_ANTIFLICKERINGSTATE= 30

# ARCOMMANDS_ID_ARDRONE3_GPSSETTINGS_CMD
ARCOMMANDS_ID_ARDRONE3_GPSSETTINGS_CMD_SETHOME = 0
ARCOMMANDS_ID_ARDRONE3_GPSSETTINGS_CMD_RESETHOME = 1
ARCOMMANDS_ID_ARDRONE3_GPSSETTINGS_CMD_SENDCONTROLLERGPS = 2
ARCOMMANDS_ID_ARDRONE3_GPSSETTINGS_CMD_HOMETYPE = 3
ARCOMMANDS_ID_ARDRONE3_GPSSETTINGS_CMD_RETURNHOMEDELAY = 4

# ARCOMMANDS_ID_ARDRONE3_GPSSETTINGSSTATE_CMD
ARCOMMANDS_ID_ARDRONE3_GPSSETTINGSSTATE_CMD_HOMECHANGED = 0
ARCOMMANDS_ID_ARDRONE3_GPSSETTINGSSTATE_CMD_RESETHOMECHANGED = 1
ARCOMMANDS_ID_ARDRONE3_GPSSETTINGSSTATE_CMD_GPSFIXSTATECHANGED = 2
ARCOMMANDS_ID_ARDRONE3_GPSSETTINGSSTATE_CMD_GPSUPDATESTATECHANGED = 3
ARCOMMANDS_ID_ARDRONE3_GPSSETTINGSSTATE_CMD_HOMETYPECHANGED = 4
ARCOMMANDS_ID_ARDRONE3_GPSSETTINGSSTATE_CMD_RETURNHOMEDELAYCHANGED = 5

# ARCOMMANDS_ID_ARDRONE3_GPSSTATE_CMD
ARCOMMANDS_ID_ARDRONE3_GPSSTATE_CMD_NUMBEROFSATELLITECHANGED = 0
ARCOMMANDS_ID_ARDRONE3_GPSSTATE_CMD_HOMETYPEAVAILABILITYCHANGED = 1
ARCOMMANDS_ID_ARDRONE3_GPSSTATE_CMD_HOMETYPECHOSENCHANGED = 2

# eARCOMMANDS_ID_ARDRONE3_MEDIARECORD_CMD
ARCOMMANDS_ID_ARDRONE3_MEDIARECORD_CMD_PICTURE = 0
ARCOMMANDS_ID_ARDRONE3_MEDIARECORD_CMD_VIDEO = 1
ARCOMMANDS_ID_ARDRONE3_MEDIARECORD_CMD_PICTUREV2 = 2
ARCOMMANDS_ID_ARDRONE3_MEDIARECORD_CMD_VIDEOV2 = 3

# eARCOMMANDS_ARDRONE3_MEDIARECORDEVENT_CMD
ARCOMMANDS_ID_ARDRONE3_MEDIARECORDEVENT_CMD_PICTUREEVENTCHANGED = 0
ARCOMMANDS_ID_ARDRONE3_MEDIARECORDEVENT_CMD_VIDEOEVENTCHANGED = 1

ARCOMMANDS_ID_ARDRONE3_MEDIARECORDSTATE_CMD_PICTURESTATECHANGED = 0
ARCOMMANDS_ID_ARDRONE3_MEDIARECORDSTATE_CMD_VIDEOSTATECHANGED = 1
ARCOMMANDS_ID_ARDRONE3_MEDIARECORDSTATE_CMD_PICTURESTATECHANGEDV2 = 2
ARCOMMANDS_ID_ARDRONE3_MEDIARECORDSTATE_CMD_VIDEOSTATECHANGEDV2 = 3

# ARCOMMANDS_ID_ARDRONE3_MEDIASTREAMING_CMD
ARCOMMANDS_ID_ARDRONE3_MEDIASTREAMING_CMD_VIDEOENABLE = 0

# ARCOMMANDS_ID_ARDRONE3_MEDIASTREAMINGSTATE_CMD
ARCOMMANDS_ID_ARDRONE3_MEDIASTREAMINGSTATE_CMD_VIDEOENABLECHANGED = 0

# ARCOMMANDS_ID_ARDRONE3_NETWORK_CMD
ARCOMMANDS_ID_ARDRONE3_NETWORK_CMD_WIFISCAN = 0
ARCOMMANDS_ID_ARDRONE3_NETWORK_CMD_WIFIAUTHCHANNEL = 1

# ARCOMMANDS_ID_ARDRONE3_NETWORKSETTINGSSTATE
ARCOMMANDS_ID_ARDRONE3_NETWORKSETTINGSSTATE_CMD_WIFISELECTIONCHANGED = 0
ARCOMMANDS_ID_ARDRONE3_NETWORKSETTINGSSTATE_CMD_WIFISECURITYCHANGED = 1
ARCOMMANDS_ID_ARDRONE3_NETWORKSETTINGSSTATE_CMD_WIFISECURITY = 2

# ARCOMMANDS_ID_ARDRONE3_NETWORKSTATE_CMD
ARCOMMANDS_ID_ARDRONE3_NETWORKSTATE_CMD_WIFISCANLISTCHANGED = 0
ARCOMMANDS_ID_ARDRONE3_NETWORKSTATE_CMD_ALLWIFISCANCHANGED = 1
ARCOMMANDS_ID_ARDRONE3_NETWORKSTATE_CMD_WIFIAUTHCHANNELLISTCHANGED = 2
ARCOMMANDS_ID_ARDRONE3_NETWORKSTATE_CMD_ALLWIFIAUTHCHANNELCHANGED = 3

# ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGS_CMD
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGS_CMD_PICTUREFORMATSELECTION = 0
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGS_CMD_AUTOWHITEBALANCESELECTION = 1
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGS_CMD_EXPOSITIONSELECTION = 2
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGS_CMD_SATURATIONSELECTION = 3
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGS_CMD_TIMELAPSESELECTION = 4
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGS_CMD_VIDEOAUTORECORDSELECTION = 5
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGS_CMD_VIDEOSTABILIZATIONMODE = 6

# ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGSSTATE_CMD
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGSSTATE_CMD_PICTUREFORMATCHANGED = 0
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGSSTATE_CMD_AUTOWHITEBALANCECHANGED = 1
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGSSTATE_CMD_EXPOSITIONCHANGED = 2
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGSSTATE_CMD_SATURATIONCHANGED = 3
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGSSTATE_CMD_TIMELAPSECHANGED = 4
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGSSTATE_CMD_VIDEOAUTORECORDCHANGED = 5
ARCOMMANDS_ID_ARDRONE3_PICTURESETTINGSSTATE_CMD_VIDEOSTABILIZATIONMODECHANGED = 6

# eARCOMMANDS_ID_ARDRONE3_PILOTING_CMD
ARCOMMANDS_ID_ARDRONE3_PILOTING_CMD_FLATTRIM = 0
ARCOMMANDS_ID_ARDRONE3_PILOTING_CMD_TAKEOFF = 1
ARCOMMANDS_ID_ARDRONE3_PILOTING_CMD_PCMD = 2
ARCOMMANDS_ID_ARDRONE3_PILOTING_CMD_LANDING = 3
ARCOMMANDS_ID_ARDRONE3_PILOTING_CMD_EMERGENCY = 4
ARCOMMANDS_ID_ARDRONE3_PILOTING_CMD_NAVIGATEHOME = 5
ARCOMMANDS_ID_ARDRONE3_PILOTING_CMD_AUTOTAKEOFFMODE = 6
ARCOMMANDS_ID_ARDRONE3_PILOTING_CMD_MOVEBY = 7
ARCOMMANDS_ID_ARDRONE3_PILOTING_CMD_USERTAKEOFF = 8
ARCOMMANDS_ID_ARDRONE3_PILOTING_CMD_CIRCLE = 9

# eARCOMMANDS_ID_ARDRONE3_PILOTINGEVENT_CMD
ARCOMMANDS_ID_ARDRONE3_PILOTINGEVENT_CMD_MOVEBYEND = 0

# ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_MAXALTITUDE = 0
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_MAXTILT = 1
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_ABSOLUTCONTROL = 2
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_MAXDISTANCE = 3
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_NOFLYOVERMAXDISTANCE = 4
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_SETAUTONOMOUSFLIGHTMAXHORIZONTALSPEED = 5
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_SETAUTONOMOUSFLIGHTMAXVERTICALSPEED = 6
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_SETAUTONOMOUSFLIGHTMAXHORIZONTALACCELERATION = 7
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_SETAUTONOMOUSFLIGHTMAXVERTICALACCELERATION = 8
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_SETAUTONOMOUSFLIGHTMAXROTATIONSPEED = 9
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_BANKEDTURN = 10
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_MINALTITUDE = 11
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_CIRCLINGDIRECTION = 12
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_CIRCLINGRADIUS = 13
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_CIRCLINGALTITUDE = 14
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_PITCHMODE = 15
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGS_CMD_LANDINGMODE = 16

# ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_MAXALTITUDECHANGED = 0
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_MAXTILTCHANGED = 1
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_ABSOLUTCONTROLCHANGED = 2
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_MAXDISTANCECHANGED = 3
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_NOFLYOVERMAXDISTANCECHANGED = 4
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_AUTONOMOUSFLIGHTMAXHORIZONTALSPEED = 5
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_AUTONOMOUSFLIGHTMAXVERTICALSPEED = 6
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_AUTONOMOUSFLIGHTMAXHORIZONTALACCELERATION = 7
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_AUTONOMOUSFLIGHTMAXVERTICALACCELERATION = 8
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_AUTONOMOUSFLIGHTMAXROTATIONSPEED = 9
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_BANKEDTURNCHANGED = 10
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_MINALTITUDECHANGED = 11
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_CIRCLINGDIRECTIONCHANGED = 12
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_CIRCLINGRADIUSCHANGED = 13
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_CIRCLINGALTITUDECHANGED = 14
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_PITCHMODECHANGED = 15
ARCOMMANDS_ID_ARDRONE3_PILOTINGSETTINGSSTATE_CMD_LANDINGMODECHANGED = 16

# eARCOMMANDS_ID_ARDRONE3_PILOTINGSTATE_CMD
ARCOMMANDS_ID_ARDRONE3_PILOTINGSTATE_CMD_FLATTRIMCHANGED= 0
ARCOMMANDS_ID_ARDRONE3_PILOTINGSTATE_CMD_FLYINGSTATECHANGED= 1
ARCOMMANDS_ID_ARDRONE3_PILOTINGSTATE_CMD_ALERTSTATECHANGED= 2
ARCOMMANDS_ID_ARDRONE3_PILOTINGSTATE_CMD_NAVIGATEHOMESTATECHANGED= 3
ARCOMMANDS_ID_ARDRONE3_PILOTINGSTATE_CMD_POSITIONCHANGED= 4
ARCOMMANDS_ID_ARDRONE3_PILOTINGSTATE_CMD_SPEEDCHANGED = 5
ARCOMMANDS_ID_ARDRONE3_PILOTINGSTATE_CMD_ATTITUDECHANGED = 6
ARCOMMANDS_ID_ARDRONE3_PILOTINGSTATE_CMD_AUTOTAKEOFFMODECHANGED = 7
ARCOMMANDS_ID_ARDRONE3_PILOTINGSTATE_CMD_ALTITUDECHANGED = 8

# ARCOMMANDS_ID_ARDRONE3_PROSTATE_CMD
ARCOMMANDS_ID_ARDRONE3_PROSTATE_CMD_FEATURES = 0

# ARCOMMANDS_ID_ARDRONE3_SETTINGSSTATE_CMD
ARCOMMANDS_ID_ARDRONE3_SETTINGSSTATE_CMD_PRODUCTMOTORVERSIONLISTCHANGED = 0
ARCOMMANDS_ID_ARDRONE3_SETTINGSSTATE_CMD_PRODUCTGPSVERSIONCHANGED = 1
ARCOMMANDS_ID_ARDRONE3_SETTINGSSTATE_CMD_MOTORERRORSTATECHANGED = 2
ARCOMMANDS_ID_ARDRONE3_SETTINGSSTATE_CMD_MOTORSOFTWAREVERSIONCHANGED = 3
ARCOMMANDS_ID_ARDRONE3_SETTINGSSTATE_CMD_MOTORFLIGHTSSTATUSCHANGED = 4
ARCOMMANDS_ID_ARDRONE3_SETTINGSSTATE_CMD_MOTORERRORLASTERRORCHANGED = 5
ARCOMMANDS_ID_ARDRONE3_SETTINGSSTATE_CMD_P7ID = 6

# eARCOMMANDS_ID_ARDRONE3_SPEEDSETTINGS
ARCOMMANDS_ID_ARDRONE3_SPEEDSETTINGS_CMD_MAXVERTICALSPEED = 0
ARCOMMANDS_ID_ARDRONE3_SPEEDSETTINGS_CMD_MAXROTATIONSPEED = 1
ARCOMMANDS_ID_ARDRONE3_SPEEDSETTINGS_CMD_HULLPROTECTION = 2
ARCOMMANDS_ID_ARDRONE3_SPEEDSETTINGS_CMD_OUTDOOR = 3

# ARCOMMANDS_ID_ARDRONE3_SPEEDSETTINGSSTATE_CMD
ARCOMMANDS_ID_ARDRONE3_SPEEDSETTINGSSTATE_CMD_MAXVERTICALSPEEDCHANGED = 0
ARCOMMANDS_ID_ARDRONE3_SPEEDSETTINGSSTATE_CMD_MAXROTATIONSPEEDCHANGED = 1
ARCOMMANDS_ID_ARDRONE3_SPEEDSETTINGSSTATE_CMD_HULLPROTECTIONCHANGED = 2
ARCOMMANDS_ID_ARDRONE3_SPEEDSETTINGSSTATE_CMD_OUTDOORCHANGED = 3
ARCOMMANDS_ID_ARDRONE3_SPEEDSETTINGSSTATE_CMD_MAXPITCHROLLROTATIONSPEEDCHANGED = 4

# ARCOMMANDS_ID_COMMON_ACCESSORYSTATE_CMD
ARCOMMANDS_ID_COMMON_ACCESSORYSTATE_CMD_SUPPORTEDACCESSORIESLISTCHANGED = 0
ARCOMMANDS_ID_COMMON_ACCESSORYSTATE_CMD_ACCESSORYCONFIGCHANGED = 1
ARCOMMANDS_ID_COMMON_ACCESSORYSTATE_CMD_ACCESSORYCONFIGMODIFICATIONENABLED = 2

# ARCOMMANDS_ID_COMMON_ANIMATIONS_CMD
ARCOMMANDS_ID_COMMON_ANIMATIONS_CMD_STARTANIMATION = 0
ARCOMMANDS_ID_COMMON_ANIMATIONS_CMD_STOPANIMATION = 1
ARCOMMANDS_ID_COMMON_ANIMATIONS_CMD_STOPALLANIMATIONS = 2

# ARCOMMANDS_ID_COMMON_ANIMATIONSSTATE_CMD
ARCOMMANDS_ID_COMMON_ANIMATIONSSTATE_CMD_LIST = 0

# ARCOMMANDS_ID_COMMON_ARLIBSVERSIONSSTATE_CMD
ARCOMMANDS_ID_COMMON_ARLIBSVERSIONSSTATE_CMD_CONTROLLERLIBARCOMMANDSVERSION = 0
ARCOMMANDS_ID_COMMON_ARLIBSVERSIONSSTATE_CMD_SKYCONTROLLERLIBARCOMMANDSVERSION = 1
ARCOMMANDS_ID_COMMON_ARLIBSVERSIONSSTATE_CMD_DEVICELIBARCOMMANDSVERSION = 2

# ARCOMMANDS_ID_COMMON_CALIBRATION_CMD
ARCOMMANDS_ID_COMMON_CALIBRATION_CMD_MAGNETOCALIBRATION = 0

# ARCOMMANDS_ID_COMMON_CALIBRATIONSTATE_CMD
ARCOMMANDS_ID_COMMON_CALIBRATIONSTATE_CMD_MAGNETOCALIBRATIONSTATECHANGED = 0
ARCOMMANDS_ID_COMMON_CALIBRATIONSTATE_CMD_MAGNETOCALIBRATIONREQUIREDSTATE = 1
ARCOMMANDS_ID_COMMON_CALIBRATIONSTATE_CMD_MAGNETOCALIBRATIONAXISTOCALIBRATECHANGED = 2
ARCOMMANDS_ID_COMMON_CALIBRATIONSTATE_CMD_MAGNETOCALIBRATIONSTARTEDCHANGED = 3

# ARCOMMANDS_ID_COMMON_CAMERASETTINGSSTATE_CMD
ARCOMMANDS_ID_COMMON_CAMERASETTINGSSTATE_CMD_CAMERASETTINGSCHANGED = 0

# ARCOMMANDS_ID_COMMON_CHARGER_CMD
ARCOMMANDS_ID_COMMON_CHARGER_CMD_SETMAXCHARGERATE = 0

# ARCOMMANDS_ID_COMMON_CHARGERSTATE_CMD
ARCOMMANDS_ID_COMMON_CHARGERSTATE_CMD_MAXCHARGERATECHANGED = 0
ARCOMMANDS_ID_COMMON_CHARGERSTATE_CMD_CURRENTCHARGESTATECHANGED = 1
ARCOMMANDS_ID_COMMON_CHARGERSTATE_CMD_LASTCHARGERATECHANGED = 2
ARCOMMANDS_ID_COMMON_CHARGERSTATE_CMD_CHARGINGINFO = 3

# eARCOMMANDS_ID_COMMON_CLASS
ARCOMMANDS_ID_COMMON_CLASS_NETWORK = 0
ARCOMMANDS_ID_COMMON_CLASS_NETWORKEVENT = 1
ARCOMMANDS_ID_COMMON_CLASS_SETTINGS = 2
ARCOMMANDS_ID_COMMON_CLASS_SETTINGSSTATE = 3
ARCOMMANDS_ID_COMMON_CLASS_COMMON = 4
ARCOMMANDS_ID_COMMON_CLASS_COMMONSTATE = 5
ARCOMMANDS_ID_COMMON_CLASS_OVERHEAT = 6
ARCOMMANDS_ID_COMMON_CLASS_OVERHEATSTATE = 7
ARCOMMANDS_ID_COMMON_CLASS_CONTROLLERSTATE = 8
ARCOMMANDS_ID_COMMON_CLASS_WIFISETTINGS = 9
ARCOMMANDS_ID_COMMON_CLASS_WIFISETTINGSSTATE = 10
ARCOMMANDS_ID_COMMON_CLASS_MAVLINK = 11
ARCOMMANDS_ID_COMMON_CLASS_MAVLINKSTATE = 12
ARCOMMANDS_ID_COMMON_CLASS_CALIBRATION = 13
ARCOMMANDS_ID_COMMON_CLASS_CALIBRATIONSTATE = 14
ARCOMMANDS_ID_COMMON_CLASS_CAMERASETTINGSSTATE = 15
ARCOMMANDS_ID_COMMON_CLASS_GPS = 16
ARCOMMANDS_ID_COMMON_CLASS_FLIGHTPLANSTATE = 17
ARCOMMANDS_ID_COMMON_CLASS_FLIGHTPLANEVENT = 19
ARCOMMANDS_ID_COMMON_CLASS_ARLIBSVERSIONSSTATE = 18
ARCOMMANDS_ID_COMMON_CLASS_AUDIO = 20
ARCOMMANDS_ID_COMMON_CLASS_AUDIOSTATE = 21
ARCOMMANDS_ID_COMMON_CLASS_HEADLIGHTS = 22
ARCOMMANDS_ID_COMMON_CLASS_HEADLIGHTSSTATE = 23
ARCOMMANDS_ID_COMMON_CLASS_ANIMATIONS = 24
ARCOMMANDS_ID_COMMON_CLASS_ANIMATIONSSTATE = 25
ARCOMMANDS_ID_COMMON_CLASS_ACCESSORY = 26
ARCOMMANDS_ID_COMMON_CLASS_ACCESSORYSTATE = 27
ARCOMMANDS_ID_COMMON_CLASS_CHARGER = 28
ARCOMMANDS_ID_COMMON_CLASS_CHARGERSTATE = 29
ARCOMMANDS_ID_COMMON_CLASS_RUNSTATE = 30

# eARCOMMANDS_ID_COMMON_COMMON_CMD
ARCOMMANDS_ID_COMMON_COMMON_CMD_ALLSTATES = 0
ARCOMMANDS_ID_COMMON_COMMON_CMD_CURRENTDATE = 1
ARCOMMANDS_ID_COMMON_COMMON_CMD_CURRENTTIME = 2
ARCOMMANDS_ID_COMMON_COMMON_CMD_REBOOT = 3

# eARCOMMANDS_ID_COMMON_COMMONSTATE_CMD
ARCOMMANDS_ID_COMMON_COMMONSTATE_CMD_ALLSTATESCHANGED = 0
ARCOMMANDS_ID_COMMON_COMMONSTATE_CMD_BATTERYSTATECHANGED = 1
ARCOMMANDS_ID_COMMON_COMMONSTATE_CMD_MASSSTORAGESTATELISTCHANGED = 2
ARCOMMANDS_ID_COMMON_COMMONSTATE_CMD_MASSSTORAGEINFOSTATELISTCHANGED = 3
ARCOMMANDS_ID_COMMON_COMMONSTATE_CMD_CURRENTDATECHANGED = 4
ARCOMMANDS_ID_COMMON_COMMONSTATE_CMD_CURRENTTIMECHANGED = 5
ARCOMMANDS_ID_COMMON_COMMONSTATE_CMD_MASSSTORAGEINFOREMAININGLISTCHANGED = 6
ARCOMMANDS_ID_COMMON_COMMONSTATE_CMD_WIFISIGNALCHANGED = 7
ARCOMMANDS_ID_COMMON_COMMONSTATE_CMD_SENSORSSTATESLISTCHANGED = 8
ARCOMMANDS_ID_COMMON_COMMONSTATE_CMD_PRODUCTMODEL = 9
ARCOMMANDS_ID_COMMON_COMMONSTATE_CMD_COUNTRYLISTKNOWN = 10

# ARCOMMANDS_ID_COMMON_CONTROLLER_CMD
ARCOMMANDS_ID_COMMON_CONTROLLER_CMD_ISPILOTING = 0

# ARCOMMANDS_ID_COMMON_FLIGHTPLANEVENT_CMD
ARCOMMANDS_ID_COMMON_FLIGHTPLANEVENT_CMD_STARTINGERROREVENT = 0
ARCOMMANDS_ID_COMMON_FLIGHTPLANEVENT_CMD_SPEEDBRIDLEEVENT = 1

# ARCOMMANDS_ID_COMMON_FLIGHTPLANSTATE_CMD
ARCOMMANDS_ID_COMMON_FLIGHTPLANSTATE_CMD_AVAILABILITYSTATECHANGED = 0
ARCOMMANDS_ID_COMMON_FLIGHTPLANSTATE_CMD_COMPONENTSTATELISTCHANGED = 1

# ARCOMMANDS_ID_COMMON_GPS_CMD
ARCOMMANDS_ID_COMMON_GPS_CMD_CONTROLLERPOSITIONFORRUN = 0

# ARCOMMANDS_ID_COMMON_MAVLINK_CMD
ARCOMMANDS_ID_COMMON_MAVLINK_CMD_START = 0
ARCOMMANDS_ID_COMMON_MAVLINK_CMD_PAUSE = 1
ARCOMMANDS_ID_COMMON_MAVLINK_CMD_STOP = 2

# ARCOMMANDS_ID_COMMON_MAVLINKSTATE_CMD
ARCOMMANDS_ID_COMMON_MAVLINKSTATE_CMD_MAVLINKFILEPLAYINGSTATECHANGED = 0
ARCOMMANDS_ID_COMMON_MAVLINKSTATE_CMD_MAVLINKPLAYERRORSTATECHANGED = 1

# ARCOMMANDS_ID_COMMON_NETWORK_CMD
ARCOMMANDS_ID_COMMON_NETWORK_CMD_DISCONNECT = 0

# ARCOMMANDS_ID_COMMON_NETWORKEVENT_CMD
ARCOMMANDS_ID_COMMON_NETWORKEVENT_CMD_DISCONNECTION = 0

# ARCOMMANDS_ID_COMMON_OVERHEAT_CMD
ARCOMMANDS_ID_COMMON_OVERHEAT_CMD_SWITCHOFF = 0
ARCOMMANDS_ID_COMMON_OVERHEAT_CMD_VENTILATE = 1

# ARCOMMANDS_ID_COMMON_OVERHEATSTATE_CMD
ARCOMMANDS_ID_COMMON_OVERHEATSTATE_CMD_OVERHEATCHANGED = 0
ARCOMMANDS_ID_COMMON_OVERHEATSTATE_CMD_OVERHEATREGULATIONCHANGED = 1

# ARCOMMANDS_ID_COMMON_RUNSTATE_CMD
ARCOMMANDS_ID_COMMON_RUNSTATE_CMD_RUNIDCHANGED = 0

# ARCOMMANDS_ID_COMMON_SETTINGS_CMD
ARCOMMANDS_ID_COMMON_SETTINGS_CMD_ALLSETTINGS = 0
ARCOMMANDS_ID_COMMON_SETTINGS_CMD_RESET = 1
ARCOMMANDS_ID_COMMON_SETTINGS_CMD_PRODUCTNAME = 2
ARCOMMANDS_ID_COMMON_SETTINGS_CMD_COUNTRY = 3
ARCOMMANDS_ID_COMMON_SETTINGS_CMD_AUTOCOUNTRY = 4

# ARCOMMANDS_ID_COMMON_SETTINGSSTATE_CMD
ARCOMMANDS_ID_COMMON_SETTINGSSTATE_CMD_ALLSETTINGSCHANGED = 0
ARCOMMANDS_ID_COMMON_SETTINGSSTATE_CMD_RESETCHANGED = 1
ARCOMMANDS_ID_COMMON_SETTINGSSTATE_CMD_PRODUCTNAMECHANGED = 2
ARCOMMANDS_ID_COMMON_SETTINGSSTATE_CMD_PRODUCTVERSIONCHANGED = 3
ARCOMMANDS_ID_COMMON_SETTINGSSTATE_CMD_PRODUCTSERIALHIGHCHANGED = 4
ARCOMMANDS_ID_COMMON_SETTINGSSTATE_CMD_PRODUCTSERIALLOWCHANGED = 5
ARCOMMANDS_ID_COMMON_SETTINGSSTATE_CMD_COUNTRYCHANGED = 6
ARCOMMANDS_ID_COMMON_SETTINGSSTATE_CMD_AUTOCOUNTRYCHANGED = 7

# ARCOMMANDS_ID_COMMON_WIFISETTINGS_CMD
ARCOMMANDS_ID_COMMON_WIFISETTINGS_CMD_OUTDOORSETTING = 0

# ARCOMMANDS_ID_COMMON_WIFISETTINGSSTATE_CMD
ARCOMMANDS_ID_COMMON_WIFISETTINGSSTATE_CMD_OUTDOORSETTINGSCHANGED = 0

# ARCOMMANDS_ID_COMMONDEBUG_DEBUGSETTINGS_CMD
ARCOMMANDS_ID_COMMONDEBUG_DEBUGSETTINGS_CMD_GETALL = 0
ARCOMMANDS_ID_COMMONDEBUG_DEBUGSETTINGS_CMD_SET = 1

# ARCOMMANDS_ID_COMMONDEBUG_DEBUGSETTINGSSTATE_CMD
ARCOMMANDS_ID_COMMONDEBUG_DEBUGSETTINGSSTATE_CMD_INFO = 0
ARCOMMANDS_ID_COMMONDEBUG_DEBUGSETTINGSSTATE_CMD_LISTCHANGED = 1

# ARCOMMANDS_ID_COMMONDEBUG_STATS_CMD
ARCOMMANDS_ID_COMMONDEBUG_STATS_CMD_SENDPACKET = 0
ARCOMMANDS_ID_COMMONDEBUG_STATS_CMD_STARTSENDINGPACKETFROMDRONE = 1
ARCOMMANDS_ID_COMMONDEBUG_STATS_CMD_STOPSENDINGPACKETFROMDRONE = 2

# ARCOMMANDS_ID_COMMONDEBUG_STATSEVENT_CMD
ARCOMMANDS_ID_COMMONDEBUG_STATSEVENT_CMD_SENDPACKET = 0

# ARCOMMANDS_ID_PRO_PRO_CMD
ARCOMMANDS_ID_PRO_PRO_CMD_BOUGHTFEATURES = 0
ARCOMMANDS_ID_PRO_PRO_CMD_RESPONSE = 1
ARCOMMANDS_ID_PRO_PRO_CMD_ACTIVATEFEATURES = 2

# ARCOMMANDS_ID_PRO_PROEVENT_CMD
ARCOMMANDS_ID_PRO_PROEVENT_CMD_CHALLENGEEVENT = 0

# ARCOMMANDS_ID_PRO_PROSTATE_CMD
ARCOMMANDS_ID_PRO_PROSTATE_CMD_SUPPORTEDFEATURES = 0
ARCOMMANDS_ID_PRO_PROSTATE_CMD_FEATURESACTIVATED = 1

# eARCOMMANDS_ID_PROJECT
ARCOMMANDS_ID_PROJECT_COMMON = 0
ARCOMMANDS_ID_PROJECT_ARDRONE3 = 1

# ARCOMMANDS_ID_WIFI_CMD
ARCOMMANDS_ID_WIFI_CMD_SCAN = 1
ARCOMMANDS_ID_WIFI_CMD_UPDATE_AUTHORIZED_CHANNELS = 3
ARCOMMANDS_ID_WIFI_CMD_SET_AP_CHANNEL = 5
ARCOMMANDS_ID_WIFI_CMD_SET_SECURITY = 7
ARCOMMANDS_ID_WIFI_CMD_SET_COUNTRY = 9
ARCOMMANDS_ID_WIFI_CMD_SET_ENVIRONEMENT = 11
ARCOMMANDS_ID_WIFI_CMD_SCANNED_ITEM = 2
ARCOMMANDS_ID_WIFI_CMD_AUTHORIZED_CHANNEL = 4
ARCOMMANDS_ID_WIFI_CMD_AP_CHANNEL_CHANGED = 6
ARCOMMANDS_ID_WIFI_CMD_SECURITY_CHANGED = 8
ARCOMMANDS_ID_WIFI_CMD_COUNTRY_CHANGED = 10
ARCOMMANDS_ID_WIFI_CMD_ENVIRONEMENT_CHANGED = 12
ARCOMMANDS_ID_WIFI_CMD_RSSI_CHANGED = 13

# eARMEDIA_ENCAPSULER_FRAME_TYPE;
ARMEDIA_ENCAPSULER_FRAME_TYPE_UNKNNOWN = 0
ARMEDIA_ENCAPSULER_FRAME_TYPE_I_FRAME = 1
ARMEDIA_ENCAPSULER_FRAME_TYPE_P_FRAME = 2
ARMEDIA_ENCAPSULER_FRAME_TYPE_JPEG = 3
ARMEDIA_ENCAPSULER_FRAME_TYPE_MAX = 4

# eARNETWORK_MANAGER_INTERNAL_BUFFER_ID
ARNETWORK_MANAGER_INTERNAL_BUFFER_ID_PING = 0
ARNETWORK_MANAGER_INTERNAL_BUFFER_ID_PONG = 1
ARNETWORK_MANAGER_INTERNAL_BUFFER_ID_MAX = 3

# eARNETWORKAL_FRAME_TYPE
ARNETWORKAL_FRAME_TYPE_UNINITIALIZED = 0
ARNETWORKAL_FRAME_TYPE_ACK = 1
ARNETWORKAL_FRAME_TYPE_DATA = 2
ARNETWORKAL_FRAME_TYPE_DATA_LOW_LATENCY = 3
ARNETWORKAL_FRAME_TYPE_DATA_WITH_ACK = 4
ARNETWORKAL_FRAME_TYPE_MAX = 5


_struct_fmt_for_type = {
    'u8'     : 'B',  # Hex length: 1
    'i8'     : 'b',  # Hex length: 1
    'u16'    : 'H',  # Hex length: 2
    'i16'    : 'h',  # Hex length: 2
    'u32'    : 'I',  # Hex length: 4
    'i32'    : 'i',  # Hex length: 4
    'u64'    : 'Q',  # Hex length: 8
    'i64'    : 'q',  # Hex length: 8
    'float'  : 'f',  # Hex length: 4
    'double' : 'd',  # Hex length: 8
    'string' : 's',  # Hex length: 2
    'enum'   : 'i',  # Hex length: 4
}