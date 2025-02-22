import serial
import time
import sys
from infi.devicemanager import DeviceManager

dm = DeviceManager()
dm.root.rescan()
devices = dm.all_devices

device_found = False

for device in devices:
    device=str(device)
    if "Enhanced" in device:
        print("Found one device:")
        print(device)
        port = device[-6:-2]
        device_found = True

if device_found == False:
    print("No COM port founded")
    Goodbye = input("Press any button and say Goodbye")
    sys.exit()

if __name__ == "__main__":
    timeout = 0 #set 0 for infinity
    login_prompt="made2 login:"
    password_prompt="Password: "
    shell_prompt = "[rfsw@made2 DFE0] /home/rfsw$"
    login = 'rfsw'
    password = '0q/7SXKjF2AlAba+yisrCxQiKz1PRJJ0IVDZuh/sOaA='
    command_to_execute = 'sudo lmi-eth on'
    uboot_prompt = 'SOCSW_BOOTROM_v2.0.6 #'
    uboot_boot_command = 'boot'
    #port = "COM4"
    baudrate = 115200

    done = False
    success_prompt = command_to_execute
    endl = '\n'
    con = serial.Serial(port, baudrate, timeout=1)
    starttime = time.time()
    print("Serial in use: " + port)
    while True:
        if timeout!=0 and time.time() - timeout > starttime:
            print("Error - timeout")
            break
        ret = con.read_all()
        if ret:
            #print(['debugbytes', ret])
            pass
        ret = ret.decode(errors='replace')
        if ret:
            print(ret)
        if login_prompt in ret:
            time.sleep(15)
            done = False
            message = login
        elif password_prompt in ret:
            done = False
            message = password
        elif success_prompt in ret:
            done = True            
            message = command_to_execute
            if timeout!=0:
                break
        elif shell_prompt in ret:
            #time.sleep(60) #for AHEGHA
            message = command_to_execute
        elif uboot_prompt in ret:
            done = False
            message = uboot_boot_command
        else:
            message = ''
        if not done:
            con.write(f'{message}{endl}'.encode())
        time.sleep(1)
    con.close()
