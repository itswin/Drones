#!/usr/bin/python
"""
  Parsing of incomming messages from Parrot Bebop
  usage:
       ./navdata.py <logged file>
"""
import sys
import struct
import binascii

ARNETWORKAL_FRAME_TYPE_ACK = 0x1
ARNETWORKAL_FRAME_TYPE_DATA = 0x2
ARNETWORKAL_FRAME_TYPE_DATA_LOW_LATENCY = 0x3
ARNETWORKAL_FRAME_TYPE_DATA_WITH_ACK = 0x4

ARNETWORK_MANAGER_INTERNAL_BUFFER_ID_PING = 0
ARNETWORK_MANAGER_INTERNAL_BUFFER_ID_PONG = 1

POSITION_TIME_DELTA = 0.2  # estimated to 5Hz


def printHex(data):
    print(" ".join(["%02X" % ord(x) for x in data]))


def parseFrameType(data):
    if len(data) < 7:
        return None
    frameType, frameId, frameSeq, frameSize = struct.unpack("<BBBI", data[:7])
    assert len(data) == frameSize, (len(data), frameSize)
    return frameType


def cutPacket(data):
    if len(data) < 7:
        return None, data
    frameType, frameId, frameSeq, frameSize = struct.unpack("<BBBI", data[:7])
    return data[:frameSize], data[frameSize:]


def structFmt(args, typeFmts, fmtHexLengths, frameSize):
    fmt = "<"
    hexLength = 0
    enums = []

    if type(args) is list:
        for arg in args:
            fmt += typeFmts[arg["type"]]
            if not arg["type"] == "string":
                hexLength += fmtHexLengths[arg["type"]]
            if arg["type"] == "enum":
                enums.append(arg["enum"])
    else:
        fmt += typeFmts[args["type"]]
        if not args["type"] == "string":
            hexLength += fmtHexLengths[args["type"]]
        if args["type"] == "enum":
            enums.append(args["enum"])

    if 's' in fmt:
        index = fmt.index('s')
        stringLength = (frameSize - hexLength - 11) / 2
        fmt = fmt[:index] + str(stringLength) + fmt[index:]

    return fmt, enums

def parse(robot, commandProject, commandClass, commandId, frameSize, cmd, data):
    commandId = int(cmd["id"])
    commandName = cmd["name"]
    fmt = ""
    enums = []
    output = ()

    if "arg" in cmd:
        args = cmd["arg"]
        fmt, enums = structFmt(args, robot.typeFmts, robot.fmtHexLengths, frameSize)

    try:
        output = struct.unpack(fmt, data[11:frameSize])
    except:
        try:
            output = struct.unpack(fmt, data[11:frameSize - 1])
        except:
            pass

    if len(enums) > 0:
        newOutput = ()
        for index in xrange(len(enums)):
            try:
                newOutput.append(enums[index][output[index]]["name"])
            except:
                pass
        output = newOutput

    if not output == ():
        print commandName, output
    else:
        print commandName

