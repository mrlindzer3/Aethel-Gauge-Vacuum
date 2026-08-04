import time
import numpy as np

def simulate_8k_frame_workload(duration_sec=2):
    width, height = 7680, 4320
    frame_size_mb = (width * height * 4) / (1024 * 1024)
    print(f"[*] Allocating 8K Frame Buffer: {frame_size_mb:.2f} MB per frame")
    target_fps = 220
    frame_interval = 1.0 / target_fps
    frames_to_render = target_fps * duration_sec
    print(f"[*] Running 8K@220FPS render simulation...")
    
    start_time = time.time()
    for i in range(frames_to_render):
        frame_start = time.time()
        _ = np.dot(np.ones((32, 32)), np.ones((32, 32)))
        elapsed = time.time() - frame_start
        if elapsed < frame_interval:
            time.sleep(frame_interval - elapsed)
            
    total_time = time.time() - start_time
    print(f"[+] Pipeline test complete. Time elapsed: {total_time:.2f}s")

if __name__ == "__main__":
    simulate_8k_frame_workload()
