#SMART HOME DEVICE CONTROL SYSTEM EXAMPLE

class Device:
    def control(self):
        print("Controlling device manually.")

class VoiceControl(Device):
    def control(self):
       print("Controlling device via voice assistant.")

class MobileAppControl(Device):
    def control(self):
       print("Controlling device via mobile app.")

class HybridSmartDevice(MobileAppControl, VoiceControl):
    pass

my_device = HybridSmartDevice()
my_device.control()
print("MRO:", [cls.__name__ for cls in HybridSmartDevice.__mro__])
