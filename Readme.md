This tool can be used to extract images from a PCAP file, where boundary marker is set. This tool will identify the boundary marker using the user input and combine the raw data to extract the images.

A boundary marker is a delimiter used in multipart data transmissions, particularly in HTTP responses, to separate individual sections within a stream. This technique is commonly used in MJPEG video feeds, live image transmissions, and multi-part file uploads where multiple objects need to be sent over a single HTTP connection. 
The boundary marker is explicitly defined in the HTTP headers and serves as a way to identify the start and end of each transmitted object within the stream.
To identify a boundary marker,look for Content-Type: multipart/x-mixed-replace in the HTTP headers. This indicates that the response contains multiple segments, each separated by a predefined boundary. Within the headers, you will typically see an entry like boundary=BoundaryString, where "BoundaryString" is the separator between individual content parts. When analysing the TCP stream, these boundary markers will appear before each image or file segment, commonly formatted as --BoundaryString, followed by metadata such as Content-Type: image/jpeg.

To extract data from a .pcap file, use the python script. Make sure the boundary string matches with yours. After running the script using capture.pcap, it will put the extracted images in the output_folder. Also dpkt module is needed. Install using pip then.
Edit the filename and output directory according to you needs. 

Dependencies.

pip install dpkt
