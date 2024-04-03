import os
from typing import Any, Optional

from llama_index.llms.openai_like import OpenAILike


class DataBricks(OpenAILike):
    """DataBricks LLM.

    Examples:
        `pip install llama-index-llms-databricks`

        ```python
        from llama_index.llms.databricks import DataBricks

        # Set up the DataBricks class with the required model, API key and serving endpoint
        llm = DataBricks(model="databricks-dbrx-instruct", api_key="your_api_key", api_base="https://[your-work-space].cloud.databricks.com/serving-endpoints/[your-serving-endpoint]")

        # Call the complete method with a query
        response = llm.complete("Explain the importance of open source LLMs")

        print(response)
        ```
    """

    def __init__(
        self,
        model: str,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        is_chat_model: bool = True,
        **kwargs: Any,
    ) -> None:
        api_key = api_key or os.environ.get("DATABRICKS_API_KEY", None)
        api_base = api_base or os.environ.get("DATABRICKS_API_BASE", None)
        super().__init__(
            model=model,
            api_key=api_key,
            api_base=api_base,
            is_chat_model=is_chat_model,
            **kwargs,
        )

    @classmethod
    def class_name(cls) -> str:
        """Get class name."""
        return "DataBricks"
