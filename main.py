import os
from signatures import FILE_SIGNATURES

def carve_files(disk_image_path):
    if not os.path.exists('output'):
        os.makedirs('output')

    try:
        with open(disk_image_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"[-] Error: The file '{disk_image_path}' was not found.")
        return

    print(f"[*] Analyzing {len(data)} bytes of binary data...")

    file_count = 0
    recovery_log = []

    for file_type, sigs in FILE_SIGNATURES.items():
        header = sigs['header']
        footer = sigs['footer']
        
        start_pos = 0

        while True:
            start_pos = data.find(header, start_pos)
            if start_pos == -1:
                break
            end_pos = data.find(footer, start_pos)
            
            if end_pos != -1:
                end_pos += len(footer)
                carved_data = data[start_pos:end_pos]
                
                if len(carved_data) > 500:
                    file_name = f"output/recovered_{file_count}.{file_type}"
                    
                    with open(file_name, 'wb') as out_f:
                        out_f.write(carved_data)
                    
                    log_entry = f"Type: {file_type.upper()}, Offset: {start_pos}, Size: {len(carved_data)} bytes"
                    print(f"[+] {log_entry}")
                    recovery_log.append(log_entry)
                    file_count += 1

                start_pos = end_pos
            else:
                start_pos += len(header)

    manifest_path = "output/manifest.txt"
    with open(manifest_path, 'w') as m:
        m.write("FORENSIC FILE CARVING REPORT\n")
        m.write("=" * 30 + "\n")
        m.write(f"Source Image: {disk_image_path}\n")
        m.write(f"Total Files Recovered: {file_count}\n\n")
        m.write("Recovery Details:\n")
        for entry in recovery_log:
            m.write(f"- {entry}\n")
    
    print(f"\n[*] Scan Complete. {file_count} files recovered.")
    print(f"[*] Forensic Manifest saved to: {manifest_path}")

if __name__ == "__main__":
    print("--- Forensic File Carver Utility ---")
    image_input = input("Enter the path to the binary file (e.g., test_disk.bin): ")

    carve_files(image_input)

