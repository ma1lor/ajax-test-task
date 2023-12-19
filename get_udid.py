import subprocess

def get_device_udid():
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True)

        output = result.stdout

        lines = output.strip().split('\n')[1:] 
        devices = [line.split('\t')[0] for line in lines if line.strip()] 

        if devices:
            return devices[0] 
        else:
            print("No devices found.")
            return None

    except:
        print('ERROR.')


udid = get_device_udid()
if udid:
    print(f"UDID: {udid}")
else:
    print('error')