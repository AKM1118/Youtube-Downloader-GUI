import subprocess
import sys

def get_formats(link):
    cmd = [
        "yt-dlp",
        "--list-formats",
        str(link)
        ]
    print(f"getting info for {link}")
    process = subprocess.run(cmd, capture_output=True, text=True)
    if process.returncode == 0:
        result = process.stdout
        print(f"✅ Scan successful\n",process.stdout)
        process.stdout = ""
        return result
    else:
        print(f"❌ Error: video not found")
        result = f"❌ Error: video not found"
        return result
        
#print(sys.argv[1])
#get_formats(link=sys.argv[1])