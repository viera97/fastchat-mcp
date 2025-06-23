from enum import Enum


class StepType(Enum):
    """
    Enum representing all available LLM processing steps.
    Each step includes a name and a clear description of its purpose.
    """

    ANALYZE_QUERY = (
        "analyze query",
        "Analyze the user query and available services to separate it into service-specific calls.",
    )
    SELECTED_QUERYS = (
        "selected querys",
        "Querys that was be selected",
    )
    SELECT_SERVICE = (
        "select service",
        "Select the most appropriate service for the current query.",
    )
    CREATE_ARGUMENTS = (
        "create arguments",
        "Generate the necessary arguments for use with the selected service.",
    )
    RESPOND_QUERY = (
        "respond query",
        "Generate and return a response to the user's query.",
    )

class Step:
    def __init__(self, step_type: StepType, data: dict[str, any] | None = None):
        self.step: str = step_type.value[0]
        self.message: str = step_type.value[1]
        self.data: dict[str, any] = data

    def __call__(self) -> dict:
        return {
            "step": self.step,
            "message": self.message,
            "data": self.data,
        }

    def __str__(self):
        result = f"""
        ## {self.step}
        {self.message}\n
        """
        if self.data is not None and len(self.data) > 0:
            result += "### Data\n"
            for key in self.data.keys():
                result += f"- **{key}:**{self.data[key]}\n"
        return result


class BaseSteps:
    analize_query = Step(step_type=StepType.ANALYZE_QUERY)
    select_service = Step(step_type=StepType.SELECT_SERVICE)
    create_arguments = Step(step_type=StepType.CREATE_ARGUMENTS)
    respond_query = Step(step_type=StepType.RESPOND_QUERY)
