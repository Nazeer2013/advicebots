import gradio as gr
import subprocess

# Define a function that runs the Python program and returns its output
def run_program(input):
    # Run the Python program and capture its output
    output = subprocess.check_output(["python3", "python_logstream.py", input])
    
    # Convert the output to a string and return it
    return output.decode("utf-8")

# Create a Gradio interface to accept user input and display program output
# iface = gr.Interface(fn=run_program, inputs="text", outputs="text", title="Your Program Output")
iface = gr.Interface(fn=run_program, inputs=None, outputs="text", title="Your Program Output")
iface.launch()
