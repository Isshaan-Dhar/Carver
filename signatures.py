FILE_SIGNATURES = {
    'jpeg': {
        'header': b'\xff\xd8\xff\xe0',
        'footer': b'\xff\xd9'
    },
    'pdf': {
        'header': b'\x25\x50\x44\x46',
        'footer': b'\x25\x25\x45\x4f\x46'
    }

}
