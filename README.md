# Debate LLM App

Welcome to the Debate LLM App! This app allows you to engage in dynamic debates powered by large language models (LLMs). You can start a statement you believe is right and watch as two AI assistants argue with each other to provide you with the best opinion.

Before you run make sure to install Ollama.
## Installation

To run the Debate LLM App, follow these steps:

Before Cloning
run these commands in terminal or powershell
  ```
  ollama run llama2
  ```
  ```
  ollama run phi3
  ```

1. Clone the repository:
   ```
   git clone https://github.com/areddysathvik/Debate-LLM-APP.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the app in your terminal:
   ```
   streamlit run main.py
   ```

## Usage

- Start the app and enter a statement you believe is right.
- Watch as two AI assistants (LLMs) argue with each other to provide you with the best opinion.

## Additional Information

- Currently, the buffer storage history size is set to 5 messages, but feel free to change it according to your preferences.
- The models used in this app are "llama2" and "phi3". You can use any other big models according to your performance requirements. All the models used in this app are free and open source.
- This app is resource-intensive. Make sure you have at least 8GB of RAM and a GPU with more than 4GB of memory for optimal performance.

Enjoy debating with our AI assistants!