def parseData(data, robot, verbose=False):
    # m:\git\ARDroneSDK3\libARNetworkAL\Includes\libARNetworkAL\ARNETWORKAL_Frame.h
    #   uint8_t type; /**< frame type eARNETWORK_FRAME_TYPE */
    #   uint8_t id; /**< identifier of the buffer sending the frame */
    #   uint8_t seq; /**< sequence number of the frame */
    #   uint32_t size; /**< size of the frame */
    #   uint8_t *dataPtr; /**< pointer on the data of the frame */
    #
    assert len(data) >= 7, len(data)
    frameType, frameId, frameSeq, frameSize = struct.unpack("<BBBI", data[:7])
    assert frameType in [0x1, 0x2, 0x3, 0x4], frameType  # 0x2 = ARNETWORKAL_FRAME_TYPE_DATA,
    # 0x4 = ARNETWORKAL_FRAME_TYPE_DATA_WITH_ACK
    if frameType == ARNETWORKAL_FRAME_TYPE_ACK:
        assert frameSize == 8, frameSize
        assert frameId == 0x8B, hex(frameId)
        if verbose:
            print("ACKACK", ord(data[frameSize - 1]))
        data = data[frameSize:]
        return data

    if frameType == ARNETWORKAL_FRAME_TYPE_DATA_LOW_LATENCY:  # 0x3
        assert frameSize >= 12, frameSize
        assert frameId == 0x7D, hex(frameId)
        frameNumber, frameFlags, fragmentNumber, fragmentsPerFrame = struct.unpack("<HBBB", data[7:12])
        # print("Video", frameNumber, frameFlags, fragmentNumber,fragmentsPerFrame)
        # printHex( data[:20] )
        data = data[frameSize:]
        return data

    assert frameId in [0x7F, 0x0, 0x7E], frameId

    if frameId == 0x7F:
        # Navdata
        commandProject, commandClass, commandId = struct.unpack("BBH", data[7:7 + 4])
        verbose = False
        if commandProject == 0:
            if (commandClass, commandId) == (5, 7):
                # ARCOMMANDS_ID_PROJECT_COMMON = 0,
                # ARCOMMANDS_ID_COMMON_CLASS_COMMONSTATE = 5,
                # ARCOMMANDS_ID_COMMON_COMMONSTATE_CMD_WIFISIGNALCHANGED = 7,
                rssi = struct.unpack("h", data[7:7 + 2])[
                    0]  # RSSI of the signal between controller and the product (in dbm)
                if verbose:
                    print("Wifi", rssi)
            else:
                printHex(data[:frameSize])
        elif commandProject == 1:
            if commandClass == 4:
                if commandId == 4:
                    lat, lon, alt = struct.unpack("ddd", data[11:11 + 3 * 8])
                    robot.positionGPS = (lat, lon, alt)
                    if verbose:
                        print("Position", lat, lon, alt)
                elif commandId == 4:
                    speedX, speedY, speedZ = struct.unpack("fff", data[11:11 + 3 * 4])
                    robot.speed = (speedX, speedY, speedZ)
                    robot.position = robot.position[0] + POSITION_TIME_DELTA * speedX, robot.position[
                        1] + POSITION_TIME_DELTA * speedY, robot.position[2] + POSITION_TIME_DELTA * speedZ
                    if verbose:
                        print("Speed", speedX, speedY, speedZ)
                elif commandId == 6:
                    roll, pitch, yaw = struct.unpack("fff", data[11:11 + 3 * 4])
                    if verbose:
                        print("Angle", roll, pitch, yaw)
                elif commandId == 8:
                    robot.altitude = struct.unpack("d", data[11:11 + 8])[0]
                    if verbose:
                        print("Altitude", robot.altitude)
            elif (commandClass, commandId) == (25, 0):
                tilt, pan = struct.unpack("BB", data[11:11 + 2])
                if verbose:
                    print("CameraState Tilt/Pan", tilt, pan)
            else:
                if verbose:
                    print("UNKNOWN",)
                    printHex(data[:frameSize])
                    assert False
        else:
            print("UNKNOWN Project", commandProject)
    elif frameId == 0x7E:
        verbose = True
        commandProject, commandClass, commandId = struct.unpack("BBH", data[7:7 + 4])
        # Events
        # Exceptions
        if (commandProject, commandClass, commandId) == (0,5,4):
            if verbose:
                print("Date:", data[11:frameSize-1])
        elif (commandProject, commandClass, commandId) == (0,5,5):
            if verbose:
                print("Time:", data[11:frameSize-1])
        elif (commandProject, commandClass, commandId) == (0,18,2):
            if verbose:
                print("DeviceLibARCommandsVersion", data[11:frameSize])
        else:
            for project in robot.constants:
                if int(project["id"]) == commandProject:
                    projectName = project["name"]
                    for cl in project["class"]:
                        if int(cl["id"]) == commandClass:
                            className = cl["name"]
                            for cmd in cl["cmd"]:
                                if type(cmd) is dict:
                                    if int(cmd["id"]) == commandId:
                                        if "$t" in cmd:
                                            try:
                                                if cmd["$t"].index("deprecated") > 0:
                                                    break
                                            except ValueError:
                                                parse(robot, commandProject, commandClass, commandId, frameSize, cmd, data)
                                        else:
                                            parse(robot, commandProject, commandClass, commandId, frameSize, cmd, data)
                                        break
                            break
                    break

    elif frameId == 0x0:  # ARNETWORK_MANAGER_INTERNAL_BUFFER_ID_PING
        assert frameSize == 15, len(data)
        seconds, nanoseconds = struct.unpack("<II", data[7:15])
        assert nanoseconds < 1000000000, nanoseconds
        timestamp = seconds + nanoseconds / 1000000000.
        robot.time = timestamp
        if verbose:
            print("Time", timestamp)
    data = data[frameSize:]
    return data


