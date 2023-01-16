

import requests
import json
import time

valve_controller_ip = "http://192.168.1.118"
valve_controller_port = 80
allOffState = "0000000000000000"

def setValveState(valveIndex: int, setState: int) :
    currentState = [c for c in getRelayState()]
    currentState[valveIndex] = str(setState)
    newState = "".join(currentState)
    setRelayState(newState)
    

def getStatus() :
    response = requests.get("http://192.168.1.118:80/status")
    print("RAW RESPONSE")
    print(response.text) 
    json_data = json.loads(response.text)
    return json_data

def getRelayState() -> str:
    return getStatus()["relayState"]

def setRelayState(relayState: str) :
    relayState = {
        "relayState" : relayState
    }
    requests.post("http://192.168.1.118:80/relaySettings", params=relayState)


def testHolisticRelayState() :
    print("================================")
    print("Get initial relay state:")
    print(getRelayState())
    print("")
    print("================================")
    print("")
    print("Setting Relay State to: 0001001101111111")
    print("Verify Match with response below:")
    setRelayState("0001001101111111")
    time.sleep(1)
    print(getRelayState())
    print("")
    print("================================")
    print("")
    print("Reset Relay State to: 0000000000000000")
    print("Verify Match with response below:")
    setRelayState("0000000000000000")
    time.sleep(1)
    print(getRelayState())
    print("")

def testUpdateSingleState() :
    setValveState(0, 1)
    print(getRelayState())
    setValveState(12, 1)
    print(getRelayState())
    setValveState(0, 0)
    setValveState(12, 0)
    print(getRelayState())



	
