Build: pio run -e ulanzi
Flash: pio run -e ulanzi --target upload OR 
cp docs/ulanzi_flasher/firmware/boot_app0.bin .pio/build/ulanzi/ && \
cd .pio/build/ulanzi && \
esptool -p /dev/tty.usbserial-210 -b 230400 erase-flash && \
esptool.py --chip esp32 --port /dev/tty.usbserial-210 --baud 230400 write_flash \
   0x1000 bootloader.bin \
   0x8000 partitions.bin \
   0xe000 boot_app0.bin \
   0x10000 firmware.bin