# Data Decoder AI Agent 🤖

This is an AI agent app that answers questions about your input data such as answering questions of inputted CSV file using the pandas library based agent.
There is plenty things what agent do:
- Convert CSV to SQL then answering questions about SQL data.
- Answering questions about uploaded CSV using pandas library as tool.
- More to come...

## How to Use

1. Clone this repository to your local machine.
2. Install the required packages using `pip install -r requirements.txt`.
3. Choose the agent (function) you would like to use from ai_agent.py.
4. Run the app using `streamlit run demo_streamlit.py` or `python demo_gradio.py` after choosing the agent.
5. In the app, upload a data file (in this case, it's CSV) using the file uploader.
6. Enter a question in the text input field.
7. Click the 'Execute' button to run the AI agent.
8. The AI agent will process the data and display the answer to your question.

## Requirements

- Python 3.6 or later
- Streamlit
- pandas
- Other requirements are listed in `requirements.txt`.

## Demo 

AI Agent demo (Pandas Agent) is available on my [HuggingFace](https://huggingface.co/spaces/0xrsydn/pandas_agent) 🤗

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
