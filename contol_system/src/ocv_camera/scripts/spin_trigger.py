import PySpin

class SpinCameraTrigger:
    # Initilizes camera pointer with first spinnaker device availible
    def __init__(self):
        self.isStreaming = False
        try:
            self.system = PySpin.System.GetInstance()
            self.cameraList = self.system.GetCameras()
            if(len(self.cameraList) == 0):
                print("No cameras found!")
                raise Exception()
            else:
                self.camera = self.cameraList[0]
        
        except PySpin.SpinnakerException as se:
            print("Spinnaker exception during enumeration")

    def setupCamTrigger(self):
        # Sets up camera with software trigger
        nodeMapTLDevice = self.camera.GetTLDeviceNodeMap()
        camp.Init()

        nodemap = cam.GetNodeMap()


    def setupTrigger(self):
        

