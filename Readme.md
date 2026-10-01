## Personal GPT 

# How to run PersonalGPT 
## 1. Clone the repository 
    ```bash 
    git clone https://github.com/sandip1203/Personal--chatbot.git
    ```
## 2. Navigate to the project directory 
    ```bash 
    cd Personal--chatbot
    ```
### 3. Install requirements 
```bash
    pip install -r requirements.txt
```
### 4. RUN the application 
``` bash 
    uvicorn main:app --reload
```

## Web search



```json
{
    "query": "latest climate research",
    "recent_only": true,
    "time_range": "week",
    "max_results": 5
}
```

`recent_only` defaults to `false`. When enabled without a `time_range`, results are filtered to the past week. Supported ranges are `day`, `week`, `month`, and `year`; responses include publication dates and a `recent_data_check` summary.