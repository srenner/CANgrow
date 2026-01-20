from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import os
from datetime import datetime

SNAPSHOT_DIR = "snapshots"
os.makedirs(SNAPSHOT_DIR, exist_ok=True)

def capture_snapshot_bytes():
    """Capture snapshot directly from camera"""
    cmd = [
        'rpicam-still',
        '-n',  # No preview
        '-t', '100',  # 100ms timeout
        '--width', '1920',
        '--height', '1080',
        '--quality', '95',
        '-o', '-'  # Output to stdout
    ]
    
    result = subprocess.run(cmd, capture_output=True, timeout=10)
    return result.stdout

class SnapshotHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path in ['/snapshot.jpg', '/cgi-bin/snapshot.cgi', '/']:
            try:
                img_bytes = capture_snapshot_bytes()
                
                self.send_response(200)
                self.send_header('Content-type', 'image/jpeg')
                self.send_header('Content-Length', len(img_bytes))
                self.end_headers()
                self.wfile.write(img_bytes)
            except Exception as e:
                self.send_error(500, str(e))
        else:
            self.send_error(404)
    
    def do_POST(self):
        if self.path.startswith('/save'):
            try:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filepath = os.path.join(SNAPSHOT_DIR, f"snapshot_{timestamp}.jpg")
                
                subprocess.run([
                    'rpicam-still',
                    '-n',
                    '-t', '100',
                    '--width', '1920',
                    '--height', '1080',
                    '--quality', '95',
                    '-o', filepath
                ], timeout=10, check=True)
                
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f"Saved: {filepath}".encode())
            except Exception as e:
                self.send_error(500, str(e))
        else:
            self.send_error(404)
    
    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")

if __name__ == '__main__':
    PORT = 8080
    server = HTTPServer(('0.0.0.0', PORT), SnapshotHandler)
    print(f"Snapshot-only server running on port {PORT}")
    print(f"Resolution: 1920x1080, Quality: 95%")
    print(f"\nEndpoints:")
    print(f"  http://0.0.0.0:{PORT}/snapshot.jpg")
    print(f"  http://0.0.0.0:{PORT}/cgi-bin/snapshot.cgi")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()