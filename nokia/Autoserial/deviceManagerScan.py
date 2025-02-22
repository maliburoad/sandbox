from infi.devicemanager import DeviceManager
dm = DeviceManager()
dm.root.rescan()
devices = dm.all_devices
for device in devices:
#    print(device)
    device=str(device)
    if "Enhanced" in device:
        #print(device)
        print(device[-6:-2])