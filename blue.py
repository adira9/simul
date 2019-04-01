from bluetooth import *
print("performing inquiry...")

nearby_devices = discover_devices(duration=4,lookup_names=True, flush_cache=True, lookup_class=False)
print("found %d devices" % len(nearby_devices))

for name, addr in nearby_devices:
    print(" %s - %s" % (addr, name))



