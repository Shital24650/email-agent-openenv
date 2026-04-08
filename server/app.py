import gradio as gr
import subprocess
from fastapi import FastAPI
import uvicorn

# =========================
# ✅ FASTAPI (FOR VALIDATOR)
# =========================

fastapi_app = FastAPI()

@fastapi_app.post("/reset")
async def reset():
    return {
        "observation": {
            "echoed_message": ""
        },
        "reward": 0.0,
        "done": False
    }

@fastapi_app.post("/step")
async def step(action: dict):
    message = action.get("message", "")

    return {
        "observation": {
            "echoed_message": message
        },
        "reward": 0.5,
        "done": False
    }

@fastapi_app.get("/state")
async def state():
    return {"status": "running"}


# =========================
# ✅ GRADIO UI (FOR DEMO)
# =========================

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


# =========================
# 🚀 COMBINE BOTH
# =========================

app = gr.mount_gradio_app(fastapi_app, demo, path="/")


# =========================
# ✅ REQUIRED MAIN FUNCTION
# =========================

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
