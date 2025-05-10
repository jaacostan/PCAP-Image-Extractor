import dpkt
import re
def extract_images_chunked(pcap_file, output_folder, boundary=b"--BoundaryString"): #Edit the boundary string
    image_count = 0
    full_http_data = b""
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for _, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            tcp = ip.data
            if isinstance(tcp, dpkt.tcp.TCP) and tcp.data:
                full_http_data += tcp.data  # Store full stream data
    # Remove chunked encoding metadata
    full_http_data = re.sub(rb"\r\n[0-9a-fA-F]+\r\n", b"", full_http_data)  
    # Split by boundaries
    parts = full_http_data.split(boundary)
    for part in parts:
        if b"Content-type: image/jpeg" in part or b"Content-type: image/png" in part:
            header_end = part.find(b"\r\n\r\n") + 4
            img_binary = part[header_end:]
            # Ensure valid JPEG/PNG data
            if img_binary.startswith(b"\xff\xd8"):  # JPEG Start Marker
                filename = f"{output_folder}/image_{image_count}.jpg"
                with open(filename, "wb") as img_file:
                    img_file.write(img_binary)
                print(f"Saved: {filename}")
                image_count += 1
    print(f"Extracted {image_count} images!")
# Usage Example
extract_images_chunked("capture.pcap", "output_folder")
