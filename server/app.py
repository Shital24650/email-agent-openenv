import gradio as gr
import subprocess

def run_agent():
    result = subprocess.run(
        ["python", "inference.py"],
        capture_output=True,
        text=True
    )
    return result.stdout


with gr.Blocks() as demo:
    gr.Markdown("# 📧 Email Agent OpenEnv")
    gr.Markdown("Click below to run the email agent and see results")

    output = gr.Textbox(label="Logs Output", lines=20)

    run_btn = gr.Button("Run Email Agent 🚀")
    run_btn.click(fn=run_agent, outputs=output)


def main():
    demo.launch(server_name="0.0.0.0", server_port=7860)


if __name__ == "__main__":
    main()
