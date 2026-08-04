import subprocess
import sys

if __name__ == "__main__":
    print("=== INITIALIZING 8K @ 220 FPS VERIFICATION PIPELINE ===")
    subprocess.run([sys.executable, "modules/display_validator.py"])
    subprocess.run([sys.executable, "modules/render_stress.py"])
    print("=== PIPELINE EXECUTION FINISHED ===")
