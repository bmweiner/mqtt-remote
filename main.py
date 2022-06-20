import os
os.environ['PYUSB_DEBUG'] = 'debug'


import usb.core
import usb.util


# flirc device
dev = usb.core.find(idVendor=0x20a0, idProduct=0x0006)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# claim ownership of device
for cfg in dev:
  for intf in cfg:
    print(dev.is_kernel_driver_active(intf.bInterfaceNumber))
    #   try:
    #     dev.detach_kernel_driver(intf.bInterfaceNumber)

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()