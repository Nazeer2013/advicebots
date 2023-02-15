import subprocess

# Define a function to stream log output in real-time
def stream_logs():
    # Start the log stream process
    proc = subprocess.Popen(["this is my log stream"], stdout=subprocess.PIPE, shell=True)

    # Stream the log output in real-time
    while True:
        output = proc.stdout.readline()
        if output == b'' and proc.poll() is not None:
            break
        if output:
            print(output.decode("utf-8").strip())

    # Close the log stream process
    proc.kill()

# Call the function to start streaming log output
stream_logs()
