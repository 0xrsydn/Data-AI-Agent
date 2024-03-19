import gradio as gr
from ai_agent import sql_agent
from ai_agent import pandas_agent

# Create Gradio interface
iface = gr.Interface(
    fn=pandas_agent, 
    inputs=[
        gr.File(label="Upload CSV file"),
        gr.Textbox(label="Question", placeholder="Enter your question about uploaded CSV here")
    ],
    outputs=gr.Textbox(label="Answer"),
    title="Pandas Agent",
    description="Ask questions about uploaded CSV and get answers from the AI Agent."
)

# Launch the interface
iface.launch()