def ackRequired(data):
    return parseFrameType(data) == ARNETWORKAL_FRAME_TYPE_DATA_WITH_ACK


def createAckPacket(data):
    assert len(data) >= 7, len(data)
    frameType, frameId, frameSeq, frameSize = struct.unpack("<BBBI", data[:7])
    assert frameType == 0x4, frameType
    assert len(data) == frameSize, (len(data), frameSize)

    # get the acknowledge sequence number from the data
    #    payload = data[7:8] # strange
    payload = struct.pack("B", frameSeq)
    #    payload = struct.pack("B", 1)
    #    print("ACK", repr(payload))

    frameType = ARNETWORKAL_FRAME_TYPE_ACK
    frameId = 0xFE  # 0x7E + 0x80
    buf = struct.pack("<BBBI", frameType, frameId, 0, len(payload) + 7)
    return buf + payload


def pongRequired(data):
    if len(data) < 7:
        return False
    frameType, frameId, frameSeq, frameSize = struct.unpack("<BBBI", data[:7])
    return frameId == ARNETWORK_MANAGER_INTERNAL_BUFFER_ID_PING


def createPongPacket(data):
    assert len(data) >= 7, len(data)
    frameType, frameId, frameSeq, frameSize = struct.unpack("<BBBI", data[:7])
    assert frameType == 0x2, frameType
    assert frameId == ARNETWORK_MANAGER_INTERNAL_BUFFER_ID_PING, frameId
    assert len(data) == frameSize, (len(data), frameSize)

    payload = data[7:]
    frameType = 2
    frameId = ARNETWORK_MANAGER_INTERNAL_BUFFER_ID_PONG
    buf = struct.pack("<BBBI", frameType, frameId, 0, len(payload) + 7)
    return buf + payload


def videoAckRequired(data):
    if len(data) < 7:
        return False
    frameType, frameId, frameSeq, frameSize = struct.unpack("<BBBI", data[:7])
    return frameType == ARNETWORKAL_FRAME_TYPE_DATA_LOW_LATENCY and frameId == 0x7D


g_currentVideoFrameNumber = None
g_lowPacketsAck = 0
g_highPacketsAck = 0


def createVideoAckPacket(data):
    global g_currentVideoFrameNumber, g_lowPacketsAck, g_highPacketsAck

    assert len(data) >= 12, len(data)
    frameNumber, frameFlags, fragmentNumber, fragmentsPerFrame = struct.unpack("<HBBB", data[7:12])

    if frameNumber != g_currentVideoFrameNumber:
        g_lowPacketsAck = 0
        g_highPacketsAck = 0
        g_currentVideoFrameNumber = frameNumber

    if fragmentNumber < 64:
        g_lowPacketsAck |= (1 << fragmentNumber)
    else:
        g_highPacketsAck |= (1 << (fragmentNumber - 64))

    payload = struct.pack("<HQQ", frameNumber, g_highPacketsAck, g_lowPacketsAck)
    frameType = 2
    frameId = 13
    buf = struct.pack("<BBBI", frameType, frameId, 0, len(payload) + 7)
    return buf + payload


class DummyRobot:
    position = (0, 0, 0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    robot = DummyRobot()
    data = open(sys.argv[1], "rb").read()
    while data:
        data = parseData(data, robot, verbose=True)

# vim: expandtab sw=4 ts=4

