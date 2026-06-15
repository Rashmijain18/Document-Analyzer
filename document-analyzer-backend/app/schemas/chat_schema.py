from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str       # what the user typed


class AnswerResponse(BaseModel):
    answer:      str    # Claude's response
    chunks_used: int    # how many chunks were found and used
    question:    str    # echo back the original question